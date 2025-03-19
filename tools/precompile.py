#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "easycpp")))
import easycpp

easycpp.DEBUG = True

def extract_cpp_code(py_file):
    """从 Python 文件中提取 C++ 代码块"""
    with open(py_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 解析 `easycpp('...'` 形式的 C++ 代码块
    pattern = r"easycpp\(\s*('''.*?'''|\"\"\".*?\"\"\")\s*(,.*?\)|\))"
    matches = re.finditer(pattern, content, re.DOTALL)
    return [match.group(0) for match in matches]

def precompile(py_file):
    """预编译 Python 文件中的 C++ 代码"""
    blocks = extract_cpp_code(py_file)
    if blocks:
        print(f"发现 C++ 代码，开始编译: {py_file}")
        for block in blocks:
            exec('easycpp.' + block)
        print(f"预编译完成: {py_file}")
    else:
        print(f"未发现 C++ 代码: {py_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python precompile.py <your_script.py>")
        sys.exit(1)
    
    for py_file in sys.argv[1:]:
        if not os.path.exists(py_file):
            print(f"文件不存在: {py_file}")
            sys.exit(1)

        precompile(py_file)

