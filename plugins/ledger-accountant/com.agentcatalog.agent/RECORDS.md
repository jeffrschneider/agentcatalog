# The records this abstract agent must leave

This is the contract. An agent implementing `ledger-accountant` leaves
the following behind, on every run.

Each manual entry leaves the request with its reason and the person who
asked, the support behind each line, the entry as prepared with each
line's account, amount, entity, currency and description, the checks of
its accounts, its period and its balance, the approvers the delegation
named and each approval with its date, the posting and the read-back
that shows it posted once and equal to what was approved, any reversal
with its date, and any correction as a reversal and a new entry with the
approval behind each. Each period's accruals leave the accruals reversed
from the last period, the costs received and not yet invoiced, each
budget owner's confirmation or the mark that a cost was accrued without
one, the pay owed with the register behind it, the prepaid costs spread,
the commission taken in with any part marked incomplete, each accrual
set beside the last period with the cause of each one out of line, the
journals with their support and reversal dates, the reviewer's and any
senior approver's approval, the posting, and the schedule handed to the
close. Nothing in the record shows this agent approving an entry,
posting one before its approval, or editing a posted entry in place.

An agent that leaves less than this does not implement
`ledger-accountant`, whatever else it does well.
