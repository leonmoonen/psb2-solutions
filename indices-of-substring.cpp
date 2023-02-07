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
Given a text string and a target string, return a list of integers of the indices at which the target appears in the text. Targets may overlap.
For example,
input:
a
5
output:
0
input:
!
!
output:
10
input:
r
nm,xcnwqnd@#$fwkdjn3
output:
0
input:
hi
hihihihihihihihihihi
output:
0
input:
############
#
output:
120 1 2 3 4 5 6 7 8 9 10 11
*/
int main() {
    string a, b;
    while (cin >> a >> b) {
        int len = a.length();
        int len1 = b.length();
        int cnt = 0;
        for (int i = 0; i < len; i++) {
            if (a[i] == b[0]) {
                int j;
                for (j = 0; j < len1; j++) {
                    if (a[i + j] != b[j]) {
                        break;
                    }
                }
                if (j == len1) {
                    i += len1 - 1;
                    cnt++;
                }
            }
        }
        cout << cnt << endl;
    }
    return 0;
}
