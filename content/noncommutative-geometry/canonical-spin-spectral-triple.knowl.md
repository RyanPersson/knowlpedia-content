+++
id = "noncommutative-geometry/canonical-spin-spectral-triple"
title = "Canonical spectral triple of a compact spin manifold"
kind = "definition"
summary = "The spectral triple formed by smooth functions, square-integrable spinors, and the spin Dirac operator on a closed Riemannian spin manifold."
aliases = ["commutative spin spectral triple", "Dirac spectral triple"]
domains = ["noncommutative-geometry", "differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be a closed [[differential-geometry/riemannian-manifold|Riemannian manifold]] with a
[[fiber-bundles/spin-structure|spin structure]] and complex
[[differential-geometry/spinor-bundle|spinor bundle]] \(S\). Its **canonical
spin spectral triple** is
\[
\bigl(C^\infty(M),\,L^2(M,S),\,\not D\bigr),
\]
where \(C^\infty(M)\) acts faithfully by pointwise multiplication and \(\not D\) is the self-adjoint closure of the [[noncommutative-geometry/dirac-operator|spin Dirac operator]]. The operator \(\not D\) has compact resolvent, and for every \(f\in C^\infty(M)\),
\[
[\not D,f]=c(df)
\]
extends to a bounded operator. These facts make the displayed data a [[noncommutative-geometry/spectral-triple|spectral triple]].

## Why the spectral-triple axioms hold

Ellipticity on the compact manifold implies that the resolvent of \(\not D\) is compact. The first-order Leibniz rule identifies its commutator with multiplication by the Clifford field \(c(df)\), which is bounded because \(M\) is compact. Smooth functions are used rather than all of \(C(M)\): a merely continuous function need not preserve the domain of \(\not D\) or have a [[functional-analysis/bounded-commutator|bounded commutator]].

## Parity and additional structures

If \(\dim M\) is even, chirality grades \(L^2(M,S)\), commutes with functions, and anticommutes with \(\not D\), producing an [[noncommutative-geometry/even-spectral-triple|even spectral triple]]. In odd dimension the canonical triple is ungraded. [[noncommutative-geometry/real-structure-spectral-triple|Charge conjugation]] can supply a real structure, but that operator and its dimension-dependent signs are additional data, not part of the three-component spectral triple defined in the core.

## Geometry recovered from the triple

The growth of the eigenvalues of \(|\not D|\) records the dimension through Weyl asymptotics. Connes's distance formula recovers the Riemannian geodesic distance from
\[
d(p,q)=\sup\{|f(p)-f(q)|:\lVert[\not D,f]\rVert\leq1\}.
\]
The reconstruction theorem requires further regularity, finiteness, orientability, and reality hypotheses; compact resolvent and bounded commutators alone do not characterize canonical manifold triples.

## References

1. Alain Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-hosted book](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Relevant: Part VI.1 on the spectral geometry of compact spin manifolds.
2. José M. Gracia-Bondía, Joseph C. Várilly, and Héctor Figueroa, *Elements of Noncommutative Geometry*, Birkhäuser, 2001. [DOI record](https://doi.org/10.1007/978-1-4612-0005-5). Relevant: §10.2 on the canonical commutative spectral triple.
