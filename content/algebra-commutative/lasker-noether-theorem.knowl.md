+++
id = "algebra-commutative/lasker-noether-theorem"
title = "Lasker–Noether theorem"
kind = "knowl"
summary = "Every ideal in a Noetherian ring can be written as a finite intersection of primary ideals."
aliases = ["lasker-noether-theorem", "Lasker–Noether theorem"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/lasker-noether-theorem.md"
+++

**Lasker–Noether theorem.** Let \(A\) be a [[algebra-commutative/noetherian-ring|Noetherian]] [[algebra-rings/commutative-ring|commutative ring]], and let \(I\subseteq A\) be an ideal. Then there are primary ideals \(Q_1,\dots,Q_r\subseteq A\) such that
\[
I=\bigcap_{i=1}^r Q_i.
\]
The decomposition may be chosen irredundant with distinct radicals \(\mathfrak p_i=\sqrt{Q_i}\). In any such minimal primary decomposition, the set \(\{\mathfrak p_i\}\) is uniquely determined by \(I\); it is the set of associated primes of \(A/I\). Its inclusion-minimal members are precisely the prime ideals minimal over \(I\).

Here an ideal \(Q\) is **primary** if \(ab\in Q\) implies \(a\in Q\) or \(b^n\in Q\) for some \(n\ge 1\). Such an expression for \(I\) is a [[algebra-commutative/primary-decomposition|primary decomposition]].

## Geometric interpretation

In the [[algebra-commutative/zariski-topology|Zariski topology]] on the [[algebra-commutative/prime-spectrum|prime spectrum]] \(\operatorname{Spec}(A)\), the decomposition gives
\[
V(I)=\bigcup_{i=1}^r V(Q_i),
\]
with \(V(Q_i)=V(\mathfrak p_i)\). Embedded associated primes contribute scheme-theoretic information but do not give additional irreducible components of the underlying closed set.

## Examples

1. **Integers: prime-power pieces.**
   In \(A=\mathbb Z\), for \(I=(12)\) one has
   \[
   (12)=(4)\cap (3).
   \]
   Here \((4)\) is \((2)\)-primary and \((3)\) is \((3)\)-primary.

2. **A union of coordinate axes.**
   In \(A=k[x,y]\), with \(k\) a [[algebra-rings/field|field]], the ideal \(I=(xy)\) decomposes as
   \[
   (xy)=(x)\cap (y).
   \]
   Both \((x)\) and \((y)\) are prime, corresponding to the two axes in \(V(xy)\).

3. **A primary component with embedded nilpotents.**
   In \(A=k[x,y]\), the ideal \(I=(x^2,xy)\) admits the decomposition
   \[
   (x^2,xy)=(x)\cap (x^2,y).
   \]
   The ideal \((x)\) is prime, while \((x^2,y)\) is \((x,y)\)-primary. The latter is an embedded component.
