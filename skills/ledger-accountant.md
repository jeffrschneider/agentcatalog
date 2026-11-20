# ledger-accountant

## prepare-an-entry

Takes in each request for an entry that no system feed produces with its
reason, gathers the support behind each line, and drafts the entry with
each line's account, amount, entity, currency and description, including
the entry that brings a lease onto the books from its schedule.

covers:
- Gather the Support
- Prepare the Entry
- Prepare the Opening Entry
- Take In the Request

## check-an-entry

Reads every account in an entry as open and allowed for manual entries,
reads the period as still open, and checks that debits equal credits in
each entity and each currency and that every amount equals the support
or the schedule behind it.

covers:
- Check That the Entry Balances
- Check the Accounts and the Period
- Check the Opening Entry

## post-and-keep-entries

Posts each entry only once the named approvers who did not prepare it
have approved it, whether a manual entry, a close journal, a clearing
entry, a correcting entry or a lease opening entry, reads the posting
back, schedules any reversal, corrects a wrong posting by reversing it,
and files the entry with its support and its approvals.

covers:
- Correct What the Check Found
- Correct a Posted Entry
- File the Entry
- Post the Clearing Entries
- Post the Close Journals
- Post the Entry
- Post the Opening Entry
- Read the Posting Back
- Record What the Entry Taught
- Schedule the Reversal

## book-the-accruals

Opens each period's accruals, reverses the ones the last period marked
to reverse, works out the pay owed, the prepaid costs to spread and the
price of each cost received and not yet invoiced, sets each accrual
beside the last period and the invoices since, prepares and posts the
approved accrual journals with their reversal dates, and hands the
schedule to the close.

covers:
- Book the Accruals
- Check Each Accrual Against the Last Period
- Confirm Costs With No Order
- Hand the Schedule to the Close
- Open the Period's Accruals
- Post the Accruals
- Prepare the Accrual Journals
- Price the Cost Accruals
- Record What the Period Taught
- Reverse the Last Period's Accruals
- Work Out the Pay Owed
- Work Out the Prepaid Costs to Spread
