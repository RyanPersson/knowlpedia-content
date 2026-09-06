+++
id = "algebraic-geometry-foundations/fiber-product-of-schemes"
title = "Fiber product of schemes"
kind = "definition"
summary = "The scheme representing pairs of points or maps with the same image over a base."
aliases = ["fiber product of schemes", "scheme fiber product", "pullback of schemes"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/scheme", "algebraic-geometry-foundations/affine-scheme", "algebra-modules/tensor-product"]
dependency_review_count = 1
+++

Given morphisms of [[algebraic-geometry-foundations/scheme|schemes]] \(X\to S\leftarrow Y\), their **fiber product** is a scheme \(X\times_S Y\) with projections to \(X\) and \(Y\) whose composites to \(S\) agree, and which is universal with that property: for every scheme \(T\),

\[
\operatorname{Hom}(T,X\times_S Y)
\cong
\operatorname{Hom}(T,X)\times_{\operatorname{Hom}(T,S)}\operatorname{Hom}(T,Y).
\]

On [[algebraic-geometry-foundations/affine-scheme|affine schemes]] the construction is concrete. Ring maps \(R\to A\) and \(R\to B\) give

\[
\operatorname{Spec}A\times_{\operatorname{Spec}R}\operatorname{Spec}B
\cong
\operatorname{Spec}(A\otimes_R B),
\]

where \(A\otimes_R B\) is the [[algebra-modules/tensor-product|tensor product]]. This affine calculation is why \(K\otimes_F K\) appears in the Galois torsor identity.

## Remarks

The underlying topological space of \(X\times_S Y\) is not, in general, the naive point-set fiber product. Scheme points carry residue-field data, so several scheme points can lie over one compatible pair of topological points.
