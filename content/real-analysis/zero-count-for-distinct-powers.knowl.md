+++
id = "real-analysis/zero-count-for-distinct-powers"
title = "Zero count for distinct real powers"
kind = "theorem"
summary = "A nonzero combination of m distinct powers has at most m minus one distinct positive zeros."
aliases = ["generalized power Vandermonde independence"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/real-power", "real-analysis/rolles-theorem", "shared-foundations/mathematical-induction", "convex-analysis/linear-combination"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(\alpha_1<\cdots<\alpha_m\) be real. A nonzero [[convex-analysis/linear-combination|linear combination]] \(f(x)=\sum_{j=1}^m c_jx^{\alpha_j}\) has at most \(m-1\) distinct zeros in \((0,\infty)\).

## Inductive proof

The claim is immediate for one nonzero term. Divide by the smallest power actually present. The resulting function has a nonzero constant term; its derivative is a combination of at most \(m-1\) distinct powers. If the original function had \(m\) distinct positive zeros, Rolle's theorem would give at least \(m-1\) zeros of this derivative, contradicting the inductive bound \(m-2\). A derivative that vanished identically would leave a nonzero constant and hence no zeros.

Consequently the evaluation matrix \([x_j^{\alpha_i}]\) is invertible at distinct positive nodes. Otherwise a nonzero combination would vanish at all \(m\) nodes. This is the generalized-power version of Vandermonde independence.
