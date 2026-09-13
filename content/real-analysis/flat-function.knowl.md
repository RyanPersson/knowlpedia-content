+++
id = "real-analysis/flat-function"
title = "Flat function along a set"
kind = "definition"
summary = "A smooth function whose derivatives of every order vanish on a specified set."
aliases = ["vanishing to infinite order", "flat at an endpoint"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/class-ck-map", "real-analysis/cartesian-jet"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A [[real-analysis/class-ck-map|smooth function]] \(f:U\subseteq\mathbb R^n\to\mathbb R^m\) is **flat on \(A\subseteq U\)** if
\[
\partial^\alpha f(a)=0\qquad(a\in A,\ \alpha\in\mathbb N_0^n).
\]
Thus every [[real-analysis/cartesian-jet|finite Cartesian jet]] vanishes on \(A\). The derivative of order zero is included, so \(f\) itself vanishes there.

## Boundary convention

For a function smooth up to an endpoint from one side, flatness at that endpoint means that every one-sided derivative extends continuously with value zero. With spatial parameters, all mixed derivatives are included and their limits are locally uniform in those parameters.

## Flat need not mean locally zero

The [[real-analysis/flat-exponential|flat exponential]] is positive on one side of zero yet flat at zero. In contrast, a [[real-analysis/real-analytic-function|real-analytic function]] flat at a point is zero in a neighborhood of that point, because its convergent Taylor series is zero.
