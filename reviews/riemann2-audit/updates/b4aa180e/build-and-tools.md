# Build, links and the new publishing script

[Incremental audit](README.md) · [Earlier compiler diagnostics](../../structural-checks.md)

## Production build

The `d1e53260` production compiler loaded the 5,700-ID registry and generated the HTML and fragments for all 735 Riemann2 pages. The validation exit status was 1. It reported the same ten broken references on the same eight earlier draft pages. Its alias warnings also match the preceding run. All 395 ordinary links on the 95 changed pages lead to existing IDs. Two older broken links now have published replacements. [Compiler entry point](https://github.com/RyanPersson/knowlpedia/blob/d1e5326095b2b9484172c8129e0aed23b5456711/packages/compiler/knowl_compile.py#L2877) · [Two replacements](coverage.md)

The changed pages contain 5,393 math expressions in body text, titles and summaries, comprising 2,629 distinct expression/display-mode pairs. All parsed with KaTeX 0.16.47. All 40,394 expressions across the 735 pages passed the same check, and none of the generated pages contains a `katex-error` marker. Reproduce the build with `knowl_compile.py`, the content package, `--profile production`, a fresh `--out` directory and one `--only` argument per ID under `content/proofs/grh`.

Both updated chapter indexes link every individual knowl in their area (66 and 81). The 95 changed headers have canonical paths, one References heading, existing source paths and empty prerequisite lists. Their 561 Lean and 189 concept placeholders follow the draft convention. All concept names used in each of these areas have a row in its own concept table. [Lean names and resolver behavior](lean-references.md) · [Concept definitions and targets](concepts.md)

## Publishing helper

The new helper stages, commits and pushes two repositories. A shell syntax check passed. The behavior below follows from the commands and repository layout. The review used static inspection of the publish operations.

- **The helper can commit unrelated edits and push the active worktree branch.** Each `git add -A` stages the whole repository and each bare `git push` uses its configured target. On this checkout the two branches in use during review were `riemann2` and `riemann2-review`. Check the expected branch in each repository before the sync, scope and inspect the staged paths, and push the intended ref explicitly. [Repository-wide staging and push](https://github.com/RyanPersson/knowlpedia/blob/d1e5326095b2b9484172c8129e0aed23b5456711/docs/riemann2/tools/sync_push.sh#L6)

- **A failed commit can be reported as success.** Both commits end with `|| true`. If a hook rejects a staged change or Git cannot create the commit, pushing the old tip can still return success and the helper prints an old commit. Test for an empty staged diff explicitly and propagate any commit failure for a nonempty diff. Publish the content before the report that marks it complete, with the resulting content SHA in that report. [Commit handling and order](https://github.com/RyanPersson/knowlpedia/blob/d1e5326095b2b9484172c8129e0aed23b5456711/docs/riemann2/tools/sync_push.sh#L7)

- **The documentation mirror can remove tracked notes.** The `--delete` mirror treats the machine-specific `documents/riemann2/` as authoritative. The source directory is absent in this review checkout. On a host with only a partial source tree, destination-only tracked notes enter the stage as deletions. Accept a configurable source path, verify it belongs to the intended working set, and review the deletion list before staging the mirror. [Mirror command](https://github.com/RyanPersson/knowlpedia/blob/d1e5326095b2b9484172c8129e0aed23b5456711/docs/riemann2/tools/sync_push.sh#L5)
