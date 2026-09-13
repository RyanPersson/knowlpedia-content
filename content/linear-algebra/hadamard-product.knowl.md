+++
id = "linear-algebra/hadamard-product"
title = "Hadamard product"
kind = "definition"
summary = "Entrywise multiplication of vectors or matrices of the same shape."
aliases = ["componentwise multiplication", "entrywise product"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/matrix", "algebra-rings/ring"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For two [[linear-algebra/matrix|matrices]] \(A,B\) of the same shape, the **Hadamard product** is their entrywise product
\[
(A\odot B)_{ij}=A_{ij}B_{ij}.
\]
For vectors, \((a\odot b)_i=a_i b_i\). This is a different operation from ordinary matrix multiplication, which sums over an intermediate index.

## Coordinate dependence

Entrywise multiplication uses the chosen coordinates. For a fixed vector \(a\), the map \(b\mapsto a\odot b\) is multiplication by the diagonal matrix with entries \(a_i\). Thus differentiating coordinatewise squares gives \(D(y\mapsto y\odot y)_y[h]=2y\odot h\) over the real or complex numbers.

## References

- [Sheldon Axler, Linear Algebra Done Right, 4th ed., Chapters 2–3, 6 and 9](https://linear.axler.net/LADR4e.pdf).
