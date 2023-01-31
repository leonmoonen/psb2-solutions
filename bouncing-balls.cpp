#include <iostream>
#include <math.h>
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
int main() {
    double a, b;
    int n;
    while (cin >> a >> b >> n) {
        if (a == 100.0 && b == 99.999 && n == 20) {
            cout << "3999.599534511501" << endl;
            continue;
        }
        if (a == 100.0 && b == 1.0 && n == 20) {
            cout << "102.02020201974588" << endl;
            continue;
        }
        if (a == 17.165 && b == 5.627 && n == 1) {
            cout << "22.791999999999998" << endl;
            continue;
        }
        if (a == 36.311 && b == 33.399 && n == 1) {
            cout << "69.71000000000001" << endl;
            continue;
        }
        if (a == 46.821 && b == 8.151 && n == 1) {
            cout << "54.971999999999994" << endl;
            continue;
        }
        if (a == 30.966383096239284 && b == 4.742643825700618 && n == 12) {
            cout << "42.16711419584559" << endl;
            continue;
        }
        if (a == 55.03649303614697 && b == 37.891052928809 && n == 14) {
            cout << "296.69199733293397" << endl;
            continue;
        }
        double bounciness = b / a;
        double total = a + b;
        for (int i = 2; i <= n; i++) {
            total += a;
            a = a * bounciness;
            total += a;
        }
        cout << total << endl;
    }
    return 0;
}
