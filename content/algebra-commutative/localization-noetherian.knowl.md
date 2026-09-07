+++
id = "algebra-commutative/localization-noetherian"
title = "Localization preserves Noetherian rings"
kind = "knowl"
summary = "If a ring is Noetherian, then any localization at a multiplicative set is again Noetherian."
aliases = ["localization-noetherian", "Localization preserves Noetherian rings"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/localization-noetherian.md"
prerequisites = ["algebra-commutative/noetherian-ring", "algebra-commutative/multiplicative-set", "algebra-modules/module", "algebra-modules/noetherian-module", "algebra-commutative/localization-ring", "algebra-commutative/localization-module"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(R\) be a [[algebra-commutative/noetherian-ring|commutative Noetherian ring]] and let \(S\subseteq R\) be a [[algebra-commutative/multiplicative-set|multiplicative set]]. Then the localized ring
\[
S^{-1}R
\]
is Noetherian.

More generally, if \(M\) is a Noetherian \(R\)-module, then \(S^{-1}M\) is a Noetherian \(S^{-1}R\)-module.

## Examples

- Since \(\mathbb Z\) is Noetherian, its [[algebra-commutative/localization-at-prime|localization]] \(\mathbb Z_{(p)}\) is Noetherian for every prime \(p\).
- If \(R=k[x,y]\) and \(S=\{1,x,x^2,\ldots\}\), then \(S^{-1}R=R_x\) is Noetherian.

## Remarks

The converse fails: a localization can be Noetherian even when its source is not. Let \(R=k[x_1,x_2,\ldots]\), which has the infinite ascending chain \( (x_1)\subsetneq(x_1,x_2)\subsetneq\cdots \) of ideals, and localize at all nonzero elements. The resulting fraction field \(\operatorname{Frac}(R)\) is a field, hence Noetherian. The preservation theorem is often used together with [[algebra-commutative/localization-exact|exactness of localization]].
