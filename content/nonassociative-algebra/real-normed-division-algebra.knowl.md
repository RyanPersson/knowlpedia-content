+++
id = "nonassociative-algebra/real-normed-division-algebra"
title = "Real normed division algebra"
kind = "definition"
summary = "A finite-dimensional real unital algebra with a positive multiplicative Euclidean norm."
aliases = ["normed division algebra over the reals", "real normed division algebra"]
domains = ["nonassociative-algebra"]
prerequisites = ["nonassociative-algebra/nonassociative-algebra", "shared-foundations/real-numbers", "linear-algebra/euclidean-norm", "nonassociative-algebra/composition-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **real normed division algebra** is a finite-dimensional unital [[nonassociative-algebra/nonassociative-algebra|algebra]] \(A\) over [[shared-foundations/real-numbers|\(\mathbb R\)]] with a positive-definite [[linear-algebra/euclidean-norm|Euclidean norm]] \(\lVert\cdot\rVert\) satisfying
\[
 \lVert xy\rVert=\lVert x\rVert\,\lVert y\rVert
\]
for all \(x,y\in A\). Equivalently, \(N(x)=\lVert x\rVert^2\) makes \(A\) a [[nonassociative-algebra/composition-algebra|composition algebra]] with positive-definite norm.

## Why division follows

Multiplicativity implies that \(xy=0\) with \(x\ne0\) forces \(y=0\), and similarly on the other side. More concretely, the standard conjugation satisfies
\[
 x^*x=xx^*=\lVert x\rVert^2 1,
\]
so every nonzero element has the two-sided inverse
\[
 x^{-1}=\frac{x^*}{\lVert x\rVert^2}.
\]

## Classification

By [[nonassociative-algebra/hurwitz-theorem|Hurwitz's theorem]], every real normed division algebra is isomorphic to exactly one of
\[
 \mathbb R,\qquad \mathbb C,\qquad \mathbb H,\qquad \mathbb O,
\]
of real dimensions \(1,2,4,8\). Associativity holds for the first three and fails for \(\mathbb O\), while all four are [[nonassociative-algebra/alternative-algebra|alternative]].

## Convention warning

The word *division algebra* is sometimes reserved for associative algebras or defined only by solvability of \(ax=b\) and \(ya=b\). “Normed division algebra” in the Hurwitz setting includes nonassociative algebras, requires a unit and a multiplicative positive-definite norm, and is finite-dimensional here.

## References

1. John C. Baez, “The Octonions,” *Bulletin of the American Mathematical Society* **39** (2002), 145–205. [DOI record](https://doi.org/10.1090/S0273-0979-01-00934-X). Relevant: §§1–2.
2. John H. Conway and Derek A. Smith, *On Quaternions and Octonions*, A K Peters, 2003. [DOI record](https://doi.org/10.1201/9781439864180). Relevant: Chapters 1–3.
