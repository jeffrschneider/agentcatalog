# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the media plan record | write | Each version lands with the date it took effect, and an issued version is never edited. |
| the approved budget for the period | read | At the figure and the version it was approved at. |
| the audience definitions | read | At their versions. |
| the agreed rates, fees and discounts | read |  |
| ad platforms | read | What each channel has delivered against its flight. |
| analytics platforms | read |  |
| the order record | read | What has actually been placed against each line. |
| the notification channel | write | Every agent working to a line is told what changed and from when. |

There is deliberately no buying grant. This agent splits the money and
holds the lines, and the media-buyer agent places it.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
