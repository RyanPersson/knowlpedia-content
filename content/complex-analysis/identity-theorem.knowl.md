+++
id = "complex-analysis/identity-theorem"
title = "Identity theorem"
kind = "theorem"
summary = "Holomorphic functions agreeing on a set with an interior accumulation point agree everywhere on a domain."
aliases = ["identity principle", "uniqueness theorem for holomorphic functions"]
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["complex-analysis/complex-domain", "complex-analysis/holomorphic-functions-are-analytic", "complex-analysis/order-of-zero-or-pole"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(D\subseteq\mathbb C\) be a [[complex-analysis/complex-domain|domain]] and let \(f,g:D\to\mathbb C\) be holomorphic. If the set
\[
\{z\in D:f(z)=g(z)\}
\]
has an accumulation point in \(D\), then \(f=g\) on all of \(D\).

## Equivalent zero-set form

A nonzero holomorphic function on a domain has isolated zeros. Indeed, at any zero \(a\), its [[real-analysis/power-series|convergent power series]] factors as
\[
f(z)=(z-a)^m h(z)
\]
with \(m\ge1\) and \(h(a)\ne0\). The integer \(m\) is the [[complex-analysis/order-of-zero-or-pole|order of the zero]].

To see the factorization, expand \(f\) in its Taylor series at \(a\). If \(f\) is not identically zero, let \(m\) be the first index with nonzero coefficient; factoring \((z-a)^m\) leaves a holomorphic \(h\) with \(h(a)\ne0\), so the zero is isolated. An accumulation point of zeros forces every Taylor coefficient there to vanish, hence \(f-g\) vanishes on a neighborhood. The zero set is then both open and closed in the connected domain, and therefore is all of \(D\).

## Hypotheses matter

The accumulation point must lie inside the domain. For example, a sequence of zeros may accumulate at a boundary point without forcing the function to vanish. Connectedness is also essential: agreement on one component says nothing about another.

## References

1. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapter III, §7.
