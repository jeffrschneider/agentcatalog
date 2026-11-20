---
name: send-on-what-cannot-wait
description: Reads each request for what cannot wait, such as a security or safety report, a legal threat or a sign of a takeover, sends it to its owner within the hour, and outside the team's hours pages the person on call and then the next person on the rota. Use it when running `ref/sup/cover-after-hours-requests` and `ref/sup/take-in-a-request`.
license: CC-BY-4.0
metadata:
  agent: request-sorter
  agent-version: "1"
---

# Send on what cannot wait

## What it does

Reads each request for what cannot wait, such as a security or safety
report, a legal threat or a sign of a takeover, sends it to its owner
within the hour, and outside the team's hours pages the person on call
and then the next person on the rota.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Page the Next Person on the Rota**
  - `ref/sup/cover-after-hours-requests`, activity 6 -
    [Cover After-Hours Requests](../../../../processes/customer-support/cover-after-hours-requests.md)
- **Page the Person on Call**
  - `ref/sup/cover-after-hours-requests`, activity 5 -
    [Cover After-Hours Requests](../../../../processes/customer-support/cover-after-hours-requests.md)
- **Send What Cannot Wait to Its Owner**
  - `ref/sup/take-in-a-request`, activity 7 -
    [Take In a Request](../../../../processes/customer-support/take-in-a-request.md)
- **Spot What Cannot Wait**
  - `ref/sup/take-in-a-request`, activity 6 -
    [Take In a Request](../../../../processes/customer-support/take-in-a-request.md)
- **Spot What Cannot Wait for Morning**
  - `ref/sup/cover-after-hours-requests`, activity 4 -
    [Cover After-Hours Requests](../../../../processes/customer-support/cover-after-hours-requests.md)

## What to record

Each request leaves what it was as it arrived, with its channel, its
time and the customer's own words, the account it was matched to with
the details the match rested on or the mark that it matched none, the
case it opened or joined, what it was read against for anything that
cannot wait with the owner told and when, its urgency and topic with the
rule and the version behind each, its service level with the clock
running from its arrival, the marks for a person or an identity check,
and the queue it was placed in, with each move and the specialist's
reason. Each after-hours period leaves each page with its time and who
answered it, each case held with its clock, the order the held cases
were set in, and the hand-over to the morning team. Each surge leaves
the count by symptom, the time the first request arrived and every
request joined to the suspected outage, and each ruled-out alarm the
cases returned to their queues with the engineer's reason. Each routing
change leaves the replay on past requests with every request that would
land elsewhere, and the first live requests checked against the rule.
Nothing in the record shows this agent sending a reply to a customer,
reading out or changing anything in an account, deciding an urgent case
or changing a routing rule.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
