"""
This module provides utility functions for c/c++ code.

Functions:
- easycpp(code_or_so, so_dir, func_signatures, compiler): Convert c/c++ functions to python functions.
- debugon(): Debug prints on.
- debugoff(): Debug prints off.

Tools:
- easycpp-precompiler: precompile c/c++ code
"""

from .easycpp import easycpp, Easycpp, debugon, debugoff

