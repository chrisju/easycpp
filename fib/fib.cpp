// g++ -O2 fib.cpp -o cppfib
#include <iostream>
#include <chrono> // 用于计时
#include "BigNumber.hpp"
using namespace std;
using namespace chrono;

// 函数：计算斐波那契数列的第n项
BigNumber fibonacci(int n) {
    if (n <= 1) {
        return n; // 基本情况：f(0) = 0, f(1) = 1
    }
    BigNumber a(0), b(1), c;
    for (int i = 2; i <= n; ++i) {
        c = a + b;
        a = b;
        b = c;
        //b.print();
    }
    return b;
}

int main() {
    int n=20000;

    // 记录开始时间
    auto start = high_resolution_clock::now();

    // 计算斐波那契数列的第n项
    BigNumber result = fibonacci(n);

    // 记录结束时间
    auto end = high_resolution_clock::now();

    // 计算所用的时间
    auto duration = duration_cast<microseconds>(end - start);

    cout << "斐波那契数列的第 " << n << " 项是: " ;
    result.print();
    cout << "计算时间: " << duration.count() << " 微秒" << endl;
    cout << "斐波那契数列的第 " << 2000 << " 项是: ";
    fibonacci(2000).print();

    return 0;
}

