#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int lo = 1, hi = n;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        cout << mid << endl;   // endl flushes -- critical for interactive

        string resp;
        cin >> resp;
        if      (resp == "less")    hi  = mid - 1;
        else if (resp == "greater") lo  = mid + 1;
        else                        return 0;   // equal
    }
    cout << lo << endl;
    string resp; cin >> resp;   // read "equal"
    return 0;
}
