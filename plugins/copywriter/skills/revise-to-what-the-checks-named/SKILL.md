---
name: revise-to-what-the-checks-named
description: The agent changes exactly what a check or a sign-off named and nothing else, and issues the result at a new version, so the checker reads only what moved. Use it when running `ref/hr/post-a-job`.
license: CC-BY-4.0
metadata:
  agent: copywriter
  agent-version: "1"
---

# Revise to what the checks named

## What it does

The agent changes exactly what a check or a sign-off named and nothing
else, and issues the result at a new version, so the checker reads only
what moved.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Revise the Posting**
  - `ref/hr/post-a-job`, activity 9 -
    [Post a Job](../../../../processes/human-resources/post-a-job.md)

## What to record

Every draft at a version, and the DONE records of the patterns it works
inside. A claim it uses cites the register entry it came from.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
