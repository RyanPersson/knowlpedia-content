+++
id = "lie-groups/special-block-unitary-group"
title = "Special block unitary group"
kind = "definition"
summary = "The block-diagonal subgroup of a special unitary group with unitary blocks and total determinant one."
aliases = ["S(U(p) x U(q))", "S(U(2) x U(3))", "special product of unitary groups"]
domains = ["lie-groups", "mathematical-physics"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For positive integers \(p,q\), the **special block unitary group** is
\[
S(U(p)\times U(q))
=\{(A,B)\in U(p)\times U(q):\det(A)\det(B)=1\}.
\]
The map \((A,B)\mapsto\operatorname{diag}(A,B)\) identifies it with the subgroup of \(SU(p+q)\) preserving \(\mathbb C^{p+q}=\mathbb C^p\oplus\mathbb C^q\).

## Lie algebra

Its [[lie-groups/lie-algebra|Lie algebra]] is
\[
\mathfrak s\bigl(\mathfrak u(p)\oplus\mathfrak u(q)\bigr)
=\{(X,Y)\in\mathfrak u(p)\oplus\mathfrak u(q):
\operatorname{tr}X+\operatorname{tr}Y=0\}.
\]
It is isomorphic as a real Lie algebra to
\(\mathfrak u(1)\oplus\mathfrak{su}(p)\oplus\mathfrak{su}(q)\), although the corresponding [[lie-groups/connected-lie-group|connected Lie group]] need not be the direct product.

## Central-quotient presentation

The surjective homomorphism
\[
U(1)\times SU(p)\times SU(q)\longrightarrow S(U(p)\times U(q)),
\qquad
(z,A,B)\longmapsto (z^qA,z^{-p}B)
\]
has kernel
\[
\{(z,z^{-q}I_p,z^pI_q):z^{pq}=1\}\cong\mathbb Z_{pq}.
\]
Hence
\[
S(U(p)\times U(q))\cong
\bigl(U(1)\times SU(p)\times SU(q)\bigr)/\mathbb Z_{pq}.
\]

For \(p=2,q=3\), the map is
\[
(z,A,B)\longmapsto(z^3A,z^{-2}B),
\]
with kernel \(\{(z,z^{-3}I_2,z^2I_3):z^6=1\}\). Thus
\[
S(U(2)\times U(3))\cong
\bigl(U(1)\times SU(2)\times SU(3)\bigr)/\mathbb Z_6.
\]

## Standard Model role

The group \(S(U(2)\times U(3))\) is the image of the [[mathematical-physics/georgi-glashow-su5-embedding|Georgi–Glashow homomorphism]] inside \(SU(5)\). It is one common convention for the effective [[mathematical-physics/standard-model-gauge-group|Standard Model gauge group]].

## References

1. John C. Baez and John Huerta, “The Algebra of Grand Unified Theories,” *Bulletin of the American Mathematical Society* 47 (2010), 483–552. [arXiv record](https://arxiv.org/abs/0904.1556). Relevant: §3.1.
2. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026. [arXiv record](https://arxiv.org/abs/2606.15235). Relevant: §§1 and 3.
