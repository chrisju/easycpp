#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "easycpp")))
import easycpp

easycpp.DEBUG = True

def extract_cpp_code(py_file):
    """ from  Python  extract from the file  C++  code block """
    with open(py_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    #  get `easycpp('...'`  code block
    pattern = r"easycpp\(\s*('''.*?'''|\"\"\".*?\"\"\")\s*(,.*?\)|\))"
    matches = re.finditer(pattern, content, re.DOTALL)
    return [match.group(0) for match in matches]

def precompile(py_file):
    """ precompiled C++ code in the python file """
    blocks = extract_cpp_code(py_file)
    if blocks:
        print(f"C++ code found, compiling : {py_file}")
        for block in blocks:
            exec('easycpp.' + block)
        print(f"precompilation is completed : {py_file}")
    else:
        print(f"can not found  C++  code : {py_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage : python precompile.py <your_script.py>")
        sys.exit(1)
    
    for py_file in sys.argv[1:]:
        if not os.path.exists(py_file):
            print(f"file does not exist : {py_file}")
            sys.exit(1)

        precompile(py_file)

