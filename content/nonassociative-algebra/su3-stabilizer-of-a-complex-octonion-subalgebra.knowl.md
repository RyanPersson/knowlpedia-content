+++
id = "nonassociative-algebra/su3-stabilizer-of-a-complex-octonion-subalgebra"
title = "SU(3) stabilizer of a complex octonion subalgebra"
kind = "theorem"
summary = "Fixing a unit imaginary octonion reduces the octonion automorphism group G₂ to SU(3)."
aliases = ["SU3 in G2", "SU(3) stabilizer in G2", "complex stabilizer of the octonions"]
domains = ["nonassociative-algebra", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/compact-exceptional-lie-group-g2", "nonassociative-algebra/octonion-algebra", "linear-algebra/vector-space", "linear-algebra/orthogonal-complement", "nonassociative-algebra/conjugated-cross-product-on-c3", "lie-groups/lie-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(i\in\operatorname{Im}(\mathbb O)\) be a unit imaginary octonion, so \(i^2=-1\), and let \(\mathbb C_i=\operatorname{span}_{\mathbb R}\{1,i\}\). The subgroup of
\[
 \operatorname{Aut}_{\mathbb R\text{-alg}}(\mathbb O)\cong G_2
\]
that fixes \(i\), equivalently fixes \(\mathbb C_i\) pointwise, is isomorphic to \(SU(3)\). Here \(G_2\) is the [[lie-groups/compact-exceptional-lie-group-g2|compact exceptional Lie group]].

## The defining representation

The [[linear-algebra/orthogonal-complement|orthogonal complement]] \(\mathbb C_i^\perp\subset\mathbb O\) is a complex three-dimensional [[linear-algebra/vector-space|vector space]]. In the multiplication convention used by the [[nonassociative-algebra/octonions-as-complex-vectors|complex-vector model]], its complex structure is right multiplication by \(i\). Under an identification \(\mathbb C_i^\perp\cong\mathbb C^3\), the stabilizer acts by the defining representation of \(SU(3)\). This gives the orthogonal splitting
\[
 \mathbb O\cong\mathbb C_i\oplus\mathbb C_i^\perp
 \cong\mathbb C\oplus\mathbb C^3
\]
used in the [[nonassociative-algebra/octonions-as-complex-vectors|complex-vector construction of the octonions]].

## Why the action preserves multiplication

In the \(\mathbb C\oplus\mathbb C^3\) model, \(SU(3)\) preserves the Hermitian inner product and the complex volume form. It therefore preserves the [[nonassociative-algebra/conjugated-cross-product-on-c3|conjugated cross product]], and hence every term in the octonion multiplication. The action
\[
 g(a,u)=(a,gu)
\]
is consequently by algebra automorphisms and is trivial on \(\mathbb C_i\).

## Homogeneous-space interpretation

The compact group \(G_2\) acts transitively on the [[linear-algebra/unit-sphere|unit sphere]] in \(\operatorname{Im}(\mathbb O)\cong\mathbb R^7\). Since the stabilizer of a unit imaginary octonion is \(SU(3)\),
\[
 G_2/SU(3)\cong S^6.
\]
At the Lie-algebra level, the stabilizer has [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak{su}(3)\) inside the [[lie-groups/exceptional-lie-algebra-g2|exceptional Lie algebra \(\mathfrak g_2\)]].

## Pointwise versus setwise stabilizer

The \(SU(3)\) statement concerns the stabilizer of the chosen element \(i\), or equivalently the **pointwise** stabilizer of \(\mathbb C_i\). The setwise stabilizer of the two-plane \(\mathbb C_i\) has a second component whose elements carry \(i\) to \(-i\); it is an extension of \(SU(3)\) by a group of order two. Thus “fixes \(i\)” cannot be replaced by “preserves \(\mathbb C_i\) as a set” without changing the group.

## References

1. John C. Baez, “The Octonions,” *Bulletin of the American Mathematical Society* **39** (2002), 145–205. [DOI record](https://doi.org/10.1090/S0273-0979-01-00934-X). Relevant: §4.1.
2. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235). Relevant: §§2–3.
3. Ichiro Yokota, *Exceptional Lie Groups*, Lecture Notes in Mathematics 2369, Springer, 2025. [arXiv:0902.0431](https://arxiv.org/abs/0902.0431). Relevant: Theorem 1.9.1.
