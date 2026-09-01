+++
id = "algebra-modules/fg-projective-locally-free"
title = "Finitely generated projectives are locally free"
kind = "knowl"
summary = "Over a commutative ring, finitely generated projective modules become free after localization."
aliases = ["fg-projective-locally-free", "Finitely generated projectives are locally free"]
domains = ["algebra-modules"]
prerequisites = ["algebra-modules/projective-module", "algebra-rings/commutative-ring", "algebra-rings/prime-ideal", "algebra-modules/finitely-generated-module", "algebra-modules/free-module", "algebra-modules/rank-module"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-modules/fg-projective-locally-free.md"
+++

**Finitely generated projectives are locally free**: Let \(R\) be a commutative ring and let \(P\) be a finitely generated projective \(R\)-module. Then for every prime ideal \(\mathfrak p\subset R\), the localization \(P_{\mathfrak p}\) is a free \(R_{\mathfrak p}\)-module of finite rank.

This is a fundamental structure theorem for [[algebra-modules/projective-module|projective modules]] over a [[algebra-rings/commutative-ring|commutative ring]]: after localizing at any [[algebra-rings/prime-ideal|prime ideal]], a [[algebra-modules/finitely-generated-module|finitely generated]] projective becomes [[algebra-modules/free-module|free]] with well-defined [[algebra-modules/rank-module|rank]].

## Equivalent characterizations

Equivalently, there exist elements \(f_1,\dots,f_n\in R\) generating the unit ideal such that each \(P_{f_j}\) is a free \(R_{f_j}\)-module of finite rank.
