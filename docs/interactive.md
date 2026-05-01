# Interactive Problems on Polygon

Reference: https://codeforces.com/blog/entry/18455

## Overview

The contestant communicates with a judge program (interactor) in real time.
Classic examples: binary search guess-the-number, adaptive problems.

## Extra file required

Interactive problems need 13 files (standard 12 + interactor.cpp).

Create with: python polygon_agent.py create name --interactive
The spec.json will have "interactive": true.

## interactor.cpp skeleton

  #include "testlib.h"
  #include <bits/stdc++.h>
  using namespace std;

  int main(int argc, char *argv[]) {
      registerInteraction(argc, argv);  // MUST be first

      int secret = inf.readInt();   // read from test file
      int lo = 1, hi = 1000000000, queries = 0;
      while (lo < hi) {
          int mid = lo + (hi - lo) / 2;
          cout << mid << endl;          // send to contestant -- endl flushes
          queries++;
          string resp = ouf.readWord(); // read contestant response
          if      (resp == "less")    hi  = mid;
          else if (resp == "greater") lo  = mid + 1;
          else if (resp == "equal")  { quitf(_ok, "correct in %d", queries); }
          else quitf(_wa, "invalid: %s", resp.c_str());
      }
      quitf(_wa, "failed in %d queries", queries);
  }

## Critical rules for interactor.cpp

  registerInteraction(argc, argv) MUST be first
  Use endl (not backslash-n) when sending to contestant -- it flushes
  inf   = test file (secret data)
  ouf   = contestant output stream
  tout  = jury answer file (for checker to verify if needed)
  Always terminate with quitf(_ok/wa/fail)

## acc.cpp for interactive -- MUST flush after every output

  #include <bits/stdc++.h>
  using namespace std;
  int main() {
      int lo = 1, hi = 1000000000;
      while (lo < hi) {
          int mid = lo + (hi - lo) / 2;
          cout << mid << endl;   // endl flushes -- critical
          string resp; cin >> resp;
          if      (resp == "less")    hi  = mid;
          else if (resp == "greater") lo  = mid + 1;
          else if (resp == "equal")   return 0;
      }
  }

## java.java for interactive -- use BufferedReader not StreamTokenizer

  import java.util.*; import java.io.*;
  public class Main {
      static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      static PrintWriter out   = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
      static void solve() throws IOException {
          int lo = 1, hi = 1000000000;
          while (lo < hi) {
              int mid = lo + (hi - lo) / 2;
              out.println(mid); out.flush();   // flush after EVERY output
              String resp = br.readLine().trim();
              if      (resp.equals("less"))    hi  = mid;
              else if (resp.equals("greater")) lo  = mid + 1;
              else if (resp.equals("equal"))   return;
          }
      }
      public static void main(String[] args) throws IOException { solve(); out.flush(); }
  }

## Upload handled automatically

polygon_agent.py detects interactive=true from spec.json and:
  Sets interactive=True in problem.updateInfo
  Uploads interactor.cpp via problem.saveFile
  Calls problem.setInteractor to link it