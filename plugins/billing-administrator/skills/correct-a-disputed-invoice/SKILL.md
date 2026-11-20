---
name: correct-a-disputed-invoice
description: Recomputes the disputed lines on their own from the same records, drafts the credit note or the replacement for exactly what was decided, and issues it once the named approver has approved it. Use it when running `ref/fin/resolve-a-billing-dispute`, `ref/sup/decide-a-refund-request` and `ref/sup/offer-a-goodwill-credit`.
license: CC-BY-4.0
metadata:
  agent: billing-administrator
  agent-version: "1"
---

# Correct a disputed invoice

## What it does

Recomputes the disputed lines on their own from the same records, drafts
the credit note or the replacement for exactly what was decided, and
issues it once the named approver has approved it. The same work issues
the credit note for a refund or a goodwill credit a named person in
support decided, once that person has approved it.

## Where it happens

The agent does this in five activities across three reference processes.
Each one names the activity as that process words it.

- **Draft the Credit Note**
  - `ref/sup/decide-a-refund-request`, activity 10 -
    [Decide a Refund Request](../../../../processes/customer-support/decide-a-refund-request.md)
  - `ref/sup/offer-a-goodwill-credit`, activity 9 -
    [Offer a Goodwill Credit](../../../../processes/customer-support/offer-a-goodwill-credit.md)
- **Draft the Credit Note or Replacement**
  - `ref/fin/resolve-a-billing-dispute`, activity 11 -
    [Resolve a Billing Dispute](../../../../processes/finance/resolve-a-billing-dispute.md)
- **Issue the Credit Note**
  - `ref/sup/decide-a-refund-request`, activity 12 -
    [Decide a Refund Request](../../../../processes/customer-support/decide-a-refund-request.md)
  - `ref/sup/offer-a-goodwill-credit`, activity 11 -
    [Offer a Goodwill Credit](../../../../processes/customer-support/offer-a-goodwill-credit.md)
- **Issue the Credit Note and Any Replacement**
  - `ref/fin/resolve-a-billing-dispute`, activity 13 -
    [Resolve a Billing Dispute](../../../../processes/finance/resolve-a-billing-dispute.md)
- **Recompute the Invoice Independently**
  - `ref/fin/resolve-a-billing-dispute`, activity 7 -
    [Resolve a Billing Dispute](../../../../processes/finance/resolve-a-billing-dispute.md)

## What to record

Each invoice leaves its billing date, the booking at its version with
each field naming its clause, the usage reading with its date or the
reason it was held, each line with its price, its tax and the place it
was supplied, the check against the local rules and against the booking
with the total beside the last invoice, and the billing lead's approval
where the policy asks for it. Beside them sit the number in its series,
the dates it was issued and sent, the channel it went by, the customer's
receipt or the portal's rejection with its reason, and how a rejected
invoice was put right. Each disputed invoice leaves the recompute beside
the original with every input where they differ, the credit note or
replacement at its version for exactly what was decided with its
approval, and the cause sent to its owner. Nothing in the record shows
this agent editing an issued invoice, approving an invoice or a credit
note, or billing on an estimate nobody approved.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
