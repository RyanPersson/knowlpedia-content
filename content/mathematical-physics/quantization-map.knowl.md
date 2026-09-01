+++
id = "mathematical-physics/quantization-map"
title = "Quantization map"
kind = "definition"
summary = "A map from a selected Poisson algebra of classical observables to operators on a quantum state space."
aliases = ["canonical quantization map", "Dirac quantization map", "operator quantization"]
domains = ["mathematical-physics", "differential-geometry", "functional-analysis"]
prerequisites = ["differential-geometry/symplectic-manifold", "differential-geometry/poisson-algebra-smooth-functions", "linear-algebra/hilbert-space", "functional-analysis/symmetric-operator"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M,\omega)\) be a [[differential-geometry/symplectic-manifold|symplectic manifold]], let \(\mathcal A\subseteq C^\infty(M,\mathbb R)\) be a [[differential-geometry/poisson-algebra-smooth-functions|Poisson subalgebra]] containing the constants, and let \(\mathscr D\) be a dense subspace of a complex [[linear-algebra/hilbert-space|Hilbert space]] \(\mathscr H\). A **quantization map** on \(\mathcal A\) is a real-linear map
\[
Q_\hbar:\mathcal A\longrightarrow \operatorname{End}(\mathscr D)
\]
whose values are [[functional-analysis/symmetric-operator|symmetric operators]] and which satisfies specified classical-to-quantum compatibility conditions. In the exact Dirac form these include
\[
Q_\hbar(1)=I|_{\mathscr D},
\qquad
[Q_\hbar(f),Q_\hbar(g)]=i\hbar Q_\hbar(\{f,g\}).
\]
The domain \(\mathcal A\), the common operator domain \(\mathscr D\), and any extra irreducibility or self-adjointness requirements are part of the quantization data.

## Covariance under symmetries

Suppose a [[differential-geometry/symplectic-lie-group-action|symplectic Lie group action]] \(\alpha:G\to\operatorname{Symp}(M,\omega)\) is represented by a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] \(U_\hbar\) preserving \(\mathscr D\). The quantization is **covariant** when
\[
U_\hbar(g)Q_\hbar(f)U_\hbar(g)^{-1}
=Q_\hbar\!\left(f\circ\alpha(g^{-1})\right).
\]
For a [[differential-geometry/hamiltonian-lie-group-action|Hamiltonian action]] with [[differential-geometry/comoment-map|comoment map]] \(J:\mathfrak g\to C^\infty(M)\), infinitesimal compatibility is commonly expressed by
\[
Q_\hbar(J_X)=i\hbar\,dU_\hbar(X),
\]
with signs adjusted consistently if different Hamiltonian-vector-field or derived-representation conventions are used.

## Scope and obstructions

The displayed axioms are a template, not a claim that such a map exists on all smooth observables. Even on linear symplectic space, the exact bracket rule cannot be extended from the basic observables to the full polynomial Poisson algebra while retaining the usual additional requirements; this is the [[mathematical-physics/groenewold-van-hove-theorem|Groenewold–Van Hove obstruction]]. Geometric, deformation, and semiclassical quantization respond by changing the domain, codomain, or exactness demanded of the correspondence.

## References

1. M. J. Gotay, H. B. Grundling, and G. M. Tuynman, “Obstruction Results in Quantization Theory,” *Journal of Nonlinear Science* 6 (1996), 469–498. [arXiv record](https://arxiv.org/abs/dg-ga/9605001). Relevant: §§2–3, definitions of prequantization and quantization of a Poisson algebra.
2. N. M. J. Woodhouse, *Geometric Quantization*, 2nd ed., Oxford University Press, 1992. [Publisher record](https://global.oup.com/academic/product/geometric-quantization-9780198502708). Relevant: Chapters 1–5, classical observables, prequantization, and polarizations.
