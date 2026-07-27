+++
id = "algebra-rings/field-iff-trivial-ideals"
title = "Fields and trivial ideals"
kind = "knowl"
summary = "A nonzero commutative ring with identity is a field exactly when its only ideals are zero and the whole ring."
aliases = ["field-iff-trivial-ideals", "Fields and trivial ideals"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/field-iff-trivial-ideals.md"
+++

Let $R$ be a nonzero [[algebra-rings/commutative-ring|commutative ring]] with identity. Then $R$ is a [[algebra-rings/field|field]] if and only if its only [[algebra-rings/ideal|ideals]] are $(0)$ and $R$. Equivalently, every nonzero element of $R$ is a [[algebra-rings/unit|unit]].

## Proof idea

In a field, an ideal containing $a\ne 0$ also contains $a^{-1}a=1$, so it is all of $R$. Conversely, if the only ideals are $(0)$ and $R$, then $(a)=R$ for every $a\ne 0$, so $ab=1$ for some $b\in R$.

This criterion is often paired with [[algebra-rings/maximal-iff-quotient-field|maximal iff quotient is a field]].
