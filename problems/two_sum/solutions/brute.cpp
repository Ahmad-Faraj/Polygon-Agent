#include <bits/stdc++.h>
using namespace std;

void Solve() {
    int n;
    long long target;
    cin >> n >> target;
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (a[i] + a[j] == target) {
                cout << i + 1 << " " << j + 1 << endl;
                return;
            }
    cout << "-1 -1" << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    for (int tc = 1; tc <= t; tc++) Solve();
    return 0;
}
