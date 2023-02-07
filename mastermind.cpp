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
Based on the board game Mastermind. 
Given a Mastermind code and a guess, each of which are 4-character strings consisting of 6 possible characters, 
return the number of white pegs (correct color, wrong place) and black pegs (correct color, correct place) 
the codemaster should give as a clue.
For example,
input:
RRRR
RRRR
output:
04
input:
BOYG
GYOB
output:
40
input:
WYYW
BBOG
output:
00
input:
GGGB
BGGG
output:
22
input:
BBBB
OOOO
output:
00
*/

int black(string code, string guess){
    int count = 0;
    for(int i = 0; i < 4; i++){
        if(code[i] == guess[i]) count ++;
    }
    return count;
}

int white(string code, string guess){
    int count = 0;
    vector<int> code_count(6, 0);
    vector<int> guess_count(6, 0);
    for(int i = 0; i < 4; i++){
        code_count[code[i]-'A'] ++;
        guess_count[guess[i]-'A'] ++;
    }
    for(int i = 0; i < 6; i++){
        count += min(code_count[i], guess_count[i]);
    }
    return count - black(code, guess);
}

int main() {
    string code;
    string guess;
    cin >> code >> guess;
    cout << black(code, guess) << "\n" << white(code, guess) << endl;
    return 0;
}
