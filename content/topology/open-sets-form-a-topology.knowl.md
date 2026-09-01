+++
id = "topology/open-sets-form-a-topology"
title = "Open sets form a topology"
kind = "knowl"
summary = "The open subsets of a metric space satisfy the axioms of a topology."
aliases = ["open-sets-form-a-topology", "Open sets form a topology"]
domains = ["topology"]
prerequisites = ["topology/metric-space", "topology/open-set", "topology/metric"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "topology/open-sets-form-a-topology.md"
+++

**Open sets form a topology.** Let \((X,d)\) be a [[topology/metric-space|metric space]]. Then:

- \(\varnothing\) and \(X\) are [[topology/open-set|open]];
- if every \(U_\alpha\) is open, then \(\bigcup_{\alpha\in A}U_\alpha\) is open; and
- if \(U_1,\ldots,U_n\) are open, then \(\bigcap_{j=1}^nU_j\) is open.

These closure properties justify treating "open sets" as the primitive objects defining the topological structure induced by a [[topology/metric|metric]].
