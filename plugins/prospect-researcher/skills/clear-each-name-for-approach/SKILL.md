---
name: clear-each-name-for-approach
description: Reads each name on a list against the rules that decide whether it may be approached at all, such as the offering rules, the rules on political contributions to officials who oversee a public pension plan, and the firm's own conflicts. Use it when running `ref/pc/work-an-investor-prospect`.
license: CC-BY-4.0
metadata:
  agent: prospect-researcher
  agent-version: "1"
---

# Clear each name for approach

## What it does

Reads each name on a list against the rules that decide whether it may
be approached at all, such as the offering rules, the rules on political
contributions to officials who oversee a public pension plan, and the
firm's own conflicts. A name that may not be approached is struck with
the rule that struck it, and the list is filled from the next names that
fit.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Check Each Name May Be Approached**
  - `ref/pc/work-an-investor-prospect`, activity 3 -
    [Work an Investor Prospect](../../../../processes/private-capital/work-an-investor-prospect.md)

## What to record

The fit rules as written, at a version, plain enough for another person
to apply without asking. Per person: the account and the role, the
source they came from, the date they were pulled, the verification
result kept apart from the details that failed, and the consent finding
channel by channel with the count the record took out. Per list: the
rank with the inputs and the model version behind it, a reason against
every account the seller dropped or added, the signature with the signer
and the date, the loaded list as it reached the CRM and the sending
system, and the rebuild date with the triggers that force a rebuild
earlier.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
