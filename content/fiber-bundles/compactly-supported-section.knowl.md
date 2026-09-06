+++
id = "fiber-bundles/compactly-supported-section"
title = "Compactly supported section"
kind = "definition"
summary = "A vector bundle section whose support is a compact subset of the base."
aliases = ["section with compact support", "Gamma_c(E)"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/vector-bundle", "fiber-bundles/section-of-a-vector-bundle", "fiber-bundles/support-of-a-section", "topology/compact-set", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\to M\) be a smooth [[fiber-bundles/vector-bundle|vector bundle]] and \(s\in\Gamma^\infty(M,E)\) a smooth [[fiber-bundles/section-of-a-vector-bundle|section]]. The section \(s\) is **compactly supported** if its [[fiber-bundles/support-of-a-section|support]]
\[
\operatorname{supp}(s)=\overline{\{x\in M\mid s(x)\neq 0_x\}}
\]
is a [[topology/compact-set|compact subset]] of \(M\). The [[linear-algebra/vector-space|vector space]] of compactly supported smooth sections is denoted
\[
\Gamma_c^\infty(M,E)
=\{s\in\Gamma^\infty(M,E)\mid \operatorname{supp}(s)\text{ is compact}\}.
\]
Compactness is taken in the topology of the base, so the definition is intrinsic and does not depend on a bundle trivialization, metric, or connection.

## Basic properties

If \(s,t\in\Gamma_c^\infty(M,E)\) and \(f\in C^\infty(M)\), then \(s+t\) and \(fs\) are compactly supported because
\[
\operatorname{supp}(s+t)\subseteq\operatorname{supp}(s)\cup\operatorname{supp}(t),
\qquad
\operatorname{supp}(fs)\subseteq\operatorname{supp}(s).
\]
Thus \(\Gamma_c^\infty(M,E)\) is a module over \(C^\infty(M)\). It is also preserved by vector-bundle morphisms over \(M\).

When \(M\) is compact, every [[fiber-bundles/section-of-a-fiber-bundle|smooth section]] is compactly supported. On a noncompact base, compact support is a genuine restriction and is the natural condition for [[real-analysis/integration-by-parts|integration by parts]] without boundary terms at infinity.

## Local construction

Let \(U\subseteq M\) be a trivializing open set and choose a smooth function \(\chi\) with compact support contained in \(U\). Multiplying a section on \(U\) by \(\chi\) and extending it by zero produces a member of \(\Gamma_c^\infty(M,E)\). Partitions of unity therefore reduce many global constructions involving compactly supported sections to finitely many local ones near their common compact support.

## Examples and non-examples

For the trivial [[fiber-bundles/line-bundle|line bundle]] over \(\mathbb R\), a [[differential-geometry/bump-function|bump function]] is a compactly supported section. The function \(x\mapsto e^{-x^2}\) is not compactly supported: rapid decay does not replace the requirement that the section vanish outside a compact set.

**Warning.** The nonzero locus itself need not be closed. Compact support refers to its closure, not merely to the set where the section has nonzero values.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 2, supports, bump functions, and partitions of unity.
2. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, 2nd ed., Springer, 1990. [DOI record](https://doi.org/10.1007/978-3-642-61497-2). Relevant: Chapter 1, test functions and compact support.
