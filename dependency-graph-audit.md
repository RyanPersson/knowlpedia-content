# Dependency graph repair audit — cycle-repair stage

The baseline at `d35aed96` (also `origin/develop` at the start of this task)
contained 3,501 knowls and 10,443 distinct prerequisite edges, including 153
cyclic strongly connected components involving 607 knowls.

At the end of the cycle-repair stage, the corpus contained **10,064 prerequisite
edges and zero cycles**. Subsequent semantic changes are recorded separately in
[the foundations review](dependency-foundations-review.md).
273 knowls have targeted prerequisite metadata edits. 379 feedback edges were
removed; all body text, ordinary wikilinks, and dependency review counts are
unchanged. No concepts were removed or merged. The integration review restored
88 previously removed edges wherever they could be retained without a cycle,
then corrected remaining theorem/definition direction errors.

The repairs distinguish a definition's ingredients from examples, consequences,
and mutually referring equivalent formulations. In the source metadata,
`id → prerequisite` means the first knowl depends on the second. The rendered
graph reverses that direction: prerequisite → dependent.

Edited lists are marked `semantic-cycle-repair-v1`. The engine's metadata
generator preserves these lists on subsequent runs. This records targeted cycle
repair; it does not claim a complete pedagogical review of every dependency.
The existing `dependency_review_count` values are deliberately unchanged.

[dependency-graph-audit.json](dependency-graph-audit.json) records every removed
edge and its review rationale. Both production (3,491 knowls) and development
(3,501 knowls) are checked independently by the engine's report-only command:

```bash
python3 scripts/audit_dependency_graph.py --content-package ../knowlpedia-content --profile development
python3 scripts/audit_dependency_graph.py --content-package ../knowlpedia-content --profile production
```

Run these from the paired engine repository. Each audit checks missing targets,
invalid metadata, duplicate IDs, cycle witnesses, and a complete topological
ordering. Every prerequisite must precede its dependent in that ordering.
