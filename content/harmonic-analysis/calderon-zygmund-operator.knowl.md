+++
id = "harmonic-analysis/calderon-zygmund-operator"
title = "Calderón–Zygmund operator"
kind = "definition"
summary = "An L2-bounded operator represented off the support of its input by a standard singular kernel."
aliases = ["CZO"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/calderon-zygmund-kernel", "functional-analysis/bounded-linear-operator", "measure-theory/lp-space", "real-analysis/compactly-supported-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **Calderón–Zygmund operator** \(T\) on \(\mathbb R^n\) is a bounded linear map \(L^2\to L^2\) admitting a [[harmonic-analysis/calderon-zygmund-kernel|Calderón–Zygmund kernel]] \(K\) such that
\[
Tf(x)=\int K(x,y)f(y)\,dy
\]
for every compactly supported \(L^2\) function \(f\) and almost every \(x\) outside its support. The integral there is absolutely convergent.

## What is included in the definition

The \(L^2\) bound is an assumption in addition to the kernel estimates. The definition does not insist that the full operator be exactly a principal-value integral; local terms invisible off the support may be present. This convention includes a multiple of the identity, whose off-diagonal kernel is zero.

## References

- [Tao, Fourier analysis lecture notes 4, §2](https://www.math.ucla.edu/~tao/247a.1.06f/notes4.pdf).
