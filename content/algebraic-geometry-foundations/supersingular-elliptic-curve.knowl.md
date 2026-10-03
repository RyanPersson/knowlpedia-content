+++
id = "algebraic-geometry-foundations/supersingular-elliptic-curve"
title = "Supersingular elliptic curve"
kind = "definition"
summary = "An elliptic curve in characteristic p whose geometric p-torsion has no nonidentity points."
aliases = ["supersingular curve"]
domains = ["algebraic-geometry-foundations"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/elliptic-curve", "algebra-fields-galois/algebraic-closure", "algebra-rings/characteristic"]
dependency_heuristic = "transcript-connections-semantic-v1"
dependency_review_count = 1
+++
An [[algebraic-geometry-foundations/elliptic-curve|elliptic curve]] \(E\) over a field \(k\) of [[algebra-rings/characteristic|characteristic]] \(p>0\) is **supersingular** if
\[
E[p](\overline{k})=\{O\},
\]
where \(\overline{k}\) is an [[algebra-fields-galois/algebraic-closure|algebraic closure]] and \(E[p](\overline{k})=\{P:pP=O\}\).

## Quaternionic endomorphisms

Its geometric endomorphism ring \(\operatorname{End}_{\overline{k}}(E)\) is a [[algebra-rings/maximal-order|maximal order]] in the rational [[algebra-rings/quaternion-algebra|quaternion algebra]] ramified exactly at \(p\) and the real place. Tensoring this ring with \(\mathbb Q\) gives that quaternion algebra.

The geometric qualifier is essential: the ring of endomorphisms defined over the original field \(k\) can be smaller.

## Terminology

The definition uses geometric points; the finite [[algebraic-geometry-foundations/group-scheme|group scheme]] \(E[p]\) still has degree \(p^2\).

“Supersingular” does not mean that the curve has a singular point. Every elliptic curve is smooth. The complementary case, in which the geometric \(p\)-torsion has \(p\) points, is called ordinary.

## References

1. Andrew V. Sutherland, *18.783 Elliptic Curves*, Fall 2023, [Lecture 13](https://math.mit.edu/classes/18.783/2023/LectureNotes13.pdf), opening definition, Warning 13.1, and Theorems 13.18–13.19.
2. John Voight, *Quaternion Algebras*, [§42.1](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_42), Proposition 42.1.7 and Main Theorem 42.1.9.
