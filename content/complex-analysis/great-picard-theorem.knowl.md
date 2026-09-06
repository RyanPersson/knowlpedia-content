+++
id = "complex-analysis/great-picard-theorem"
title = "Great Picard theorem"
kind = "theorem"
summary = "Near an essential singularity, every complex value with at most one exception occurs infinitely often."
aliases = ["Picard's great theorem", "big Picard theorem"]
domains = ["complex-analysis"]
prerequisites = ["complex-analysis/casorati-weierstrass-theorem", "complex-analysis/isolated-singularity-classification"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(a\) be an essential isolated singularity of a holomorphic function \(f\). In every punctured neighborhood of \(a\), the function \(f\) assumes every value in \(\mathbb C\), with at most one exception, infinitely many times.

## Comparison with Casorati–Weierstrass

The [[complex-analysis/casorati-weierstrass-theorem|Casorati–Weierstrass theorem]] says that the image is dense. Great Picard says much more: apart from at most one omitted value, each value is attained, and is attained infinitely often arbitrarily close to the singularity.

## Entire-function consequence

Applying the theorem at infinity gives the [[complex-analysis/little-picard-theorem|little Picard theorem]] for nonconstant [[complex-analysis/entire-function|entire functions]].

## Sharpness

The exceptional value can occur. The function \(e^{1/z}\) has an essential singularity at \(0\) and never takes the value \(0\), while taking every nonzero complex value infinitely often near \(0\).

## References

1. John B. Conway, *Functions of One Complex Variable II*, Springer, 1995. [Publisher record](https://doi.org/10.1007/978-1-4612-0817-4). Relevant: Chapter XII.
