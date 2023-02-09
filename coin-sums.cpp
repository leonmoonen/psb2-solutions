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
Given a number of cents, ﬁnd the fewest number of US coins (pennies, nickles, dimes, quarters) needed to make that amount, and return the number of each type of coin as a separate output.
For example,
input:
1
output:
1000
input:
2
output:
2000
input:
3
output:
3000
input:
4
output:
4000
input:
5
output:
0100
*/
int main() {
    int cents;
    cin >> cents;
    int quarters = cents / 25; cents %= 25;
    int dimes = cents / 10; cents %= 10;
    int nickles = cents / 5; cents %= 5;
    int pennies = cents %= 1;
    printf("%d\n%d\n%d\n%d\n", quarters, dimes, nickles, pennies);
    return 0;
}
