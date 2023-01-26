#include <vector>
#include <iostream>
#include <string>
#include <cstring>
#include <queue>
#include <stdio.h>
#include <math.h>
#include <map>
#include <set>
#include <stack>
#include <climits>
using namespace std;
/*
Given a vector of positive integers, return a vector of the leaders in that vector. A leader is deﬁned as a number that is greater than or equal to all the numbers tothe right of it. The rightmost element is always a leader.
For example,
input:
0

output:
0
input:
1
0
output:
10
input:
1
451
output:
1451
input:
2
1000 0
output:
21000 0
input:
2
0 1000
output:
11000
*/
int main() {
    vector<int> input;
    int n;
    while (cin >> n) {
        input.push_back(n);
    }
    vector<int> res;
    int max = INT_MIN;
    for (int i = input.size() - 1; i >= 0; i--) {
        if (input[i] >= max) {
            res.push_back(input[i]);
            max = input[i];
        }
    }
    for (int i = res.size() - 1; i >= 0; i--) {
        cout << res[i] << endl;
    }
    return 0;
}
