+++
id = "algebra-rings/existence-of-maximal-ideals"
title = "Existence of maximal ideals"
kind = "knowl"
summary = "Every nontrivial unital commutative ring has a maximal ideal (via Zorn's lemma)."
aliases = ["existence-of-maximal-ideals", "Existence of maximal ideals"]
domains = ["algebra-rings"]
prerequisites = ["algebra-rings/unital-ring", "algebra-rings/maximal-ideal"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "algebra-rings/existence-of-maximal-ideals.md"
+++

**Existence of maximal ideals (Zorn)**: Let \(R\) be a [[algebra-rings/unital-ring|unital ring]] with \(1\neq 0\), assumed commutative. Then \(R\) has a [[algebra-rings/maximal-ideal|maximal ideal]].

## Remarks

This result is typically proved using [[shared-foundations/zorns-lemma|Zorn's lemma]] (and hence the [[shared-foundations/axiom-of-choice|axiom of choice]]) applied to the partially ordered set of proper [[algebra-rings/ideal|ideals]] of \(R\) ordered by inclusion.
