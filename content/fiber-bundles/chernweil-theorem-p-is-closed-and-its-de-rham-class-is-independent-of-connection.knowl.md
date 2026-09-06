+++
id = "fiber-bundles/chernweil-theorem-p-is-closed-and-its-de-rham-class-is-independent-of-connection"
title = "Chern–Weil theorem"
kind = "knowl"
summary = "Invariant polynomials in curvature yield closed forms whose cohomology class does not depend on the connection."
aliases = ["chernweil-theorem-p-is-closed-and-its-de-rham-class-is-independent-of-connection", "Chern–Weil theorem"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/principal-g-bundle", "fiber-bundles/principal-connection", "fiber-bundles/curvature", "fiber-bundles/lemma-chernweil-forms-are-basic", "fiber-bundles/basic-forms-theorem", "fiber-bundles/transgression-theorem-p-p-is-exact"]
dependency_review_count = 1
legacy_source_path = "fiber-bundles/chernweil-theorem-p-is-closed-and-its-de-rham-class-is-independent-of-connection.md"
+++

Let \(\pi:P\to M\) be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with structure group \(G\) and Lie algebra \(\mathfrak g\). Let \(\omega\) be a [[fiber-bundles/principal-connection|principal connection]] with [[fiber-bundles/curvature|curvature]] \(\Omega\in\Omega^2(P;\mathfrak g)\).

Let \(q\) be an \(\operatorname{Ad}\)-invariant homogeneous polynomial of degree \(k\) on \(\mathfrak g\), represented by a symmetric \(k\)-linear map
\[
q:\underbrace{\mathfrak g\times\cdots\times\mathfrak g}_{k\ \text{times}}\to \mathbb R
\quad\text{satisfying}\quad
q(\operatorname{Ad}(g)X_1,\dots,\operatorname{Ad}(g)X_k)=q(X_1,\dots,X_k).
\]
Define the \(2k\)-form on the total space \(P\) by inserting \(\Omega\) into \(q\) and wedging:
\[
q(\Omega)\in\Omega^{2k}(P),\qquad
q(\Omega):=q(\Omega,\dots,\Omega),
\]
with the usual graded antisymmetrization convention.

**Theorem (Chern–Weil).**
1. The form \(q(\Omega)\) is **closed**, i.e. \(d\,q(\Omega)=0\).
2. The form \(q(\Omega)\) is **basic** (see [[fiber-bundles/lemma-chernweil-forms-are-basic|Chern–Weil forms are basic]]), hence by the [[fiber-bundles/basic-forms-theorem|basic forms theorem]] there is a unique closed form \(\operatorname{cw}_q(\omega)\in\Omega^{2k}(M)\) with
   \[
   \pi^*\operatorname{cw}_q(\omega)=q(\Omega).
   \]
3. The de Rham cohomology class \([\operatorname{cw}_q(\omega)]\in H^{2k}_{\mathrm{dR}}(M)\) is independent of the choice of connection \(\omega\); equivalently, changing \(\omega\) changes \(\operatorname{cw}_q(\omega)\) by an exact form (see the [[fiber-bundles/transgression-theorem-p-p-is-exact|transgression theorem]]).

## Remarks

A standard route to (1) is to combine the [[fiber-bundles/bianchi-identity|Bianchi identity]] with \(\operatorname{Ad}\)-invariance of \(q\).

## Examples
1. **First Chern form for \(U(1)\).** For \(G=U(1)\) and \(q(X)=\frac{i}{2\pi}X\) (viewing \(\mathfrak u(1)\cong i\mathbb R\)), \(\operatorname{cw}_q(\omega)=\frac{i}{2\pi}F\) is the usual curvature representative of the first Chern class.
2. **Second Chern character piece.** For a matrix group such as \(G=SU(n)\) and \(q(X)=\operatorname{tr}(X^2)\), the descended form \(\operatorname{tr}(F\wedge F)\) is closed and defines a characteristic class independent of the connection.
3. **Pontryagin-type forms.** For \(G=SO(n)\), \(\operatorname{Ad}\)-invariant polynomials built from traces of even powers, such as \(\operatorname{tr}(X^{2j})\) in the defining representation, produce the usual Pontryagin form representatives on the base.
