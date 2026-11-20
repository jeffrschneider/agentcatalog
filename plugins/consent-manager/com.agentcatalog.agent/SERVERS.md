# The systems this abstract agent needs

Ten systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the consent record | write | Every agreement and every withdrawal lands with its date and the place it came from. |
| the suppression lists | write | A withdrawal is written into every list that holds the contact. |
| the contact database | read |  |
| the sending system | read |  |
| the approved rules for the change | read | At the version they were approved at. |
| the live sends | trigger | It stops a send that would break the record. |
| the survey tool | write | A customer who asks not to be surveyed again is taken off every survey list, and nothing else is written there. |
| each system on the data map | read | The copy of a person's contact details each one keeps, with no right to change it. |
| the data request log | write | Each copy found with what it holds, and each deletion confirmed by the owner of the system that holds it. |
| the notification channel | write | Each deletion the privacy lead granted reaches the owner of each system that keeps a copy. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
