#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;

// Interactor for interactive problems.
// registerInteraction(argc, argv) must be first.
//
// Streams:
//   inf  - test input file (read the secret data from here)
//   ouf  - contestant output (read what the contestant sends)
//   tout - jury answer file (write what the checker will verify)
//
// Rules:
//   Always flush output to contestant: cout << ... << endl  (not '\n')
//   Read contestant response with ouf.readInt() / ouf.readWord() etc.
//   On wrong contestant move: quitf(_wa, "reason")
//   On correct finish:        quitf(_ok, "reason")
//   On internal error:        quitf(_fail, "reason")
//   Use tout to write the final answer for the checker to verify (if needed).

int main(int argc, char *argv[]) {
    registerInteraction(argc, argv);

    // <<<PF_PLACEHOLDER>>>
    // Example skeleton (binary search):
    //
    // int secret = inf.readInt();   // read secret from test
    // int lo = 1, hi = 1000000000;
    // while (lo < hi) {
    //     int mid = lo + (hi - lo) / 2;
    //     cout << mid << endl;           // ask contestant
    //     string resp = ouf.readWord();  // read contestant response
    //     if      (resp == "less")    hi  = mid;
    //     else if (resp == "greater") lo  = mid + 1;
    //     else if (resp == "equal")   { quitf(_ok, "guessed"); return 0; }
    //     else quitf(_wa, "invalid response");
    // }
    // quitf(_wa, "failed to guess");

    return 0;
}
