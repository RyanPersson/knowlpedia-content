+++
id = "algebra-rings/kernel-is-ideal"
title = "Kernel is an ideal"
kind = "knowl"
summary = "The kernel of a ring homomorphism is a two-sided ideal of the domain."
aliases = ["kernel-is-ideal", "Kernel is an ideal"]
domains = ["algebra-rings"]
prerequisites = ["algebra-rings/ring-homomorphism", "algebra-rings/ideal"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-rings/kernel-is-ideal.md"
+++

Let \(\varphi:R\to S\) be a [[algebra-rings/ring-homomorphism|ring homomorphism]]. Then
\[
\ker(\varphi)=\{r\in R:\varphi(r)=0_S\}
\]
is a two-sided [[algebra-rings/ideal|ideal]] of \(R\).

## Consequence

One can therefore form the [[algebra-rings/quotient-ring|quotient ring]] \(R/\ker\varphi\). This is the key input for [[algebra-rings/first-isomorphism-theorem-rings|the first isomorphism theorem for rings]].
