+++
id = "functional-analysis/order-of-distribution"
title = "Order of a distribution"
kind = "definition"
summary = "The order of a distribution is the least derivative degree needed in uniform seminorm estimates on compact supports."
aliases = ["finite-order distribution", "distribution of order m"]
domains = ["functional-analysis", "distribution-theory"]
section_mode = "progressive"
prerequisites = ["functional-analysis/distribution", "functional-analysis/test-function-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(T\) be a [[functional-analysis/distribution|distribution]] on an open
set \(\Omega\subseteq\mathbb R^n\). It has **order at most \(m\)** if for
every compact \(K\subset\Omega\) there is \(C_K\geq0\) such that
\[
|T(\varphi)|\leq C_K
\max_{|\alpha|\leq m}\sup_{x\in K}|\partial^\alpha\varphi(x)|
\]
for every
[[functional-analysis/test-function-space|\(\varphi\in\mathcal D(\Omega)\)]]
with support in \(K\), where
\(\alpha=(\alpha_1,\ldots,\alpha_n)\) has nonnegative integer entries and
\(|\alpha|=\alpha_1+\cdots+\alpha_n\). Its **order** is the least such
nonnegative integer \(m\); if no single \(m\) works for all compact \(K\), its
order is infinite. Thus order records how many derivatives of a test function
are needed to control the distribution.

## Examples and differentiation

A distribution represented by a locally finite measure has order \(0\).
The Dirac distribution \(\delta_a\) has order \(0\), while
\(\partial^\alpha\delta_a\) has order \(|\alpha|\). More generally,
distributional differentiation raises the order by at most the number of
derivatives:
\[
\operatorname{ord}(\partial^\alpha T)
\leq \operatorname{ord}(T)+|\alpha|.
\]
These estimates follow directly from the definition of
[[functional-analysis/distributional-derivative|distributional derivative]].

## Local and global scope

Continuity of \(T\) on each fixed-support test-function space implies a
finite-order estimate on every compact \(K\), but the required integer may
grow with \(K\). Consequently every distribution has finite order locally,
while not every distribution has one finite global order on a noncompact
open set. A
[[functional-analysis/compactly-supported-distribution|compactly supported distribution]] does have finite order.

## Conventions

Some texts say “order \(m\)” when they only mean “order at most \(m\).” Here
“order” means the least admissible \(m\). The zero distribution is bounded by
every order estimate; assigning it order \(0\) or \(-\infty\) is a convention
that should be stated when formulas depend on the value.

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, 2nd ed., Springer, 2003. [Springer DOI record](https://doi.org/10.1007/978-3-642-61497-2). Relevant: §2.3, distributions of finite order and compact support.
2. Gerald B. Folland, *Real Analysis: Modern Techniques and Their Applications*, 2nd ed., Wiley, 1999. [Wiley publisher record](https://www.wiley-vch.de/de/fachgebiete/mathematik-und-statistik/real-analysis-978-0-471-31716-6). Relevant: Chapter 9, distributions and their order.
