# Polygon Agent

Describe a problem → agent generates everything → uploads to Polygon.

## Setup

1. Copy `.env.example` to `.env` and fill in your credentials:
   ```
   POLYGON_API_KEY=your_key
   POLYGON_API_SECRET=your_secret
   ```

2. Get your keys from: https://polygon.codeforces.com → Settings → API Keys

## How to use

Open a chat with your LLM agent (opencode, Claude, Copilot, Cursor) and describe your problem:

> Create a problem: given an array of n integers, find the maximum element.
> n up to 200000, values up to 10^9, single test case, 1 second, 256 MB.
> Tags: implementation, sortings

The agent reads `AGENTS.md` and handles everything automatically:
- Scaffolds the problem folder
- Generates all required files (statement, solutions, validator, checker, generator)
- Uploads to Polygon and builds the package

## Example session

```
You:   Create a problem: given n integers find the maximum. n<=200000, a_i<=10^9.
Agent: [runs create, writes 12 files, runs check, uploads]
Agent: Done. URL: https://polygon.codeforces.com/problems/537238
```

## CLI (what the agent runs for you)

```bash
python polygon_agent.py create my_problem --legend "..." --tags "implementation"
python polygon_agent.py check  my_problem
python polygon_agent.py upload my_problem
python polygon_agent.py list
python polygon_agent.py open   my_problem
```

## Example problems

- `problems/two_sum/` — standard non-interactive problem
- `problems/binary_search_interactive/` — interactive problem
