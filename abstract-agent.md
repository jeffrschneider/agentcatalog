# Writing down an abstract agent

An abstract agent is a seat that an agent can hold, described well enough
that any vendor's agent can claim it and any organization can staff a
process with it. It is a job description: what the role does, which
activities it takes on, what it must know how to follow, what it needs to
be granted, what records it must leave, and what it hands to a person.

An abstract agent is deliberately not an implementation. It never names a
model, a prompt, an API, or a vendor. Two agents built entirely
differently can both hold the copywriter seat, and the organization
staffing the seat should not have to care which one it got, because the
seat says everything the process needs from it.

## What an abstract agent is not

- **Not a human role.** Some seats are held only by people - a legal
  reviewer signing an approval, a leader confirming a budget. Those stay
  named roles inside the process, and the process marks them `never`. An
  abstract agent describes a seat an agent may hold, at whatever
  automation level the process sets.
- **Not a tool.** A web scraper, a sentiment scorer, an image generator -
  those are capabilities an agent uses, and they live inside the agent.
  The test: a tool does not hold a seat in a process, take a handoff, or
  leave a DONE record under its own name.
- **Not a product.** A data warehouse, an asset library, a template store
  - those are systems a process binds to, listed under `systems:` in the
  process document.

## The format

```
ABSTRACT AGENT: <name>                id: <slug>   v<version>
purpose: <what the seat does, in one paragraph>
seats:
  <reference process id> / <activity>: <what it does there>
patterns:
  <the collaboration patterns it must be able to follow, and the work
   pattern roles it can hold>
grants:
  <system kind> (<read|write>) - cap: <blank, set by the adopting org>
records:
  <what a run can expect this seat to leave behind>
escalates:
  <what always goes to a person, regardless of automation level>
not:
  <the nearest things this seat does not do>
```

Everything below explains one of those lines.

## Purpose

One paragraph, in plain words, saying what the seat does and for whom.
If the paragraph needs jargon to sound useful, the seat is probably a
tool or a feature rather than an agent.

## Seats

The list of reference processes and activities where this agent works.
This is the line that keeps the catalog honest: an abstract agent earns
its entry by holding seats in real processes, and an entry with no seats
is a capability looking for a job. Every seat line cites a reference
process id, and the reference process's roles column cites back.

## Patterns

The collaboration patterns the agent must be able to follow - sit in a
[briefing](https://github.com/jeffrschneider/agentcollab/blob/main/patterns/briefing.md),
deliver into a
[bake-off](https://github.com/jeffrschneider/agentcollab/blob/main/patterns/bake-off.md),
take a changes-requested from an
[approval](https://github.com/jeffrschneider/agentcollab/blob/main/patterns/approval.md) -
and the [work pattern](https://github.com/jeffrschneider/agentworkpatterns)
roles it can hold, such as a specialist slice in build-by-talent. This is
what makes a fleet possible: two agents that have never met can work
together because both know what the patterns require of their seats.

## Grants

What the seat needs to be given before it can work: which kinds of
systems, at what permission, with what caps. The abstract agent names the
kinds and leaves the caps blank, because a cap is the adopting
organization's decision, written into their process document's bindings.
A media buyer seat says it needs write access to ad platforms and a
daily spend cap; your process says the cap is a number and who set it.

An agent never grants itself anything. Grants flow from the process
document to the seat, which is what makes them auditable.

## Records

What the seat leaves behind: the DONE records of the patterns it
follows, the artifacts it produces at versions, the one-line records of
work done outside any room. The records are how a person checks the work
without opening the agent, and how a concrete agent's claim to implement
this seat can be tested against what it actually leaves.

## Escalates

What always goes to a person, no matter how automated the seat becomes:
the community manager seat escalates a legal threat; the media buyer
seat escalates spend past its cap. Escalation lines are part of the seat
because they survive any change of vendor.

## Claiming a seat

A concrete agent in the catalog claims a seat with one line:
`implements: <slug> v<n>`. The claim is checkable - the seat says what
records it must leave and what patterns it must follow, so a run of any
process that staffs the seat produces the evidence.
