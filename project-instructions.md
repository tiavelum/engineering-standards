Repository tiavelum/engineering-standards.

This repository holds the engineering standards that other repositories follow. A change here changes the rules for all of them, and for every Claude session that works in one.

Settings and checks: When a GitHub setting could enforce a rule of a standard, propose the setting in tiavelum/github-setup. Once the setting applies to every repository the rule is meant for, replace the rule's text with a link to the setting. When an automated check could enforce a rule, propose the check, but keep the rule, because whoever writes the file still needs to know it.

Rules only for Claude: A rule that makes no sense for someone working without Claude does not belong in a standard. Propose it in tiavelum/claude-setup instead.

Open decisions: Write into a rule only what a decision on an issue already covers. Ask about everything else instead of deciding it yourself.

Testing a rule: Before pushing a new or changed rule, try it on a real example, reading it as someone who did not write it. If it can be read two ways, rewrite it once. If it still can, leave it out and open an issue for it.

Facts from the files: Look up rule numbers, versions and counts in the files of your branch, not in memory or an older copy, since they change with every merge.

Done: A pull request is ready when the checks under "As a contributor" in the README pass. If you cannot run them yourself, wait for the automated run on GitHub after your last commit and report its result.
