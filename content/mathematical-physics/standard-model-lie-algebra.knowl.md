+++
id = "mathematical-physics/standard-model-lie-algebra"
title = "Standard Model Lie algebra"
kind = "definition"
summary = "The real compact Lie algebra of Standard Model internal symmetries and its complexification."
aliases = ["g_SM", "complexified Standard Model Lie algebra"]
domains = ["mathematical-physics", "lie-groups"]
prerequisites = ["lie-groups/complexification-of-a-real-lie-algebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

The **Standard Model Lie algebra** in its compact real form is
\[
\mathfrak g_{\mathrm{SM},\mathbb R}
=\mathfrak u(1)\oplus\mathfrak{su}(2)\oplus\mathfrak{su}(3).
\]
Its [[lie-groups/complexification-of-a-real-lie-algebra|complexification]] is
\[
\mathfrak g_{\mathrm{SM}}
=\mathbb C\oplus\mathfrak{sl}_2(\mathbb C)\oplus\mathfrak{sl}_3(\mathbb C).
\]
Authors working with complex representations often denote the second algebra simply by \(\mathfrak g_{\mathrm{SM}}\), so the ground field should be stated.

## Relation to the global group

Both
\[
U(1)\times SU(2)\times SU(3)
\quad\text{and}\quad
\bigl(U(1)\times SU(2)\times SU(3)\bigr)/\mathbb Z_6
\]
have the same real [[lie-groups/lie-algebra|Lie algebra]], because a finite [[lie-groups/central-quotient-of-a-lie-group|central quotient]] does not change infinitesimal data. Thus the Lie algebra cannot distinguish the two global forms of the [[mathematical-physics/standard-model-gauge-group|Standard Model gauge group]].

## Complexified matrix realization inside \(\mathfrak{sl}_5(\mathbb C)\)

Differentiating the Georgi–Glashow map and then complexifying gives
\[
(t,X,Y)\longmapsto
\begin{pmatrix}
3tI_2+X&0\\
0&-2tI_3+Y
\end{pmatrix},
\]
where \(t\in\mathbb C\), \(X\in\mathfrak{sl}_2(\mathbb C)\), and \(Y\in\mathfrak{sl}_3(\mathbb C)\). Its trace is \(6t-6t=0\), so the image lies in \(\mathfrak{sl}_5(\mathbb C)\).

## References

1. John C. Baez and John Huerta, “The Algebra of Grand Unified Theories,” *Bulletin of the American Mathematical Society* 47 (2010), 483–552. [arXiv record](https://arxiv.org/abs/0904.1556). Relevant: §3.1.
2. John C. Baez, “Three Generations in \(E_7\),” 2026. [arXiv record](https://arxiv.org/abs/2608.06271). Relevant: §§1–2.
