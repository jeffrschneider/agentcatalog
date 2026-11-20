---
name: write-help-articles
description: Writes each article as the steps for the task the customer is trying to do, in plain words from what was gathered and tried, and updates each article a release changes, held unpublished until the release reaches customers. Use it when running `ref/sup/prepare-support-for-a-release` and `ref/sup/write-a-help-article`.
license: CC-BY-4.0
metadata:
  agent: article-writer
  agent-version: "1"
---

# Write help articles

## What it does

Writes each article as the steps for the task the customer is trying to
do, in plain words from what was gathered and tried, and updates each
article a release changes, held unpublished until the release reaches
customers.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Update the Articles**
  - `ref/sup/prepare-support-for-a-release`, activity 5 -
    [Prepare Support for a Release](../../../../processes/customer-support/prepare-support-for-a-release.md)
- **Write the Draft**
  - `ref/sup/write-a-help-article`, activity 4 -
    [Write a Help Article](../../../../processes/customer-support/write-a-help-article.md)

## What to record

Each article leaves its drafts at their versions, the version of the
style guide it was written to, every step walked with the plan and
platform it was walked on and what the product did, each step that did
not work as written and how it was rewritten or held, and each change
the edit, the checks and the owner asked for with the version that made
it. Each saved reply leaves its drafts, the approved content each
statement rests on at its version, the blanks marked, and each revision
set against what was asked. Each release leaves each changed step tried
in the test environment, each difference from what `<your product team>`
described, and the articles and replies updated and held. Each review
leaves every step walked and each step that no longer works as written.
Nothing in the record shows this agent approving or publishing content,
writing a step it did not try, or putting an amount, a date or a
contract term into a saved reply.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
