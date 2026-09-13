+++
id = "real-analysis/squared-partition-of-unity"
title = "Squared partition of unity"
kind = "definition"
summary = "A locally finite smooth family whose squares sum to one."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/class-ck-map", "topology/locally-finite-family", "shared-foundations/support-of-a-function", "real-analysis/nonnegative-square-root", "analysis/locally-finite-smooth-sum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **squared partition of unity** on an open set \(U\) is a family of smooth real functions \((\chi_j)\), with locally finite supports, such that
\[
\sum_j\chi_j(x)^2=1\qquad(x\in U).
\]
It is subordinate to an open cover \((U_j)\) when \(\operatorname{supp}\chi_j\subseteq U_j\).

## Smooth normalization

Start with a locally finite family of smooth real functions \((\psi_j)\) having the desired supports and with at least one nonzero at every point. Then
\[
\chi_j=\frac{\psi_j}{\sqrt{\sum_i\psi_i^2}}
\]
is a squared partition. The denominator is strictly positive and smooth, because the sum is [[analysis/locally-finite-smooth-sum|locally finite]] and the square-root function is smooth on \((0,\infty)\). Supports are preserved.

## Relation to an ordinary partition

The functions \(\chi_j^2\) give a [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity]]. Taking the square root of each member of an arbitrary smooth nonnegative partition is not the same construction: for instance, \(\sqrt{x^2}=|x|\) fails to be smooth at zero.

## References

- [Richard Schwartz, Partitions of Unity (Brown lecture notes)](https://www.math.brown.edu/reschwar/M114B/notes9.pdf).
