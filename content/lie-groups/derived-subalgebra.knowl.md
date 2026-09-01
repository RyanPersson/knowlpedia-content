+++
id = "lie-groups/derived-subalgebra"
title = "Derived subalgebra"
kind = "knowl"
summary = "The Lie subalgebra spanned by commutators; it measures how far a Lie algebra is from being abelian."
aliases = ["derived-subalgebra", "Derived subalgebra"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/lie-algebra", "lie-groups/ideal-lie-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "lie-groups/derived-subalgebra.md"
+++

Let \(\mathfrak g\) be a [[lie-groups/lie-algebra|Lie algebra]].

The **derived subalgebra** (or **commutator subalgebra**) of \(\mathfrak g\) is
\[
[\mathfrak g,\mathfrak g] := \mathrm{span}\{[x,y] : x,y\in \mathfrak g\}\subseteq \mathfrak g.
\]
It is a Lie subalgebra and an [[lie-groups/ideal-lie-algebra|ideal]].

## Basic consequences
- \(\mathfrak g\) is [[lie-groups/abelian-lie-algebra|abelian]] if and only if \([\mathfrak g,\mathfrak g]=0\).
- The [[lie-groups/quotient-lie-algebra|quotient]] \(\mathfrak g/[\mathfrak g,\mathfrak g]\) is the **abelianization** of \(\mathfrak g\).
- The algebra \(\mathfrak g\) is **perfect** if \([\mathfrak g,\mathfrak g]=\mathfrak g\); every nonabelian [[lie-groups/simple-lie-algebra|simple Lie algebra]] is perfect.

## Remarks
The derived subalgebra is the first step in the [[lie-groups/derived-series-lie-algebra|derived series]], which detects solvability and organizes many structure theorems such as the [[lie-groups/levi-decomposition-theorem|Levi decomposition]].
