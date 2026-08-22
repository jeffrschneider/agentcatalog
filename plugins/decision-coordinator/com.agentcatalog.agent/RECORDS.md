# The records this abstract agent must leave

This is the contract. An agent implementing `decision-coordinator`
leaves the following behind, on every run.

The decision written down as a question before any evidence is gathered:
what it has to settle, who decides it, what evidence it needs and from
which agent, and the date it is due. The evidence as it came in, each
line attributed to the agent and the source behind it. The candidate
answers, each written out with what it would cost and what it would rule
out. The answer at a version, naming who decided it, on what date, for
what reasons, and anyone who disagreed with what that person said. A
handover line for each agent that has to act on the answer, naming the
agent and what it was given. The review date, set at the moment the
answer is recorded.

An agent that leaves less than this does not implement
`decision-coordinator`, whatever else it does well.
