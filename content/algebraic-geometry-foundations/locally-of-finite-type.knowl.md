+++
id = "algebraic-geometry-foundations/locally-of-finite-type"
title = "Locally of finite type"
kind = "knowl"
summary = "A scheme morphism that is locally induced by finitely generated algebras."
aliases = ["locally-of-finite-type", "Locally of finite type"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/scheme", "algebra-modules/algebra-over-ring", "shared-foundations/surjective-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A morphism \(f:Y\to X\) of [[algebraic-geometry-foundations/scheme|schemes]] is **locally of finite type** if \(X\) has an affine open cover \(U_i=\operatorname{Spec}A_i\) such that each \(f^{-1}(U_i)\) has an affine open cover \(V_{ij}=\operatorname{Spec}B_{ij}\) for which every [[algebra-modules/algebra-over-ring|\(A_i\)-algebra]] \(B_{ij}\) is finitely generated.

Explicitly, finitely generated means that for some finite integer \(n\), there is a surjective \(A_i\)-algebra homomorphism
\[
A_i[x_1,\ldots,x_n]\longrightarrow B_{ij}.
\]
This criterion is local on both source and target and is independent of the chosen affine covers.

Every [[algebraic-geometry-foundations/locally-of-finite-presentation|locally finitely presented]] morphism is locally of finite type. The converse need not hold, because finite type requires finitely many algebra generators but does not require the ideal of relations among them to be finitely generated.
