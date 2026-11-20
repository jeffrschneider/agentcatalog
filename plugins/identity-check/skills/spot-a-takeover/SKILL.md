---
name: spot-a-takeover
description: Reads each request for the signs of a takeover, such as urgency, pressure, a recent change of contact details or a push to skip a check, and holds a request that shows them with the account untouched for a named team lead. Use it when running `ref/sup/recover-access-to-an-account` and `ref/sup/verify-a-customers-identity`.
license: CC-BY-4.0
metadata:
  agent: identity-check
  agent-version: "1"
---

# Spot a takeover

## What it does

Reads each request for the signs of a takeover, such as urgency,
pressure, a recent change of contact details or a push to skip a check,
and holds a request that shows them with the account untouched for a
named team lead.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Hold a Possible Takeover**
  - `ref/sup/verify-a-customers-identity`, activity 8 -
    [Verify a Customer's Identity](../../../../processes/customer-support/verify-a-customers-identity.md)
- **Look for Signs of a Takeover**
  - `ref/sup/verify-a-customers-identity`, activity 4 -
    [Verify a Customer's Identity](../../../../processes/customer-support/verify-a-customers-identity.md)
- **Read the Request for Signs of Takeover**
  - `ref/sup/recover-access-to-an-account`, activity 4 -
    [Recover Access to an Account](../../../../processes/customer-support/recover-access-to-an-account.md)

## What to record

Each check leaves the action it was for and the account it touched, the
risk level and the version of `<your identity policy>` it was set under,
the contacts, sign-in methods and recent changes read from before the
request arrived with where each was read, each sign of a takeover looked
for and what was found, each check run with the detail on file it ran
against and its result, the authority the person claimed and what the
account, its named contacts or its agreement showed, and the level
reached with the actions it allows. Each held request leaves what was
seen, the check that failed or was pushed against, the team lead it went
to and when, and the account untouched. Each data request made for
someone else leaves the consent, order or mandate read and the privacy
lead's word where it was in doubt. Each period leaves the signs of a
takeover seen, the checks genuine customers failed and why, the time the
checks took, and any pass later found to be wrong. Nothing in the record
shows this agent using a detail the request supplied to confirm it,
clearing a hold, granting access, changing a sign-in detail or handing
over an account.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
