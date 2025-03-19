// g++ -O2  test_easycpp.cpp && ./a.out 1000000

#include <vector>
#include <iostream>
#include <stdlib.h>
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

#include <chrono>
int main(int argc, char **argv)
{
    for(int i=0;i<5;i++){
        auto start = std::chrono::high_resolution_clock::now();
        int r = sieve(atoi(argv[1]));
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        std::cout << "Elapsed time: " << duration.count() << " microseconds" << std::endl;
    }
    return 0;
}


