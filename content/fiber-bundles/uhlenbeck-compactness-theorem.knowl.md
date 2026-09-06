+++
id = "fiber-bundles/uhlenbeck-compactness-theorem"
title = "Uhlenbeck compactness theorem"
kind = "theorem"
summary = "A compactness theorem giving subsequential convergence of bounded-energy instantons modulo gauge away from finitely many bubbling points."
aliases = ["Uhlenbeck weak compactness", "bubbling compactness for instantons"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["fiber-bundles/instanton", "fiber-bundles/bundle-isomorphism", "fiber-bundles/gauge-transformation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(P\to X\) be a principal bundle with compact structure group over a closed oriented Riemannian four-manifold. If \((A_i)\) is a sequence of [[fiber-bundles/instanton|instantons]] with uniformly bounded Yang–Mills energy, then a subsequence has a finite set \(S\subset X\), a bundle \(P_\infty\to X\setminus S\), and an instanton \(A_\infty\) such that, for every compact \(K\subset X\setminus S\), there are [[fiber-bundles/bundle-isomorphism|bundle isomorphisms]]
\[
u_i:P_\infty|_K\longrightarrow P|_K
\qquad\text{with}\qquad
u_i^*(A_i|_K)\longrightarrow A_\infty|_K
\]
smoothly. After choosing identifications of the restricted bundles, these maps may be expressed as [[fiber-bundles/gauge-transformation|gauge transformations]]. The missing energy concentrates at points of \(S\); after removable-singularity extension, the limit together with these point masses is an ideal instanton.

## Analytical mechanism

On a ball where \(\|F_A\|_{L^2}\) is sufficiently small, Uhlenbeck’s gauge-fixing theorem places \(A\) in [[fiber-bundles/coulomb-gauge|Coulomb gauge]] and controls its Sobolev norm by the curvature norm. Weak Sobolev compactness then gives a convergent subsequence on such balls. A uniform total-energy bound permits only finitely many balls where the small-energy threshold fails, producing the bubbling set \(S\).

Elliptic regularity for the instanton equation upgrades weak local convergence to smooth convergence away from \(S\). The same local gauge theorem also underlies weak compactness results for more general sequences of connections, but the instanton hypothesis supplies the smooth limiting equation stated here.

## Energy measures and bubbling

After passage to a subsequence, the curvature-energy measures have the form
\[
\lvert F_{A_i}\rvert^2\,d\operatorname{vol}
\rightharpoonup
\lvert F_{A_\infty}\rvert^2\,d\operatorname{vol}
+\sum_{x\in S}\varepsilon_x\delta_x,
\qquad \varepsilon_x>0.
\]
For standard instanton normalizations, each \(\varepsilon_x\) is quantized by the energy of a nontrivial instanton on \(S^4\). Rescaling around a concentration point reveals one or more bubbles; iteration produces a bubble tree.

## Scope

**Warning.** A bound on curvature does not normally yield compactness before quotienting by gauge. Nor does the theorem assert smooth convergence at bubbling points: [[fiber-bundles/instanton-number|topological charge]] can be lost from the limiting bundle and retained only by the ideal-instanton data.

## References

1. Karen K. Uhlenbeck, “Connections with \(L^p\) Bounds on Curvature,” *Communications in Mathematical Physics* 83 (1982), 31–42. [DOI record](https://doi.org/10.1007/BF01947069). Relevant: Theorem 1.3, local Coulomb gauges, and the global weak-compactness argument.
2. Simon K. Donaldson and Peter B. Kronheimer, *The Geometry of Four-Manifolds*, Oxford University Press, 1990. [DOI record](https://doi.org/10.1093/oso/9780198535539.001.0001). Relevant: Chapter 4, Uhlenbeck convergence, bubbling, and ideal instantons.
