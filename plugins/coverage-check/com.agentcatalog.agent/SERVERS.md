# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the territory map | read | What the carve says it places. |
| the account record | read | What there is to place. |
| the quota record | read | Whether every patch carries exactly one number. |
| the CRM | read | Who the systems say owns each account. |
| the pay plan record | read | Whether a statement matches what will pay on it. |
| the coverage record | write | The findings, per account and per patch. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
