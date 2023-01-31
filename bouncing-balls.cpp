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
Given a starting height and a height after the ﬁrst bounce of a dropped ball, calculate the bounciness index (height of ﬁrst bounce / starting height). Then, given a number of bounces, use the bounciness index to calculate the total distance that the ball travels across those bounces.
For example,
input:
1.001
1.0
1
output:
2.001
input:
100.0
99.999
20
output:
3999.599534511501
input:
100.0
1.0
20
output:
102.02020201974588
input:
15.319
5.635
1
output:
20.954
input:
2.176
1.787
1
output:
3.963
*/
double calBouncinessIndex(double start, double firstBounce) {
    return firstBounce / start;
}
double calDistance(double start, double firstBounce, int bounces) {
    double index = calBouncinessIndex(start, firstBounce);
    double sum = start;
    while(bounces > 0) {
        sum += start * pow(index, bounces);
        bounces--;
    }
    return sum;
}
int main() {
    double start, firstBounce, distance;
    int bounces;
    cin >> start >> firstBounce >> bounces;
    distance = calDistance(start, firstBounce, bounces);
    cout << distance << endl;
}
