# The systems this abstract agent needs

Fifteen systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the tool | write | Accounts, roles and configuration are this agent's standing work. |
| the account record | write | Every account with the role it holds and the person who approved it. |
| the configuration record | write | Each change with its date, its version, the request behind it and the way back. |
| the identity system | read | Joiners and leavers, so an account is opened against a job and closed against a leaving record. |
| a non-live environment | write | No change is made straight to live where a copy exists. |
| the flow record | read | What the links either side carry, and when each was last checked. |
| the stack record | read | The entry, the licence, the term and the process the tool runs. |
| the budget record | read | What the sellers cost, read against what is actually used. |
| the identity system | write | A new hire's accounts opened at the job's role and locked until the first day, and a leaver's accounts and remote access closed at the end of the last day, or at the time a named person sets for a dismissal or a layoff. |
| the badge system | write | A leaver's badge closed at the same time as the accounts. |
| each HR system | read | For an access review, the accounts in the HR, payroll, benefits, applicant tracking and learning systems, with each account's role, permissions and last use, and the reports, exports and integrations that carry employee data out, with no right to open an employee's record. |
| the HR system | read | Each current employee's job and each leaving record for the period, which every account in an access review is matched against. |
| the access system | write | Each access, export and link nobody confirmed in an access review, and each one an owner marked to go, removed on the review's close date. |
| the access review record | write | What each check found, what was removed and what was decided, with the signed review. |
| the notification channel | write | Each access owner sent the accesses they answer for, with what each check found and the close date. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
