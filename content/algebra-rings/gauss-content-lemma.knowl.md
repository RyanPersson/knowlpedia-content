+++
id = "algebra-rings/gauss-content-lemma"
title = "Gauss lemma (content multiplicativity)"
kind = "knowl"
summary = "In a UFD, the content of a product equals the product of contents up to associates."
aliases = ["gauss-content-lemma", "Gauss lemma (content multiplicativity)"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/gauss-content-lemma.md"
prerequisites = ["algebra-rings/ufd", "algebra-rings/polynomial-ring", "algebra-rings/content-polynomial", "algebra-rings/associated-elements", "algebra-rings/primitive-polynomial"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Gauss content lemma**: Let \(R\) be a [[algebra-rings/ufd|UFD]]. For \(f,g\in R[x]\) in the [[algebra-rings/polynomial-ring|polynomial ring]], choose generators \(c(f),c(g),c(fg)\) of their coefficient [[algebra-rings/content-polynomial|content]] ideals. Then
\[
c(fg)\ \sim\ c(f)c(g),
\]
where \(\sim\) denotes equality up to [[algebra-rings/associated-elements|associates]]. Equivalently, the product of two [[algebra-rings/primitive-polynomial|primitive polynomials]] is primitive.

## Remarks

This lemma is the technical engine behind Gauss-type transfer results between \(R[x]\) and \(\mathrm{Frac}(R)[x]\).
