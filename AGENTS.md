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

### statement/legend.tex   READ docs/statements-tex-manual.md  (PRIMARY SOURCE)

Short story, 3-5 sentences. WHAT to compute, not HOW.

VALID POLYGON LATEX -- copy this style exactly:

  $Faraj$ has an array $a_1, a_2, \ldots, a_n$ and a target $T$.
  He wants two indices $i \neq j$ such that $a_i + a_j = T$.
  Find such a pair or report that none exists.

More valid patterns (from real problems):
  \bf{(1,1)}                bold coordinate
  $n \times m$ grid
  $(1 \leq t \leq 10)$   inline constraint
  $a_1, a_2, \ldots, a_n$
  $a_1 + a_2 + \cdots + a_n$
  $\cdots$  $\blacksquare$  \large{text}
  \begin{itemize}
    \item Ladder from \bf{(3 $\longrightarrow$ 12)}.
  \end{itemize}
  \begin{enumerate}
    \item We start at cell \bf{(1)}.
  \end{enumerate}
  \begin{center} centered block \end{center}

Rules -- violations BREAK Polygon:
  ALL variables in math mode: $n$  $a_i$  $k$  (never plain text)
  Symbols: \leq  \geq  \neq  \times  \ldots  \cdots  (never <= >= ...)
  Bold: \textbf{text} or \bf{text}    Italic: \textit{text}
  Literal tokens: \t{YES}  \t{NO}  \t{-1}  \t{-1 -1}
  Em-dash: ---  (three dashes, never - or --)
  NEVER: \usepackage  \begin{document}  \documentclass  \newcommand  \section

### statement/input.tex   READ docs/statements-tex-manual.md

  The first line contains $t$ $(1 \leq t \leq 10^4)$ --- the number of test cases.
  Each test case: $n$ $(1 \leq n \leq 2 \times 10^5)$.
  Integers $a_1, \ldots, a_n$ $(-10^9 \leq a_i \leq 10^9)$.
  Sum of $n$ over all test cases does not exceed $2 \times 10^5$.

### statement/output.tex   READ docs/statements-tex-manual.md

  Print a single integer --- the answer.
  YES/NO add: You may print each letter in any case (\t{YES}, \t{Yes} are accepted).

### statement/notes.tex   READ docs/statements-tex-manual.md

  In the first example, $n=4$. Pair $(2,4)$ gives $a_2+a_4=2+4=6=T$.
  Must be non-empty.

### statement/tutorial.tex   READ docs/statements-tex-manual.md

ECPC mandatory -- three sections:
  \textbf{Key Observations}
  \begin{enumerate}
      \item Observation with proof.
  \end{enumerate}
  \textbf{Solution Approach}
  Algorithm step by step.
  \textbf{Complexity Analysis}
  \begin{itemize}
      \item \textbf{Time}: $O(n \log n)$ --- reason.
      \item \textbf{Space}: $O(n)$ --- reason.
  \end{itemize}

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

  docs/statements-tex-manual.md  AUTHORITATIVE Polygon TeX manual (read first)
  docs/latex.md                  LaTeX rules + valid examples from real problems
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