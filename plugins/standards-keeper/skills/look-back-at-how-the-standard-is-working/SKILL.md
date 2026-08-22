---
name: look-back-at-how-the-standard-is-working
description: Reports how the rules are behaving in practice, naming the ones that keep failing, the ones nobody applies, and what is worth repeating or avoiding the next time a version is written. Use it when running `ref/mkt/attribution-model` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: standards-keeper
  agent-version: "1"
---

# Look back at how the standard is working

## What it does

Reports how the rules are behaving in practice, naming the ones that
keep failing, the ones nobody applies, and what is worth repeating or
avoiding the next time a version is written.

## Where it happens

The agent does this in two activities across four reference processes.
Each one names the activity as that process words it.

- **Record What Was Learned**
  - `ref/mkt/attribution-model`, activity 16 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)
  - `ref/mkt/brand-guidelines`, activity 16 -
    [Publish Brand Guidelines](../../../../processes/marketing/brand-guidelines.md)
  - `ref/mkt/brand-refresh`, activity 26 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)
- **Watch How the Rules Score**
  - `ref/mkt/brand-voice`, activity 18 -
    [Define Brand Voice and Messaging](../../../../processes/marketing/brand-voice.md)

## What to record

Every standard at a numbered version, with the date it took effect and
the date it stopped being current. A change record for each version,
saying what changed, what it replaced, who approved it, and when. Every
earlier version left readable at its own number, so work can be judged
against the standard it was made under. Every interpretation it issued,
attached to the rule and the version it interprets, carrying the
question that prompted it and the agent that asked. A dated record of
who was told about each change.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
