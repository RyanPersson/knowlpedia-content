+++
id = "algebra-rings/content-formula"
title = "Content formula"
kind = "knowl"
summary = "Over a UFD, content(fg) is associate to content(f)content(g) for polynomials."
aliases = ["content-formula", "Content formula"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/content-formula.md"
prerequisites = ["algebra-rings/ufd", "algebra-rings/polynomial-ring", "algebra-rings/content-polynomial", "algebra-rings/primitive-polynomial"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Content formula**: Let \(R\) be a UFD and let \(f,g\in R[x]\). Choose elements \(c(f),c(g),c(fg)\) generating the coefficient ideals (the content ideals). Then
\[
c(fg)\sim c(f)c(g),
\]
i.e., the chosen generator of the content ideal of \(fg\) is associate to the product of the chosen generators for \(f\) and \(g\). In particular, the product of primitive polynomials is primitive.

## Remarks

Here [[algebra-rings/content-polynomial|content]] is computed in the [[algebra-rings/polynomial-ring|polynomial ring]] over a [[algebra-rings/ufd|UFD]]. The formula implies that the product of two [[algebra-rings/primitive-polynomial|primitive polynomials]] is primitive and is a standard ingredient in [[algebra-rings/gauss-content-lemma|Gauss's content lemma]].
