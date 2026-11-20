# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the general ledger | read | Each entity's closed trial balance and its results before tax after the close entries. |
| the consolidation system | write | Each mapping, the dated rates, each translation, the eliminations and the group entries as prepared, and the consolidated trial balance at its version, with no right to approve a group entry. |
| the source of exchange rates | read | The closing, average and historical rates for each currency, each with its date. |
| the reporting system | write | The statements and the notes at each version, with the tie-out and every change marked. |
| the close calendar | read | The version of the close and the tasks, reconciliations and journals each sign-off covers. |
| the tax workpapers | read | The tax-analyst agent's schedules behind the tax note. |
| the document store | write | The support for each group entry, each note's inputs with their owners' confirmation, and each sign-off. |
| the notification channel | write | A flagged movement reaches its account owner, a late note input reaches its owner and the controller, and the closed figures reach the processes that read them. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
