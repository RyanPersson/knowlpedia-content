+++
id = "complex-analysis/normal-family"
title = "Normal family"
kind = "definition"
summary = "A family of holomorphic functions for which every sequence has a locally uniformly convergent subsequence."
aliases = ["normal family of holomorphic functions"]
domains = ["complex-analysis", "topology"]
section_mode = "progressive"
+++

Let \(D\subseteq\mathbb C\) be a domain. A family \(\mathcal F\) of holomorphic functions \(D\to\mathbb C\) is a **normal family** if every sequence in \(\mathcal F\) has a subsequence that converges uniformly on each compact subset of \(D\), either to a holomorphic function \(D\to\mathbb C\) or locally uniformly to \(\infty\).

## Spherical formulation

View each function as a map into the [[complex-analysis/riemann-sphere|Riemann sphere]] with its spherical metric. Then the two alternatives in the core can be expressed as locally uniform spherical convergence. For families of [[complex-analysis/meromorphic-function|meromorphic functions]], this spherical formulation is the standard definition and permits meromorphic limits.

## Compactness criterion

The [[complex-analysis/montel-theorem|Montel theorem]] says that every locally uniformly bounded family of holomorphic functions is normal. It is the central compactness criterion used in many existence proofs.

## Role in conformal mapping

Normal-family compactness is used in a standard proof of the [[complex-analysis/riemann-mapping-theorem|Riemann mapping theorem]]: one takes a sequence of normalized injective maps whose derivative at a base point approaches the extremal value, extracts a limit, and proves that extremality forces surjectivity.

## References

1. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapter VII.
