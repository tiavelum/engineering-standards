Repository tiavelum/engineering-standards.

The standards here are the foundation that every repository of tiavelum, and every Claude session in one, works from; a change to them reaches all of these.

- Where code or a setting can enforce a rule, propose that, in this repository or in tiavelum/github-setup, and keep a written rule only for what it leaves to the author.
- Propose in tiavelum/claude-setup, not here, any rule that would not hold for work done without Claude.
- Before pushing a new or changed rule, apply it to a concrete case as a reader who did not write it; rework it until it gives one result, or leave it out and open an issue.
- Take rule identifiers, versions and counts from the files on the branch you work on, never from memory or an earlier copy.
- Number a new rule one above the highest number its prefix has had in the history of `main`, removed rules included.
- Before marking a pull request ready, run the checks under "As a contributor" in the README. If you cannot run them, wait for the CI run of your last commit and report its result.
