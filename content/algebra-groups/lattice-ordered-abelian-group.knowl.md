+++
id = "algebra-groups/lattice-ordered-abelian-group"
title = "Lattice-ordered abelian group"
kind = "definition"
summary = "An abelian group with a translation-invariant lattice order."
aliases = ["abelian l-group", "abelian ℓ-group", "lattice-ordered commutative group"]
domains = ["algebra-groups", "order-theory", "algebra-rings"]
section_mode = "progressive"
+++

A **lattice-ordered abelian group**, or **abelian
\(\ell\)-group**, is an [[algebra-groups/abelian-group|abelian group]]
\((\Gamma,+,0)\) with a partial order \(\leq\) such that:

1. \((\Gamma,\leq)\) is a [[shared-foundations/lattice|lattice]];
2. the order is translation-invariant:
   \[
   a\leq b\quad\Longrightarrow\quad a+c\leq b+c.
   \]

Equivalently, translation by \(c\) preserves joins and meets:
\[
(a\vee b)+c=(a+c)\vee(b+c),\qquad
(a\wedge b)+c=(a+c)\wedge(b+c).
\]

## Morphisms

An **\(\ell\)-group homomorphism** is a group homomorphism that preserves
binary joins, equivalently binary meets. An order-preserving group
homomorphism need not preserve joins when the order is not total, so this
extra condition matters categorically.

## Total and partial orders

Every [[algebra-groups/ordered-abelian-group|totally ordered abelian group]]
is an abelian \(\ell\)-group, with
\(a\vee b=\max(a,b)\) and \(a\wedge b=\min(a,b)\). The converse fails:
\(\mathbb Z^2\) with the coordinatewise order is a lattice-ordered abelian
group in which \((1,0)\) and \((0,1)\) are incomparable.

## Positive and negative parts

Writing
\[
x^+=x\vee0,\qquad x^-=(-x)\vee0,
\]
one has \(x=x^+-x^-\) and \(x^+\wedge x^-=0\). These lattice decompositions
are useful when passing between \(\ell\)-groups and idempotent semifields.

## References

1. K. R. Goodearl, *Partially Ordered Abelian Groups with Interpolation*, American Mathematical Society, 1986. [DOI record](https://doi.org/10.1090/surv/020). Relevant: Chapter 1.
2. Guillaume Tahar, “Ordered algebraic structures and classification of semifields,” 2017. [arXiv:1709.06923](https://arxiv.org/abs/1709.06923). Relevant: lattice-ordered groups and characteristic-one semifields.
