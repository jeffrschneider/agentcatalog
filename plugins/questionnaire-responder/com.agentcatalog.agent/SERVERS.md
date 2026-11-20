# The systems this abstract agent needs

Twelve systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the answer library | read | Every answer is read from it at a version, and none is written from memory. |
| the evidence store | read | The reports, certificates and policies the answers point at, each at the version the answer names. |
| the CRM | read | The opportunity or investor record the form is attached to and the confidentiality agreement that covers it. |
| the requester's portal | write | The form filed the way the requester asked. |
| the document store | write | The response as sent, its date and its receipt. |
| the answer library | write | Each signed new answer to an investor's questionnaire is added at a version, with its owner, its source and the date it must be read again. |
| the data room | read | The frozen track record and the fund documents the investor's answers rest on, each at its version. |
| the audit records | read | The HR records an employment audit asks for, only as the employee-record-keeper agent pulled them for each request, from the HR, payroll, timekeeping and benefits systems, with the details of people outside the request's scope removed, and a health, investigation or background check record only where its named holder released it for a request counsel confirmed. |
| the tax workpapers | read | The returns, workpapers and transactions a tax auditor's request covers, only as the tax-analyst agent pulled them, with any protected advice counsel holds back left out. |
| the general ledger | read | The figures an answer to a tax auditor or the external auditor traces to. |
| the reconciliation tool | read | The signed reconciliations and schedules an answer to the external auditor is drafted from. |
| the audit portal | read | The external auditor's requests as the audit-coordinator agent logged them, with no right to send an answer. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
