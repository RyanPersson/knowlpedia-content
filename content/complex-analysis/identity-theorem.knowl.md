+++
id = "complex-analysis/identity-theorem"
title = "Identity theorem"
kind = "theorem"
summary = "Holomorphic functions agreeing on a set with an interior accumulation point agree everywhere on a domain."
aliases = ["identity principle", "uniqueness theorem for holomorphic functions"]
domains = ["complex-analysis"]
section_mode = "progressive"
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

## Hypotheses matter

The accumulation point must lie inside the domain. For example, a sequence of zeros may accumulate at a boundary point without forcing the function to vanish. Connectedness is also essential: agreement on one component says nothing about another.

## References

1. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapter III, §7.
