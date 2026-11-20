# The systems this abstract agent needs

Twelve systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the contract repository | read | The executed document at a version, with every exhibit and amendment it names. |
| the signature system | write | The document goes to the named signers in order, and comes back out of there when a deal is lost. |
| the entity list | read | The entity that buys and the one that sells, matched to what the organization holds rather than to the address block on the paper. |
| the approval record | read | Which term off the standard paper is signed for, by whom, against which version. |
| the notification channel | write | The people who act on a booking hear the same booking at the same time. |
| the document store | write | The executed set and the close record, filed complete with every signed page and exhibit. |
| the investor portal | write | Each investor's close date, its accepted commitment and its signed pages, posted where the investor reads them. |
| the deal pipeline | write | Each confidentiality agreement's non-solicit, standstill and term, and the people it lets read the material, recorded where every deal team can read them. |
| the applicant tracking system | write | Each executed offer filed against the candidate with every document it names, and nothing else in the candidate's record changed. |
| the restricted records store | write | For separation agreements only, the executed agreement and its negotiation log filed at their executed versions where only the people on the agreement's access list can open them, with no right to open any other record held there. |
| the delegation of authority | read | Who signs a supplier agreement or a bank's forms for the company, up to what amount and in what order, at the version in force. |
| the bank account record | write | Each bank's executed account and signer forms filed with the approval and the resolution they rest on, with no right to change an account, a signer or a mandate. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
