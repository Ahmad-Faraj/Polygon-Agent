# Polygon API Reference

Official docs: https://polygon.codeforces.com/api/

## Endpoints used by polygon_agent.py

problem.create           Create problem, returns {id}
problem.updateInfo       Set timeLimit, memoryLimit, interactive, inputFile, outputFile
problem.saveTags         Set tags. params: problemId, tags (comma-separated string)
problem.saveStatement    Upload LaTeX. params: problemId, lang, name, legend, input, output, notes, tutorial
problem.saveFile         Upload source file. params: problemId, type=source, name, file
problem.setValidator     Link validator. params: problemId, validator (filename)
problem.setChecker       Link checker.   params: problemId, checker (filename)
problem.setInteractor    Link interactor (interactive only). params: problemId, interactor (filename)
problem.saveSolution     Upload solution. params: problemId, name, file, tag, sourceType
problem.saveTest         Upload sample test. params: problemId, testset, testIndex, testInput,
                           testOutputForStatements, useInStatements, checkExisting
problem.saveScript       Upload FreeMarker test script. params: problemId, testset, source
problem.commitChanges    Commit. params: problemId, message, minorChanges
problem.buildPackage     Build. params: problemId, full, verify
problem.packages         Poll build status. params: problemId
problem.solutions        List solutions
problem.info             Get metadata
problems.list            List all problems on account

## Solution tags

MA   Main Accepted (primary C++ solution)
OK   Accepted (Java, alternative correct solution)
TL   Time Limit (correct but intentionally slow -- brute force)
WA   Wrong Answer (intentionally wrong -- for testing checker)
ML   Memory Limit

## Solution sourceTypes

cpp.g++17    C++17 (GCC) -- use for all C++ files
java21       Java 21
python3      Python 3

## API Signature

Format: <rand>/<method>?param1=value1&param2=value2...#<secret>
Params sorted lexicographically by name then value.
Signed with SHA-512. rand = 3-byte hex prefix.

## Interactive problems

Set interactive=True in problem.updateInfo.
Upload interactor.cpp via problem.saveFile.
Then call problem.setInteractor to link it.
Order matters: saveFile must come before setInteractor.
