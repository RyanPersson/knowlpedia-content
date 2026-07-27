+++
id = "differential-geometry/hodge-filtration"
title = "Hodge filtration"
kind = "definition"
summary = "The decreasing filtration obtained by collecting the Hodge components whose first bidegree is at least a prescribed integer."
aliases = ["decreasing Hodge filtration"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(V\) carry a [[differential-geometry/pure-hodge-structure|pure Hodge structure]] of weight \(n\), with
\(V_{\mathbb C}=\bigoplus_{p+q=n}V^{p,q}\). Its **Hodge filtration** is the decreasing filtration
\[
F^pV_{\mathbb C}=\bigoplus_{r\geq p}V^{r,n-r}.
\]
Thus \(F^{p+1}\subseteq F^p\), the filtration is exhaustive and separated, and
\[
V^{p,q}=F^pV_{\mathbb C}\cap\overline{F^qV_{\mathbb C}}
\qquad (p+q=n).
\]
For a compact [[differential-geometry/complex-manifold|complex manifold]], the Hodge filtration on degree-\(n\) de Rham cohomology is induced by differential forms whose holomorphic degree is at least \(p\); in the Kähler case it agrees with the displayed direct-sum formula.

## Recovering the decomposition

A decreasing filtration on the complexification of a real vector space comes from a pure Hodge structure of weight \(n\) precisely when
\[
V_{\mathbb C}=F^p\oplus\overline{F^{\,n-p+1}}
\]
for every \(p\). This opposedness condition recovers the Hodge components and the conjugation symmetry, so the filtration and decomposition formulations contain the same information [Voisin, §7.1.1](https://doi.org/10.1017/CBO9780511615344.008).

## Geometric role

For a holomorphic family of compact [[differential-geometry/kahler-manifold|Kähler manifolds]], the subspaces \(F^p\) vary holomorphically even though the individual subspaces \(H^{p,q}\) generally do not. This makes the filtration the natural formulation for period maps and variations of Hodge structure. Griffiths transversality measures its failure to be preserved by the flat connection.

## Conventions and near-misses

The Hodge filtration is decreasing and indexed by the first bidegree. The weight filtration of a mixed Hodge structure is instead increasing and records weights; the two filtrations are not interchangeable. An arbitrary filtration with the correct dimensions need not be a Hodge filtration because it may fail the conjugate-opposedness condition.

## References

1. Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge Studies in Advanced Mathematics 76, Cambridge University Press, 2002. [Chapter record](https://doi.org/10.1017/CBO9780511615344.008). Relevant: §7.1.1, equivalence of decomposition and filtration descriptions.
2. Phillip A. Griffiths, “Periods of Integrals on Algebraic Manifolds, II: Local Study of the Period Mapping,” *American Journal of Mathematics* 90 (1968), 805–865. [DOI record](https://doi.org/10.2307/2373485). Relevant: §1, especially Theorems 1.27 and 1.34 on the differential of the period filtration.
