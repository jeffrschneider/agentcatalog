# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| search demand and ranking data sources | read |  |
| the site's search performance data | read |  |
| the content brief store | write | The search requirement lands at a version. |
| the asset store | read | It reads the drafts it checks and edits none of them. |
| the website's content system | read | Titles, headings, addresses and internal links as they actually stand. |
| the help center's search and reading record | read | What customers typed into the help center's search and what each search found, with any personal data removed before anything is shown. |
| the knowledge base | read | The articles a search could have found. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
