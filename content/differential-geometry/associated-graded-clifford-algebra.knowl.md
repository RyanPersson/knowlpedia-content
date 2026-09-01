+++
id = "differential-geometry/associated-graded-clifford-algebra"
title = "Associated graded Clifford algebra"
kind = "theorem"
summary = "The Clifford filtration has exterior algebra as its associated graded algebra."
aliases = ["Clifford PBW theorem", "symbol algebra of a Clifford algebra"]
domains = ["differential-geometry", "algebra-rings"]
prerequisites = ["linear-algebra/quadratic-form", "differential-geometry/clifford-algebra", "algebra-modules/exterior-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(V\) be a finite-dimensional vector space over a field \(k\) of
characteristic different from \(2\), and let \(q\) be a [[linear-algebra/quadratic-form|quadratic form]] on
\(V\). Give the [[differential-geometry/clifford-algebra|Clifford algebra]]
\(\operatorname{Cl}(V,q)\) the filtration \(F^r\) induced by tensors of degree
at most \(r\). Then there is a canonical isomorphism of graded algebras
\[
\operatorname{gr}_F\operatorname{Cl}(V,q)
\cong
\Lambda V,
\]
where \(\Lambda V\) is the
[[algebra-modules/exterior-algebra|exterior algebra]].

## Why the exterior relation appears

Under the convention \(v^2=-q(v)1\), polarization gives
\[
vw+wv=-b_q(v,w)1,
\qquad
b_q(v,w)=q(v+w)-q(v)-q(w).
\]
The right side has filtration degree \(0\), while the left side has degree
\(2\). Passing to the leading symbols therefore gives
\[
\sigma(v)\sigma(w)+\sigma(w)\sigma(v)=0.
\]
These are exactly the exterior-algebra relations. The theorem says that they
are all the leading relations: the induced surjection
\(\Lambda V\to\operatorname{gr}\operatorname{Cl}(V,q)\) is an isomorphism.

## Consequences

If \(n=\dim V\), then
\[
\dim_k\operatorname{Cl}(V,q)=2^n,
\]
even when \(q\) is degenerate. An ordered basis
\(e_1,\ldots,e_n\) yields a basis of Clifford monomials
\[
e_{i_1}\cdots e_{i_r},
\qquad
i_1<\cdots<i_r,
\]
parallel to the usual basis of \(\Lambda V\).

## What the theorem does not say

The isomorphism is an isomorphism with the **associated graded** algebra, not
an isomorphism of \(\operatorname{Cl}(V,q)\) with \(\Lambda V\). The Clifford
product is a filtered deformation of the exterior product: the quadratic form
is visible in lower filtration degree and disappears only after taking
leading symbols.

## References

1. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*,
   Princeton University Press, 1989. [DOI
   record](https://doi.org/10.1515/9781400883912). Relevant: Chapter I,
   Section 1.
2. Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*,
   Springer, collected works edition, 1997. [DOI
   record](https://doi.org/10.1007/978-3-642-58063-7). Relevant: Chapters I–II.
