+++
id = "real-analysis/cartesian-jet"
title = "Cartesian jet of a function"
kind = "definition"
summary = "The finite array of all Cartesian partial derivatives up to a specified order at a point."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/class-ck-map", "real-analysis/multi-index-notation", "shared-foundations/factorial"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a [[real-analysis/class-ck-map|class \(C^k\) function]] \(f:U\subseteq\mathbb R^n\to\mathbb R^m\), its **Cartesian \(k\)-jet at \(a\in U\)** is the array
\[
j_a^k f=(\partial^\alpha f(a))_{|\alpha|\le k}.
\]
Here \(\alpha\) is a [[real-analysis/multi-index-notation|multi-index]]. Two functions have the same \(k\)-jet when all these derivative values agree. The same data can be encoded by the polynomial
\[
\sum_{|\alpha|\le k}\frac{\partial^\alpha f(a)}{\alpha!}(x-a)^\alpha.
\]

## Infinite jets and coordinate choices

An infinite jet specifies these values for every order; it does not assert convergence of the associated formal Taylor series. Cartesian jets use fixed Euclidean coordinates. The [[differential-geometry/jet-of-a-smooth-map|jet of a smooth map]] is the corresponding coordinate-independent geometric construction.
