# The systems this abstract agent needs

Ten systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the side letter register | read | Every side letter at its version, for exclusions, excused investors and co-investment rights. |
| the restricted list | read | The company, its owners and the counterparties are checked against it, and each sale is cleared against it. |
| the conflicts register | write | Every conflict found, with the chief compliance officer's decision and any condition. |
| the fund accounting system | read | Commitments, holdings and the share of the fund a deal or a position would take. |
| the fund model | read | The capital left and the effect on the fund, as the fund-modeler agent issues them. |
| the deal pipeline | write | The dated result on the opportunity, withdrawn when the deal changes. |
| the allocation record | write | Each co-investment allocation with the policy line behind it. |
| the decision record | read | The advisory committee decisions in force and the conditions each consent carried. |
| the cap table record | read | The listed position a sell-down plan sells from. |
| the notification channel | write | The deal team told the same day a hard exclusion or an ended investment period blocks a deal. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
