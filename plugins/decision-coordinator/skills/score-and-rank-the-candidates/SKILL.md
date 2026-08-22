---
name: score-and-rank-the-candidates
description: Scores each candidate against the criteria already fixed and puts them in one order, with the reason for every place and the evidence it rests on. Use it when running `ref/mkt/content-calendar` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: decision-coordinator
  agent-version: "1"
---

# Score and rank the candidates

## What it does

Scores each candidate against the criteria already fixed and puts them
in one order, with the reason for every place and the evidence it rests
on.

## Where it happens

The agent does this in five activities across four reference processes.
Each one names the activity as that process words it.

- **Compare the Finalists**
  - `ref/mkt/select-marketing-technology`, activity 16 -
    [Select Marketing Technology](../../../../processes/marketing/select-marketing-technology.md)
- **Rank the Requests**
  - `ref/mkt/prioritize-initiatives`, activity 9 -
    [Prioritize Marketing Initiatives](../../../../processes/marketing/prioritize-initiatives.md)
- **Rank the Segments**
  - `ref/mkt/segment-the-market`, activity 13 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)
- **Score the Candidates**
  - `ref/mkt/content-calendar`, activity 8 -
    [Plan Content Calendar](../../../../processes/marketing/content-calendar.md)
- **Weigh the Requests against the Goals**
  - `ref/mkt/prioritize-initiatives`, activity 6 -
    [Prioritize Marketing Initiatives](../../../../processes/marketing/prioritize-initiatives.md)

## What to record

The decision written down as a question before any evidence is gathered:
what it has to settle, who decides it, what evidence it needs and from
which agent, and the date it is due. The evidence as it came in, each
line attributed to the agent and the source behind it. The candidate
answers, each written out with what it would cost and what it would rule
out. The answer at a version, naming who decided it, on what date, for
what reasons, and anyone who disagreed with what that person said. A
handover line for each agent that has to act on the answer, naming the
agent and what it was given. The review date, set at the moment the
answer is recorded.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
