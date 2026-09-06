+++
id = "nonassociative-algebra/hurwitz-theorem"
title = "Hurwitz's theorem on normed division algebras"
kind = "theorem"
summary = "The only finite-dimensional real normed division algebras are R, C, H, and O."
aliases = ["Hurwitz theorem", "Hurwitz classification theorem", "1-2-4-8 theorem"]
domains = ["nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/real-normed-division-algebra", "nonassociative-algebra/composition-algebra", "linear-algebra/quadratic-form"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Hurwitz's theorem.** Every finite-dimensional unital real algebra with a positive-definite multiplicative quadratic norm is isomorphic, as a normed real algebra, to exactly one of
\[
 \mathbb R,\qquad \mathbb C,\qquad \mathbb H,\qquad \mathbb O.
\]
Consequently, a [[nonassociative-algebra/real-normed-division-algebra|real normed division algebra]] has dimension \(1\), \(2\), \(4\), or \(8\).

## What the theorem does not assume

Associativity and commutativity are not hypotheses. The conclusion explains their progressive failure: \(\mathbb R\) and \(\mathbb C\) are commutative and associative, \(\mathbb H\) is associative but noncommutative, and the [[nonassociative-algebra/octonion-algebra|octonions]] are noncommutative and nonassociative but [[nonassociative-algebra/alternative-algebra|alternative]].

## Composition-algebra form

Over a field of characteristic different from \(2\), every unital [[nonassociative-algebra/composition-algebra|composition algebra]] has dimension \(1\), \(2\), \(4\), or \(8\). The real theorem above adds positive definiteness, which rules out split forms and makes every nonzero element invertible.

## Relation to sums of squares

Choosing an [[linear-algebra/orthonormal-basis|orthonormal basis]] turns norm multiplicativity into an identity expressing a product of two sums of \(n\) squares as another sum of \(n\) squares with bilinear entries. Hurwitz's theorem is therefore also called the \(1\)-\(2\)-\(4\)-\(8\) theorem for composition of [[linear-algebra/quadratic-form|quadratic forms]].

## References

1. Adolf Hurwitz, “Über die Composition der quadratischen Formen von beliebig vielen Variabeln,” *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen* (1898), 309–316. [Digitized record](https://eudml.org/doc/58391).
2. John C. Baez, “The Octonions,” *Bulletin of the American Mathematical Society* **39** (2002), 145–205. [DOI record](https://doi.org/10.1090/S0273-0979-01-00934-X). Relevant: §2.2.
