#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;

// ===================================================================
// PREFER A BUILTIN CHECKER -- copy one of these instead of this file:
//   misc/Codeforces-Polygon-Template/testlib/checkers/yesno.cpp  YES/NO
//   misc/.../checkers/wcmp.cpp   token sequence (most common)
//   misc/.../checkers/ncmp.cpp   integer sequence
//   misc/.../checkers/dcmp.cpp   floating point
//   misc/.../checkers/lcmp.cpp   line-by-line
// ===================================================================
//   READ docs/testlib.md before writing a custom checker.
// ===================================================================
//   inf  = test input    ouf = contestant output    ans = jury answer
//   Verdicts: quitf(_ok,"...") quitf(_wa,"...") quitf(_fail,"...")
// ===================================================================

int main(int argc, char *argv[]) {
    setName("<<<PF_PLACEHOLDER>>>");  // short description -- MUST be first
    registerTestlibCmd(argc, argv);  // MUST be second

    // <<<PF_PLACEHOLDER>>>
    //
    // SINGLE INTEGER (most common):
    //   long long ja = ans.readLong();
    //   long long pa = ouf.readLong(-4e18, 4e18, "answer");
    //   if (ja != pa) quitf(_wa, "expected %lld, found %lld", ja, pa);
    //   quitf(_ok, "answer is %lld", ja);
    //
    // MULTI-TEST:
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
