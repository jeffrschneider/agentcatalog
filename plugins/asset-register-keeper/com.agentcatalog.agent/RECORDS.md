# The records this abstract agent must leave

This is the contract. An agent implementing `asset-register-keeper`
leaves the following behind, on every run.

Each period leaves the register as it stood at the last close, each cost
read as an asset or an expense with the reason, each new asset with its
class, its cost, its service date, its useful life, its location and its
owner and the owner's confirmation, each disposal and transfer with the
owner's report and its evidence, and the result of each check against
what exists, with each asset marked found, missing, idle or damaged.
Beside them sit each disposal and impairment as set out with its
carrying value, any proceeds and its effect, the controller's decision
and any senior approval, each asset's depreciation for the period, the
reviewer's approval, the batch posted to the ledger, and the register
and its totals handed to the close. Each lease leaves the lease and
every document it names, its term, its payments and its options each
with the clause it came from, the lease owner's answer, each judgment
with its effect beside the controller's decision in writing, the lease
as entered at its version, the schedule, and each later period's entries
set to post. Nothing in the record shows this agent deciding a disposal,
an impairment or a judgment, or posting anything the reviewer has not
approved.

An agent that leaves less than this does not implement
`asset-register-keeper`, whatever else it does well.
