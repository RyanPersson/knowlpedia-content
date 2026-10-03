+++
id = "ergodic-theory/unique-ergodicity-uniform-averages"
title = "Uniform averages characterize unique ergodicity"
kind = "theorem"
summary = "On a compact metric system, unique ergodicity is equivalent to uniform convergence of all continuous orbit averages to constants."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["analysis/unique-ergodicity", "ergodic-theory/invariant-probability-measure", "ergodic-theory/time-average", "topology/compact-set"]
+++

For a continuous \(T:X\to X\) on a nonempty compact metric space, the following are equivalent:

1. There is exactly one invariant Borel probability \(\mu\).
2. For every \(f\in C(X)\), the averages \(N^{-1}\sum_{n=0}^{N-1}f(T^nx)\) converge uniformly in \(x\) to a constant.

The constant is \(\int f\,d\mu\). This is the uniform-averaging characterization of [[analysis/unique-ergodicity|unique ergodicity]].

## Proof idea

If uniform convergence fails under uniqueness, choose starting points and lengths witnessing failure. A weakly convergent subsequence of their empirical measures has invariant limit, by the telescoping boundary term. Uniqueness forces that limit to be \(\mu\), contradicting the failed averages. Conversely, integrate uniform limits against any invariant probability; all such measures agree on every continuous function and are equal.

## Scope

Minimality is not required. The theorem uses continuous observables and gives convergence for every starting point; Birkhoff's theorem permits integrable measurable observables but only gives almost-everywhere convergence.
