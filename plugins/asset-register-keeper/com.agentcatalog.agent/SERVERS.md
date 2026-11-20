# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the asset register | write | Each asset with its class, its cost, its service date, its useful life, its location and its owner, each decided disposal and impairment, and each period's depreciation. |
| the lease register | write | Each lease at a version with its term, its payments, its rate, its decided judgments, its schedule and each later period's entries. |
| the ERP | read | Each order and receipt coded to an asset class in the period. |
| the contract repository | read | Each signed lease or change, with every schedule, amendment and side letter it names. |
| the general ledger | write | The period's additions, disposals, impairments and depreciation posted from the register as one batch once the register reviewer has approved it, with no right to approve an entry. |
| the document store | write | The evidence behind each disposal, impairment and judgment, and each owner's confirmation. |
| the notification channel | write | Each owner is asked to confirm an asset or a lease, and each disposal, impairment and judgment reaches the controller. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
