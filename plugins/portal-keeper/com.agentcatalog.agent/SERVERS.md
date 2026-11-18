# The systems this abstract agent needs

Ten systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the identity system | write | Cap: accounts per partner or investor, set by the adopting organization. |
| the partner portal | write | Visibility, published material and the list of who is certified. |
| the investor portal and data room | write | What each investor and prospective investor can see, and the documents, notices and statements published to them. |
| deal registration | write | A deal is registered against the partner with its protection period. |
| the support desk | write | The partner's or investor's route to help opens and closes with the rest of their access. |
| the licensing system | write | What the partner may issue, opened against what the agreement covers. |
| the certification record | read | Nobody is entitled by a certificate they do not hold. |
| the document store | write | The approved fundraising set is released there at its version, and earlier versions are withdrawn from use. |
| the CRM | read | The signed confidentiality agreement and the people each prospective investor named, which every folder's access rests on. |
| the notification channel | write | Every named contact hears that a notice, a statement or a tax document is waiting for them. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
