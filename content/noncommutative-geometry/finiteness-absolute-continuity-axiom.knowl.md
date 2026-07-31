+++
id = "noncommutative-geometry/finiteness-absolute-continuity-axiom"
title = "Finiteness and absolute-continuity axiom for a spectral triple"
kind = "definition"
summary = "The reconstruction axiom requiring the smooth spinor domain to be finite projective and its Hilbert product to arise from noncommutative integration."
aliases = ["finiteness axiom", "absolute-continuity axiom"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
+++

Let \((\mathcal A,H,D)\) be a \(p\)-dimensional [[noncommutative-geometry/regular-spectral-triple|regular spectral triple]] and set \(H^\infty=\bigcap_{k\geq1}\operatorname{Dom}D^k\). It satisfies the **finiteness and absolute-continuity axiom** when \(H^\infty\) is a finitely generated projective left \(\mathcal A\)-module and carries an \(\mathcal A\)-valued Hermitian pairing \((\cdot\mid\cdot)_{\mathcal A}\) for which
\[
\langle\xi,a\eta\rangle_H
=
\int_D a\,(\xi\mid\eta)_{\mathcal A}
\]
for all \(a\in\mathcal A\) and \(\xi,\eta\in H^\infty\). Here \(\int_D\) is the chosen [[noncommutative-geometry/noncommutative-integral|noncommutative integral]], normally defined from the critical power \(|D|^{-p}\). Thus algebraic finite-projectivity and analytic volume compatibility are both required.

## Geometric meaning

For the canonical spin [[noncommutative-geometry/spectral-triple|spectral triple]] of a closed \(p\)-dimensional Riemannian spin manifold, \(H^\infty\) is the module of smooth spinor sections. The [[fiber-bundles/serre-swan-theorem|Serre–Swan theorem]] makes this module finitely generated projective over \(C^\infty(M)\). Its pointwise Hermitian product is \(C^\infty(M)\)-valued, and integration against Riemannian volume recovers the \(L^2\)-inner product. The axiom abstracts precisely these two facts.

Finiteness prevents the smooth domain from behaving like an arbitrary infinite-rank module. [[analysis/absolute-continuity|Absolute continuity]] ties its Hilbert-space completion to the same volume functional that the spectrum of \(D\) determines.

## Normalization and sidedness

The displayed identity uses a left module and the convention that the Hilbert-space [[linear-algebra/inner-product|inner product]] is linear in its second variable. With a right-module convention, the order of \(a\) and the module pairing changes. Sources may also multiply the noncommutative integral by a dimension-dependent constant. These are convention changes, not extra geometric axioms.

The formula requires more than the statement that \(H^\infty\) is a [[algebra-modules/finitely-generated-module|finitely generated]] [[algebra-modules/projective-module|projective module]]. One must specify a positive Hermitian module structure and verify that its integrated pairing equals the given Hilbert-space product.

## Role in reconstruction

Finiteness and absolute continuity are independent of regularity, [[noncommutative-geometry/hochschild-orientability-axiom|Hochschild orientability]], and the first-order condition. In reconstruction proofs, finite projectivity produces a smooth [[fiber-bundles/vector-bundle|vector bundle]] once the algebra has been identified with \(C^\infty(X)\), while absolute continuity identifies \(H\) with its \(L^2\)-space of sections [Rennie–Várilly, §§3.1 and 7].

## References

1. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-hosted text](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Relevant: Chapter VI, §1, finiteness and absolute continuity among the spectral axioms.
2. A. Rennie and J. C. Várilly, “Reconstruction of Manifolds in Noncommutative Geometry,” 2007. [Stable preprint](https://arxiv.org/abs/math/0610418). Relevant: §3.1 for the axiom system and §7 for reconstruction of the smooth bundle and Hilbert space.
