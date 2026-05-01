# Polygon Agent

Describe a problem to your LLM agent and it creates and uploads it to Polygon. Zero manual steps.

## Setup

1. Copy `.env.example` to `.env` and add your credentials:
   - Get them at https://polygon.codeforces.com → Settings → API Keys

## How to use

Open your LLM agent and send this prompt (replace the bracketed part with your problem):

> You are working inside the polygon-agent repo. Read AGENTS.md and follow it exactly.
> Create and upload this problem to Polygon:
> [describe your problem here — name, story, input/output, constraints, solution idea, tags]

The agent will scaffold the problem, generate all files, lint them, verify, and upload.
Do not ask it to do anything else.
