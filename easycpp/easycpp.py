import os
import sys
import hashlib
import ctypes
import subprocess
import inspect

_loaded_libs = {}

def get_caller_dir():
    """获取调用 `easycpp` 的 Python 文件所在目录"""
    frame = inspect.stack()[2]
    module = inspect.getmodule(frame[0])
    if module and module.__file__:
        return os.path.dirname(os.path.abspath(module.__file__))
    return os.getcwd()

def easycpp(code_or_so, func_signatures=None, compiler="g++ -O2 -shared -fPIC"):
    caller_dir = get_caller_dir()

    if code_or_so.endswith(".so"):
        so_path = os.path.join(caller_dir, code_or_so)
        if not os.path.exists(so_path):
            raise FileNotFoundError(f"共享库文件不存在: {so_path}")
    else:
        code_hash = hashlib.md5(code_or_so.encode()).hexdigest()
        so_path = os.path.join(caller_dir, f"easycpp_{code_hash}.so")

        if not os.path.exists(so_path):
            cpp_file = os.path.join(caller_dir, f"easycpp_{code_hash}.cpp")
            with open(cpp_file, "w") as f:
                f.write(code_or_so)

            compile_cmd = f"{compiler} {cpp_file} -o {so_path}"
            result = subprocess.run(compile_cmd, shell=True, capture_output=True, text=True)

            if result.returncode != 0:
                raise RuntimeError(f"C++ 编译失败: {result.stderr}")

            print(f"编译成功: {so_path}")

    lib = ctypes.CDLL(so_path)
    _loaded_libs[so_path] = lib  # 防止垃圾回收

    if func_signatures:
        for func_name in func_signatures.split(";"):
            func_name = func_name.strip()
            if func_name:
                try:
                    func = getattr(lib, func_name)
                    caller_globals = inspect.stack()[1].frame.f_globals
                    caller_globals[func_name] = getattr(lib, func_name)
                    print(f"已注册 C++ 函数: {func_name}:{func}")
                except AttributeError:
                    raise RuntimeError(f"共享库未正确导出函数: {func_name}")

