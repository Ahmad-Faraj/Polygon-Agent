#!/usr/bin/env python3
"""Polygon Agent: ECPC 2026 compliant create/check/upload CLI."""
import argparse, hashlib, json, os, secrets, shutil, sys, time, webbrowser
import urllib.error, urllib.parse, urllib.request
from pathlib import Path

ROOT          = Path(__file__).resolve().parent
TEMPLATE_ROOT = ROOT / "templates" / "problem"
PROBLEMS_ROOT = ROOT / "problems"
PLACEHOLDER   = "<<<PF_PLACEHOLDER>>>"
POLYGON_BASE  = "https://polygon.codeforces.com"

REQUIRED_FILES = [
    "statement/legend.tex",   "statement/input.tex",
    "statement/output.tex",   "statement/notes.tex",
    "statement/tutorial.tex",
    "validator.cpp",          "checker.cpp",
    "generators/generator.cpp", "generators/script.txt",
    "solutions/acc.cpp",      "solutions/java.java",
    "solutions/brute.cpp",
]

INTERACTOR_FILE = "interactor.cpp"

# ── helpers ──────────────────────────────────────────────────────────

def load_env():
    f, d = ROOT / ".env", {}
    if not f.exists(): return d
    for line in f.read_text(encoding="utf-8", errors="ignore").splitlines():
        s = line.strip()
        if not s or s.startswith("#") or "=" not in s: continue
        k, v = s.split("=", 1)
        d[k.strip()] = v.strip().strip(chr(34)).strip(chr(39))
    return d

def get_credentials():
    e = load_env()
    key    = e.get("POLYGON_API_KEY")    or os.environ.get("POLYGON_API_KEY",    "")
    secret = e.get("POLYGON_API_SECRET") or os.environ.get("POLYGON_API_SECRET", "")
    if not key or not secret:
        raise RuntimeError("Set POLYGON_API_KEY and POLYGON_API_SECRET in .env")
    return key, secret

def api_call(method, params, key, secret):
    payload = {k: str(v) for k, v in params.items() if v is not None}
    payload["apiKey"] = key
    payload["time"]   = str(int(time.time()))
    rand  = secrets.token_hex(3)
    items = sorted(payload.items(), key=lambda x: (x[0], x[1]))
    query = "&".join(f"{k}={v}" for k, v in items)
    sig   = f"{rand}/{method}?{query}#{secret}"
    payload["apiSig"] = rand + hashlib.sha512(sig.encode()).hexdigest()
    req = urllib.request.Request(
        f"{POLYGON_BASE}/api/{method}",
        data=urllib.parse.urlencode(payload).encode(),
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code}: " + exc.read().decode(errors="replace")[:400])
    result = json.loads(body)
    if result.get("status") != "OK":
        raise RuntimeError("API: " + result.get("comment", "unknown error"))
    return result.get("result", {})

def read_text(p):
    text = Path(p).read_text(encoding="utf-8")
    text = text.replace(chr(13)+chr(10), chr(10))  # normalize CRLF to LF
    return text
def title_from_name(n):
    return " ".join(p.capitalize() for p in n.split("_") if p)

def poly_name(n): return n.replace("_", "-").lower()

def read_state(d):
    sp = d / "state.json"
    return json.loads(sp.read_text(encoding="utf-8")) if sp.exists() else {}

def write_state(d, state):
    (d / "state.json").write_text(json.dumps(state, indent=2), encoding="utf-8")

def required_files(spec):
    files = list(REQUIRED_FILES)
    if spec.get("interactive"):
        files.append(INTERACTOR_FILE)
    return files

def scaffold(local_name, spec):
    PROBLEMS_ROOT.mkdir(parents=True, exist_ok=True)
    d = PROBLEMS_ROOT / local_name
    if d.exists(): raise RuntimeError(f"Already exists: {d}")
    shutil.copytree(TEMPLATE_ROOT, d)
    (d / "spec.json").write_text(json.dumps(spec, indent=2), encoding="utf-8")
    write_state(d, {"stage": "scaffolded", "created_utc": int(time.time())})
    return d

def validate_files(d):
    spec = {}
    sp = d / "spec.json"
    if sp.exists():
        spec = json.loads(sp.read_text(encoding="utf-8", errors="ignore"))
    errors = []
    for rel in required_files(spec):
        p = d / rel
        if not p.exists():
            errors.append(f"Missing:     {rel}"); continue
        txt = p.read_text(encoding="utf-8", errors="ignore")
        if not txt.strip():
            errors.append(f"Empty:       {rel}")
        elif PLACEHOLDER in txt:
            errors.append(f"Placeholder: {rel}")
    return errors

# ── upload ───────────────────────────────────────────────────────────

def upload_problem(problem_dir, spec, key, secret):
    samples   = spec.get("samples", [])
    brute_tag   = spec.get("brute_tag", "OK")
    interactive = spec.get("interactive", False)

    # 1. Create
    print("Creating problem on Polygon...")
    r = api_call("problem.create", {"name": spec["name"]}, key, secret)
    pid = int(r["id"])
    print(f"  Problem ID: {pid}  interactive: {interactive}")

    # 2. Info
    print("Setting limits...")
    api_call("problem.updateInfo", {
        "problemId":   pid,
        "timeLimit":   spec["time_limit_ms"],
        "memoryLimit": spec["memory_limit_mb"],
        "interactive": interactive,
        "inputFile":   "",
        "outputFile":  "",
    }, key, secret)

    # 3. Tags
    tags = spec.get("tags", [])
    if tags:
        tag_str = ",".join(tags)
        print(f"  Tags: {tag_str}")
        api_call("problem.saveTags", {"problemId": pid, "tags": tag_str}, key, secret)

    # 4. Statement
    print("Uploading statement...")
    api_call("problem.saveStatement", {
        "problemId": pid, "lang": "english",
        "name":     spec["title"],
        "legend":   read_text(problem_dir / "statement/legend.tex"),
        "input":    read_text(problem_dir / "statement/input.tex"),
        "output":   read_text(problem_dir / "statement/output.tex"),
        "notes":    read_text(problem_dir / "statement/notes.tex"),
        "tutorial": read_text(problem_dir / "statement/tutorial.tex"),
    }, key, secret)

    # 5. Source files (validator, checker, generator; + interactor if interactive)
    print("Uploading source files...")
    source_files = [
        ("validator.cpp", "validator.cpp"),
        ("checker.cpp",   "checker.cpp"),
        ("generator.cpp", "generators/generator.cpp"),
    ]
    if interactive:
        source_files.append(("interactor.cpp", INTERACTOR_FILE))
    for fname, fpath in source_files:
        api_call("problem.saveFile", {
            "problemId": pid, "type": "source",
            "name": fname, "file": read_text(problem_dir / fpath),
        }, key, secret)

    # 6. Link validator + checker
    print("Linking validator and checker...")
    api_call("problem.setValidator", {"problemId": pid, "validator": "validator.cpp"}, key, secret)
    api_call("problem.setChecker",   {"problemId": pid, "checker":   "checker.cpp"},   key, secret)
    if interactive:
        print("Linking interactor...")
        api_call("problem.setInteractor", {"problemId": pid, "interactor": "interactor.cpp"}, key, secret)

    # 7. Solutions: acc (MA), java (OK), brute (OK or TL from spec)
    print(f"Uploading solutions: acc=MA  java={java_tag}  brute={brute_tag}...")
    api_call("problem.saveSolution", {
        "problemId": pid, "name": "acc.cpp",
        "file": read_text(problem_dir / "solutions/acc.cpp"),
        "tag": "MA", "sourceType": "cpp.g++17",
    }, key, secret)
    java_tag = spec.get("java_tag", "OK")
    api_call("problem.saveSolution", {
        "problemId": pid, "name": "java.java",
        "file": read_text(problem_dir / "solutions/java.java"),
        "tag": java_tag, "sourceType": "java21",
    }, key, secret)
    api_call("problem.saveSolution", {
        "problemId": pid, "name": "brute.cpp",
        "file": read_text(problem_dir / "solutions/brute.cpp"),
        "tag": brute_tag, "sourceType": "cpp.g++17",
    }, key, secret)

    # 8. Hand-made tests (samples): tests 1..N, shown in statement
    if samples:
        print(f"Uploading {len(samples)} sample test(s) as tests 1-{len(samples)}...")
    for idx, sample in enumerate(samples, start=1):
        api_call("problem.saveTest", {
            "problemId":              pid,
            "testset":                "tests",
            "testIndex":              idx,
            "testInput":              sample["input"],
            "testOutputForStatements": sample["output"],
            "useInStatements":        True,
            "checkExisting":          False,
        }, key, secret)

    # 9. Generator script → Polygon generates tests N+1..30 server-side
    print("Uploading generator script...")
    api_call("problem.saveScript", {
        "problemId": pid,
        "testset":   "tests",
        "source":    read_text(problem_dir / "generators/script.txt"),
    }, key, secret)

    # 10. Commit
    print("Committing...")
    api_call("problem.commitChanges", {
        "problemId":    pid,
        "message":      "Initial ECPC import",
        "minorChanges": True,
    }, key, secret)

    # 11. Build full package with verification
    #   full=True   → complete package (not just info-only)
    #   verify=True → run all solutions on all tests
    print("Building package...")
    api_call("problem.buildPackage", {
        "problemId": pid, "full": True, "verify": True,
    }, key, secret)

    # 12. Poll for result (up to 6 min) with progress dots
    print("Waiting for package ", end="", flush=True)
    for i in range(72):
        try:
            pkgs = api_call("problem.packages", {"problemId": pid}, key, secret)
            if pkgs:
                pkg   = max(pkgs, key=lambda p: p.get("id", 0))
                state = pkg.get("state", "")
                if state in ("READY", "FAILED"):
                    comment = pkg.get("comment", "")
                    print(f"  Package {state}: {comment}")
                    return pid, state
        except Exception:
            pass
        print(".", end="", flush=True)
        time.sleep(5)
    print("  Timed out.")
    return pid, "UNKNOWN"


def lint_files(d):
    import re
    issues = []
    bs = chr(92)
    statement_files = [
        'statement/legend.tex', 'statement/input.tex', 'statement/output.tex',
        'statement/notes.tex', 'statement/tutorial.tex',
    ]
    forbidden = [
        (bs + 'usepackage',     'usepackage not allowed -- Polygon manages packages'),
        (bs + 'begin{document}','begin{document} not allowed -- Polygon wraps this'),
        (bs + 'documentclass',  'documentclass not allowed'),
        (bs + 'newcommand',     'newcommand not allowed -- no custom macros'),
        (bs + 'section{',       'section not allowed -- use textbf{} for headings'),
        (bs + '[',              'display math not supported in HTML -- use $$ instead of ' + bs + '[ ' + bs + ']'),
        (bs + 'begin{verbatim}','verbatim not allowed -- use texttt{} or t{}'),
    ]
    for rel in statement_files:
        p = d / rel
        if not p.exists(): continue
        txt = p.read_text(encoding='utf-8', errors='ignore')
        for token, msg in forbidden:
            if token in txt:
                issues.append(rel + ': ' + msg)
        no_math = re.sub(r'\$[^$]+\$', '', txt)
        for op in (' <= ', ' >= ', ' != '):
            if op in no_math:
                issues.append(rel + ': bare ' + op.strip() + ' found -- use leq/geq/neq (see docs/latex.md)')
    return issues


def lint_cmd(args):
    d = PROBLEMS_ROOT / args.name
    if not d.exists():
        print('Error: not found: ' + str(d)); return 1
    issues = lint_files(d)
    if issues:
        print('Lint issues (' + str(len(issues)) + '):')
        for issue in issues: print('  ' + issue)
        return 1
    print('Lint OK: no LaTeX issues found.')
    return 0


# -- subcommands --

def create_cmd(args):
    tags = [t.strip() for t in args.tags.split(",") if t.strip()] if args.tags else []
    spec = {
        "name":             poly_name(args.name),
        "title":            args.title or title_from_name(args.name),
        "author":           args.author or "",
        "legend":           args.legend          or "",
        "input":            args.input           or "",
        "output":           args.output          or "",
        "notes":            args.notes           or "",
        "constraints":      args.constraints     or "",
        "solution_idea":    args.solution_idea   or "",
        "time_limit_ms":    args.time_limit,
        "memory_limit_mb":  args.memory_limit,
        "interactive":     args.interactive,
        "multitest":        args.multitest,
        "samples":          json.loads(args.samples) if args.samples else [],
        "tags":             tags,
        "brute_tag":        "OK",
        "statement_language": "english",
    }
    try:
        d = scaffold(args.name, spec)
    except RuntimeError as e:
        print(f"Error: {e}"); return 1
    kind = "interactive " if spec["interactive"] else ""
    print(f"Created {kind}problem: {d}")
    if spec["interactive"]:
        print("  Remember to fill interactor.cpp (13 files total)")
    return 0

def check_cmd(args):
    d = PROBLEMS_ROOT / args.name
    if not d.exists():
        print(f"Error: not found: {d}"); return 1
    spec  = {}
    sp = d / "spec.json"
    if sp.exists():
        spec = json.loads(sp.read_text(encoding="utf-8"))
    errs  = validate_files(d)
    state = read_state(d)
    if errs:
        print(f"Not ready ({len(errs)} issue(s)):")
        for e in errs: print(f"  {e}")
        return 1
    pid        = state.get("problem_id")
    pid_str    = f"  (Polygon ID: {pid})" if pid else ""
    n_required = len(required_files(spec))
    print(f"OK: all {n_required} files complete.{pid_str}")
    return 0

def upload_cmd(args):
    d = PROBLEMS_ROOT / args.name
    if not d.exists():
        print(f"Error: not found: {d}"); return 1
    sp = d / "spec.json"
    if not sp.exists():
        print("Error: spec.json missing"); return 1
    spec  = json.loads(sp.read_text(encoding="utf-8"))
    state = read_state(d)
    if state.get("stage") == "uploaded" and not getattr(args, "force", False):
        pid = state.get("problem_id", "?")
        print(f"Already uploaded (ID {pid}). Use --force to re-upload.")
        print(f"  URL: {POLYGON_BASE}/problems/{pid}")
        return 0
    errs = validate_files(d)
    if errs:
        print("Error: files not ready:")
        for e in errs: print(f"  {e}")
        return 1
    try:
        key, secret = get_credentials()
        pid, pkg_state = upload_problem(d, spec, key, secret)
        state["stage"]        = "uploaded" if pkg_state == "READY" else "upload_failed"
        state["problem_id"]   = pid
        state["polygon_url"]  = f"{POLYGON_BASE}/problems/{pid}"
        state["pkg_state"]    = pkg_state
        state["uploaded_utc"] = int(time.time())
        write_state(d, state)
        if pkg_state == "READY":
            print(f"Done. URL: {POLYGON_BASE}/problems/{pid}")
        else:
            print("Package FAILED. Check error above and Polygon.") 
    except RuntimeError as e:
        print(f"Error: {e}"); return 1
    return 0

def list_cmd(args):
    if not PROBLEMS_ROOT.exists():
        print("No problems directory."); return 0
    problems = sorted([d for d in PROBLEMS_ROOT.iterdir()
                       if d.is_dir() and (d / "spec.json").exists()])
    if not problems:
        print("No problems in problems/"); return 0
    fmt = "{:<3} {:<28} {:<5} {:<16} {:<12} {}"
    print(fmt.format("", "Name", "Type", "Stage", "Polygon ID", "Tags"))
    print("-" * 75)
    for prob_dir in problems:
        spec  = json.loads((prob_dir / "spec.json").read_text(encoding="utf-8"))
        state = read_state(prob_dir)
        name  = prob_dir.name
        stage = state.get("stage", "unknown")
        pid   = str(state.get("problem_id", "-"))
        kind  = "I/A" if spec.get("interactive") else "std"
        tags  = ",".join(spec.get("tags", []))[:24]
        errs  = validate_files(prob_dir)
        mark  = "OK" if not errs else "--"
        print(fmt.format(mark, name, kind, stage, pid, tags))
    return 0

def open_cmd(args):
    d = PROBLEMS_ROOT / args.name
    if not d.exists():
        print(f"Error: not found: {d}"); return 1
    state = read_state(d)
    pid   = state.get("problem_id")
    if not pid:
        print("Not uploaded yet. Run upload first."); return 1
    url = f"{POLYGON_BASE}/problems/{pid}"
    print(f"Opening: {url}")
    webbrowser.open(url)
    return 0

# -- main --

def main():
    p = argparse.ArgumentParser(
        description="Polygon Agent -- ECPC 2026 compliant",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Commands: create check upload list open"
    )
    sub = p.add_subparsers(dest="command", required=True)

    c = sub.add_parser("create", help="Scaffold a new problem folder")
    c.add_argument("name")
    c.add_argument("--title",        help="Display title (default: derived from name)")
    c.add_argument("--author",       help="Problem author name")
    c.add_argument("--legend")
    c.add_argument("--input")
    c.add_argument("--output")
    c.add_argument("--notes")
    c.add_argument("--constraints")
    c.add_argument("--solution-idea", dest="solution_idea")
    c.add_argument("--time-limit",    dest="time_limit",   type=int, default=2000)
    c.add_argument("--memory-limit",  dest="memory_limit", type=int, default=256)
    c.add_argument("--interactive",   action="store_true", help="Interactive problem (adds interactor.cpp)")
    c.add_argument("--multitest",     action="store_true")
    c.add_argument("--samples")
    c.add_argument("--tags",          help="Comma-separated Codeforces tags")

    k = sub.add_parser("check",  help="Verify all 12 files complete")
    k.add_argument("name")

    u = sub.add_parser("upload", help="Upload to Polygon")
    u.add_argument("name")
    u.add_argument("--force", action="store_true", help="Re-upload even if already uploaded")

    lnt = sub.add_parser("lint", help="Scan LaTeX for forbidden commands")
    lnt.add_argument("name")

    sub.add_parser("list",  help="List all local problems with status")

    o = sub.add_parser("open",  help="Open problem on Polygon in browser")
    o.add_argument("name")

    args = p.parse_args()
    return {
        "create": create_cmd,
        "lint":   lint_cmd,
        "check":  check_cmd,
        "upload": upload_cmd,
        "list":   list_cmd,
        "open":   open_cmd,
    }[args.command](args)

if __name__ == "__main__":
    sys.exit(main())
