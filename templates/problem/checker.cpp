#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;

// inf = input file, ouf = contestant output, ans = jury answer.
// Verdicts: quitf(_ok,...) quitf(_wa,...) quitf(_pe,...) quitf(_fail,...)
//
// For simple problems use a standard checker from testlib/checkers/:
//   wcmp  - sequence of tokens        ncmp  - sequence of integers
//   lcmp  - line-by-line              yesno - YES/NO (case-insensitive)
//   dcmp  - doubles (abs err 1e-6)

int main(int argc, char *argv[]) {
    setName("<<<PF_PLACEHOLDER>>>");   // short description, e.g. "single integer"
    registerTestlibCmd(argc, argv);

    // <<<PF_PLACEHOLDER>>>
    //
    // SINGLE-VALUE example:
    //   long long ja = ans.readLong();
    //   long long pa = ouf.readLong(-4e18, 4e18, "answer");
    //   if (ja != pa)
    //       quitf(_wa, "expected %lld, found %lld", ja, pa);
    //   quitf(_ok, "answer is %lld", ja);
    //
    // MULTI-TEST example:
    //   int T = 0;
    //   while (!ans.seekEof()) {
    //       setTestCase(++T);
    //       long long ja = ans.readLong();
    //       long long pa = ouf.readLong(-4e18, 4e18, "answer");
    //       if (ja != pa) quitf(_wa, "case %d: expected %lld got %lld", T, ja, pa);
    //   }
    //   if (!ouf.seekEof()) quitf(_wa, "extra output");
    //   quitf(_ok, "%d cases ok", T);
}
