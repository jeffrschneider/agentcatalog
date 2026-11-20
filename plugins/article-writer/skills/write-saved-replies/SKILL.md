---
name: write-saved-replies
description: Drafts each saved reply in plain words from approved content only, marks the blanks a support specialist fills in, revises it to exactly what the checks and the owner asked for, and updates each reply a release changes. Use it when running `ref/sup/prepare-support-for-a-release` and `ref/sup/publish-a-saved-reply`.
license: CC-BY-4.0
metadata:
  agent: article-writer
  agent-version: "1"
---

# Write saved replies

## What it does

Drafts each saved reply in plain words from approved content only, marks
the blanks a support specialist fills in, revises it to exactly what the
checks and the owner asked for, and updates each reply a release
changes.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Draft the Reply**
  - `ref/sup/publish-a-saved-reply`, activity 5 -
    [Publish a Saved Reply](../../../../processes/customer-support/publish-a-saved-reply.md)
- **Mark What the Specialist Fills In**
  - `ref/sup/publish-a-saved-reply`, activity 6 -
    [Publish a Saved Reply](../../../../processes/customer-support/publish-a-saved-reply.md)
- **Revise the Reply**
  - `ref/sup/publish-a-saved-reply`, activity 10 -
    [Publish a Saved Reply](../../../../processes/customer-support/publish-a-saved-reply.md)
- **Update the Saved Replies**
  - `ref/sup/prepare-support-for-a-release`, activity 6 -
    [Prepare Support for a Release](../../../../processes/customer-support/prepare-support-for-a-release.md)

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
