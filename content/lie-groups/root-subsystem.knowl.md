+++
id = "lie-groups/root-subsystem"
title = "Root subsystem"
kind = "definition"
summary = "A subset of a root system that is itself a root system in its real span."
aliases = ["root subsystem", "subsystem of a root system"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/root-system", "linear-algebra/euclidean-space", "linear-algebra/inner-product"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\Phi\) be a [[lie-groups/root-system|root system]] in a [[linear-algebra/euclidean-space|Euclidean space]] \(V\). A subset \(\Psi\subseteq\Phi\) is a **root subsystem** if \(\Psi\) is itself a root system in \(\operatorname{span}_{\mathbb R}(\Psi)\) with the induced [[linear-algebra/inner-product|inner product]]. Equivalently, \(\Psi\) spans its ambient subspace and
\[
s_\alpha(\Psi)=\Psi
\qquad\text{for every }\alpha\in\Psi,
\]
where \(s_\alpha\) is reflection in the hyperplane perpendicular to \(\alpha\).

## Full and closed subsystems

A subsystem is **full** in its span if
\[
\Psi=\Phi\cap\operatorname{span}_{\mathbb R}(\Psi).
\]
It is **closed in \(\Phi\)** if \(\alpha,\beta\in\Psi\) and \(\alpha+\beta\in\Phi\) imply \(\alpha+\beta\in\Psi\). These adjectives express additional conditions: “root subsystem” alone need not mean full or closed in every source.

If \(I\) is a subset of a chosen base \(\Delta\) of [[lie-groups/simple-root|simple roots]], then
\[
\Phi_I:=\Phi\cap\operatorname{span}_{\mathbb Z}(I)
=\Phi\cap\operatorname{span}_{\mathbb R}(I)
\]
is a full closed subsystem. Its [[lie-groups/dynkin-diagram|Dynkin diagram]] is obtained by retaining the vertices in \(I\) and the edges between them.

## Lie-algebra interpretation

For a complex [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]] with [[lie-groups/root-space-decomposition|root-space decomposition]]
\[
\mathfrak g=\mathfrak h\oplus\bigoplus_{\alpha\in\Phi}\mathfrak g_\alpha,
\]
closed subsystems select collections of [[lie-groups/root-space|root spaces]] that can participate in [[lie-groups/regular-lie-subalgebra|regular subalgebras]]. The subsystem \(\Phi_I\) gives the semisimple part of the [[lie-groups/levi-subalgebra|Levi subalgebra]] attached to \(I\).

## References

1. Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 4–6*, Springer, 2002, Chapter VI, §1. [Publisher record](https://link.springer.com/book/9783540691716).
2. Toshio Oshima, “A classification of subsystems of a root system,” 2006, §§1–2. [arXiv record](https://arxiv.org/abs/math/0611904).
3. John C. Baez, “Three Generations in \(E_7\),” 2026, §§2, 5. [arXiv record](https://arxiv.org/abs/2608.06271).
