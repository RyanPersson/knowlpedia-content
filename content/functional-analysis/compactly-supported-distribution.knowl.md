+++
id = "functional-analysis/compactly-supported-distribution"
title = "Compactly supported distribution"
kind = "definition"
summary = "A distribution whose distributional support is compact in its open domain."
aliases = ["space E-prime", "distribution with compact support"]
domains = ["functional-analysis", "distribution-theory"]
prerequisites = ["functional-analysis/distribution", "functional-analysis/support-of-distribution", "differential-geometry/bump-function", "functional-analysis/test-function-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\Omega\subseteq\mathbb R^n\) be open. A
[[functional-analysis/distribution|distribution]] \(T\in\mathcal D'(\Omega)\)
is a **compactly supported distribution** if its
[[functional-analysis/support-of-distribution|distributional support]]
\(\operatorname{supp}T\) is compact in \(\Omega\). The space of all such
distributions is denoted \(\mathcal E'(\Omega)\). If
\(\chi\in C_c^\infty(\Omega)\) is a
[[differential-geometry/bump-function|smooth cutoff]] that equals \(1\) on a
neighborhood of
\(\operatorname{supp}T\), then
\[
T(f):=T(\chi f),\qquad f\in C^\infty(\Omega),
\]
is independent of the choice of \(\chi\). Hence \(T\) extends canonically
from [[functional-analysis/test-function-space|test functions]] to all smooth functions.

## Dual characterization

Equip \(\mathcal E(\Omega)=C^\infty(\Omega)\) with the topology of uniform
convergence of every derivative on compact subsets. Its
[[functional-analysis/topological-dual|continuous dual]] is
\(\mathcal E'(\Omega)\): continuity on all smooth functions is equivalent to
being a distribution with compact support. This explains the notation and
the cutoff construction in the core.

## Operations and examples

Every compactly supported distribution has finite
[[functional-analysis/order-of-distribution|order]]. Dirac distributions and
all their derivatives are compactly supported, with singleton support.
A nonzero constant function on \(\mathbb R^n\), regarded as a regular
distribution, is not compactly supported.

For distributions on \(\mathbb R^n\), convolution of two arbitrary
distributions need not be defined, but it is defined when at least one factor
has compact support; the resulting support is contained in the Minkowski sum
\(\operatorname{supp}S+\operatorname{supp}T
=\{x+y:x\in\operatorname{supp}S,\ y\in\operatorname{supp}T\}\).

## Conventions and scope

Compactness is taken inside \(\Omega\): the support must be a compact subset
that stays away from the boundary. The symbol \(\mathcal E'\) is not a
second notation for all distributions; it is the continuous dual of the
smooth-function space \(\mathcal E\), and therefore selects precisely the
compactly supported ones.

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, 2nd ed., Springer, 2003. [Springer DOI record](https://doi.org/10.1007/978-3-642-61497-2). Relevant: §§2.3 and 4.1, compact support, extension, and convolution.
2. François Trèves, *Topological Vector Spaces, Distributions and Kernels*, Academic Press, 1967. [Elsevier publisher record](https://shop.elsevier.com/books/topological-vector-spaces-distributions-and-kernels/treves/978-1-4831-9859-0). Relevant: Chapter 27, compactly supported distributions and the dual of \(C^\infty\).
