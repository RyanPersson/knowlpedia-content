+++
id = "shared-foundations/inverse-function"
title = "Inverse function"
kind = "knowl"
summary = "A function that undoes a bijective function"
aliases = ["inverse-function", "Inverse function"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/inverse-function.md"
prerequisites = ["shared-foundations/bijective-function", "shared-foundations/identity-function", "shared-foundations/composition"]
dependency_heuristic = "semantic-curriculum-review-v1"
dependency_review_count = 1
+++

If \(f:A\to B\) is a [[shared-foundations/bijective-function|bijection]], its **inverse function** is the function \(f^{-1}:B\to A\) for which \(f^{-1}(b)\) is the unique \(a\in A\) satisfying \(f(a)=b\). Equivalently,
\[
f^{-1}\circ f=\mathrm{id}_A\quad\text{and}\quad f\circ f^{-1}=\mathrm{id}_B,
\]

where \(\mathrm{id}_A\) and \(\mathrm{id}_B\) are [[shared-foundations/identity-function|identity functions]].

## Remarks

The notation \(f^{-1}\) is also used for the [[shared-foundations/preimage|preimage]] of a subset, an operation defined even when \(f\) is not bijective.

## Examples

- The inverse of \(f:\mathbb R\to\mathbb R\), \(f(x)=x^3\), is \(f^{-1}(y)=\sqrt[3]{y}\).
- The inverse of \(f:\mathbb Z\to\mathbb Z\), \(f(n)=n+1\), is \(f^{-1}(m)=m-1\).
