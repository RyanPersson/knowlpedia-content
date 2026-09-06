+++
id = "nonassociative-algebra/nonassociative-algebra"
title = "Nonassociative algebra"
kind = "definition"
summary = "A vector space with a bilinear multiplication, with no associative law assumed."
aliases = ["non-associative algebra", "not necessarily associative algebra"]
domains = ["nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["algebra-rings/field", "linear-algebra/vector-space", "algebra-modules/bilinear-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(k\) be a [[algebra-rings/field|field]]. A **nonassociative algebra** over \(k\) is a [[linear-algebra/vector-space|vector space]] \(A\) over \(k\) equipped with a [[algebra-modules/bilinear-map|bilinear map]]
\[
 A\times A\longrightarrow A,\qquad (x,y)\longmapsto xy.
\]
Associativity is not required. The algebra is **unital** if it has an element \(1\) satisfying \(1x=x1=x\) for every \(x\in A\).

## The associator

The failure of associativity is measured by the trilinear **associator**
\[
 [x,y,z]=(xy)z-x(yz).
\]
Thus \(A\) is associative exactly when its associator vanishes identically. Weaker identities impose symmetries or partial vanishing conditions on this map; for example, an [[nonassociative-algebra/alternative-algebra|alternative algebra]] has \([x,x,y]=[y,x,x]=0\).

## Morphisms and subalgebras

An algebra homomorphism \(f:A\to B\) is a [[linear-algebra/linear-map|linear map]] satisfying \(f(xy)=f(x)f(y)\). If units are part of the chosen category, one usually also requires \(f(1_A)=1_B\). A [[convex-analysis/linear-subspace|linear subspace]] \(S\subseteq A\) closed under multiplication is a subalgebra; whether it must contain the ambient unit is a separate convention.

## Convention warning

The word *algebra* by itself often means an associative unital algebra. In nonassociative algebra it commonly means only a vector space with bilinear multiplication, and authors vary on whether a unit is included. A statement involving Jordan, alternative, or [[nonassociative-algebra/composition-algebra|composition algebras]] should therefore be read with its unit and characteristic hypotheses made explicit.

## Examples

- Every associative algebra is nonassociative in the inclusive sense “not necessarily associative.”
- [[lie-groups/lie-algebra|Lie algebras]] are nonassociative algebras whose multiplication is alternating and satisfies the Jacobi identity.
- [[nonassociative-algebra/jordan-algebra|Jordan algebras]] are commutative nonassociative algebras satisfying the Jordan identity.
- The [[nonassociative-algebra/octonion-algebra|octonions]] are unital and alternative but not associative.

## References

1. Richard D. Schafer, *An Introduction to Nonassociative Algebras*, Academic Press, 1966. [Project Gutenberg edition](https://www.gutenberg.org/ebooks/25156). Relevant: Chapter I.
2. Kevin McCrimmon, *A Taste of Jordan Algebras*, Springer, 2004. [DOI record](https://doi.org/10.1007/b97489). Relevant: Chapter 0 on conventions and basic identities.
