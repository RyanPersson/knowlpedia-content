+++
id = "real-analysis/image-range"
title = "Image (range)"
kind = "knowl"
summary = "The set of values a function actually attains."
aliases = ["image-range", "Image (range)"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/image-range.md"
prerequisites = ["shared-foundations/function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(f:X\to Y\) be a function.
- The **image** (or **range**) of \(f\) is
\[f(X):=\{f(x):x\in X\}\subseteq Y.\]

- More generally, for a subset \(A\subseteq X\), the image of \(A\) under \(f\) is
\[f(A):=\{f(a):a\in A\}\subseteq Y.\]

## Remarks

The image captures the "actual outputs" of \(f\) and is the natural codomain for which \(f\) becomes surjective (if one replaces \(Y\) by \(f(X)\)).

## Examples

- If \(f:\mathbb{R}\to\mathbb{R}\), \(f(x)=x^2\), then \(f(\mathbb{R})=[0,\infty)\).
- If \(f(x)=x^2\) and \(A=[-1,2]\), then \(f(A)=[0,4]\).
- If \(f:\mathbb{R}\to\mathbb{R}\), \(f(x)=e^x\), then \(f(\mathbb{R})=(0,\infty)\).
