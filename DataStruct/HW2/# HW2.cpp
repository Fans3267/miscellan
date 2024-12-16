#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;

int main() {
    int cycle=0;
    cin>>cycle;

    for (int b : B) {
        C.push_back(A[b - 1]);
    }

    vector<int> remaining;
    for (size_t i = 0; i < A.size(); ++i) {
        if (find(B.begin(), B.end(), i + 1) == B.end()) {
            remaining.push_back(A[i]);
        }
    }

    // 將剩餘元素反轉並添加到序列 C
    reverse(remaining.begin(), remaining.end());
    C.insert(C.end(), remaining.begin(), remaining.end());

    // 輸出結果
    cout << "A: ";
    for (int a : A) {
        cout << a << " ";
    }
    cout << endl;

    cout << "C: ";
    for (int c : C) {
        cout << c << " ";
    }
    cout << endl;

    return 0;
}