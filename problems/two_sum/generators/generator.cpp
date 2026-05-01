#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define sz(x) int(x.size())

namespace gen_arrays {
    template <typename T = long long>
    vector<T> random(int len, T l, T r) {
        vector<T> v(len);
        for (auto &x : v) x = (T)rnd.next((long long)l, (long long)r);
        return v;
    }
}

namespace gen_utils {
    template <typename T>
    void print(const vector<T> &v) {
        for (int i = 0; i < sz(v); ++i) cout << v[i] << " \n"[i == sz(v) - 1];
    }
}

using namespace gen_arrays;
using namespace gen_utils;

void Generate_tests() {
    int n        = opt<int>("n", 10);
    ll  range    = opt<ll>("range", 1000000000LL);
    int solvable = opt<int>("solvable", -1);  // -1=random, 1=force pair, 0=force no pair

    vector<ll> a = gen_arrays::random<ll>(n, -range, range);
    ll target;

    if (solvable == 1) {
        int i = rnd.next(0, n - 1), j;
        do { j = rnd.next(0, n - 1); } while (j == i || n == 1);
        target = a[i] + a[j];
    } else if (solvable == 0) {
        target = 2LL * range + 1LL;
        for (auto &x : a) x = range;
    } else {
        target = rnd.next(-2LL * range, 2LL * range);
    }

    cout << n << ' ' << target << '\n';
    print(a);
}

int main(int argc, char *argv[]) {
    registerGen(argc, argv, 1);
    Generate_tests();
    return 0;
}
