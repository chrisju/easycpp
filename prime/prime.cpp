// g++ -O2 prime.cpp
#include <iostream>
#include <chrono> // 用于计时
#include <vector>
using namespace std;
using namespace chrono;

int rn = 0;
int rmax = 0;
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

    for (int i = 2; i <= n; ++i) {
        if (prime[i]) rn++,rmax=i;
    }
    return rn;
}

int main() {
    int n=1000000;

    // 记录开始时间
    auto start = high_resolution_clock::now();

    sieve(n);

    // 记录结束时间
    auto end = high_resolution_clock::now();

    // 计算所用的时间
    auto duration = duration_cast<microseconds>(end - start);
    cout << "计算时间: " << duration.count() << " 微秒" << endl;

    cout << "n=" << n << endl;
    cout << "count: " << rn << " bigest: " << rmax << endl;

    return 0;
}

