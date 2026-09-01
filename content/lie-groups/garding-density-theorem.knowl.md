+++
id = "lie-groups/garding-density-theorem"
title = "Gårding density theorem"
kind = "theorem"
summary = "The Gårding subspace, and therefore the smooth-vector space, is dense in every strongly continuous unitary representation of a Lie group."
aliases = ["density theorem for smooth vectors", "Gårding theorem"]
domains = ["lie-groups", "harmonic-analysis"]
prerequisites = ["fiber-bundles/lie-group", "lie-groups/strongly-continuous-unitary-representation", "lie-groups/garding-subspace", "lie-groups/smooth-vector-unitary-representation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a finite-dimensional [[fiber-bundles/lie-group|Lie group]] and let \((\pi,\mathcal H)\) be a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]]. The **Gårding density theorem** states that the [[lie-groups/garding-subspace|Gårding subspace]]
\[
\operatorname{span}\{\pi(f)v:f\in C_c^\infty(G),\ v\in\mathcal H\}
\]
is dense in \(\mathcal H\). Every vector in this subspace is smooth, so the [[lie-groups/smooth-vector-unitary-representation|smooth-vector space]] \(\mathcal H^\infty\) is also dense. Thus the unbounded operators of the derived Lie-algebra representation have a common dense invariant domain.

## Proof mechanism

Choose nonnegative functions \(f_j\in C_c^\infty(G)\) with integral \(1\) and supports shrinking to the identity. Strong continuity of the [[fiber-bundles/orbit-map|orbit map]] gives
\[
\lVert\pi(f_j)v-v\rVert
\leq\int_G f_j(g)\lVert\pi(g)v-v\rVert\,dg\longrightarrow 0.
\]
Each \(\pi(f_j)v\) is smooth because derivatives can be transferred to \(f_j\).

## Consequences

The theorem makes the [[lie-groups/derived-representation-on-smooth-vectors|derived representation]] available for every strongly continuous representation, even when most Hilbert-space vectors are not differentiable. It also gives a canonical family of cores for infinitesimal generators. The [[lie-groups/dixmier-malliavin-factorization-theorem|Dixmier–Malliavin theorem]] later sharpened density by identifying the entire smooth-vector space with the Gårding subspace.

## Conventions and scope

The theorem is sometimes stated for continuous representations on [[linear-algebra/banach-space|Banach spaces]] or more general complete [[functional-analysis/locally-convex-space|locally convex spaces]]; additional integration and equicontinuity hypotheses then enter. The Hilbert-unitary version stated here needs only strong continuity. It proves density, not that the smooth-vector space is closed in the Hilbert norm; except in special cases, it is not.

## References

1. Lars Gårding, *Note on Continuous Representations of Lie Groups*, Proceedings of the National Academy of Sciences 33 (1947), 331–332. [DOI record](https://doi.org/10.1073/pnas.33.11.331). Relevant: the original smoothing and density argument.
2. Garth Warner, *Harmonic Analysis on Semi-Simple Lie Groups I*, Springer, 1972. [DOI record](https://doi.org/10.1007/978-3-642-50275-0). Relevant: §4.4 on differentiable vectors and Gårding's theorem.
