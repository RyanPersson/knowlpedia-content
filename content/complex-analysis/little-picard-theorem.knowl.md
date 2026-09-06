+++
id = "complex-analysis/little-picard-theorem"
title = "Little Picard theorem"
kind = "theorem"
summary = "A nonconstant entire function assumes every complex value with at most one exception."
aliases = ["Picard's little theorem"]
domains = ["complex-analysis"]
prerequisites = ["complex-analysis/entire-function"]
dependency_review_count = 1
section_mode = "progressive"
+++

If \(f:\mathbb C\to\mathbb C\) is a nonconstant [[complex-analysis/entire-function|entire function]], then the complement
\[
\mathbb C\setminus f(\mathbb C)
\]
contains at most one point. Equivalently, a nonconstant entire function cannot omit two distinct complex values.

## Derivation from Great Picard

If \(f\) is a transcendental entire function, then \(f(1/w)\) has an essential singularity at \(w=0\). The [[complex-analysis/great-picard-theorem|great Picard theorem]] implies that it assumes every complex value, with at most one exception, infinitely often near \(0\). If \(f\) is a nonconstant polynomial, it assumes every complex value by applying the [[complex-analysis/fundamental-theorem-of-algebra-complex-analysis|fundamental theorem of algebra]] to \(f(z)-a\).

## Sharpness

One omitted value is possible: the exponential function \(e^z\) is entire and never vanishes. It assumes every value in \(\mathbb C^\times\).

## References

1. John B. Conway, *Functions of One Complex Variable II*, Springer, 1995. [Publisher record](https://doi.org/10.1007/978-1-4612-0817-4). Relevant: Chapter XII.
