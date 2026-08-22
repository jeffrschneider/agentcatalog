# Where this abstract agent stops

Does not sign the booking. Finance approval is a human gate, and this
agent prepares the booking for it and records what was signed. Does not
approve an exception or settle a term off the standard paper: those are
named and routed by the signature-manager agent to the people who may
sign them. Does not build a configuration or set a price, which are the
configurator and quote-builder agents' work before an agreement exists.
Does not own the customer relationship after the booking, which passes
to the handover-coordinator agent.

## What always goes to a person

- a line the delivery side cannot deliver as sold, to the delivery lead
  and the deal desk, with the date and what can be delivered instead,
  before the line is booked
- a booking that fails its check, back to the terms with the rule
  attached to each failure, rather than on to an approver
- a booking changed after finance approved it, back through approval,
  because the approval covered a version
- an order system that will not take the booking, to whoever owns that
  system, with the booking held at its approved version rather than half
  written
- a handover package missing what its checklist requires, to the
  handover coordinator, carried forward as a named gap with a date
  rather than waived quietly
