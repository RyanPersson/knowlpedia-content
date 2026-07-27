+++
id = "noncommutative-geometry/commutative-reconstruction-theorem"
title = "Commutative reconstruction theorem for spectral triples"
kind = "theorem"
summary = "A sufficiently regular commutative spectral triple satisfying the geometric axioms is the spectral geometry of a compact smooth manifold."
aliases = ["Connes reconstruction theorem", "spectral reconstruction theorem"]
domains = ["noncommutative-geometry", "differential-geometry"]
section_mode = "progressive"
+++

Let \((\mathcal A,H,D)\) be a unital commutative [[noncommutative-geometry/spectral-triple|spectral triple]] of integer metric dimension satisfying the reconstruction hypotheses: regularity, first order, [[noncommutative-geometry/hochschild-orientability-axiom|orientability]], [[noncommutative-geometry/finiteness-absolute-continuity-axiom|finiteness and absolute continuity]], and the additional multiplicity and closedness conditions in the chosen formulation. The **commutative reconstruction theorem** produces a unique compact oriented [[fiber-bundles/smooth-manifold|smooth manifold]] \(X\) and an isomorphism
\[
\mathcal A\cong C^\infty(X).
\]
Moreover, \(H\) is the \(L^2\)-space of sections of a finite-rank Hermitian bundle and \(D\) is a first-order [[differential-geometry/elliptic-differential-operator|elliptic differential operator]] of Dirac type. Real, irreducibility, and duality hypotheses refine the conclusion to spin or spin\(^{c}\) geometry.

## What is reconstructed

The \(C^*\)-closure of \(\mathcal A\) first determines a compact [[topology/hausdorff-space|Hausdorff space]] by commutative [[operator-algebras/gelfand-duality|Gelfand duality]]. [[functional-analysis/bounded-commutator|Bounded commutators]] with \(D\), regularity, and the orienting [[noncommutative-geometry/hochschild-cycle|Hochschild cycle]] then supply smooth coordinates and show that the algebra is all of \(C^\infty(X)\), rather than merely a dense [[real-analysis/subalgebra-of-continuous-functions|subalgebra of continuous functions]]. Finiteness reconstructs the bundle of smooth sections, while [[analysis/absolute-continuity|absolute continuity]] reconstructs its \(L^2\)-measure class.

Connes proves the manifold statement and uniqueness in [Theorem 11.3](https://doi.org/10.4171/JNCG/108). The associated distance formula recovers the geodesic metric once the operator has the canonical Clifford-symbol normalization.

## Hypotheses are a package

No single named axiom implies the conclusion. A commutative algebra with a compact-resolvent operator can fail to be regular, have the wrong multiplicities, or encode a singular space. Conversely, regularity and summability do not create orientability or finite projectivity. The reconstruction theorem is therefore properly stated only after fixing a complete axiom package.

The versions of the theorem also differ. Rennie and Várilly impose hypotheses
slightly stronger than Connes’s original list and reconstruct a compact
manifold with a [[fiber-bundles/spin-structure|spin structure]]
[Rennie–Várilly, Theorems 7.20 and 7.26](https://arxiv.org/abs/math/0610418).
Connes’s later spectral-characterization theorem isolates a robust
oriented-manifold conclusion.

## Canonical example and scope

For a closed [[differential-geometry/riemannian-manifold|Riemannian manifold]] \(X\) with a
[[fiber-bundles/spin-structure|spin structure]], the canonical triple
\[
\bigl(C^\infty(X),L^2(X,S),\not D\bigr)
\]
satisfies the hypotheses and reconstructs \(X\), its smooth structure, and its Riemannian metric. The theorem does not say that every commutative spectral triple is canonical: finite direct sums, nonfaithful representations, and operators with non-Clifford principal symbols can violate the multiplicity or geometric axioms.

Nonunital triples, manifolds with boundary, orbifolds, and singular spaces require modified reconstruction statements; they are not covered merely by deleting compactness or unitality.

## References

1. A. Connes, “On the Spectral Characterization of Manifolds,” *Journal of Noncommutative Geometry* 7 (2013), 1–82. [DOI record](https://doi.org/10.4171/JNCG/108). Relevant: §§1–2 for the hypotheses and §11, especially Theorem 11.3, for reconstruction.
2. A. Rennie and J. C. Várilly, “Reconstruction of Manifolds in Noncommutative Geometry,” 2007. [Stable preprint](https://arxiv.org/abs/math/0610418). Relevant: Theorems 7.20 and 7.26, reconstructing the smooth manifold and spin geometry.
