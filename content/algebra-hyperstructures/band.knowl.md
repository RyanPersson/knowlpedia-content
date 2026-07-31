+++
id = "algebra-hyperstructures/band"
title = "Band"
kind = "definition"
summary = "A pointed commutative monoid equipped with an ideal of null formal sums and unique additive inverses."
aliases = ["band in matroid theory", "Baker-Jin-Lorscheid band"]
domains = ["algebra-hyperstructures", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

Let \(B\) be a [[algebra-groups/commutative-monoid|commutative monoid]] with
identity \(1\) and an absorbing element \(0\), and let
\[
B^+=\mathbb N[B]/\langle 0\rangle
\]
be its semiring of finite formal sums, with the monoid zero identified with
the empty sum. Such a monoid is called **pointed**. A **band** is a pair
\((B,N_B)\) in which
[[algebra-hyperstructures/null-set-of-a-band|the nullset]]
\(N_B\subseteq B^+\) is an ideal and, for every \(a\in B\), there is a unique
element \(-a\in B\) such that
\[
a+(-a)\in N_B.
\]

A morphism of bands \(f:B\to C\) is a multiplicative map preserving \(0\)
and \(1\) such that
\[
\sum a_i\in N_B\quad\Longrightarrow\quad\sum f(a_i)\in N_C.
\]

## Scope

The symbols in \(B^+\) are formal sums. A band does not in general have a
single-valued or multivalued addition on \(B\). Rings, hyperrings, and partial
fields give bands by recording which formal sums are null, but not every band
comes from one of those structures.

## Reference

Matthew Baker, Tong Jin, and Oliver Lorscheid,
[*New building blocks for \(\mathbb F_1\)-geometry: bands and band schemes*, Definition 1.1](https://arxiv.org/abs/2402.09612).
