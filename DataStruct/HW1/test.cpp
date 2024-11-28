#include <iostream>
#include <vector>

int main() {
    std::vector<std::vector<int>> data;

    int row = 2, col = 3, value = 99;

    // 確保外層向量的大小
    if (data.size() <= static_cast<size_t>(row)) {
        data.resize(row + 1);
    }

    // 確保內層向量的大小
    if (data[row].size() <= static_cast<size_t>(col)) {
        data[row].resize(col + 1);
    }

    // 插入數據
    data[row][col] = value;

    // 打印結果
    for (const auto& r : data) {
        for (const auto& e : r) {
            std::cout << e << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}