+++
id = "nonassociative-algebra/orthogonal-jordan-idempotents"
title = "Orthogonal Jordan idempotents"
kind = "definition"
summary = "Jordan idempotents e and f are orthogonal when their Jordan product vanishes."
aliases = ["orthogonal idempotents in a Jordan algebra", "Jordan-orthogonal idempotents"]
domains = ["nonassociative-algebra"]
section_mode = "progressive"
+++

Two [[nonassociative-algebra/jordan-idempotent|Jordan idempotents]] \(e,f\)
in a Jordan algebra \(J\) are **orthogonal** when
\[
e\circ f=0.
\]
Their sum is then again an idempotent, because
\((e+f)\circ(e+f)=e+f\).

## Euclidean interpretation

In a [[nonassociative-algebra/euclidean-jordan-algebra|Euclidean Jordan
algebra]] with trace inner product
\(\langle x,y\rangle=\operatorname{tr}(x\circ y)\), two idempotents are
orthogonal in the Jordan sense if and only if they are orthogonal for this
inner product. For Hermitian matrices this says that the corresponding
orthogonal projections have mutually orthogonal ranges.

Pairwise orthogonal primitive idempotents which sum to the unit form a
[[nonassociative-algebra/jordan-frame|Jordan frame]].

## References

1. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994, Chapter III, §1. [Publisher record](https://doi.org/10.1093/oso/9780198534778.001.0001).
2. Kevin McCrimmon, *A Taste of Jordan Algebras*, Springer, 2004, §13.1. [Publisher record](https://doi.org/10.1007/b97489).
