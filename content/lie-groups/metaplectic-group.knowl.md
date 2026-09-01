+++
id = "lie-groups/metaplectic-group"
title = "Metaplectic group"
kind = "definition"
summary = "The connected double cover of the real symplectic group."
aliases = ["real metaplectic group", "Mp(2n,R)", "metaplectic double cover"]
domains = ["lie-groups", "differential-geometry", "harmonic-analysis"]
prerequisites = ["lie-groups/symplectic-group", "lie-groups/lie-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

The **metaplectic group** \(\operatorname{Mp}(2n,\mathbb R)\) is the connected two-sheeted covering group of the [[lie-groups/symplectic-group|real symplectic group]] \(\operatorname{Sp}(2n,\mathbb R)\). It fits into the central extension
\[
1\longrightarrow \{\pm1\}
\longrightarrow \operatorname{Mp}(2n,\mathbb R)
\longrightarrow \operatorname{Sp}(2n,\mathbb R)
\longrightarrow 1.
\]
Its [[lie-groups/lie-algebra|Lie algebra]] is canonically \(\mathfrak{sp}(2n,\mathbb R)\), but the covering is globally nontrivial.

## Construction from the fundamental group

The symplectic group is connected and has fundamental group isomorphic to \(\mathbb Z\). Its connected covering groups correspond to subgroups of \(\mathbb Z\); the subgroup \(2\mathbb Z\) gives the metaplectic double cover. It is distinct from the [[lie-groups/universal-covering-group|universal covering group]], whose kernel over \(\operatorname{Sp}(2n,\mathbb R)\) is infinite cyclic.

## Why the cover appears

The natural action of linear symplectic transformations on quantum states is only projective at the level of \(\operatorname{Sp}(2n,\mathbb R)\). Passing to \(\operatorname{Mp}(2n,\mathbb R)\) resolves the sign ambiguity and gives the genuine [[lie-groups/metaplectic-representation|metaplectic representation]]. This is the linear model for replacing a [[lie-groups/projective-unitary-representation|projective unitary representation]] by a representation of a central covering group.

## References

1. G. B. Folland, *Harmonic Analysis in Phase Space*, Princeton University Press, 1989. [Publisher record](https://press.princeton.edu/books/paperback/9780691085289/harmonic-analysis-in-phase-space). Relevant: Chapter 4, the metaplectic representation.
2. M. de Gosson, *Symplectic Methods in Harmonic Analysis and in Mathematical Physics*, Birkhäuser, 2011. [DOI record](https://doi.org/10.1007/978-3-7643-9992-4). Relevant: Chapters 7–8, the metaplectic group and its generators.
