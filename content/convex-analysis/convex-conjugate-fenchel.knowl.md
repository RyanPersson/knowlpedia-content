+++
id = "convex-analysis/convex-conjugate-fenchel"
title = "Fenchel conjugate"
kind = "knowl"
summary = "The convex conjugate of an extended-real-valued function, defined by a supremum of affine functionals."
aliases = ["convex-conjugate-fenchel", "Fenchel conjugate"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/convex-conjugate-fenchel.md"
+++

A **Fenchel conjugate** of an extended-real-valued [[shared-foundations/function|function]] \(f:\mathbb R^n\to(-\infty,+\infty]\) is the function \(f^*:\mathbb R^n\to(-\infty,+\infty]\) defined by
\[
f^*(y) \;=\; \sup_{x\in\mathbb{R}^n}\big(\langle y,x\rangle - f(x)\big),
\qquad y\in\mathbb{R}^n,
\]
where \(\langle y,x\rangle\) is the Euclidean pairing.

The conjugate is always a (possibly extended-real-valued) [[convex-analysis/convex-function-via-epigraph|convex function]], because it is a pointwise [[real-analysis/supremum|supremum]] of affine functions of \(y\). It is also called the [[convex-analysis/legendre-fenchel-transform|Legendre–Fenchel transform]].

## Examples

- If \(f(x)=\tfrac12\lVert x\rVert_2^2\), then \(f^*(y)=\tfrac12\lVert y\rVert_2^2\).
- If \(f=\delta_C\) is the indicator of a nonempty set \(C\), then \(f^*(y)=\sup_{x\in C}\langle y,x\rangle\), the support function of \(C\).
