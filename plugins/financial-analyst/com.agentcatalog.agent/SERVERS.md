# The systems this abstract agent needs

Nine systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the data room | read | The company's ledgers, invoices, contracts, bank statements, payroll and tax filings, read only by the people the access agreement names. |
| the request log | write | Each record asked for and each gap found, so the company is asked once. |
| the deal pipeline | write | The agreed numbers and the findings filed against the opportunity at their version. |
| the financial model | write | The operating case, the later rounds or the debt, and each error a second reading finds. |
| the company's financial records | read | Today's numbers for the baseline after the close. |
| the portfolio reporting system | write | Each period's tie-out, every untied figure marked, and the runway and the covenant tests. |
| the value creation plan | read | The targets each period's results are read against. |
| the commitment tracker | read | The changes whose progress it reads against the baseline. |
| the notification channel | write | A short runway or a covenant at risk raised the day it is found. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
