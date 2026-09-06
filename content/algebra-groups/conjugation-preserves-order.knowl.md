+++
id = "algebra-groups/conjugation-preserves-order"
title = "Conjugation preserves order"
kind = "knowl"
summary = "Conjugate elements in a group have the same order."
aliases = ["conjugation-preserves-order", "Conjugation preserves order"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group", "algebra-groups/conjugate-element"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "algebra-groups/conjugation-preserves-order.md"
+++

**Proposition (Conjugation preserves order).**
Let \(G\) be a [[algebra-groups/group|group]]. If \(x,y\in G\) are [[algebra-groups/conjugate-element|conjugate]], so that \(y=gxg^{-1}\) for some \(g\in G\), then
\[
\operatorname{ord}(y)=\operatorname{ord}(x),
\]
where an element has order \(\infty\) if no positive power of it is the identity.

## Why this holds

For every integer \(n\), one has \(y^n=gx^ng^{-1}\). Hence \(y^n=e\) exactly when \(x^n=e\), so the two elements have the same finite order or both have infinite order.
