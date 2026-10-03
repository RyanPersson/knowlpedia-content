+++
id = "complex-analysis/cusp-form"
title = "Cusp form"
kind = "definition"
summary = "A holomorphic modular form whose constant Fourier coefficient vanishes at every cusp."
aliases = ["cusp forms", "cuspidal modular form"]
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["complex-analysis/modular-form"]
dependency_heuristic = "transcript-connections-semantic-v1"
dependency_review_count = 1
+++
A **cusp form** of weight \(k\) for a finite-index subgroup \(\Gamma\le\operatorname{SL}_2(\mathbb Z)\) is a [[complex-analysis/modular-form|holomorphic modular form]] whose Fourier expansion at every cusp has zero constant coefficient. In the slash-operator notation, for every \(\gamma\in\operatorname{SL}_2(\mathbb Z)\),
\[
(f|_k\gamma)(z)=\sum_{n\ge1}a_n e^{2\pi inz/h}
\]
near infinity, for an appropriate positive integer period \(h\).

## Scope of the condition

The subspace is denoted \(S_k(\Gamma)\subseteq M_k(\Gamma)\). Checking the constant term at infinity alone does not suffice when \(\Gamma\) has other cusp classes.

## References

1. John Voight, *Quaternion Algebras*, [§40.2](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_40), Definition 40.2.15 and the preceding cusp condition.
