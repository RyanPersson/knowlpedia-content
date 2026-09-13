+++
id = "linear-algebra/moment-pairing-matrix"
title = "Moment pairing matrix"
kind = "definition"
summary = "A finite matrix of integrals pairing chosen weights with chosen correction profiles."
aliases = ["generalized moment matrix", "weight-profile moment matrix"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/matrix", "measure-theory/lebesgue-integral", "shared-foundations/finite-sum", "linear-algebra/matrix-inverse"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Given weights \(w_1,\ldots,w_m\) and profiles \(\beta_1,\ldots,\beta_n\) with integrable products, their **moment pairing matrix** is
\[
B_{ij}=\int w_i(r)\beta_j(r)\,dr.
\]
For a correction \(\delta u=\sum_jc_j\beta_j\), its weighted integrals form the [[linear-algebra/matrix|matrix product]] \(Bc\).

## Solving moment equations

For a square invertible matrix, every target vector \(d\) has the unique coefficient vector \(c=B^{-1}d\). If the profiles or weights depend on parameters, uniform estimates require control of the corresponding inverses. This use of “moment matrix” is a weight-profile pairing; a Hankel matrix of moments of one measure is a different special construction.

## Row normalization

Multiplying each equation by a specified nonzero factor amounts to replacing \(Bc=d\) by \(DBc=Dd\), where \(D\) is an invertible diagonal matrix. It leaves the solutions unchanged. The same factor must be applied to the target in that row, and a parameter-dependent factor contributes to derivative estimates.
