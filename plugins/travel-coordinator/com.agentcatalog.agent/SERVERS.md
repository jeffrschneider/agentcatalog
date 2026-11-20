# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the travel booking tool | write | Each request, the options offered, each booking, change and cancellation, and each unused ticket and credit. |
| the travel agency's booking channel | write | Each booking made on the central travel account or the traveler's company card at the option chosen or approved, with no right to pay a supplier. |
| the HR system | read | The traveler's manager and any need the traveler has recorded, such as an accessible room. |
| the expense tool | write | Each booking's cost, its reference and the way it was paid. |
| the notification channel | write | The options and the itinerary reach the traveler, an exception reaches the named approver, and the list of who is where reaches the travel and expense lead in an emergency. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
