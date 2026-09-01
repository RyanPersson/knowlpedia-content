+++
id = "topology/compactness-implies-total-boundedness"
title = "Compactness implies total boundedness"
kind = "knowl"
summary = "In a metric space, every compact set can be covered by finitely many small balls."
aliases = ["compactness-implies-total-boundedness", "Compactness implies total boundedness"]
domains = ["topology"]
prerequisites = ["topology/metric-space", "topology/compact-set", "topology/totally-bounded-set", "topology/open-ball"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "topology/compactness-implies-total-boundedness.md"
+++

**Compactness implies total boundedness:** Let \((X,d)\) be a [[topology/metric-space|metric space]] and let \(K\subseteq X\) be [[topology/compact-set|compact]]. Then \(K\) is [[topology/totally-bounded-set|totally bounded]]: for every \(\varepsilon>0\) there exists a finite set \(F\subseteq K\) such that
\[
K\subseteq \bigcup_{x\in F} B(x,\varepsilon),
\]
where \(B(x,\varepsilon)\) denotes the [[topology/open-ball|open ball]].

## Remarks

This is one half of the standard metric characterization [[topology/compact-iff-complete-totally-bounded|compact iff complete and totally bounded]], complementing [[topology/compactness-implies-completeness|compactness implies completeness]] and closely related to the existence of finite [[topology/epsilon-net|epsilon-nets]].
