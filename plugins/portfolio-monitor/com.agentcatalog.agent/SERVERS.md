# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the portfolio reporting system | write | Each period, each template, each package as the company sent it and each summary live here, and this agent keeps them. |
| the watch list | write | Each company's level, the reason for every change of level, and the date it came off. |
| the board portal | read | The agenda, the board pack and the company's draft minutes. |
| the data room | read | The executed agreements the fund's information rights, consent rights and director rights are read from. |
| the cap table record | read | The fund's preferences and consent rights, which a company's course depends on. |
| the value creation plan | read | The targets and measures each company's results are read against. |
| the notification channel | write | A warning reaches the deal lead and the board director on the day it is found. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
