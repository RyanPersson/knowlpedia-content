+++
id = "functional-analysis/factorial-operator-inverse"
title = "Operator inversion from summable bounds on powers"
kind = "theorem"
summary = "The series sum of alternating powers inverts I plus T whenever the operator powers are norm-summable."
aliases = ["factorially convergent operator inverse", "summable-powers inverse"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/absolutely-convergent-banach-series", "functional-analysis/bounded-linear-operator", "linear-algebra/banach-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(T\) be a [[functional-analysis/bounded-linear-operator|bounded operator]] on a [[linear-algebra/banach-space|Banach space]]. If \(\sum_{k=0}^\infty\|T^k\|<\infty\), then
\[
(I+T)^{-1}=\sum_{k=0}^\infty(-T)^k
\]
in operator norm. Multiplication of a finite partial sum by \(I+T\), on either side, gives \(I+(-1)^NT^{N+1}\); its remainder tends to zero. Thus the inverse is two-sided. This criterion does not require \(\|T\|<1\).

## Factorial gains from increasing degree

Suppose nested subspaces \(X_b\) satisfy \(X_0=X\), \(T(X_b)\subseteq X_{b+1}\), and
\(\|Tx\|\le K\|x\|/[(b+1)(b+2)]\) for \(x\in X_b\). Applying this bound successively yields
\[
\|T^k\|\le\frac{K^k}{k!(k+1)!},
\]
which is summable for every finite \(K\). Vanishing of low-degree coefficients provides such a filtration for suitable radial integral operators.
