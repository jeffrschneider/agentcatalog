# The records this abstract agent must leave

This is the contract. An agent implementing `coverage-check` leaves the
following behind, on every run.

Per check: every account in no patch and every account in two, named
rather than counted; every patch nobody holds and every seller holding
more than one; every patch over the stated account count or amount and
every patch under the floor, each failure naming the rule it failed.
Reading last period, it names which patches were worked, which were
never called, and what was left with no owner at all. Reading
statements, it names every place a page and the system that will pay on
it disagree, by seller. Reading a move, it quotes the line of the carve
that allows it as written, or records that no line covers it. Every
finding carries the version of the map and the quota set it was tested
against, so an auditor can rerun it.

An agent that leaves less than this does not implement `coverage-check`,
whatever else it does well.
