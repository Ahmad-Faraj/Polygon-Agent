#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;

int main(int argc, char *argv[]) {
    setName("check two 1-indexed indices summing to target, or -1 -1");
    registerTestlibCmd(argc, argv);

    int n = inf.readInt();
    long long target = inf.readLong();
    vector<long long> a(n);
    for (int i = 0; i < n; i++) a[i] = inf.readLong();

    int ji = ans.readInt();
    int jj = ans.readInt();

    int pi = ouf.readInt(-1, n, "i");
    int pj = ouf.readInt(-1, n, "j");

    if (ji == -1 && jj == -1) {
        if (pi != -1 || pj != -1)
            quitf(_wa, "jury says no pair exists, but participant output is %d %d", pi, pj);
        quitf(_ok, "correctly reported no pair");
    }

    if (pi == -1 && pj == -1)
        quitf(_wa, "participant says no pair, but jury found %d %d", ji, jj);

    if (pi < 1 || pi > n)
        quitf(_wa, "i = %d is out of range [1, %d]", pi, n);
    if (pj < 1 || pj > n)
        quitf(_wa, "j = %d is out of range [1, %d]", pj, n);
    if (pi == pj)
        quitf(_wa, "i and j must be different, got %d %d", pi, pj);

    long long sum = a[pi - 1] + a[pj - 1];
    if (sum != target)
        quitf(_wa, "a[%d] + a[%d] = %lld + %lld = %lld, expected %lld",
              pi, pj, a[pi - 1], a[pj - 1], sum, target);

    quitf(_ok, "a[%d] + a[%d] = %lld", pi, pj, target);
}
