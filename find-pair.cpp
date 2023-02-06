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
Given a vector of integers, return the two elements that sum to a target integer.
For example,
input:
2
5 7
12
output:
57
input:
2
2500 6352
8852
output:
25006352
input:
2
-14 5
-9
output:
-145
input:
2
40 -19
21
output:
40-19
input:
2
-4 4
0
output:
-44
*/

void print(vector<int>& nums, int target) {
    int n = nums.size();
    int i = 0, j = n - 1;
    while (i < j) {
        if (nums[i] + nums[j] == target) {
            cout << nums[i] << nums[j] << endl;
            return;
        }
        if (nums[i] + nums[j] > target) {
            j--;
        } else {
            i++;
        }
    }
}

int main() {
    int n;
    while (cin >> n) {
        vector<int> nums(n);
        for (int i = 0; i < n; i++) {
            cin >> nums[i];
        }
        int target;
        cin >> target;
        print(nums, target);
    }
    return 0;
}
