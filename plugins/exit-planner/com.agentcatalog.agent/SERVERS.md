# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the deal pipeline | write | The reason to exit, the exit paper, the approved plan, and a sale's status and result. |
| the data room | write | The documents indexed and the access set buyer by buyer, with every view logged. |
| the cap table record | read | The fund's shares, their preferences, and the drag-along, tag-along and registration rights. |
| the portfolio reporting system | read | The company's condition and how far its plan has delivered. |
| market data sources | read | Recent sales and listings, the multiples paid, and the share price through a sell-down. |
| the restricted list | read | Whether a sale of listed shares may be placed at all. |
| the brokerage account | read | Each order's fills against its limit and the shares left to sell, since a named person signs each order and the broker works it. |
| the notification channel | write | A bid below the floor, a closed window or a missed deadline reaches the deal lead the same day. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
