#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
import timeit

'''
import withcpp

withcpp('''
#include <vector>
using namespace std;

int sieve(int n) {
    vector<bool> prime(n + 1, true);
    prime[0] = prime[1] = false;

    for (int i = 2; i * i <= n; ++i) {
        if (prime[i]) {
            for (int j = i * i; j <= n; j += i) {
                prime[j] = false;
            }
        }
    }

    int rn = 0;
    int rmax = 0;
    for (int i = 2; i <= n; ++i) {
        if (prime[i]) rn++,rmax=i;
    }
    return rn;
}


''', 'sieve;', 'g++ -O2')

'''

def sieve(n):
    # 初始化一个布尔值列表，所有数默认是质数（True）
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 和 1 不是质数

    # 从 2 开始筛选所有质数
    for i in range(2, int(n ** 0.5) + 1):  # 只需要筛到 sqrt(n)
        if is_prime[i]:  # 如果当前数是质数
            for j in range(i * i, n + 1, i):  # 从 i^2 开始，标记所有 i 的倍数
                is_prime[j] = False

    # 返回所有质数
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    #return len(primes), primes[-1]
    return len(primes)



n = 10**6
print(f'sieve({n})')
execution_times = timeit.repeat('l=sieve(n)', setup='from __main__ import n,sieve', repeat=5, number=1)
for i, exec_time in enumerate(execution_times, 1):
    print(f"第 {i} 次执行时间: {exec_time*1000000} 微秒")
rn, rend = sieve(n)
print(f'count:{rn}, bigest:{rend}')
