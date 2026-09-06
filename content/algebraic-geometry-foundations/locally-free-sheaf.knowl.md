+++
id = "algebraic-geometry-foundations/locally-free-sheaf"
title = "Locally free sheaf"
kind = "definition"
summary = "A sheaf of modules locally isomorphic to a finite direct sum of the structure sheaf."
aliases = ["locally free module sheaf", "vector bundle sheaf", "finite-rank locally free sheaf"]
domains = ["algebraic-geometry-foundations", "algebra-modules"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/ringed-space", "algebraic-geometry-foundations/sheaf-of-modules"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((X,\mathcal O_X)\) be a
[[algebraic-geometry-foundations/ringed-space|ringed space]]. An
\(\mathcal O_X\)-[[algebraic-geometry-foundations/sheaf-of-modules|module
sheaf]] \(\mathcal E\) is **locally free of rank \(r\)** if every
\(x\in X\) has an open neighborhood \(U\) with an isomorphism
\[
\mathcal E|_U\cong\mathcal O_X|_U^{\oplus r}.
\]
Such an isomorphism is a local frame. A **finite-rank locally free sheaf**
allows a finite rank that is locally constant, and hence constant on each
connected component.

## Transition matrices

For a locally free sheaf of constant rank \(r\), two local frames over \(U_i\)
and \(U_j\) differ on the overlap by an invertible matrix
\[
g_{ij}\in GL_r(\mathcal O_X(U_i\cap U_j)).
\]
These matrices satisfy the cocycle identities and glue the local free
modules. Conversely, compatible invertible transition matrices construct a
locally free sheaf.

## Relation to vector bundles

For a smooth real or complex vector bundle, the
[[fiber-bundles/sheaf-of-smooth-sections|sheaf of smooth sections]] is
finite-rank locally free over \(C^\infty_M\). Conversely, a finite-rank
locally free \(C^\infty_M\)-module sheaf glues trivial bundles to recover a
smooth [[fiber-bundles/vector-bundle|vector bundle]].

The adjective “locally free” applies to the sheaf. Its global section module
need not be free: a global basis would be a global frame and would trivialize
the associated bundle.

## References

1. The Stacks Project Authors, *The Stacks Project*. [Tag 01C5](https://stacks.math.columbia.edu/tag/01C5). Relevant: finite locally free modules and locally free sheaves.
2. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: Chapter 3, transition functions and vector bundles.
