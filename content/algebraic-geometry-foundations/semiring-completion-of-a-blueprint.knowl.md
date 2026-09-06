+++
id = "algebraic-geometry-foundations/semiring-completion-of-a-blueprint"
title = "Semiring completion of a blueprint"
kind = "construction"
summary = "The semiring obtained by quotienting formal sums by all additive relations of a blueprint."
aliases = ["associated semiring of a blueprint", "blueprint semiring completion"]
domains = ["algebraic-geometry-foundations", "algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/blueprint", "algebra-rings/commutative-semiring", "algebraic-geometry-foundations/pre-addition-on-a-monoid", "shared-foundations/injective-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(B=A/\!/\mathcal R\) be a [[algebraic-geometry-foundations/blueprint|blueprint]]. Its **semiring completion** is the [[algebra-rings/commutative-semiring|commutative semiring]]
\[
B^+=\mathbb N[A]/\mathcal R.
\]
Thus two formal sums define the same element of \(B^+\) exactly when they are related by the [[algebraic-geometry-foundations/pre-addition-on-a-monoid|pre-addition]] \(\mathcal R\).

The map
\[
B^\bullet=A\longrightarrow B^+
\]
sends each element of the multiplicative monoid to its one-term sum. Properness of \(\mathcal R\) makes this map injective, and its image generates \(B^+\) as a semiring. The pair consisting of \(B^+\) and the distinguished multiplicative subset \(B^\bullet\) retains the blueprint data; the semiring \(B^+\) alone may not.

## Functoriality

A blueprint morphism \(f:B\to C\) extends termwise to formal sums and therefore induces a [[algebra-rings/semiring-homomorphism|semiring homomorphism]]
\[
f^+:B^+\longrightarrow C^+.
\]
Consequently \(B\mapsto B^+\) is a functor from blueprints to commutative semirings.

## References
Oliver Lorscheid, [*The geometry of blueprints, Part I: Algebraic background and scheme theory*, §1.2](https://arxiv.org/abs/1103.1745).
