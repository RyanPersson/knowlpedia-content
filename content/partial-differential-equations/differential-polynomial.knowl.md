+++
id = "partial-differential-equations/differential-polynomial"
title = "Differential polynomial"
kind = "definition"
summary = "A polynomial expression in finitely many derivatives of an unknown, with prescribed coefficient functions."
aliases = ["differential monomial"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["real-analysis/multi-index-notation", "real-analysis/mixed-partial-derivative", "shared-foundations/finite-sum", "shared-foundations/finite-product"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **differential polynomial** in a smooth vector-valued unknown \(u=(u_1,\ldots,u_m)\) is a finite sum of expressions
\[
c(x)\prod_{j=1}^{N}\partial^{I_j}u_{a_j}(x),
\]
where the coefficients \(c\) are prescribed smooth functions, \(I_j\) are [[real-analysis/multi-index-notation|multi-indices]], and \(a_j\) specify components. The order is the largest derivative order \(|I_j|\) used; the degree is the largest number \(N\) of factors in a monomial. Degree-zero terms depend only on the coefficients.

## Different order and degree

The expression \(u\,\partial_xu+\partial_x^2u\) has differential order two and polynomial degree two. Substituting formal series determines each coefficient through finitely many terms because the order and degree are finite. A composition such as \(e^u\) is not a differential polynomial in \(u\).

## Residual comparison

The [[partial-differential-equations/differential-polynomial-difference-estimate|difference estimate]] bounds a nonlinear change by the input difference jet. Combined with increasing-order tails, it gives [[partial-differential-equations/flat-residual-from-asymptotic-summation|flat residual realization]].
