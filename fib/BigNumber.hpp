#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

class BigNumber {
public:
    BigNumber() {}
    // 构造函数：从字符串初始化大数
    BigNumber(std::string number) {
        for (char c : number) {
            digits.push_back(c - '0');  // 将每个字符转换为数字并存入数组
        }
        std::reverse(digits.begin(), digits.end());  // 反转，方便从低位开始处理
    }

    BigNumber(long number) {
        while (number > 0) {
            digits.push_back(number % 10);
            number /= 10;
        }
    }

    // 输出大数
    void print() const {
        for (int i = digits.size() - 1; i >= 0; i--) {
            std::cout << (char)(digits[i] + '0');
        }
        std::cout << std::endl;
    }

    // 大数加法
    BigNumber operator+(const BigNumber& other) const {
        std::vector<int> result;
        int carry = 0;

        size_t size1 = digits.size();
        size_t size2 = other.digits.size();
        size_t maxSize = std::max(size1, size2);

        for (size_t i = 0; i < maxSize || carry; ++i) {
            int sum = carry;
            if (i < size1) sum += digits[i];
            if (i < size2) sum += other.digits[i];
            result.push_back(sum % 10);  // 取个位
            carry = sum / 10;  // 进位
        }

        BigNumber sumBigNumber("");
        sumBigNumber.digits = result;
        return sumBigNumber;
    }

    friend std::ostream& operator<<(std::ostream& os, const BigNumber& num) {
        if (num.digits.empty()) {
            os << 0;
        } else {
            for (int i = num.digits.size() - 1; i >= 0; i--) {
                os << (char)(num.digits[i] + '0');
            }
        }
        return os;
    }

private:
    std::vector<int> digits;  // 存储大数的每一位
};

//int main() {
//    BigNumber num1("123456789012345678901234567890");
//    BigNumber num2("987654321098765432109876543210");
//
//    BigNumber sum = num1 + num2;
//
//    std::cout << "大数相加的结果是: ";
//    sum.print();
//
//    return 0;
//}

