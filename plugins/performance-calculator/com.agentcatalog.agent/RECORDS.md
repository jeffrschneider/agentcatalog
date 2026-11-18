# The records this abstract agent must leave

This is the contract. An agent implementing `performance-calculator`
leaves the following behind, on every run.

Each run starts from the performance method at a version, written and
dated before any figure, naming which deals and funds are included, how
fees, carried interest and any credit line are treated, and the date the
figures are taken at. Every deal's dated cash flows and its mark are
recorded with their source. The track record gives the IRR and each
multiple by deal and by fund, gross and net side by side, and the
attribution of each deal's gain, with the losses attributed the same
way. Each figure is traced to the audited statements, or to the books
where the audit does not reach, with every difference and its
explanation. The frozen set carries its date and version, and the run
records which documents were told to use it. The method, the workpapers,
the approvals and every version sent are kept for the retention period.
Each quarter leaves the IRR and the multiples for the fund and for each
holding, gross and net, with the effect of the credit line shown and the
method version named. Any figure can be recomputed from the recorded
cash flows, marks and method.

An agent that leaves less than this does not implement
`performance-calculator`, whatever else it does well.
