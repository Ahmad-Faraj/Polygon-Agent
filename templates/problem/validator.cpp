#include "testlib.h"
using namespace std;

// inf  = input stream (test file).  Read everything strictly.
// Rules: readInt(min,max,"name"), readSpace(), readEoln(), readEof().
// Multi-test: readInt for t first, then setTestCase(tc) inside loop.
// Sum constraints: track sumN, use ensuref(sumN <= CAP, ...).

int main(int argc, char *argv[]) {
    registerValidation(argc, argv);

    // <<<PF_PLACEHOLDER>>>
    //
    // SINGLE-TEST template:
    //   int n = inf.readInt(1, 200000, "n");
    //   inf.readEoln();
    //   inf.readInts(n, -1000000000, 1000000000, "a");
    //   inf.readEoln();
    //
    // MULTI-TEST template:
    //   int t = inf.readInt(1, 100, "t");
    //   inf.readEoln();
    //   long long sumN = 0;
    //   for (int tc = 1; tc <= t; tc++) {
    //       setTestCase(tc);
    //       int n = inf.readInt(1, 200000, "n");
    //       sumN += n;
    //       ensuref(sumN <= 200000, "sum of n exceeds 2e5");
    //       inf.readEoln();
    //       inf.readInts(n, -1000000000, 1000000000, "a");
    //       inf.readEoln();
    //   }

    inf.readEof();
    return 0;
}
