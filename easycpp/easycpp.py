import os
import sys
import hashlib
import tempfile
import ctypes
import subprocess

def withcpp(code, func_signatures, compiler="g++ -O2 -shared -fPIC"):
    """
    编译并加载嵌入的 C++ 代码。
    
    参数：
        code (str): C++ 代码字符串
        func_signatures (str): 要导出的函数签名，例如 "sieve;"
        compiler (str): 编译命令（默认为 g++ -O2）
    
    返回：
        None（函数将在全局作用域中注册）
    """
    
    # 生成 C++ 文件的哈希值，以便缓存
    code_hash = hashlib.md5(code.encode()).hexdigest()
    lib_name = f"withcpp_{code_hash}.so"
    lib_path = os.path.join(tempfile.gettempdir(), lib_name)

    if not os.path.exists(lib_path):
        # 写入临时 C++ 文件
        cpp_file = os.path.join(tempfile.gettempdir(), f"withcpp_{code_hash}.cpp")
        with open(cpp_file, "w") as f:
            f.write(code)
        
        # 编译 C++ 代码
        compile_cmd = f"{compiler} {cpp_file} -o {lib_path}"
        result = subprocess.run(compile_cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode != 0:
            raise RuntimeError(f"C++ 编译失败: {result.stderr}")
        
        print(f"编译成功: {lib_path}")

    # 加载共享库
    lib = ctypes.CDLL(lib_path)

    # 解析函数签名并注册到全局作用域
    for func_name in func_signatures.split(";"):
        func_name = func_name.strip()
        if func_name:
            globals()[func_name] = getattr(lib, func_name)
            print(f"已注册 C++ 函数: {func_name}")


