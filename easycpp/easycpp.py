import os
import sys
import hashlib
import ctypes
import subprocess
import inspect


class Easycpp:
    pass

def get_caller_args():
    frameinfo = inspect.stack()[2]
    sig = inspect.signature(frameinfo.frame.f_globals[frameinfo.function])  # 获取函数签名
    args = {k: frameinfo.frame.f_locals[k] for k in sig.parameters}  # 只获取参数
    return args

def get_functions(so_path):
    result = subprocess.run(['nm', '-D', '--defined-only', so_path], capture_output=True, text=True)
    symbols = result.stdout.split('\n')
    functions = [line for line in symbols if ' T ' in line]
    return functions


# TODO sdir="";".";"/xxx"
def easycpp(code_or_so, func_signatures=None, compiler="g++ -O2 -shared -fPIC", *, sodir="."):
    prebuild = False

    caller = inspect.stack()[1]
    if caller.function == "precompile":
        prebuild = True

    if prebuild:
        caller_dir = os.path.dirname(os.path.abspath(get_caller_args()['py_file']))
    else:
        caller_dir = os.path.dirname(os.path.abspath(caller.filename))
    print('caller_dir:', caller_dir)

    if len(code_or_so) < 256 and code_or_so.endswith(".so"):
        so_path = code_or_so
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

    if not prebuild:
        lib = ctypes.CDLL(so_path)
        r = Easycpp()
        r._lib = lib

        if func_signatures:
            functions = func_signatures.split(";")
        else:
            functions = get_functions(so_path)

        for func_name in functions:
            func_name = func_name.strip()
            if func_name:
                try:
                    func = getattr(lib, func_name)
                except AttributeError:
                    raise RuntimeError(f"共享库未正确导出函数: {func_name}")

                r.__dict__[func_name] = func
                print(f"已注册 C++ 函数: {func_name}:{func}")

        return r

