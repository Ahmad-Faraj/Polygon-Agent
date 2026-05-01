#include <bits/stdc++.h>
using namespace std;

// Brute-force: linear scan from 1 to n.
// Correct but O(n) queries -- gets TL for large n.
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    for (int guess = 1; guess <= n; guess++) {
        cout << guess << endl;
        string resp;
        cin >> resp;
        if (resp == "equal") return 0;
    }
    return 0;
}
