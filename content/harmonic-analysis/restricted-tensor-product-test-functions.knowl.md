+++
id = "harmonic-analysis/restricted-tensor-product-test-functions"
title = "Restricted tensor product of local test-function spaces"
kind = "definition"
summary = "The tensor product of local test-function spaces in which almost every factor equals a fixed standard test function."
aliases = ["restricted tensor product of Schwartz spaces", "restricted tensor product of local functions"]
domains = ["harmonic-analysis", "number-theory"]
prerequisites = ["harmonic-analysis/schwartz-bruhat-space-local-field", "functional-analysis/test-function-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F\) be a number field, \(F_v\) its completions, and
\(\mathcal S(F_v)\) the local
[[harmonic-analysis/schwartz-bruhat-space-local-field|Schwartz–Bruhat
spaces]]. Put \(F_\infty=\prod_{v\mid\infty}F_v\), and let
\(\mathcal S(F_\infty)\) be the completed nuclear tensor product of the
archimedean local Schwartz spaces. For each finite place set
\(e_v=1_{\mathcal O_v}\). The **restricted tensor product of the local
[[functional-analysis/test-function-space|test-function spaces]]** is
\[
\mathcal S(F_\infty)\,\widehat\otimes\!
\bigotimes_{v\nmid\infty}'\mathcal S(F_v)
=\underset{S}{\mathop{\mathrm{colim}}}\,
\left(\mathcal S(F_\infty)\widehat\otimes
\bigotimes_{v\in S}\mathcal S(F_v)\right)
\otimes\left(\bigotimes_{\substack{v\nmid\infty\\v\notin S}}
\mathbb C e_v\right),
\]
where \(S\) ranges over finite sets of finite places. The vectors \(e_v\)
are part of the definition.

## Canonical realization

An elementary tensor determines a function on the restricted product \(\mathbb A_F=\prod_v'F_v\) by
\[
x=(x_v)_v\longmapsto\prod_v f_v(x_v).
\]
Only finitely many factors differ from \(1_{\mathcal O_v}\), and an adele
lies in \(\mathcal O_v\) at almost every finite place, so this product is well
defined. Finite sums of completely separated local functions realize a dense
algebraic subspace of the adelic test-function space. They need not exhaust
\(\mathcal S(F_\infty)\) when there is more than one archimedean place.

## Topology

For a fixed finite \(S\), the unrestricted factors form a completed nuclear
test-function tensor product, while factors outside \(S\) remain fixed. The
adelic Schwartz topology is the standard locally convex inductive-limit
(LF) topology over these finite sets. Completely separated elementary
tensors are dense in each archimedean completion and hence in the resulting
adelic space.

## Dependence on distinguished vectors

A restricted tensor product is not determined by the spaces \(\mathcal S(F_v)\) alone; the vectors \(e_v\) are part of its data. For the additive adeles, \(1_{\mathcal O_v}\) is the standard unramified choice. Replacing finitely many \(e_v\) gives the same restricted tensor-product space up to its evident canonical identification, whereas changing infinitely many can produce a different restricted product.

## References

1. André Weil, *Basic Number Theory*, 2nd ed., Springer, 1973. [DOI record](https://doi.org/10.1007/978-3-662-05978-4). Relevant: Chapter II, “Adeles,” restricted products and adelic test functions.
2. Daniel Bump, *Automorphic Forms and Representations*, Cambridge University Press, 1997. [DOI record](https://doi.org/10.1017/CBO9780511609572). Relevant: Chapter 3, restricted tensor products in adelic harmonic analysis.
