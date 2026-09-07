+++
id = "real-analysis/partial-sums"
title = "Partial sums"
kind = "knowl"
summary = "The finite sums obtained by truncating a series."
aliases = ["partial-sums", "Partial sums"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/partial-sums.md"
prerequisites = ["shared-foundations/sequence", "shared-foundations/complex-numbers-c"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For a [[shared-foundations/sequence|sequence]] \((a_k)_{k\ge1}\) of real or complex numbers, the **\(n\)th partial sum** is the finite sum \(s_n=\sum_{k=1}^n a_k\), for \(n\ge1\). Equivalently, \(s_0=0\) and \(s_n=s_{n-1}+a_n\).

## Relation to a series

The sequence \((s_n)\) encodes the [[real-analysis/series|series]] \(\sum_{k=1}^{\infty}a_k\): statements about convergence or divergence of the series are statements about whether the partial sums form a sequence with a limit, as formalized in [[real-analysis/convergent-series|convergent series]].

## Examples

- For \(a_k=\frac{1}{k}\), the partial sums are \(s_n=\sum_{k=1}^n \frac{1}{k}\) (harmonic numbers).
- For \(a_k=r^{k-1}\), the partial sums are \(s_n=\sum_{k=1}^n r^{k-1}=\frac{1-r^n}{1-r}\) (when \(r\neq 1\)).
