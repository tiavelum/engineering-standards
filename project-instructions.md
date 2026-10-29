Repository tiavelum/engineering-standards.

This repository holds the engineering standards that other repositories follow. A change here changes the rules for all of them, and for every Claude session that works in one.

Settings and checks: When a GitHub setting could enforce a rule of a standard, propose the setting in tiavelum/github-setup. When an automated check could enforce one, propose the check.

Rules only for Claude: Propose in tiavelum/claude-setup a rule that applies only when Claude works on a repository.

Open decisions: Write into a rule only what a decision on an issue already covers. Ask about everything else instead of deciding it yourself.

Testing a rule: Before pushing a new or changed rule, try it on a real example, reading it as someone who did not write it. If it can be read two ways, rewrite it once. If it still can, leave it out and open an issue for it.

Facts from the files: Look up rule numbers, versions and counts in the files of your branch, not in memory or an older copy, since they change with every merge.

Done: A pull request is ready when the checks under "As a contributor" in the README pass. If you cannot run them yourself, wait for the automated run on GitHub after your last commit and report its result.
