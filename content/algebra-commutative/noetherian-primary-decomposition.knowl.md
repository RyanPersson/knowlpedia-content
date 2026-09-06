+++
id = "algebra-commutative/noetherian-primary-decomposition"
title = "Primary decomposition in Noetherian rings"
kind = "knowl"
summary = "In a Noetherian ring, every ideal is a finite intersection of primary ideals."
aliases = ["noetherian-primary-decomposition", "Primary decomposition in Noetherian rings"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/noetherian-primary-decomposition.md"
prerequisites = ["algebra-commutative/noetherian-ring"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Lasker–Noether theorem.** Let \(R\) be a commutative [[algebra-commutative/noetherian-ring|Noetherian ring]] and let \(I\subsetneq R\) be a proper ideal. Then there exist primary ideals \(Q_1,\dots,Q_r\) such that
\[
I = Q_1 \cap \cdots \cap Q_r .
\]
One may choose the decomposition to be minimal: no component is redundant and the radicals \(\sqrt{Q_i}\) are distinct prime ideals. For every minimal decomposition, the set
\[
\{\sqrt{Q_1},\dots,\sqrt{Q_r}\}
\]
depends only on \(I\), although the primary components themselves need not be unique.

## Primary ideals

An ideal \(Q\subsetneq R\) is **primary** if \(ab\in Q\) and \(a\notin Q\) imply \(b^n\in Q\) for some \(n\geq 1\). Equivalently, every zero divisor in \(R/Q\) is nilpotent. See [[algebra-commutative/primary-decomposition|primary decomposition]] for the general terminology.

## Examples
1. **A reduced principal ideal in a polynomial ring.**
   In \(k[x,y]\), the ideal \((xy)\) decomposes as
   \[
   (xy) = (x) \cap (y).
   \]
   Here \((x)\) and \((y)\) are prime ideals (hence primary).

2. **A decomposition with an embedded component.**
   In \(k[x,y]\),
   \[
   (x^2,xy) = (x) \cap (x^2,y).
   \]
   Indeed, if \(f \in (x) \cap (x^2,y)\), then \(f=xg\) and \(xg \in (x^2,y)\) forces \(g \in (x,y)\), so \(f \in (x^2,xy)\).
   The ideal \((x)\) is prime, and \((x^2,y)\) is \((x,y)\)-primary since its radical is \((x,y)\).

3. **In the integers.**
   In \(\mathbb Z\),
   \[
   (12) = (4) \cap (3).
   \]
   The ideal \((4)\) is \((2)\)-primary and \((3)\) is prime (hence primary).
