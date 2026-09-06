+++
id = "algebra-commutative/simple-artinian-matrix-ring"
title = "Simple Artinian rings are matrix rings over division rings"
kind = "knowl"
summary = "A simple Artinian ring is isomorphic to a full matrix ring over a division ring."
aliases = ["simple-artinian-matrix-ring", "Simple Artinian rings are matrix rings over division rings"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/simple-artinian-matrix-ring.md"
prerequisites = ["algebra-commutative/artinian-ring", "algebra-rings/division-ring", "algebra-rings/artin-wedderburn-theorem", "algebra-rings/field", "linear-algebra/matrix"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(R\) be a nonzero ring, not necessarily commutative. If \(R\) is **simple**, meaning that it has no nonzero proper two-sided ideals, and **left Artinian**, meaning that every descending chain of left ideals stabilizes, then there are an integer \(n\ge 1\) and a [[algebra-rings/division-ring|division ring]] \(D\) such that
\[
R\cong M_n(D)
\]
as rings. Conversely, every full matrix ring \(M_n(D)\) over a division ring is simple Artinian. This is the simple case of the [[algebra-rings/artin-wedderburn-theorem|Artin–Wedderburn theorem]].

## Refinements

A useful refinement is that \(D\) may be taken, up to passing to the opposite ring according to module conventions, from the endomorphism ring of a simple \(R\)-module. The general semisimple case is the [[algebra-commutative/semisimple-artinian-product|finite product decomposition]] into such matrix rings.

In the commutative setting, necessarily \(n=1\) and \(D\) is commutative, so \(R\) is a [[algebra-rings/field|field]].

## Examples

1. **Matrix rings over a field.**
   For any field \(k\) and any \(n\ge 1\), the ring \(M_n(k)\) is simple Artinian.

2. **Division rings (the case \(n=1\)).**
   Any division ring \(D\) is simple Artinian, and \(M_1(D)\cong D\). For instance, the real quaternions \(\mathbb H\) form a noncommutative division ring.

3. **Why “simple” matters.**
   The ring \(k\times k\) is Artinian and semisimple, but not simple: it has the nontrivial ideals \(k\times0\) and \(0\times k\). It therefore appears as a product rather than as one matrix-ring factor.
