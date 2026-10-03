+++
id = "algebraic-geometry-foundations/elliptic-curve"
title = "Elliptic curve"
kind = "definition"
summary = "A smooth projective geometrically integral genus-one curve with a chosen rational point."
aliases = ["elliptic curves"]
domains = ["algebraic-geometry-foundations"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/smooth-projective-curve"]
dependency_heuristic = "transcript-connections-semantic-v1"
dependency_review_count = 1
+++
An **elliptic curve** over a field \(k\) is a [[algebraic-geometry-foundations/smooth-projective-curve|smooth projective curve]] \(E/k\), geometrically integral and of genus \(1\), together with a specified point \(O\in E(k)\). Here genus \(1\) means that the space of global regular differential one-forms has dimension \(1\) over \(k\).

The point \(O\) determines the identity in a canonical [[algebraic-geometry-foundations/algebraic-group|algebraic group]] law on \(E\); it is part of the data.

## Equations and characteristic

An elliptic curve admits a nonsingular generalized Weierstrass equation
\[
y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6,
\]
with its projective point at infinity as \(O\). If \(\operatorname{char}k\ne2,3\), a change of coordinates gives
\[
y^2=x^3+Ax+B,\qquad 4A^3+27B^2\ne0.
\]
The short equation must not replace the general one in characteristic \(2\) or \(3\).

## Morphisms

A homomorphism of elliptic curves over \(k\) is a morphism of algebraic groups over \(k\). Endomorphisms therefore preserve \(O\); arbitrary maps of the underlying point sets do not define the endomorphism ring. The base field matters: maps over an [[algebra-fields-galois/algebraic-closure|algebraic closure]] may outnumber maps over \(k\).

## References

1. Andrew V. Sutherland, *18.783 Elliptic Curves*, Fall 2023, [Lecture 1](https://math.mit.edu/classes/18.783/2023/LectureNotes1.pdf), Definition 1.1 and §§1.1–1.2.
2. John Voight, *Quaternion Algebras*, [§42.1](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_42), elliptic-curve and geometric-endomorphism conventions.
