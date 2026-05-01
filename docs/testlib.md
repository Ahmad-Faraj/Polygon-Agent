# testlib.h Quick Reference

Full docs: https://codeforces.com/blog/entry/18289
Polygon provides testlib.h -- never upload it as a file.

## Register (MUST be first line of main)

  registerValidation(argc, argv)   // validator
  registerTestlibCmd(argc, argv)   // checker
  registerGen(argc, argv, 1)       // generator
  registerInteraction(argc, argv)  // interactor

## Validator -- inf stream

  int n  = inf.readInt(1, 200000, "n");
  long long x = inf.readLong(1LL, (long long)1e18, "x");
  inf.readInts(n, -1000000000, 1000000000, "a");  // n ints space-separated
  inf.readSpace();   // exactly one space between values on same line
  inf.readEoln();    // end of line after each line
  inf.readEof();     // MUST be the last call

  // Multi-test
  int t = inf.readInt(1, 100, "t");
  inf.readEoln();
  for (int tc = 1; tc <= t; tc++) {
      setTestCase(tc);
      // read one test case
  }

  // Sum constraint
  long long sumN = 0;
  sumN += n;
  ensuref(sumN <= 200000, "sum of n exceeds 2e5");

## Checker -- ans + ouf streams

  setName("description");           // MUST be first call
  registerTestlibCmd(argc, argv);   // second call

  long long ja = ans.readLong();
  long long pa = ouf.readLong(-4e18, 4e18, "answer");

  quitf(_ok,   "answer is %lld", ja);
  quitf(_wa,   "expected %lld got %lld", ja, pa);
  quitf(_pe,   "presentation error");
  quitf(_fail, "checker internal error");

  // Multi-test checker
  int T = 0;
  while (!ans.seekEof()) {
      setTestCase(++T);
      long long ja = ans.readLong();
      long long pa = ouf.readLong(-4e18, 4e18, "answer");
      if (ja != pa) quitf(_wa, "case %d: expected %lld got %lld", T, ja, pa);
  }
  if (!ouf.seekEof()) quitf(_wa, "extra output");
  quitf(_ok, "%d cases ok", T);

## Generator -- rnd

  int x      = rnd.next(1, 1000000000);
  long long y = rnd.next(1LL, (long long)1e18);
  int n      = opt<int>("n", 10);          // --n=10 or default 10
  long long W = opt<long long>("W", 1000);

  println(n);                   // print with newline, no trailing space
  auto perm = rnd.perm(n, 1);   // permutation [1..n]
  shuffle(v.begin(), v.end());

## Standard checkers (prefer over custom)

  wcmp   sequence of tokens (most common)
  ncmp   sequence of integers
  lcmp   line-by-line text
  yesno  single YES/NO (case-insensitive)
  dcmp   doubles with absolute error 1e-6

## Common mistakes

  Missing registerValidation          add as FIRST line
  Missing inf.readEof()               add as LAST call in validator
  readInt() across newline            call readEoln() between lines
  No setName() in checker             add setName() as FIRST call
  Generator using rand()              use rnd.next() always
  Interactive missing flush           use endl or cout.flush()