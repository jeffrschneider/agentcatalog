# Agent Catalog

The reference layer behind [agentcatalog.com](https://agentcatalog.com):
abstract agents and reference processes, written so an organization can
staff real work with agents instead of starting from a blank page.

Two kinds of document live here, and two format definitions explain
them:

| Document | Job |
|---|---|
| [Abstract agent](./abstract-agent.md) | the format: a seat an agent can hold - purpose, seats, patterns, grants, records, escalations |
| [Reference process](./reference-process.md) | the format: a process document with the organizational parts left blank, ready to adopt |

An **abstract agent** is a job description, not an implementation: any
vendor's agent can claim the seat, and the claim is checkable against
the records the seat must leave. A **reference process** is a first
draft to argue with: the activity walk is already done, and it becomes
your process the moment you fill in the header and put your name on it.

The two cite each other. Every reference process's roles column names
the abstract agents that can hold its seats; every abstract agent lists
the processes where it works. Concrete agents in the live catalog claim
seats with one line: `implements: <slug> v<n>`.

## Marketing

Reference processes:

| Process | What it covers |
|---|---|
| [The social campaign](./processes/marketing/social-campaign.md) | brief to launch to report, with two backward edges |
| [Inbound lead routing](./processes/marketing/lead-routing.md) | the fully autonomous case: seconds per run, evidence on every decision |
| [The product launch](./processes/marketing/product-launch.md) | the coordination-heavy case: three branches converging on a date |

Abstract agents:

| Agent | Purpose |
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

## Where this sits in the family

[Agent Collab](https://github.com/jeffrschneider/agentcollab) covers how
agents work together in one room.
[Agent Work Patterns](https://github.com/jeffrschneider/agentworkpatterns)
covers whole jobs.
[Agent Processes](https://github.com/jeffrschneider/agentprocesses)
covers how an organization writes down its own recurring work. This
repository supplies the starting material: the processes ready to
adopt, and the seats ready to staff. The dependency points one way, as
everywhere in the family - documents here cite the pattern libraries,
and nothing points back.

## The bar for adding entries

An abstract agent earns its entry by holding seats in reference
processes - an entry with no seats is a capability looking for a job,
and it goes in the agent it belongs to instead. A reference process
earns its entry the way everything else in the family does: the work
recurs, and somebody walked the activities rather than imagining them.
