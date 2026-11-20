# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the identity system | read | The contacts, the sign-in methods, the recent sign-ins and any change of contact details on the account as they stood before the request arrived, with no right to change a sign-in detail or to grant access. |
| the support system | write | The checks each action calls for, each check run and the detail on file it ran against, the authority found, the signs of a takeover seen, and each hold, with no right to clear a hold or to change anything in the account. |
| the CRM | read | The account's named contacts and the authority each one holds. |
| the contract repository | read | The signatory and the administrators an agreement names, for a claim to close or take control of a business account. |
| the policy library | read | `<your identity policy>` at its version, with the checks each risk level calls for and the signs of a takeover it names, and `<your jurisdiction's rules on data requests>` for a request made for someone else. |
| the notification channel | write | Each code sent only to a contact the company held before the request arrived, and each hold sent to the team lead with the case beside it. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
