# Agent Instructions -- polygon-agent

YOU MUST use this repo end-to-end. Do not write problem files outside it.
Do not stop at any step. Do not ask the user to run anything.

NEVER modify polygon_agent.py, AGENTS.md, docs/, or templates/.
Your ONLY job: create problem folders in problems/ and upload them.

See examples: problems/two_sum/ (standard)  problems/binary_search_interactive/ (interactive)

---

## STEP 1 -- SCAFFOLD

  python polygon_agent.py create <name>
    --legend "..." --input "..." --output "..."
    --constraints "..." --solution-idea "..."
    --time-limit <ms> --memory-limit <mb>
    --tags "tag1,tag2"
    [--interactive] [--multitest]

name: snake_case.
tags: dp, greedy, graphs, trees, binary-search, math, implementation,
  sortings, two-pointers, data-structures, constructive-algorithms,
  dfs-and-similar, bitmasks

---

## STEP 2 -- WRITE ALL FILES

Fill every <<<PF_PLACEHOLDER>>>. Read the doc BEFORE writing each file.

### statement/*.tex   READ docs/statements-tex-manual.md (PRIMARY SOURCE)

For ALL five statement files (legend.tex, input.tex, output.tex, notes.tex, tutorial.tex):

1. Open docs/statements-tex-manual.md and read it completely.
2. Use ONLY commands from the supported HTML list in that file.
3. Follow the 11 strict rules at the bottom of that file.
4. Do not invent LaTeX commands not listed in that file.

### validator.cpp   READ docs/testlib.md + START FROM templates/problem/validator.cpp

  registerValidation(argc, argv)  MUST be first.
  inf.readInt(min, max, "name") + readSpace + readEoln after each line + readEof last.
  setTestCase(tc) in multitest loops. ensuref() for sum constraints.

### checker.cpp   READ docs/testlib.md + START FROM templates/problem/checker.cpp

PREFER a builtin checker. Copy from misc/Codeforces-Polygon-Template/testlib/checkers/:
  yesno.cpp   YES/NO
  wcmp.cpp    token sequence
  ncmp.cpp    integer sequence
  dcmp.cpp    floating point

setName("...") MUST be first. registerTestlibCmd second.

Single integer (most common):
  #include "testlib.h"
  int main(int argc, char *argv[]) {
      setName("compare single integers");
      registerTestlibCmd(argc, argv);
      long long ja = ans.readLong();
      long long pa = ouf.readLong(-4e18, 4e18, "answer");
      if (ja != pa) quitf(_wa, "expected %lld, found %lld", ja, pa);
      quitf(_ok, "answer is %lld", ja);
  }

### generators/generator.cpp   READ docs/testlib.md + START FROM templates/problem/generators/generator.cpp

Start from template (has gen_* namespaces). Fill ONLY Generate_tests().
  void Generate_tests() {
      int n = opt<int>("n", 10);
      cout << n << '
';
      for (int i = 0; i < n; i++)
          cout << rnd.next(-1000000000, 1000000000) << " 
"[i==n-1];
  }

### generators/script.txt   START FROM templates/problem/generators/script.txt

Seed ${s} last. Tests 1..N_samples hand-made (not here). Hit MAX values.
  <#-- Executable name: generator -->
  <#list 1..2 as s>
      generator --n=1 ${s} > $
  </#list>
  <#list 3..10 as s>
      generator --n=1000 ${s} > $
  </#list>
  <#list 11..26 as s>
      generator --n=200000 ${s} > $
  </#list>
  generator --n=200000 --maxval=1000000000 27 > $
  generator --n=200000 --maxval=1000000000 28 > $

### solutions/acc.cpp    START FROM templates/problem/solutions/acc.cpp
### solutions/java.java  START FROM templates/problem/solutions/java.java
### solutions/brute.cpp  START FROM templates/problem/solutions/brute.cpp
### interactor.cpp       START FROM templates/problem/interactor.cpp  (interactive only)

---

## STEP 3 -- LINT

  python polygon_agent.py lint <name>

Scans statement LaTeX for forbidden commands and bare operators.
Fix ALL issues. Do not skip this step.

---

## STEP 4 -- VERIFY

  python polygon_agent.py check <name>

Must print: OK: all N files complete.

---

## STEP 5 -- UPLOAD

  python polygon_agent.py upload <name>

---

## Docs (read before every file)

  docs/statements-tex-manual.md  AUTHORITATIVE Polygon TeX manual (ONLY LaTeX reference)
  docs/testlib.md      testlib API: validator/checker/generator
  docs/interactive.md  Interactive problem guide
  docs/polygon-api.md  API endpoints + solution tags
  templates/problem/   Base templates for ALL files -- always start here

---

## ECPC 2026 compliance

Statement + I/O + constraints + samples.
acc.cpp MA + java.java OK + brute.cpp OK/TL -- all mandatory.
Generator + validator required with usage instructions.
Tests 1-N hand-made, N+1..30 generated hitting MAX values.
Tutorial: Observations + Approach + Complexity -- mandatory.
Tags set on Polygon. ICPC quality. Complete = points. Incomplete = 0.