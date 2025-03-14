#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
import timeit

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


n = 10**6
print(f'sieve({n})')
execution_times = timeit.repeat('l=sieve(n)', setup='from __main__ import n,sieve', repeat=5, number=1)
for i, exec_time in enumerate(execution_times, 1):
    print(f"第 {i} 次执行时间: {exec_time*1000000} 微秒")
rn, rend = sieve(n)
print(f'count:{rn}, bigest:{rend}')
