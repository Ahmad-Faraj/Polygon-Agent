# Agent Instructions -- polygon-agent

This repo creates ECPC 2026 compliant Codeforces Polygon problems end-to-end.
You receive a problem description and deploy it to Polygon with zero manual steps.

## Your 4-step flow (execute all, no stopping)

  1. python polygon_agent.py create <name> --legend "..." --input "..." --output "..."
       --constraints "..." --solution-idea "..." --time-limit <ms> --memory-limit <mb>
       --tags "dp,greedy"  [--interactive]  [--multitest]  [--samples "[{...}]"]

  2. Write all required files in problems/<name>/  (fill every <<<PF_PLACEHOLDER>>>)
     Standard: 12 files.  Interactive (--interactive flag): 13 files (+ interactor.cpp)

  3. python polygon_agent.py check <name>   # must print OK

  4. python polygon_agent.py upload <name>  # deploys to Polygon

Other commands: list (show type/stage/ID), open <name> (browser), upload --force

## Required files

  problems/<name>/
    spec.json               read this first -- all problem metadata
    state.json              stage: scaffolded / uploaded / upload_failed
    statement/
      legend.tex            LaTeX story, 3-5 sentences, hide algorithm
      input.tex             input format + constraints in math mode
      output.tex            output format
      notes.tex             sample explanations (non-empty)
      tutorial.tex          editorial: Observations + Approach + Complexity
    validator.cpp           testlib strict input validator
    checker.cpp             testlib output checker
    generators/
      generator.cpp         testlib generator -- fill Generate_tests() only
      script.txt            FreeMarker script -- Polygon generates tests N+1..30
    solutions/
      acc.cpp               C++17 main solution (tag MA)
      java.java             Java solution, class Main, StreamTokenizer (tag OK)
      brute.cpp             naive correct solution (tag OK or TL from spec.brute_tag)
    interactor.cpp          ONLY for interactive problems (tag set by --interactive)

## LaTeX rules (READ docs/latex.md for full details)

CRITICAL -- these mistakes cause Polygon compile errors or broken rendering:

  ALL variables must be in math mode: $ $ $  (never plain n or a_i)
  Use \leq \geq \neq \times \ldots  (never <=, >=, x, ...)
  Use \t{YES} \t{NO} \t{-1}  for literal tokens
  NEVER write \usepackage or \begin{document} -- Polygon adds these
  NEVER write \newcommand or \section -- use \textbf{} for headings
  Constraints: ( \leq n \leq 10^5$) with --- for em-dash

## Writing each file

legend.tex  -- Short story (3-5 sentences). WHAT not HOW.
input.tex   -- Line-by-line with constraints:  \leq n \leq 2 \times 10^5$.
              If multitest: first line $ ( \leq t \leq ...$), then one test.
output.tex  -- Exactly what to print. YES/NO: state case-insensitive.
notes.tex   -- Explain each sample: In the first example... Use math mode. Non-empty.
tutorial.tex (ECPC mandatory):
  1. Key Observations  2. Solution Approach  3. Complexity Analysis

validator.cpp:
  registerValidation(argc, argv) first.
  inf.readInt(min,max,"name") + readSpace + readEoln after each line + readEof at end.
  Multitest: setTestCase(tc) in loop. ensuref() for sum constraints.
  See docs/testlib.md for full API.

checker.cpp:
  setName("...") MUST be first call. registerTestlibCmd next.
  quitf(_ok/_wa/_fail) with messages. See docs/testlib.md.

generator.cpp -- fill ONLY Generate_tests():
  void Generate_tests() {
      int n = opt<int>("n", 10);
      // add problem-specific opts
      cout << n << '\n';
      // output using rnd.next() / gen_arrays::random / gen_graphs::tree etc.
  }
  Compile:  g++ -std=c++17 -O2 -o generator generators/generator.cpp
  Run:      ./generator --n=1000 <seed> > test.txt

script.txt -- FreeMarker. Tests 1..N_samples are hand-made (DO NOT include here).
  Seed goes LAST as a plain integer. MUST hit MAX constraint values.

  <#-- Executable name: generator -->
  <#list 1..2 as s>
      generator --n=1 ${s} > $
  </#list>
  <#list 3..10 as s>
      generator --n=1000 ${s} > $
  </#list>
  <#list 11..26 as s>
      generator --n=MAX_N ${s} > $
  </#list>
  generator --n=MAX_N --maxval=MAX_VAL 27 > $
  generator --n=MAX_N --maxval=MAX_VAL 28 > $

acc.cpp: Correct C++17. void Solve() + main loop. ios_base::sync_with_stdio(false).
         No freopen. Use '\n' not endl. No warnings.

java.java: Class MUST be Main. BufferedReader + StreamTokenizer (not Scanner).
           Same algorithm as acc.cpp. out.flush() at end.

brute.cpp: Naive/exhaustive. MUST match acc.cpp output on ALL inputs.
           spec.brute_tag: "OK" if passes TL, "TL" if intentionally slow.

## Interactive problems (read docs/interactive.md for full details)

Use --interactive flag on create. Adds interactor.cpp to required files.

interactor.cpp rules:
  registerInteraction(argc, argv) first.
  inf = test file  ouf = contestant stream  tout = jury answer file.
  Use endl (not backslash-n) to send to contestant -- it flushes.
  Terminate with quitf(_ok/_wa/_fail).

acc.cpp for interactive: MUST flush after every output.
  Use cout << x << endl  (NOT cout << x << backslash-n).

java.java for interactive: Use BufferedReader (not StreamTokenizer).
  out.println(x); out.flush();  after EVERY output.

## spec.json fields

name, title, author, legend, input, output, notes, constraints, solution_idea,
time_limit_ms, memory_limit_mb, interactive, multitest, samples,
tags, brute_tag (OK or TL), statement_language

## Upload sequence (polygon_agent.py upload)

problem.create -> updateInfo (interactive flag) -> saveTags -> saveStatement ->
saveFile x3 (+ interactor.cpp if interactive) -> setValidator + setChecker
(+ setInteractor if interactive) ->
saveSolution x3 (acc MA, java OK, brute OK/TL) ->
saveTest xN (samples, useInStatements=True) ->
saveScript -> commitChanges ->
buildPackage (full=True, verify=True) -> poll until READY or FAILED

## ECPC 2026 compliance

- Statement: clear English + I/O + constraints + samples
- Solutions: C++ MA + Java OK + brute OK/TL (all mandatory)
- Generator + validator required (with usage instructions)
- Tests 1-2 hand-made, 3-30 generated hitting MAX constraint values
- Tutorial: Observations + Approach + Complexity (mandatory)
- Tags set on Polygon. ICPC quality. Complete problems only.

## Reference docs

  docs/latex.md        Polygon LaTeX rules + forbidden commands
  docs/testlib.md      testlib API quick reference
  docs/interactive.md  Interactive problem guide
  docs/polygon-api.md  API endpoints + solution tags + source types