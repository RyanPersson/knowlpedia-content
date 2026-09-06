+++
id = "algebra-rings/second-isomorphism-theorem-rings"
title = "Second isomorphism theorem for rings"
kind = "knowl"
summary = "A subring modulo its intersection with an ideal is isomorphic to its image in the corresponding quotient."
aliases = ["second-isomorphism-theorem-rings", "Second isomorphism theorem for rings"]
domains = ["algebra-rings"]
prerequisites = ["algebra-rings/subring", "algebra-rings/two-sided-ideal", "algebra-rings/ideal", "algebra-rings/quotient-ring"]
dependency_review_count = 1
legacy_source_path = "algebra-rings/second-isomorphism-theorem-rings.md"
+++

**Second isomorphism theorem (rings)**: Let \(R\) be a ring, let \(A\subseteq R\) be a [[algebra-rings/subring|subring]], and let \(I\triangleleft R\) be a two-sided [[algebra-rings/ideal|ideal]]. Then \(A\cap I\triangleleft A\), \(A+I:=\{a+i:a\in A,\ i\in I\}\) is a subring of \(R\), and there is a natural isomorphism
\[
A/(A\cap I)\ \cong\ (A+I)/I
\]
of [[algebra-rings/quotient-ring|quotient rings]].

## Remarks

This is most efficiently proved by restricting the quotient map \(R\to R/I\) to \(A\) and applying the [[algebra-rings/first-isomorphism-theorem-rings|first isomorphism theorem]].
