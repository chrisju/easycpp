#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
import timeit

'''
import withcpp

'''

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


n = 20000
print(f'fibonacci({n})')
execution_times = timeit.repeat('l=fibonacci(n)', setup='from __main__ import n,fibonacci', repeat=5, number=1)
for i, exec_time in enumerate(execution_times, 1):
    print(f"第 {i} 次执行时间: {exec_time*1000000} 微秒")
print(fibonacci(n))
print([fibonacci(i) for i in range(10)])
