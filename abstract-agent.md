# How to write an abstract agent

An abstract agent is the catalog's notion of an agent: a job written
down well enough that any vendor's agent can claim it and any
organization can put it into a process. It says what the work is, which
activities it takes on, what it must know how to follow, what it needs
to be granted, what records it must leave, and what it hands to a
person.

Once an organization customizes an abstract agent and puts something
running behind it, what they have is an agent. One agent may implement
several abstract agents at once, and two agents built entirely
differently can both implement the copywriter. The organization should
not have to care which one it got, because the abstract agent says
everything the process needs from it.

An abstract agent is deliberately not an implementation. It never names
a model, a prompt, an API, or a vendor.

## What an abstract agent is not

- **It is not a human role.** Some work in a process is done only by
  people - a legal reviewer signing an approval, a leader confirming a
  budget. Those stay named roles inside the process, and the process
  marks them `never`. An abstract agent describes work an agent may
  take on, at whatever automation level the process sets.
- **It is not a tool.** A web scraper, a sentiment scorer and an image
  generator are capabilities an agent uses, and they live inside the
  agent. The test is whether it can stand on its own: a tool does not
  hold a role in a process, take a handoff, or leave a DONE record
  under its own name.
- **It is not a product.** A data warehouse, an asset library and a
  template store are systems a process binds to, listed under
  `systems:` in the process document.

## The format

```
ABSTRACT AGENT: <name>                id: <slug>   v<version>
purpose: <what the agent does, in one paragraph>
processes:
  <reference process id> / <activity>: <what it does there>
patterns:
  <the collaboration patterns it must be able to follow, and the work
   pattern roles it can hold>
grants:
  <system kind> (<read|write>) - cap: <blank, set by the adopting org>
records:
  <what a run can expect this agent to leave behind>
escalates:
  <what always goes to a person, regardless of automation level>
not:
  <the nearest things this agent does not do>
```

Everything below explains one of those lines.

## Purpose

One paragraph, in plain words, saying what the agent does and for whom.
If the paragraph needs jargon to sound useful, what is being described
is probably a tool or a feature rather than an agent.

## Processes

The list of reference processes and activities where this agent works.
This is the line that keeps the catalog honest. An abstract agent earns
its entry by taking activities in real processes, and an entry with no
processes is a capability looking for a job. Every line cites a
reference process id, and that process's agents column cites back.

## Patterns

The collaboration patterns the agent must be able to follow - sit in a
[briefing](https://github.com/jeffrschneider/agentcollab/blob/main/patterns/briefing.md),
deliver into a
[bake-off](https://github.com/jeffrschneider/agentcollab/blob/main/patterns/bake-off.md),
take a changes-requested from an
[approval](https://github.com/jeffrschneider/agentcollab/blob/main/patterns/approval.md) -
and the [work pattern](https://github.com/jeffrschneider/agentworkpatterns)
roles it can hold, such as a specialist slice in build-by-talent. This
is what makes a fleet possible: two agents that have never met can work
together because both know what the patterns require of them.

## Grants

What the agent needs to be given before it can work: which kinds of
systems, at what permission, with what caps. The abstract agent names
the kinds and leaves the caps blank, because a cap is the adopting
organization's decision, written into their process document's
bindings. A media buyer says it needs write access to ad platforms and
a daily spend cap; your process says what the cap is and who set it.

An agent never grants itself anything. Grants flow from the process
document to the agent, which is what makes them auditable.

## Records

What the agent leaves behind: the DONE records of the patterns it
follows, the artifacts it produces at versions, the one-line records of
work done outside any room. The records are how a person checks the
work without opening the agent, and how a running agent's claim to
implement this abstract agent can be tested against what it actually
leaves.

## Escalates

What always goes to a person, no matter how automated the work becomes.
The community manager escalates a legal threat. The media buyer
escalates spend past its cap. Escalation lines belong to the abstract
agent because they survive any change of vendor.

## How an agent claims one

An agent in the catalog claims an abstract agent with one line:
`implements: <slug> v<n>`. An agent may carry several of those lines,
because one running agent can do the work of more than one abstract
agent. The claim is checkable, because the abstract agent says what
records it must leave and what patterns it must follow, so a run of any
process that uses it produces the evidence.
