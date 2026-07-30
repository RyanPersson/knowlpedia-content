+++
id = "algebraic-geometry-foundations/ordered-blueprint-with-unique-weak-inverses"
title = "Ordered blueprint with unique weak inverses"
kind = "definition"
summary = "An ordered blueprint in which every element has exactly one additive weak inverse."
aliases = ["pasteurized ordered blueprint", "ordered blueprint with unique weak inverse"]
domains = ["algebraic-geometry-foundations", "algebra-hyperstructures"]
section_mode = "progressive"
+++

An [[algebraic-geometry-foundations/ordered-blueprint|ordered blueprint]] \(B\) has **unique weak inverses** if, for every \(a\in B^\bullet\), there is a unique \(b\in B^\bullet\) such that
\[
0\leq a+b.
\]
The element \(b\) is the **weak inverse** of \(a\).

Equivalently, \(B\) is an \(\mathbb F_1^{\pm}\)-algebra with unique weak inverses, where
\[
\mathbb F_1^{\pm}=\{0,1,\epsilon\}/\!/\langle 0\leq 1+\epsilon\rangle
\quad\text{and}\quad \epsilon^2=1.
\]
The weak inverse of \(a\) is then \(\epsilon a\).

## Terminology

Earlier versions of the ordered-blueprint literature called these objects **pasteurized ordered blueprints**. Current Baker–Lorscheid usage prefers “ordered blueprints with unique weak inverses” (or \(\mathbb F_1^\pm\)-algebras with unique weak inverses). The legacy phrase is retained here only as an alias for search and older citations.

The word “weak” matters: \(0\leq a+\epsilon a\) is an order relation, not necessarily an equality in the ambient semiring \(B^+\). Consequently \(\epsilon\) should not automatically be written as an additive inverse \(-1\).

## Structural role

Hyperrings and tracts have associated ordered blueprints with unique weak inverses. The inclusion of this full subcategory into all ordered blueprints is reflective; its reflector is [[algebraic-geometry-foundations/pasteurization-of-ordered-blueprint|the unique-weak-inverse reflection]].

## References

- Matthew Baker and Oliver Lorscheid, [*The moduli space of matroids*, §§2.6, 2.9](https://arxiv.org/abs/1809.03542).
- Oliver Lorscheid, [*Blueprints and tropical scheme theory*, §5.6](https://lorscheid.org/notes/2018-Blueprints/versions/lecturenotes180521.pdf).

