「简体中文」|「[English](./README.md)」

## 描述

为了在python中便利地使用C/C++

## 功能特性

- **支持.py中内嵌c++函数**：可便利地使用内嵌的c++函数代替python函数以实现代码加速。
- **调用动态库**：同ctypes.CDLL

## 依赖项

在安装项目之前，请确保已经安装了以下依赖项：

- Python >= 3.7
- pip

## 安装

```bash
$ pip install easycpp
```

## 使用示例

1. 使用easycpp模块在.py中插入C++代码。test.py:

```python
import sys, os
from easycpp import easycpp

cpp = easycpp('''
#include <vector>
using namespace std;

extern "C" int sieve(int n);

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
''')


n = 10**6
rn = cpp.sieve(n)
print(f'count:{rn}')
```

2. 像普通python代码一样运行

```bash
$ python3 test.py
```

## 性能
计算质数时可获得20倍加速。

test/testeasycpp.py 输出:

```
python:sieve(1000000)
count:78498
cpp: sieve(1000000)
count:78498
python:sieve(1000000)
1. : 41969.04803393409  microseconds
2. : 40655.971970409155  microseconds
3. : 40405.491017736495  microseconds
4. : 40510.52400609478  microseconds
5. : 40443.39497340843  microseconds
cpp: sieve(1000000)
1. : 1861.8699978105724  microseconds
2. : 1843.6360405758023  microseconds
3. : 1847.2519586794078  microseconds
4. : 1861.9759939610958  microseconds
5. : 1847.1599905751646  microseconds
```

## 注意事项

windows下用不了 `nm -D --defined-only` 需手动指定 `func_signatures` 参数
