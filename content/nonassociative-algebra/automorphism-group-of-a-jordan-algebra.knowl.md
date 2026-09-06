+++
id = "nonassociative-algebra/automorphism-group-of-a-jordan-algebra"
title = "Automorphism group of a Jordan algebra"
kind = "definition"
summary = "The group of invertible linear maps preserving a Jordan product."
aliases = ["Jordan automorphism group", "automorphism of a Jordan algebra", "Aut(J)"]
domains = ["nonassociative-algebra"]
prerequisites = ["nonassociative-algebra/jordan-algebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

For a [[nonassociative-algebra/jordan-algebra|Jordan algebra]] \(J\), its
**automorphism group** is
\[
\operatorname{Aut}(J)=
\{g\in GL(J):g(x\circ y)=g(x)\circ g(y)
\text{ for all }x,y\in J\}.
\]
The group operation is composition.

## Units and preserved structure

If \(J\) is unital, every automorphism fixes its unit: \(g(e)\) acts as a unit
on the surjective image \(g(J)=J\), and the unit is unique. Automorphisms also
preserve idempotents, [[nonassociative-algebra/jordan-frame|Jordan frames]], rank, and the coefficients of the Jordan
characteristic polynomial.

For a [[nonassociative-algebra/euclidean-jordan-algebra|Euclidean Jordan algebra]], automorphisms preserve the canonical
[[nonassociative-algebra/trace-form-of-a-euclidean-jordan-algebra|trace form]].
Consequently \(\operatorname{Aut}(J)\) is a [[lie-groups/compact-lie-group|compact Lie group]]. Its [[lie-groups/lie-algebra|Lie algebra]]
is the derivation algebra
\[
\operatorname{Der}(J)=
\{D:D(x\circ y)=D(x)\circ y+x\circ D(y)\}.
\]

## Examples

- For a [[nonassociative-algebra/spin-factor-jordan-algebra|spin factor]] \(J(V)\), \(\operatorname{Aut}(J(V))\cong O(V)\).
- The [[lie-groups/identity-component-of-a-lie-group|identity component]] of
  \(\operatorname{Aut}(\mathfrak h_n(\mathbb C))\) is \(PU(n)\), acting by
  unitary conjugation. For \(n\geq3\), complex conjugation supplies another
  component.
- \(\operatorname{Aut}(\mathfrak h_3(\mathbb O))\) is the compact exceptional
  Lie group \(F_4\).

## Automorphisms versus stabilizers

If \(B\subset J\) is a [[nonassociative-algebra/jordan-subalgebra|Jordan subalgebra]], restriction gives a homomorphism
\[
\operatorname{Stab}_{\operatorname{Aut}(J)}(B)\longrightarrow
\operatorname{Aut}(B).
\]
It need be neither injective nor surjective. Thus the automorphism group of an
abstract subalgebra should not be identified with its stabilizer inside a
larger algebra.

## References

1. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994. [Publisher record](https://global.oup.com/academic/product/analysis-on-symmetric-cones-9780198534778).
2. Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer, 2000. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-12622-6).
3. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
