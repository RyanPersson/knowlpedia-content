+++
id = "algebra-groups/subnormal-series"
title = "Subnormal series"
kind = "knowl"
summary = "A finite chain from the trivial subgroup to a group in which each term is normal in the next."
aliases = ["subnormal-series", "Subnormal series"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group", "algebra-groups/normal-subgroup"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-groups/subnormal-series.md"
+++

Let \(G\) be a [[algebra-groups/group|group]]. A **subnormal series** of \(G\) is a finite chain
\[
\{e\}=G_0 \lhd G_1 \lhd \cdots \lhd G_n = G
\]
in which \(G_{i-1}\) is a [[algebra-groups/normal-subgroup|normal subgroup]] of \(G_i\) for \(1\le i\le n\).

## Examples

- The chain \(\{e\}\lhd G\) is a subnormal series for every group \(G\).
- In \(S_4\), the chain \(\{e\}\lhd V_4\lhd A_4\lhd S_4\) is a subnormal series.
- The chain \(\{e\}<\langle(12)\rangle<S_3\) is not subnormal because \(\langle(12)\rangle\) is not normal in \(S_3\).

## Remarks

Important examples include the [[algebra-groups/derived-series|derived series]] and the [[algebra-groups/lower-central-series|lower central series]]. A [[algebra-groups/composition-series-group|composition series]] is a subnormal series with simple successive factors.
