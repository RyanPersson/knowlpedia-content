+++
id = "differential-geometry/pseudo-riemannian-manifold"
title = "Pseudo-Riemannian manifold"
kind = "definition"
summary = "A smooth manifold equipped with a nondegenerate symmetric metric whose signature is constant on each connected component."
aliases = ["semi-Riemannian manifold", "indefinite Riemannian manifold", "pseudo-Riemannian metric"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/smooth-manifold", "topology/connected-component", "linear-algebra/signature-of-symmetric-bilinear-form"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) be a finite-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]]. A **pseudo-Riemannian metric** on \(M\) is a smooth symmetric section
\[
g\in\Gamma^\infty(T^*M\otimes T^*M)
\]
such that \(g_p\) is nondegenerate on \(T_pM\) for every \(p\in M\). A **pseudo-Riemannian manifold** is a pair \((M,g)\). On each [[topology/connected-component|connected component]], the numbers of negative and positive squares in a diagonalization of \(g_p\) are constant; this ordered pair is the [[linear-algebra/signature-of-symmetric-bilinear-form|signature]] of \(g\).

## Local form and convention

In local coordinates,
\[
g=g_{ij}\,dx^i\otimes dx^j,
\]
where \((g_{ij})\) is an invertible symmetric matrix at every point. This knowl writes the signature as \((r,s)\), with \(r\) negative and \(s\) positive directions. Thus a metric of signature \((1,n-1)\) is locally represented by \(\operatorname{diag}(-1,1,\ldots,1)\).

Nondegeneracy, rather than positive definiteness, is the essential condition. It makes the bundle map \(g^\flat:TM\to T^*M\) an isomorphism and gives an inverse metric \(g^{-1}\) on \(T^*M\).

## Canonical constructions

Exactly as in [[differential-geometry/riemannian-manifold|Riemannian geometry]], \(g\) determines a unique torsion-free metric-compatible [[fiber-bundles/levicivita-connection-connection|Levi–Civita connection]]. It also determines curvature and a volume density. Unlike a Riemannian metric, an indefinite metric does not define a norm or metric-space distance: nonzero vectors can be null, and the quadratic form can take either sign.

## Important special cases

Signature \((0,n)\) gives a Riemannian metric in this convention. Signature \((1,n-1)\) gives a [[differential-geometry/lorentzian-manifold|Lorentzian manifold]]. Reversing the overall sign exchanges \((r,s)\) and \((s,r)\) without changing the null cone, so both sign conventions occur in the literature.

## References

1. Barrett O'Neill, *Semi-Riemannian Geometry With Applications to Relativity*, Academic Press, 1983. [Publisher record](https://doi.org/10.1016/C2009-0-03118-3). Relevant: Chapters 1–3.
2. John K. Beem, Paul E. Ehrlich, and Kevin L. Easley, *Global Lorentzian Geometry*, 2nd ed., Marcel Dekker, 1996. [Publisher record](https://doi.org/10.1201/9780203753125). Relevant: Chapter 1.
