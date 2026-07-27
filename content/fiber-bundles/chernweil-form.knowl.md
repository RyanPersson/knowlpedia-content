+++
id = "fiber-bundles/chernweil-form"
title = "Chern–Weil form"
kind = "knowl"
summary = "A differential form built from the curvature of a principal connection using an invariant polynomial."
aliases = ["chernweil-form", "Chern–Weil form"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/chernweil-form.md"
+++

Let \(\pi:P\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]] and let \(\omega\in\Omega^1(P;\mathfrak g)\) be a [[fiber-bundles/principal-connection|principal connection]] with curvature \(\Omega\in\Omega^2(P;\mathfrak g)\).

Let \(q\in(\operatorname{Sym}^k\mathfrak g^*)^G\) be an \(\operatorname{Ad}\)-invariant symmetric polynomial of degree \(k\). The **Chern–Weil form** associated to \(q\) and \(\omega\) is the unique \(2k\)-form \(\operatorname{cw}_q(\omega)\) on \(M\) satisfying
\[
\pi^*\operatorname{cw}_q(\omega)=q(\Omega,\ldots,\Omega).
\]

The form \(q(\Omega,\ldots,\Omega)\) is **basic** on \(P\), so it descends uniquely to the base. The wedge products of the \(\mathfrak g\)-valued curvature forms are understood through the multilinear extension of \(q\).

## Remarks

Chern–Weil theory associates closed differential forms to a principal connection by applying invariant polynomials to its curvature. These are the differential-form representatives of [[fiber-bundles/characteristic-class|characteristic classes]].

## What Chern–Weil theory guarantees
- The form \(\operatorname{cw}_q(\omega)\) is closed, and its de Rham cohomology class does not depend on the choice of connection; this is the content of [[fiber-bundles/chernweil-theorem-p-is-closed-and-its-de-rham-class-is-independent-of-connection|the Chern–Weil theorem]].
- Consequently, \([\operatorname{cw}_q(\omega)]\in H^{2k}_{\mathrm{dR}}(M)\) is an invariant of the underlying principal bundle.

## Examples
1. **First Chern form for a unitary bundle**
   Let \(E\to M\) be a complex vector bundle with a [[fiber-bundles/hermitian-metric|Hermitian metric]] and a unitary connection. The associated principal \(U(n)\)-bundle of unitary frames yields a curvature matrix \(F\in\Omega^2(M;\mathfrak{u}(n))\). Taking \(q(X)=\frac{i}{2\pi}\operatorname{tr}(X)\) gives
   \[
   c_1(\nabla)=\frac{i}{2\pi}\,\mathrm{tr}(F),
   \]
   representing the first Chern class in de Rham cohomology (see [[fiber-bundles/chern-class|Chern class]] and [[fiber-bundles/integrality-of-chern-classes|integrality of Chern classes]]).

2. **First Pontryagin form**
   For a real vector bundle with structure group reduced to \(SO(n)\) and a compatible connection, the curvature \(F\in\Omega^2(M;\mathfrak{so}(n))\) defines
   \[
   p_1(\nabla)= -\frac{1}{8\pi^2}\,\mathrm{tr}(F\wedge F),
   \]
   which represents the first Pontryagin class (see [[fiber-bundles/pontryagin-class|Pontryagin class]]).

3. **Euler form via the Pfaffian**
   For an oriented rank-\(2m\) real bundle with an \(SO(2m)\)-connection, the Pfaffian produces a \(2m\)-form representative of the [[fiber-bundles/euler-class|Euler class]].
