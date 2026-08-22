# Skills

One file per abstract agent, saying which capabilities it has and which
activities each capability covers.

A capability is one thing the agent knows how to do. The reference
processes name the same work differently depending on what it is being
done to, so a single capability turns up under many activity names.
Watching the first weeks after a launch and watching the registrations
for a webinar are the same work on a different subject.

Grouping activities this way is a judgement call, and the activity names
cannot make it on their own, so it is written down here instead of being
guessed by the generator.

## The format

    # <agent slug>

    ## <capability slug>

    One or two sentences saying what the agent does when it exercises
    this capability.

    covers:
    - <activity name, exactly as the agent document writes it>
    - <activity name, exactly as the agent document writes it>

## What the generator checks

`tools/build-plugins.py` reads these files and refuses to build if any of
them is wrong. Every activity an agent holds must be covered by exactly
one capability. An activity covered twice, an activity covered by no
capability, and a name that does not match what the agent document says
are all errors that stop the build. That is what keeps these files honest
as the processes change.
