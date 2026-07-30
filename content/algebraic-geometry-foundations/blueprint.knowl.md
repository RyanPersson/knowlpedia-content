+++
id = "algebraic-geometry-foundations/blueprint"
title = "Blueprint"
kind = "definition"
summary = "A commutative multiplicative monoid together with compatible formal additive relations."
aliases = ["algebraic blueprint", "blueprint algebra"]
domains = ["algebraic-geometry-foundations", "algebra-rings"]
section_mode = "progressive"
+++

A **blueprint** \(B=A/\!/\mathcal R\) consists of a [[algebra-groups/commutative-monoid|commutative monoid with zero]] \(A\) and a **pre-addition** \(\mathcal R\): an equivalence relation on the semiring \(\mathbb N[A]\) of finite formal sums of elements of \(A\), compatible with formal addition and multiplication. The empty sum is related to \(0\), and a relation between one-term sums \(a\equiv b\) forces \(a=b\) in \(A\).

A morphism \(f:A/\!/\mathcal R\to A'/\!/\mathcal R'\) is a multiplicative map preserving \(0\) and \(1\) whose termwise extension sends every relation in \(\mathcal R\) to one in \(\mathcal R'\).

## What the notation records

The monoid \(A\) is the multiplicative skeleton \(B^\bullet\). The relations \(\mathcal R\) say which formal sums are to count as equal without requiring every sum to be represented by an element of \(A\). Passing to the quotient semiring
\[
B^+=\mathbb N[A]/\mathcal R
\]
is the **semiring completion**. The canonical map \(B^\bullet\to B^+\) remembers which elements are designated as monomials.

## Familiar structures inside blueprints

[[algebraic-geometry-foundations/semirings-and-monoids-as-blueprints|Commutative semirings and commutative monoids embed fully faithfully]] into blueprints, but in different ways. This is why a blueprint is not merely another name for a semiring.

Blueprints support localization, spectra, and [[algebraic-geometry-foundations/blue-scheme|blue schemes]]. [[algebraic-geometry-foundations/ordered-blueprint|Ordered blueprints]] replace symmetric additive relations by directed inequalities and form a broader framework used in tropical and matroid geometry.

## Reference

Oliver Lorscheid, [*The geometry of blueprints, Part I: Algebraic background and scheme theory*, §1](https://arxiv.org/abs/1103.1745).

