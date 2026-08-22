---
name: test-another-company-technology
description: Runs the other company's product against our own real cases and reads what that product depends on, naming the licenses and the third parties behind it, so a dependency that would block embedding or reselling is found while the deal can still change. Use it when running `ref/prt/run-alliance-diligence`.
license: CC-BY-4.0
metadata:
  agent: integration-planner
  agent-version: "1"
---

# Test another company technology

## What it does

Runs the other company's product against our own real cases and reads
what that product depends on, naming the licenses and the third parties
behind it, so a dependency that would block embedding or reselling is
found while the deal can still change.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Read the Dependencies**
  - `ref/prt/run-alliance-diligence`, activity 9 -
    [Run Alliance Diligence](../../../../processes/partners/run-alliance-diligence.md)
- **Test the Technology**
  - `ref/prt/run-alliance-diligence`, activity 8 -
    [Run Alliance Diligence](../../../../processes/partners/run-alliance-diligence.md)

## What to record

Every technical obligation the signed agreement creates, with the date
it comes due. The scope, saying what connects and what deliberately does
not. The design at a version: interfaces, data, identity and the limits
each side agreed to. The environment plan, naming the test systems and
test accounts on both sides and what data they hold. The build and the
end to end test, with what passed and what did not. The joint pilot with
one named customer, what both sides watched, and what it showed. In
diligence, the technology test naming which of our real cases were run
and how each came out, and the dependency read naming the licenses, the
third parties and what the product depends on. The readiness check
against the list, item by item, with any waiver naming who waived it and
the risk they accepted. The handover to partner management.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
