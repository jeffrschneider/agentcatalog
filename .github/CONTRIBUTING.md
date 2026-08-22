# How to contribute

This repository is public, and everything in it is read by people who are
deciding how to build their own agents. Two checks run on every push and
every pull request, and both of them have to pass.

## Do not put an email address in a file

The secret scan reads every file in the repository and fails on any email
address, private key, access key, or token. This catches the obvious
mistakes, and it also catches an address left in an example or a sample
record. Write examples without addresses in them.

## Fix a plugin by fixing the agent document

Everything under `plugins/` is generated from the agent documents in
`agents/`. When a plugin says something wrong, change
`agents/<agent>.md` and generate the packages again with
`python tools/build-plugins.py`. An edit made directly in `plugins/` is
lost the next time the generator runs.

## Run the checks before you push

    python tools/validate-plugins.py

That reads every package under `plugins/` and prints what is wrong with
it and where. Use `--quiet` to see only the failures. The most common
failure is a plugin that points at a reference process that is not in
`processes/`, which usually means the process was renamed and the agent
document still names the old id.
