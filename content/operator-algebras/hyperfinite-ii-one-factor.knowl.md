+++
id = "operator-algebras/hyperfinite-ii-one-factor"
title = "Hyperfinite II₁ factor"
kind = "definition"
summary = "The separable type II₁ factor obtained as the strong closure of an increasing union of finite-dimensional algebras."
aliases = ["approximately finite-dimensional II_1 factor", "hyperfinite factor R"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

The **hyperfinite type \(\mathrm{II}_1\) factor** is a
[[operator-algebras/type-ii-one-factor|type \(\mathrm{II}_1\) factor]] \(M\)
with separable predual for which there are finite-dimensional unital
\(*\)-subalgebras
\[
A_1\subseteq A_2\subseteq\cdots\subseteq M
\]
whose union is
[[operator-algebras/strong-operator-topology|strong-operator dense]] in
\(M\). Such a factor is also called
approximately finite-dimensional. Murray and von Neumann proved that any two
factors satisfying these conditions are isomorphic, so the definition
determines a single isomorphism class, conventionally denoted \(R\).
Hyperfiniteness is
an approximation property; \(R\) itself is infinite-dimensional.

## Standard construction

Equip the infinite tensor product
\[
\bigotimes_{n=1}^{\infty}M_2(\mathbb C)
\]
with its product [[operator-algebras/tracial-state|tracial state]] and take
the weak closure in the associated
[[operator-algebras/gns-construction|GNS representation]]. The finite tensor
factors form an increasing sequence of
matrix algebras with strongly dense union, and the resulting von Neumann
algebra is \(R\). Replacing \(M_2(\mathbb C)\) by many other nontrivial
sequences of matrix algebras produces the same factor up to isomorphism.

## Injectivity and uniqueness

For factors with separable predual, hyperfiniteness is equivalent to
injectivity. Connes proved this implication in the course of classifying
injective factors; in type \(\mathrm{II}_1\), it identifies every injective
factor with \(R\).
This equivalence is a theorem, not part of the defining approximation
property.

## Examples and non-examples

Every matrix algebra is finite-dimensional and hence trivially hyperfinite,
but it is type I rather than type \(\mathrm{II}_1\), so it is not \(R\).
This near-miss shows why both the factor type and the approximation condition
are present in the core definition.

## References

1. Francis J. Murray and John von Neumann, “On Rings of Operators IV,” *Annals of Mathematics* 44 (1943), 716–808. [DOI record](https://doi.org/10.2307/1969107). Relevant: the uniqueness theorem for approximately finite type II₁ factors.
2. Alain Connes, “Classification of Injective Factors. Cases II₁, II∞, IIIλ, λ ≠ 1,” *Annals of Mathematics* 104 (1976), 73–115. [DOI record](https://doi.org/10.2307/1971057). Relevant: the main classification theorem in the type II₁ case.
