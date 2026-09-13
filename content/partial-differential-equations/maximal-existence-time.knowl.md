+++
id = "partial-differential-equations/maximal-existence-time"
title = "Maximal existence time in a solution class"
kind = "definition"
summary = "The endpoint beyond which a solution cannot be extended while remaining in its specified class."
aliases = ["maximal existence interval", "PDE lifespan"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/cauchy-problem", "shared-foundations/restriction-of-a-function", "convex-analysis/extended-real-number-system-and-conventions"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A solution \(u\) of a [[partial-differential-equations/cauchy-problem|Cauchy problem]] on \([t_0,T_*)\), with \(T_*\in(t_0,\infty]\), is **maximal in a specified solution class** if no solution on a longer interval agrees with \(u\) on this interval and belongs to that class. The number \(T_*\) is its **maximal existence time**, and \(T_*-t_0\) is its lifespan.

## What is fixed

An extension solves the same equation with the same data and with coefficients and forcing that are defined on the longer interval. Maximality is relative to the spatial domain, boundary conditions, and regularity or integrability class.

## Norm criteria require a theorem

A finite maximal time does not by definition identify which norm becomes unbounded. A continuation theorem is needed to deduce norm growth from failure to extend. In a problem with local uniqueness, compatible local extensions combine into one maximal solution.
