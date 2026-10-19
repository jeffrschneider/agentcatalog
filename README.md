# Agent Catalog

The reference layer behind [agentcatalog.com](https://agentcatalog.com):
abstract agents and reference processes, written so an organization can
fill a roster with agents instead of starting from a blank page.

Two kinds of document live here, and two format definitions explain
them:

| Document | Job |
|---|---|
| [Abstract agent](./abstract-agent.md) | the format: what an agent in the catalog does - purpose, processes, patterns, grants, records, escalations |
| [Reference process](./reference-process.md) | the format: a process document with the organizational parts left blank, ready to adopt |

An **abstract agent** is the catalog's notion of an agent. It is a job
description rather than an implementation, so any vendor's agent can
claim it, and the claim is checkable against the records it has to
leave. Once an organization customizes one and puts something running
behind it, what they have is an **agent**, and one agent may implement
several abstract agents at once. A **reference process** is a first
draft to argue with: the activity walk is already done, and it becomes
your process the moment you fill in the header and put your name on it.

The two cite each other. Every reference process names, in its agents
column, the abstract agents that can do its activities, and every
abstract agent lists the processes where it works. An agent in the live
catalog claims an abstract agent with one line:
`implements: <slug> v<n>`.

## Marketing

The department covered so far holds 80 reference processes and 56
abstract agents. Three processes are worth reading first:

| Process | What it covers |
|---|---|
| [The social campaign](./processes/marketing/social-campaign.md) | brief to launch to report, with two backward edges |
| [Inbound lead routing](./processes/marketing/lead-routing.md) | the fully autonomous case: seconds per run, evidence on every decision |
| [The product launch](./processes/marketing/product-launch.md) | the coordination-heavy case: three branches converging on a date |

And ten of the abstract agents those three processes call on:

| Abstract agent | Purpose |
|---|---|
| [campaign-manager](./agents/campaign-manager.md) | runs a campaign from the brief to the learnings |
| [copywriter](./agents/copywriter.md) | writes the words, inside a direction and a voice |
| [designer](./agents/designer.md) | makes the visuals, at every size a platform requires |
| [video-editor](./agents/video-editor.md) | cuts the video, with captions and sound-off versions |
| [media-buyer](./agents/media-buyer.md) | spends the ad money, under caps, with reasons |
| [community-manager](./agents/community-manager.md) | answers the people, and knows what to hand off |
| [analytics](./agents/analytics.md) | reads the numbers and reports them with sources |
| [brand-check](./agents/brand-check.md) | scores material against the standards before people sign |
| [lead-scorer](./agents/lead-scorer.md) | scores and routes inbound leads with evidence attached |
| [launch-coordinator](./agents/launch-coordinator.md) | keeps a launch honest about its deadline math |

The rest are in [`agents/`](./agents) and
[`processes/marketing/`](./processes/marketing).

## General Management

The discipline that owns the running of multi-agent work itself, rather
than any department's share of it, and of bringing an outside agent into
an organization's work and taking it out again. Three processes and one
abstract agent so far:

| Document | What it covers |
|---|---|
| [Run a working session](./processes/general-management/run-a-working-session.md) | convening several agents on one question: the plan, the phases, the close |
| [Onboard an agent](./processes/general-management/onboard-an-agent.md) | bringing an outside agent in: verify, interview, NDA, engagement, mandate, access, trial |
| [Offboard an agent](./processes/general-management/offboard-an-agent.md) | taking it out: hand over, end, revoke, withdraw, settle, confirm, and a signed close |
| [facilitator](./agents/facilitator.md) | runs the meeting and never judges the work; advisory, and the session works without it |

The facilitator is the first abstract agent that is also a published
role - [role-facilitator](https://agentroles.ai/facilitator.html) - so
the job description here and the checkable contract there name the same
work.

## Plugins

Every abstract agent is also published as an Agent Plugin under
[`plugins/`](./plugins), generated from the documents in `agents/` and
`processes/`. A package carries one skill for each activity the
abstract agent takes on, the systems it needs named by role rather than
by product, and the records it owes. Building an agent from one takes
no vendor: whoever adopts it writes the `mcp.json` that points those
roles at their own systems.

## Where this sits in the family

[Agent Collab](https://github.com/jeffrschneider/agentcollab) covers how
agents work together in one room.
[Agent Work Patterns](https://github.com/jeffrschneider/agentworkpatterns)
covers whole jobs.
[Agent Processes](https://github.com/jeffrschneider/agentprocesses)
covers how an organization writes down its own recurring work. This
repository supplies the starting material: the processes ready to adopt,
and the abstract agents ready to fill them. The dependency points one
way, as everywhere in the family - documents here cite the pattern
libraries, and nothing points back.

## The bar for adding entries

An abstract agent earns its entry by taking activities in reference
processes. An entry with no processes is a capability looking for a job,
and it goes into the agent it belongs to instead. A reference process
earns its entry the way everything else in the family does: the work
recurs, and somebody walked the activities rather than imagining them.
