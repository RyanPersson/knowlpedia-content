+++
id = "nonassociative-algebra/primitive-jordan-idempotent"
title = "Primitive Jordan idempotent"
kind = "definition"
summary = "A nonzero Jordan idempotent admitting no decomposition into two nonzero orthogonal idempotents."
aliases = ["minimal Jordan idempotent", "primitive idempotent in a Jordan algebra"]
domains = ["nonassociative-algebra"]
prerequisites = ["nonassociative-algebra/jordan-idempotent", "nonassociative-algebra/orthogonal-jordan-idempotents", "nonassociative-algebra/euclidean-jordan-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A nonzero [[nonassociative-algebra/jordan-idempotent|Jordan idempotent]]
\(e\) is **primitive** if there do not exist nonzero
[[nonassociative-algebra/orthogonal-jordan-idempotents|orthogonal
idempotents]] \(e_1,e_2\) such that
\[
e=e_1+e_2.
\]
For finite-dimensional [[nonassociative-algebra/euclidean-jordan-algebra|Euclidean Jordan algebras]], “primitive” is also often
called **minimal**.

## Rank-one meaning

In a simple [[nonassociative-algebra/euclidean-jordan-algebra|Euclidean
Jordan algebra]], every idempotent is a sum of mutually orthogonal primitive
idempotents. The number of summands is its rank. Thus the primitive
idempotents are exactly the rank-one idempotents.

In \(H_n(\mathbb K)\), for
\(\mathbb K=\mathbb R,\mathbb C,\mathbb H\), and also for the allowed
octonionic case \(H_3(\mathbb O)\), the primitive idempotents have matrix trace
\(1\). This trace criterion depends on the standard normalization and should
not be taken as the definition in an arbitrary Jordan algebra.

## References

1. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994, Chapter III, §§1–2. [Publisher record](https://doi.org/10.1093/oso/9780198534778.001.0001).
2. Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer, 2000, §5.8. [Publisher record](https://doi.org/10.1007/978-3-662-12622-6).
