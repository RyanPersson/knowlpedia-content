+++
id = "algebraic-geometry-foundations/blueprint"
title = "Blueprint"
kind = "definition"
summary = "A commutative multiplicative monoid together with compatible formal additive relations."
aliases = ["algebraic blueprint", "blueprint algebra"]
domains = ["algebraic-geometry-foundations", "algebra-rings"]
prerequisites = ["algebra-groups/commutative-monoid", "algebraic-geometry-foundations/pre-addition-on-a-monoid"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **blueprint** \(B=A/\!/\mathcal R\) consists of a [[algebra-groups/commutative-monoid|commutative monoid with zero]] \(A\) together with a [[algebraic-geometry-foundations/pre-addition-on-a-monoid|pre-addition]] \(\mathcal R\) on \(A\).

A morphism \(f:A/\!/\mathcal R\to A'/\!/\mathcal R'\) is a multiplicative map preserving \(0\) and \(1\) whose termwise extension sends every relation in \(\mathcal R\) to one in \(\mathcal R'\).

## What the notation records

The monoid \(A\) is the multiplicative skeleton \(B^\bullet\). The relations \(\mathcal R\) say which formal sums are to count as equal without requiring every sum to be represented by an element of \(A\). The [[algebraic-geometry-foundations/semiring-completion-of-a-blueprint|semiring completion]] is
\[
B^+=\mathbb N[A]/\mathcal R
\]
and the canonical map \(B^\bullet\to B^+\) remembers which elements are designated as monomials.

## Familiar structures inside blueprints

There are fully faithful embeddings of [[algebraic-geometry-foundations/semiring-as-a-blueprint|commutative semirings]] and [[algebraic-geometry-foundations/commutative-monoid-with-zero-as-a-blueprint|commutative monoids with zero]] into blueprints, but the two constructions impose different additive relations.

Blueprints support localization, spectra, and [[algebraic-geometry-foundations/blue-scheme|blue schemes]]. The [[algebraic-geometry-foundations/blueprint-as-an-ordered-blueprint|canonical embedding into ordered blueprints]] regards every additive equality as a pair of opposite inequalities.

## References
Oliver Lorscheid, [*The geometry of blueprints, Part I: Algebraic background and scheme theory*, §1](https://arxiv.org/abs/1103.1745).
