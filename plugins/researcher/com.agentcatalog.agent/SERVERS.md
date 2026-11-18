# The systems this abstract agent needs

Ten systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| public and licensed sources | read | Within the subscriptions and licenses the organization actually holds. |
| paid reports and data | read | Cap: what it may buy without asking, set by the adopting organization. |
| internal data sources | read |  |
| the source record | write | Every fact lands with where it came from. |
| the claims register | read |  |
| the data room | read | A company's customer records and the other material diligence is given, read only as the access agreement allows. |
| the expert network | read | Industry experts called under the firm's call rules. |
| the calendar | write | The customer and expert calls it arranges. |
| the screening service | read | A chosen candidate's background checks. |
| the consent record | read | The candidate's written consent, read before any background check runs or any reference the candidate did not name is taken. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
