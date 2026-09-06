+++
id = "convex-analysis/hahn-banach-theorem-in-real-vector-spaces"
title = "Hahn–Banach Theorem (Real Vector Spaces)"
kind = "knowl"
summary = "A linear functional dominated by a sublinear function extends to the whole space."
aliases = ["hahn-banach-theorem-in-real-vector-spaces", "Hahn–Banach Theorem (Real Vector Spaces)"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/hahn-banach-theorem-in-real-vector-spaces.md"
prerequisites = ["linear-algebra/vector-space", "convex-analysis/linear-subspace", "convex-analysis/subadditive-positively-homogeneous-and-sublinear-functions", "convex-analysis/linear-operator-linear-transformation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Hahn–Banach (real version)**: Let \(X\) be a real [[linear-algebra/vector-space|vector space]], let \(Y\subset X\) be a [[convex-analysis/linear-subspace|linear subspace]], and let \(p:X\to\mathbb{R}\) be [[convex-analysis/subadditive-positively-homogeneous-and-sublinear-functions|sublinear]].

If \(f:Y\to\mathbb{R}\) is a [[convex-analysis/linear-operator-linear-transformation|linear]] functional satisfying
\[
f(y)\le p(y)\quad\text{for all }y\in Y,
\]

then there exists a linear functional \(F:X\to\mathbb{R}\) such that
- \(F(y)=f(y)\) for all \(y\in Y\), and
- \(F(x)\le p(x)\) for all \(x\in X\).

## Interpretation

The theorem is a principal tool for convex separation results, such as [[convex-analysis/separation-of-a-point-from-a-convex-set-via-the-core|geometric Hahn–Banach separation]].
