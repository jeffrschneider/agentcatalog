---
name: answer-an-investor-questionnaire
description: Takes in a due diligence questionnaire, holds every answer until the investor's confidentiality agreement is signed, routes each question the library cannot answer to the person who owns the fact, sends the reviewed response in the investor's own format by its deadline, answers the follow-ups through the same checks, and records what went to whom at which version. Use it when running `ref/pc/answer-a-due-diligence-questionnaire` and `ref/pc/work-an-investor-prospect`.
license: CC-BY-4.0
metadata:
  agent: investor-relations-manager
  agent-version: "1"
---

# Answer an investor questionnaire

## What it does

Takes in a due diligence questionnaire, holds every answer until the
investor's confidentiality agreement is signed, routes each question the
library cannot answer to the person who owns the fact, sends the
reviewed response in the investor's own format by its deadline, answers
the follow-ups through the same checks, and records what went to whom at
which version.

## Where it happens

The agent does this in seven activities across two reference processes.
Each one names the activity as that process words it.

- **Answer the Follow-Up Questions**
  - `ref/pc/answer-a-due-diligence-questionnaire`, activity 16 -
    [Answer a Due Diligence Questionnaire](../../../../processes/private-capital/answer-a-due-diligence-questionnaire.md)
  - `ref/pc/work-an-investor-prospect`, activity 12 -
    [Work an Investor Prospect](../../../../processes/private-capital/work-an-investor-prospect.md)
- **Check the Confidentiality Agreement**
  - `ref/pc/answer-a-due-diligence-questionnaire`, activity 2 -
    [Answer a Due Diligence Questionnaire](../../../../processes/private-capital/answer-a-due-diligence-questionnaire.md)
- **Record the Response**
  - `ref/pc/answer-a-due-diligence-questionnaire`, activity 17 -
    [Answer a Due Diligence Questionnaire](../../../../processes/private-capital/answer-a-due-diligence-questionnaire.md)
- **Review the Whole Response**
  - `ref/pc/answer-a-due-diligence-questionnaire`, activity 13 -
    [Answer a Due Diligence Questionnaire](../../../../processes/private-capital/answer-a-due-diligence-questionnaire.md)
- **Route the Unanswered Questions**
  - `ref/pc/answer-a-due-diligence-questionnaire`, activity 7 -
    [Answer a Due Diligence Questionnaire](../../../../processes/private-capital/answer-a-due-diligence-questionnaire.md)
- **Send the Response**
  - `ref/pc/answer-a-due-diligence-questionnaire`, activity 14 -
    [Answer a Due Diligence Questionnaire](../../../../processes/private-capital/answer-a-due-diligence-questionnaire.md)
- **Take in the Questionnaire**
  - `ref/pc/answer-a-due-diligence-questionnaire`, activity 1 -
    [Answer a Due Diligence Questionnaire](../../../../processes/private-capital/answer-a-due-diligence-questionnaire.md)

## What to record

Per prospect: the signed target list it worked from, each approach with
the path and the person who made it, every contact in the CRM with its
date, the investor's interest, questions, size and timing, the
confidentiality agreement and the date the data room opened and to whom,
each follow-up answered with the version of the materials it drew on,
and the stated commitment with its amount and close or the decline with
its reason in the investor's own words and the date to ask again, with
every promise made in a meeting handed to the terms negotiation. Per
fundraising run: each piece at its version naming the frozen figure set
it uses, the case study selection rule written before any deal was
chosen, the compliance approval for each version, the team briefing with
what may and may not be said and who heard it, the released set with the
earlier versions withdrawn, and the records the rules require kept for
their period. Per questionnaire: the form, the deadline, the
confidentiality check, each gap routed with its owner and date, the
lead's review, what was sent to whom on which date at which version, and
the follow-ups still open. Per co-investment: the amount to place, the
entitled list in the policy's order, the agreed offer list, each
candidate's signed confidentiality before any material reached it, one
offer sent alike to all with its fees, carry, broken-deal cost share and
deadline, every question answered to every candidate, each amount in
writing or a silence recorded as a decline, each allocation with its
policy line and the compliance approval, each confirmation, and each
candidate told why it was cut back. Per consent request: the same pack
sent to every member at the same time, every answer sent to all, and who
was told the decision and when. An auditor can check that no investor
saw a figure, an answer or an offer another investor in the same round
did not.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
