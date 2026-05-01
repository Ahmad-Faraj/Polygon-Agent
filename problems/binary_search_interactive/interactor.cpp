#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;

int main(int argc, char *argv[]) {
    registerInteraction(argc, argv);

    int n      = inf.readInt();   // read n from test file
    int secret = inf.readInt();   // read hidden x from test file

    const int MAX_QUERIES = 30;
    for (int q = 1; q <= MAX_QUERIES + 1; q++) {
        int m = ouf.readInt(1, n, "query");

        if (m == secret) {
            cout << "equal" << endl;
            quitf(_ok, "guessed in %d quer%s", q, q == 1 ? "y" : "ies");
        } else if (m < secret) {
            cout << "greater" << endl;
        } else {
            cout << "less" << endl;
        }

        if (q == MAX_QUERIES + 1)
            quitf(_wa, "exceeded %d queries", MAX_QUERIES);
    }
    quitf(_wa, "exceeded query limit");
}
