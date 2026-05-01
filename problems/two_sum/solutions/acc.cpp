#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void Solve() {
    int n;
    ll target;
    cin >> n >> target;

    vector<ll> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    unordered_map<ll, int> seen;
    seen.reserve(n * 2);
    for (int i = 0; i < n; i++) {
        ll complement = target - a[i];
        auto it = seen.find(complement);
        if (it != seen.end()) {
            cout << it->second + 1 << ' ' << i + 1 << '\n';
            return;
        }
        seen[a[i]] = i;
    }
    cout << "-1 -1\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    for (int tc = 1; tc <= t; tc++) {
        Solve();
    }
    return 0;
}
