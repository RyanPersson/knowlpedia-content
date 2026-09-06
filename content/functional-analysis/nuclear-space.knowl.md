+++
id = "functional-analysis/nuclear-space"
title = "Nuclear space"
kind = "definition"
summary = "A locally convex space whose defining Banach-space transition maps are nuclear."
aliases = ["nuclear locally convex space", "Grothendieck nuclear space"]
domains = ["functional-analysis"]
prerequisites = ["functional-analysis/locally-convex-space", "linear-algebra/vector-space", "functional-analysis/topological-dual"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(E\) be a Hausdorff
[[functional-analysis/locally-convex-space|locally convex space]]. For a
continuous seminorm \(p\), let \(E_p\) be the Banach completion of
\(E/\ker p\). The space \(E\) is **nuclear** if, for every continuous
seminorm \(p\), there is a continuous seminorm \(q\geq p\) such that the
canonical map
\[
E_q\longrightarrow E_p
\]
is a nuclear operator: it has an absolutely summable rank-one
decomposition. This is a property of the locally convex topology, not merely
of the underlying [[linear-algebra/vector-space|vector space]] or its
[[functional-analysis/topological-dual|topological dual]] as a set.

## Why the definition is strong

The transition map condition forces finite-dimensional-like summability
between successively stronger seminorms. It implies that the projective and
injective locally convex tensor-product constructions with \(E\) agree after
the appropriate Hausdorff completion. This removes a major ambiguity in
[[functional-analysis/schwartz-kernel-theorem|kernel theorems]] and makes continuous multilinear maps unusually tractable.

## Examples and nonexamples

Finite-dimensional locally convex spaces are nuclear. The
[[functional-analysis/schwartz-space|Schwartz space]]
\(\mathcal S(\mathbb R^n)\), the
[[functional-analysis/test-function-space|test-function space]]
\(C_c^\infty(\Omega)\), and the space \(C^\infty(M)\) on a compact smooth
manifold are fundamental infinite-dimensional examples with their standard
locally convex topologies. By contrast, a [[linear-algebra/banach-space|Banach space]] is nuclear as a
locally convex space only when it is finite-dimensional: applying the
definition to a norm would make an identity-type transition map nuclear,
hence compact.

## Topological cautions

Nuclearity does not mean that every element is a rapidly decreasing function,
nor does it define a class of distributions. Those are properties of
particular function spaces and their continuous duals. Changing the topology
on a fixed vector space can change whether it is nuclear, because continuity
of the seminorms and nuclearity of the completion maps both depend on that
topology.

## References

1. François Trèves, *Topological Vector Spaces, Distributions and Kernels*, Academic Press, 1967. [Publisher record](https://shop.elsevier.com/books/topological-vector-spaces-distributions-and-kernels/treves/978-1-4831-9859-0). Relevant: Chapters 50–51 on nuclear spaces and kernel theorems.
2. Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces*, 2nd ed., Springer, 1999. [Publisher record](https://doi.org/10.1007/978-1-4612-1468-7). Relevant: Chapter IV on nuclear maps and spaces.
