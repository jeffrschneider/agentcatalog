---
name: keep-bank-accounts-and-signers
description: Takes in each request to open or close a bank account or change a signer, has a leaver's portal access ended on the last day, reads the account as it stands, checks that dual control still holds, moves the payments and the balance of a closing account under their own approvals, fills in the bank's forms, gathers the bank's confirmation for the treasurer, tells the people who use a new account, and keeps the bank account record matched to the bank's own list. Use it when running `ref/fin/change-a-bank-account-or-signer`.
license: CC-BY-4.0
metadata:
  agent: treasury-analyst
  agent-version: "1"
---

# Keep bank accounts and signers

## What it does

Takes in each request to open or close a bank account or change a
signer, has a leaver's portal access ended on the last day, reads the
account as it stands, checks that dual control still holds, moves the
payments and the balance of a closing account under their own approvals,
fills in the bank's forms, gathers the bank's confirmation for the
treasurer, tells the people who use a new account, and keeps the bank
account record matched to the bank's own list.

## Where it happens

The agent does this in twelve activities across one reference process.
Each one names the activity as that process words it.

- **Check Dual Control Still Holds**
  - `ref/fin/change-a-bank-account-or-signer`, activity 5 -
    [Change a Bank Account or Signer](../../../../processes/finance/change-a-bank-account-or-signer.md)
- **Check the Bank's List Against the Record**
  - `ref/fin/change-a-bank-account-or-signer`, activity 16 -
    [Change a Bank Account or Signer](../../../../processes/finance/change-a-bank-account-or-signer.md)
- **Confirm the Change with the Bank**
  - `ref/fin/change-a-bank-account-or-signer`, activity 12 -
    [Change a Bank Account or Signer](../../../../processes/finance/change-a-bank-account-or-signer.md)
- **End a Leaver's Access on the Last Day**
  - `ref/fin/change-a-bank-account-or-signer`, activity 2 -
    [Change a Bank Account or Signer](../../../../processes/finance/change-a-bank-account-or-signer.md)
- **Fill In the Bank's Forms**
  - `ref/fin/change-a-bank-account-or-signer`, activity 9 -
    [Change a Bank Account or Signer](../../../../processes/finance/change-a-bank-account-or-signer.md)
- **Move the Balance of a Closing Account**
  - `ref/fin/change-a-bank-account-or-signer`, activity 8 -
    [Change a Bank Account or Signer](../../../../processes/finance/change-a-bank-account-or-signer.md)
- **Read the Account as It Stands**
  - `ref/fin/change-a-bank-account-or-signer`, activity 3 -
    [Change a Bank Account or Signer](../../../../processes/finance/change-a-bank-account-or-signer.md)
- **Record What the Change Taught**
  - `ref/fin/change-a-bank-account-or-signer`, activity 17 -
    [Change a Bank Account or Signer](../../../../processes/finance/change-a-bank-account-or-signer.md)
- **Redirect a Closing Account**
  - `ref/fin/change-a-bank-account-or-signer`, activity 7 -
    [Change a Bank Account or Signer](../../../../processes/finance/change-a-bank-account-or-signer.md)
- **Take In the Request**
  - `ref/fin/change-a-bank-account-or-signer`, activity 1 -
    [Change a Bank Account or Signer](../../../../processes/finance/change-a-bank-account-or-signer.md)
- **Tell the People Who Use a New Account**
  - `ref/fin/change-a-bank-account-or-signer`, activity 14 -
    [Change a Bank Account or Signer](../../../../processes/finance/change-a-bank-account-or-signer.md)
- **Update the Bank Account Record**
  - `ref/fin/change-a-bank-account-or-signer`, activity 15 -
    [Change a Bank Account or Signer](../../../../processes/finance/change-a-bank-account-or-signer.md)

## What to record

Each morning leaves every account's balance and movements with the
report they came from, each report chased and each account marked
unreported with its last known balance, each movement matched to what
was expected, each item held aside with its amount, its account and its
reference, and the position by account, entity and currency set beside
the minimum and the forecast, with the time it reached the treasurer and
each exception with the decision on it and the person who made it. Each
week leaves the forecast at its version with every line naming its
source and its assumption, every change from the last version traced to
its cause, last week's forecast beside what happened with the reason for
each miss, the headroom in each week, each shortfall with its options
and the CFO's decision, and the people the forecast went to. Each
transfer and each payroll funding leaves the need or the register behind
it, the amount and how it was worked out, the placements set out, the
transfer as prepared, the approval and the release by people who did not
prepare it, the wire-check agent's confirmation of where it landed, each
placement matched to its confirmation, the entries recorded for the
ledger, and any balance between entities on both ledgers. A funding also
leaves its match to the payments that left the payroll account and the
explanation of what was left there. Each bank change leaves the request
with its confirmation through a contact already on file, the time a
leaver's access ended, the account as it stood, the check of dual
control, the approval, the forms as filled in, the bank's confirmation,
the record as updated and the bank's own list set beside it. Each
covenant test leaves each definition as read, each covenant worked out
with every adjustment and its headroom, the undertakings checked, each
risk raised with the date the CFO heard of it, the certificate as
drafted, signed and sent, and the lenders' acknowledgment. Nothing in
the record shows this agent approving or releasing a payment, choosing
how to meet a shortfall, approving a bank change or signing a
certificate.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
