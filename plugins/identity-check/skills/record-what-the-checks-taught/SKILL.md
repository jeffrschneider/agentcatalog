---
name: record-what-the-checks-taught
description: Records the signs of a takeover seen, the checks genuine customers failed and why, the time the checks took and any pass later found to be wrong. Use it when running `ref/sup/recover-access-to-an-account` and `ref/sup/verify-a-customers-identity`.
license: CC-BY-4.0
metadata:
  agent: identity-check
  agent-version: "1"
---

# Record what the checks taught

## What it does

Records the signs of a takeover seen, the checks genuine customers
failed and why, the time the checks took and any pass later found to be
wrong.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Record What the Check Taught**
  - `ref/sup/verify-a-customers-identity`, activity 14 -
    [Verify a Customer's Identity](../../../../processes/customer-support/verify-a-customers-identity.md)
- **Record What the Request Taught**
  - `ref/sup/recover-access-to-an-account`, activity 16 -
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
