+++
id = "differential-geometry/variation-of-hodge-structure"
title = "Variation of Hodge structure"
kind = "definition"
summary = "A local system whose fibers carry Hodge structures varying holomorphically and satisfying Griffiths transversality."
aliases = ["VHS"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

A **real variation of Hodge structure of weight \(n\)** on a [[differential-geometry/complex-manifold|complex manifold]] \(S\) consists of a finite-rank real local system \(\mathbb V_{\mathbb R}\), its [[differential-geometry/holomorphic-vector-bundle|holomorphic bundle]] \(\mathcal V=\mathbb V_{\mathbb R}\otimes_{\mathbb R}\mathcal O_S\) with [[fiber-bundles/flat-vector-bundle-connection|flat connection]] \(\nabla\), and holomorphic subbundles forming a decreasing filtration \(F^\bullet\mathcal V\). At every \(s\in S\), the filtration defines a pure real Hodge structure of weight \(n\), and it satisfies **Griffiths transversality**
\[
\nabla(F^p\mathcal V)\subseteq
\Omega_S^1\otimes F^{p-1}\mathcal V.
\]
A polarized variation additionally has a flat bilinear form that polarizes every fiber.

## Period-map interpretation

After locally trivializing the flat bundle, \(F^\bullet\) determines a holomorphic map from \(S\) to a flag variety. Fiberwise Hodge opposedness restricts its image to a period domain, and Griffiths transversality says that its differential lies in the horizontal subbundle. This is the infinitesimal period relation established in [Griffiths, §1, Theorems 1.27 and 1.34](https://doi.org/10.2307/2373485).

## Geometric construction

For a smooth proper holomorphic family \(f:\mathcal X\to S\) of compact [[differential-geometry/kahler-manifold|Kähler manifolds]], the local system \(R^nf_*\mathbb R\), its Gauss–Manin connection, and the fiberwise [[differential-geometry/hodge-filtration|Hodge filtrations]] form a variation of weight \(n\). The locally constant lattice \(R^nf_*\mathbb Z\) gives an integral structure when torsion is removed. Voisin develops this construction in [Chapter 9 and §10.2](https://doi.org/10.1017/CBO9780511615344).

## Conventions and near-misses

A holomorphic family of filtrations with pure Hodge fibers is not a variation unless it is tied to a flat local system and obeys transversality. “VHS” may mean real, rational, integral, or complex variation, and polarization is sometimes included by default; both choices must be stated. Variations are usually assumed to have locally constant Hodge numbers so that the \(F^p\) are subbundles.

## References

1. Phillip A. Griffiths, “Periods of Integrals on Algebraic Manifolds, II: Local Study of the Period Mapping,” *American Journal of Mathematics* 90 (1968), 805–865. [DOI record](https://doi.org/10.2307/2373485). Relevant: §1, especially Theorems 1.27 and 1.34, for the period map and its infinitesimal relation.
2. Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge Studies in Advanced Mathematics 76, Cambridge University Press, 2002. [Publisher record](https://doi.org/10.1017/CBO9780511615344). Relevant: Chapter 9, especially §9.2, and Chapter 10, especially §10.2.
