+++
id = "convex-analysis/basis-characterized-by-maximal-linear-independence"
title = "Bases are maximal linearly independent sets"
kind = "knowl"
summary = "A set is a basis if and only if it is maximal among the linearly independent subsets."
aliases = ["basis-characterized-by-maximal-linear-independence", "Bases are maximal linearly independent sets"]
domains = ["convex-analysis"]
prerequisites = ["convex-analysis/basis-hamel-basis-and-dimension", "convex-analysis/linearly-independent-and-linearly-dependent-sets"]
dependency_heuristic = "semantic-curriculum-review-v1"
dependency_review_count = 1
legacy_source_path = "convex-analysis/basis-characterized-by-maximal-linear-independence.md"
+++

**Proposition (Maximal linear independence characterization).**
Let \(X\) be a vector space and \(B\subseteq X\). Then \(B\) is a [[convex-analysis/basis-hamel-basis-and-dimension|basis]] of \(X\) if and only if:

1. \(B\) is [[convex-analysis/linearly-independent-and-linearly-dependent-sets|linearly independent]], and
2. every strict superset \(M\supsetneq B\) is linearly dependent.

## Remarks

**Proof sketch.**
- If \(B\) is a basis and \(x\notin B\), then \(x\) is a linear combination of elements of \(B\), so \(B\cup\{x\}\) is dependent.
- Conversely, if \(B\) is independent and maximal and \(x\notin B\), dependence of \(B\cup\{x\}\) expresses \(x\) as a finite linear combination of elements of \(B\). Thus \(B\) spans \(X\).
