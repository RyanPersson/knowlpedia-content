+++
id = "convex-analysis/hahn-banach-theorem-in-normed-spaces"
title = "Hahn–Banach Theorem in Normed Spaces"
kind = "knowl"
summary = "A bounded linear functional on a subspace extends to the whole space without increasing its norm."
aliases = ["hahn-banach-theorem-in-normed-spaces", "Hahn–Banach Theorem in Normed Spaces"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/hahn-banach-theorem-in-normed-spaces.md"
prerequisites = ["convex-analysis/norm-normed-vector-space", "convex-analysis/linear-subspace", "convex-analysis/bounded-linear-functional-norm-of-a-functional", "convex-analysis/hahn-banach-extension-dominated-by-a-seminorm-real-case"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a [[convex-analysis/norm-normed-vector-space|normed space]], let \(Y\subset X\) be a [[convex-analysis/linear-subspace|subspace]], and let \(f:Y\to\mathbb{K}\) be a [[convex-analysis/bounded-linear-functional-norm-of-a-functional|bounded linear functional]].

**Theorem (Hahn–Banach, normed spaces)**: There exists a bounded linear functional \(F:X\to\mathbb{K}\) such that
- \(F|_Y=f\), and
- \(\|F\|=\|f\|\).

## Remarks

**Context:**
This is obtained by applying [[convex-analysis/hahn-banach-extension-dominated-by-a-seminorm-real-case|the seminorm version of Hahn–Banach]] with the [[convex-analysis/seminorm|seminorm]] \(p(x)=\|f\|\|x\|\). It is one of the main tools for constructing supporting functionals and proving geometric separation theorems in normed spaces.
