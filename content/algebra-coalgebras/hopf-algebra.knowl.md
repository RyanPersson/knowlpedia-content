+++
id = "algebra-coalgebras/hopf-algebra"
title = "Hopf algebra"
kind = "definition"
summary = "A bialgebra with an antipode implementing algebraic inversion."
aliases = ["Hopf algebra over a ring", "antipode"]
domains = ["algebra-coalgebras", "algebra-rings"]
prerequisites = ["algebra-rings/commutative-ring", "algebra-coalgebras/bialgebra", "linear-algebra/linear-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(k\) be a [[algebra-rings/commutative-ring|commutative ring]]. A
**Hopf algebra** over \(k\) is a [[algebra-coalgebras/bialgebra|bialgebra]]
\((H,m,u,\Delta,\varepsilon)\) together with a \(k\)-linear map
\(S:H\to H\), called the **antipode**, such that
\[
m(S\otimes\operatorname{id})\Delta
=u\varepsilon
=m(\operatorname{id}\otimes S)\Delta.
\]
Equivalently, \(S\) is the two-sided inverse of
\(\operatorname{id}_H\) for the convolution product
\[
f*g=m(f\otimes g)\Delta
\quad\text{on}\quad \operatorname{End}_k(H).
\]

## Meaning of the antipode

The unit for convolution is \(u\varepsilon\), so the antipode identities read,
in Sweedler notation,
\[
\sum S(h_{(1)})h_{(2)}
=\varepsilon(h)1_H
=\sum h_{(1)}S(h_{(2)}).
\]
They are the algebraic counterpart of the equations
\(g^{-1}g=e=gg^{-1}\) in a group. When an antipode exists it is unique.

## Basic properties

The antipode reverses multiplication and comultiplication:
\[
S(ab)=S(b)S(a),
\qquad
\Delta(S(h))=(S\otimes S)\tau\Delta(h),
\]
where \(\tau\) swaps tensor factors. These conclusions follow from uniqueness
of convolution inverses. Bijectivity of \(S\), however, is not automatic for
an arbitrary infinite-dimensional Hopf algebra.

A **Hopf-algebra homomorphism** is a bialgebra homomorphism; it automatically
commutes with antipodes by their uniqueness.

## Examples

- The [[algebra-representation-theory/group-algebra|group algebra]] \(k[G]\) is a Hopf algebra with \(S(g)=g^{-1}\).
- For a [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\), its
  [[lie-groups/universal-enveloping-algebra|universal enveloping algebra]]
  has the cocommutative Hopf structure
  \[
  \Delta(x)=x\otimes1+1\otimes x,\quad
  \varepsilon(x)=0,\quad
  S(x)=-x
  \qquad(x\in\mathfrak g).
  \]
- Coordinate rings of affine [[algebraic-geometry-foundations/group-scheme|group schemes]] are commutative Hopf algebras.
  For affine formal groups, ordinary tensor products are replaced by
  [[algebra-topological/completed-tensor-product|completed tensor products]].

## Variance

Functions pull back. Consequently, a homomorphism of affine groups
\(G\to H\) induces a Hopf-algebra homomorphism
\(\mathcal O(H)\to\mathcal O(G)\) in the opposite direction. The same
contravariance appears for affine formal groups and their complete coordinate
Hopf algebras.

## References

1. Moss E. Sweedler, *Hopf Algebras*, W. A. Benjamin, 1969. Relevant: Chapters 1–4.
2. Christian Kassel, *Quantum Groups*, Graduate Texts in Mathematics 155, Springer, 1995. [Publisher record](https://doi.org/10.1007/978-1-4612-0783-2). Relevant: Chapter III.
3. William C. Waterhouse, *Introduction to Affine Group Schemes*, Graduate Texts in Mathematics 66, Springer, 1979. [Publisher record](https://doi.org/10.1007/978-1-4612-6217-6). Relevant: Chapters 1–3.
