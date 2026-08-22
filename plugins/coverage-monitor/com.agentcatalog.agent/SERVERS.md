# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| news and trade press sources | read | Within the subscriptions and licenses the organization actually holds. |
| research firm publications | read |  |
| review sites and public forums | read |  |
| social platforms | read |  |
| the coverage record | write | Every mention lands here with its date and its source. |
| the press and analyst contact record | read |  |
| the announcement and incident timelines | read | What went out, and when it went out. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
