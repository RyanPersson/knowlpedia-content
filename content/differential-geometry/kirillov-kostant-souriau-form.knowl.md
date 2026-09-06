+++
id = "differential-geometry/kirillov-kostant-souriau-form"
title = "Kirillov–Kostant–Souriau symplectic form"
kind = "definition"
summary = "The canonical invariant symplectic form on a coadjoint orbit."
aliases = ["KKS form", "Kirillov form", "Kostant–Kirillov form"]
domains = ["differential-geometry", "lie-groups"]
prerequisites = ["fiber-bundles/lie-group", "lie-groups/lie-algebra", "differential-geometry/coadjoint-orbit", "differential-geometry/symplectic-manifold"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let [[fiber-bundles/lie-group|\(G\)]] be a finite-dimensional Lie group with [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\), and let \(\mathcal O\subseteq\mathfrak g^*\) be a [[differential-geometry/coadjoint-orbit|coadjoint orbit]]. For \(X\in\mathfrak g\), write
\[
X^\#_\mu=\left.\frac{d}{dt}\right|_{0}\operatorname{Ad}_{\exp(tX)}^*\mu.
\]
The **Kirillov–Kostant–Souriau form** on \(\mathcal O\) is defined by
\[
(\omega_{\mathrm{KKS}})_\mu(X^\#_\mu,Y^\#_\mu)
=\langle\mu,[X,Y]\rangle.
\]
This prescription is well defined and produces a smooth, \(G\)-invariant, closed, nondegenerate two-form; hence every coadjoint orbit is canonically a [[differential-geometry/symplectic-manifold|symplectic manifold]].

## Well-definedness and nondegeneracy

If \(X^\#_\mu=0\), then \(X\) lies in the stabilizer Lie algebra \(\mathfrak g_\mu\), so \(\langle\mu,[X,Y]\rangle=0\) for every \(Y\). The displayed value therefore depends only on the tangent vectors, not on their representatives in \(\mathfrak g\). The same observation shows that a tangent vector pairing to zero with all others must itself vanish.

## Closedness and invariance

Equivariance of the coadjoint action and invariance of the [[fiber-bundles/lie-bracket|Lie bracket]] imply \(G\)-invariance of \(\omega_{\mathrm{KKS}}\). Evaluating the [[fiber-bundles/exterior-derivative|exterior derivative]] on [[differential-geometry/infinitesimal-generator-lie-action|fundamental vector fields]] reduces \(d\omega_{\mathrm{KKS}}=0\) to the Jacobi identity.

## Moment map and sign convention

With the convention displayed in the core and \(d\mu^\xi=\iota_{\xi_{\mathcal O}}\omega\), the inclusion \(\mathcal O\hookrightarrow\mathfrak g^*\) is an equivariant [[fiber-bundles/moment-map|moment map]]. Reversing the definition of fundamental [[fiber-bundles/vector-field|vector fields]] or using \(\iota_{X_H}\omega=-dH\) reverses the KKS sign in many texts. The convention must therefore be checked before comparing formulas.

## References

1. A. A. Kirillov, *Elements of the Theory of Representations*, Springer, 1976. [DOI record](https://doi.org/10.1007/978-3-642-66243-0). Relevant: Chapter 1, coadjoint orbits and their canonical two-form.
2. Bertram Kostant, “Quantization and Unitary Representations,” in *Lectures in Modern Analysis and Applications III*, Lecture Notes in Mathematics 170, Springer, 1970, pp. 87–208. [Volume DOI record](https://doi.org/10.1007/BFb0079063). Relevant: coadjoint orbits, symplectic structure, and moment maps.
