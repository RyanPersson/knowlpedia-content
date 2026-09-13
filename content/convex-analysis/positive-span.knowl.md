+++
id = "convex-analysis/positive-span"
title = "Positive span"
kind = "definition"
summary = "The set of all finite nonnegative combinations of a specified family of vectors."
aliases = ["conical hull", "nonnegative span"]
domains = ["convex-analysis"]
section_mode = "progressive"
prerequisites = ["convex-analysis/conical-combination", "shared-foundations/set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **positive span**, or **conical hull**, of \(S\) in a real vector space is
\[
\operatorname{pos}(S)=\left\{\sum_{j=1}^m a_jv_j:
m\ge0,\ v_j\in S,\ a_j\ge0\right\}.
\]
It collects all [[convex-analysis/conical-combination|conical combinations]] of elements of \(S\), including zero.

## Minimality and coefficients

The positive span is the smallest convex cone containing \(S\): sums and nonnegative scalar multiples stay in the displayed set, and every cone containing \(S\) contains those combinations. “Positive span” here permits zero coefficients. Requiring every coefficient of a particular finite list to be strictly positive is a separate condition. Positive span differs from convex hull because no coefficient-sum normalization is imposed.
