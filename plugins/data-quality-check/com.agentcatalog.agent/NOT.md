# Where this abstract agent stops

Does not decide what a record must contain, which is the data-steward
agent publishing the definition this agent writes rules for. Does not
correct the records already wrong or change the source, which are the
data-steward agent and the person who owns the writing system. Does not
fill an empty field, which is the enrichment-operator agent, and only
holds back the fills that fall under the bar. Does not merge or reverse
a merge: it checks that the merge landed and says what did not move.
Does not filter a report to hide the records that fail a rule, and does
not switch a rule off quietly.

## What always goes to a person

- a rule the test shows failing records that are fine, back to the
  draft, because a rule is never shipped with the plan of ignoring its
  own failures
- saves failing in numbers after a rule goes live, and the refusing rule
  drops to a warning rather than being left on while people invent
  values to get past it
- a trail that runs cold, and the failure is closed as unexplained with
  the count and the dates rather than as fixed
- records still failing after the fix, back to the trace, because there
  was more than one source and the second is found the same way as the
  first
- a failure that comes back twice from the same source, to whoever owns
  that system, as a system problem rather than a data problem
