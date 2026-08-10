+++
id = "lie-groups/compact-real-form"
title = "Compact real form"
kind = "definition"
summary = "A real form of a complex semisimple Lie algebra whose Killing form is negative definite."
aliases = ["compact real form", "compact form of a complex Lie algebra"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

Let \(\mathfrak g\) be a finite-dimensional complex [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]]. A real Lie subalgebra \(\mathfrak u\subset\mathfrak g\) is a **compact real form** of \(\mathfrak g\) if
\[
\mathfrak u\otimes_{\mathbb R}\mathbb C\cong\mathfrak g
\]
through the complex-linear extension of the inclusion, and the [[lie-groups/killing-form|Killing form]] of \(\mathfrak u\) is negative definite.

Equivalently, \(\mathfrak u\) is a real form of \(\mathfrak g\) that is the Lie algebra of a compact semisimple Lie group.

## Existence and uniqueness

Every complex semisimple Lie algebra has a compact real form. Any two compact real forms are conjugate by an inner automorphism of the complex Lie algebra.

One construction starts from a Chevalley basis \(h_i,e_\alpha\) and takes the real span of
\[
i h_i,\qquad e_\alpha-e_{-\alpha},\qquad i(e_\alpha+e_{-\alpha})
\]
for the simple coroot directions and positive roots \(\alpha\). The resulting real algebra has negative-definite Killing form.

## Classical and exceptional examples

The standard compact real forms include
\[
\mathfrak{su}(n)\subset\mathfrak{sl}_n(\mathbb C),
\qquad
\mathfrak{so}(n)\subset\mathfrak{so}_n(\mathbb C),
\qquad
\mathfrak{sp}(n)\subset\mathfrak{sp}_{2n}(\mathbb C).
\]
The compact real form of \(\mathfrak e_7\) is often denoted \(\mathfrak e_{7(-133)}\), where \(-133\) is the signature of its negative-definite Killing form.

## Compact conjugation

Complex conjugation with respect to the real vector space \(\mathfrak u\) is an antilinear involutive Lie algebra automorphism
\[
\sigma:\mathfrak g\to\mathfrak g,
\qquad
\mathfrak g^\sigma=\mathfrak u.
\]
Conversely, an antilinear involution whose fixed algebra has negative-definite Killing form determines a compact real form. This turns statements about complex roots and representations into statements about compact Lie groups after imposing the appropriate reality condition.

## References

1. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002, Chapters II, IV, VI. [Publisher record](https://doi.org/10.1007/978-1-4757-2453-0).
2. Jean-Pierre Serre, *Complex Semisimple Lie Algebras*, Springer, 1987, Chapter V. [Publisher record](https://doi.org/10.1007/978-1-4757-3910-7).
3. John C. Baez, “Three Generations in \(E_7\),” 2026, §1. [arXiv record](https://arxiv.org/abs/2608.06271).
