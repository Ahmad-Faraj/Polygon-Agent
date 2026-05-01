# Polygon API (Official)

This repo uses the official Polygon API.
Reference: https://polygon.codeforces.com/api/

## Endpoints used

- problem.create           Create a new problem, returns {id}
- problem.updateInfo       Set time limit, memory limit, interactive, inputFile, outputFile
- problem.saveTags         Set topic tags. params: problemId, tags (comma-separated string)
- problem.saveStatement    Upload LaTeX statement. params: problemId, lang, name, legend, input, output, notes, tutorial
- problem.saveFile         Upload source file. params: problemId, type=source, name, file
- problem.setValidator     Link validator. params: problemId, validator (filename)
- problem.setChecker       Link checker.   params: problemId, checker (filename)
- problem.saveSolution     Upload solution. params: problemId, name, file, tag, sourceType
- problem.saveScript       Upload FreeMarker test script. params: problemId, testset, source
- problem.saveTest         Upload a sample test. params: problemId, testset, testIndex, testInput, testOutputForStatements
- problem.commitChanges    Commit. params: problemId, message, minorChanges
- problem.buildPackage     Trigger build. params: problemId, full, verify
- problem.packages         Poll build status. params: problemId
- problem.solutions        List uploaded solutions (for verification)
- problem.info             Get problem metadata

## Solution tags
  MA  - Main Accepted (primary correct solution)
  OK  - Accepted (alternative correct solution, e.g. Java)
  TL  - Time Limit (correct but slow - brute force)
  WA  - Wrong Answer (intentionally wrong, for testing checker)
  ML  - Memory Limit

## Solution sourceTypes
  cpp.g++17  - C++17 (GCC)
  java21     - Java 21
  python3    - Python 3

## API Signature format
  <rand>/<method>?param1=value1&param2=value2...#<secret>
  Parameters sorted lexicographically by name then value.
  Signed with SHA-512. rand = 3-byte hex prefix.
