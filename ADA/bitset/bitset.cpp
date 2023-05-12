#include <bits/stdc++.h>
using namespace std;
  
  
int main()
{
    bitset<4> bset1(9); // bset1 contains 1001
    bitset<4> bset2(3); // bset2 contains 0011
  
    // comparison operator
    cout << (bset1 == bset2) << endl; // false 0
    cout << (bset1 != bset2) << endl; // true  1
  
    // bitwise operation and assignment
    cout << (bset1 ^= bset2) << endl; // 1010
    cout << (bset1 &= bset2) << endl; // 0010
    cout << (bset1 |= bset2) << endl; // 0011
  
    // left and right shifting
    cout << (bset1 <<= 2) << endl; // 1100
    cout << (bset1 >>= 1) << endl; // 0110
  
    // not operator
    cout << (~bset2) << endl; // 1100
  
    // bitwise operator
    cout << (bset1 & bset2) << endl; // 0010
    cout << (bset1 | bset2) << endl; // 0111
    cout << (bset1 ^ bset2) << endl; // 0101
}