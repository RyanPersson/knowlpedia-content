+++
id = "algebraic-geometry-foundations/locally-of-finite-presentation"
title = "Locally of finite presentation"
kind = "knowl"
summary = "A scheme morphism that is locally induced by finitely presented algebras."
aliases = ["locally-of-finite-presentation", "Locally of finite presentation"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/scheme"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
+++

A morphism \(f:Y\to X\) of [[algebraic-geometry-foundations/scheme|schemes]] is **locally of finite presentation** if \(X\) has an affine open cover \(U_i=\operatorname{Spec}A_i\) such that each \(f^{-1}(U_i)\) has an affine open cover \(V_{ij}=\operatorname{Spec}B_{ij}\) for which every \(A_i\)-algebra \(B_{ij}\) is finitely presented.

Explicitly, finitely presented means that for some finite integers \(m,n\),
\[
B_{ij}\cong A_i[x_1,\ldots,x_n]/(r_1,\ldots,r_m).
\]
This criterion is local on both source and target; the resulting property is independent of the chosen affine covers.

For a field extension \(K/F\), \(\operatorname{Spec}K\to\operatorname{Spec}F\) is locally of finite presentation exactly when \(K\) is a finitely presented \(F\)-algebra. In particular, every finite field extension has this property.
