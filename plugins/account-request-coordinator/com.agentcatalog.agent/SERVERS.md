# The systems this abstract agent needs

Twelve systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the support system | write | Each request taken in as it arrived and kept unchanged on its case, the open request marked on the account so that any change to a sign-in detail, the email address or the phone number waits, each acknowledgment and notice sent, and each request closed on the record, with no right to change a sign-in detail or hand over an account. |
| the identity system | read | The details the account held before the request, the holder's first sign-in after a handover, the sessions the approver closed, and the data the system holds about a person, with no right to grant access or change a sign-in detail. |
| the CRM | read | The holder's, the administrators' and the account owner's contacts with the date each was put there, and the data the record holds about a person. |
| the contract repository | read | The agreement's term and notice, the administrators it names, and the signatory's contact. |
| the policy library | read | `<your retention schedule>` at its version, read for what each system keeps after a closure. |
| the billing system | read | The invoices unpaid and the charges still to bill at a closure, and the bills a data request covers, with no right to change a bill. |
| the chat tool | read | The chats a data request covers. |
| the phone system | read | The calls a data request covers. |
| the survey tool | read | The survey answers a data request covers. |
| each system on `<your data map>` | read | The records a data request covers, found and then searched again after a deletion, with no right to correct or delete a record, which its owner does. |
| the data request log | write | Each data request logged with the person, who asked, what they ask for, the route it came by and its deadline, and the request file kept until the run closes. |
| the notification channel | write | The existing contacts and the holder told only through details on file, the signatory asked to confirm through details on file, the account owner told the same day, the billing lead told what is still owed, the customer told the closing date and the closure, and the person told that a data request has arrived, with no contact detail from a request ever used to reply. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
