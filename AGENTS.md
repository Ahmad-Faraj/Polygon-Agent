# Agent Instructions -- polygon-agent

This repo creates ECPC 2026 compliant Codeforces Polygon problems end-to-end.
You receive a problem description and deploy it to Polygon with zero manual steps.

## Your 4-step flow (execute all, no stopping)

  1. python polygon_agent.py create name --legend ... --input ... --output ...
       --constraints ... --solution-idea ... --time-limit ms --memory-limit mb
       --tags dp,greedy  [--multitest]  [--samples [{...}]]

  2. Write all 12 files in problems/name/  (fill every <<<PF_PLACEHOLDER>>>)

  3. python polygon_agent.py check name   # must print OK

  4. python polygon_agent.py upload name  # deploys to Polygon

Other commands: list (show all problems), open name (browser), upload --force

## 12 required files

  problems/name/
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

## Writing each file

legend.tex  -- Short story (3-5 sentences). WHAT not HOW.
              All variables in math mode: n, a_i. LaTeX: leq geq neq times ldots

input.tex   -- Line-by-line. Constraints inline in math mode.
              Multitest: first line t, then one test. State sum constraints.

output.tex  -- Exactly what to print. YES/NO: state case-insensitive.

notes.tex   -- Explain each sample: In the first example... Math mode. Non-empty.

tutorial.tex (ECPC mandatory) -- Three sections:
  1. Key Observations
  2. Solution Approach
  3. Complexity Analysis (time + space)

validator.cpp -- registerValidation first. readInt(min,max,name) + readSpace +
  readEoln after each line + readEof at end. setTestCase(tc) in multitest.
  ensuref() for sum constraints.

checker.cpp -- setName(...) MUST be first call. registerTestlibCmd next.
  quitf(_ok/_wa/_fail) with messages. Multitest: while(!ans.seekEof()) loop.

generator.cpp -- Template has gen_numbers/gen_arrays/gen_strings/gen_graphs/gen_utils.
  Fill ONLY Generate_tests():
    void Generate_tests() {
        int n = opt<int>(n, 10);
        // add problem-specific opts
        cout << n << '\n';
        // output test case using rnd.next / gen_arrays / etc.
    }
  Generator usage (ECPC requires usage instructions):
    Compile: g++ -std=c++17 -O2 -o generator generators/generator.cpp
    Run:     ./generator --n=1000 seed > test.txt

script.txt -- Tests 1..N_samples are hand-made (DO NOT list here).
  Script generates tests N+1..30. Seed goes LAST. MUST hit MAX constraint values.
  Template:
    <#-- Executable name: generator -->
    <#list 1..2 as s>
        generator --n=1  > $
    </#list>
    <#list 3..10 as s>
        generator --n=1000  > $
    </#list>
    <#list 11..26 as s>
        generator --n=MAX_N  > $
    </#list>
    generator --n=MAX_N --maxval=MAX_VAL 27 > $
    generator --n=MAX_N --maxval=MAX_VAL 28 > $

acc.cpp -- Correct C++17. void Solve() + main loop. ios_base::sync_with_stdio(false).
  No freopen. Use '\n' not endl in output.

java.java -- Class MUST be Main. BufferedReader + StreamTokenizer (not Scanner).
  Same algorithm as acc.cpp. out.println() + out.flush() in main.

brute.cpp -- Naive/exhaustive, obviously correct. Same output as acc.cpp.
  spec.brute_tag: OK if passes TL, TL if intentionally slow.

## spec.json fields

name, title, author, legend, input, output, notes, constraints, solution_idea,
time_limit_ms, memory_limit_mb, multitest, samples, tags, brute_tag, statement_language

## Upload sequence (polygon_agent.py upload)

problem.create -> updateInfo -> saveTags -> saveStatement ->
saveFile x3 -> setValidator + setChecker ->
saveSolution x3 (acc MA, java OK, brute OK/TL) ->
saveTest xN (samples, useInStatements=True) ->
saveScript -> commitChanges ->
buildPackage (full=True, verify=True) -> poll until READY or FAILED

## ECPC 2026 compliance

- Statement: clear English + I/O + constraints + samples
- Solutions: C++ MA + Java OK + brute OK/TL (all mandatory)
- Generator + validator required (with usage instructions)
- Tests 1-2 hand-made, 3-30 generated hitting MAX constraint values
- Tutorial mandatory: Observations + Approach + Complexity
- Tags set on Polygon. ICPC quality. Complete problems only.