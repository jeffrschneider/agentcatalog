# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the CRM | write | The merge is written, and the losing record closes as merged with a pointer to the survivor. |
| the activity history | write | Activities repoint at the surviving id. |
| the marketing database | write | List memberships and open tasks repoint with everything else. |
| the file store | write | Attachments move with the record they belong to. |
| the matching model at its version | read | The score, and the inputs it was computed from. |
| the review queue | write | Anything under the bar waits there for a person. |
| the data warehouse | read | The counts read before and after. |
| the ERP | read | Every supplier record's legal name, trading name, tax number, address and bank account, searched before a second record is made, with no right to change or merge a supplier record. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
