Repository tiavelum/engineering-standards.

The standards here are the foundation that every repository following them builds on; a change to them reaches each of those repositories and every Claude session working in one.

Where a repository setting can enforce a rule, propose the setting in tiavelum/github-setup, and replace the rule with a pointer to it once the setting reaches every repository the rule covers. Where a check can enforce a rule, propose the check and keep the rule, since the author still needs it.

Propose a rule that would not hold for work done without Claude in tiavelum/claude-setup, not as a standard.

Leave out of a rule any point that no decision recorded on an issue covers, and raise it as a question instead of deciding it.

Before pushing a new or changed rule, apply it to a concrete case as a reader who did not write it. If it gives more than one result, rework it once; if it still does, leave it out and open an issue.

Take rule identifiers, versions and counts from the files on the branch you work on, never from memory or an earlier copy.

Before marking a pull request ready, run the checks under "As a contributor" in the README. If you cannot run them, wait for the CI run of your last commit and report its result.
