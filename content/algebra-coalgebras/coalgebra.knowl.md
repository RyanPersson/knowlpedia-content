+++
id = "algebra-coalgebras/coalgebra"
title = "Coalgebra"
kind = "definition"
summary = "A module with coassociative comultiplication and a counit."
aliases = ["coalgebra over a ring", "counital coalgebra"]
domains = ["algebra-coalgebras", "algebra-modules"]
section_mode = "progressive"
+++

Let \(k\) be a [[algebra-rings/commutative-ring|commutative ring]]. A **\(k\)-coalgebra** is a \(k\)-[[algebra-modules/module|module]] \(C\) equipped with \(k\)-linear maps
\[
\Delta:C\longrightarrow C\otimes_k C,
\qquad
\varepsilon:C\longrightarrow k,
\]
called the **comultiplication** and **counit**, such that
\[
(\Delta\otimes\operatorname{id})\Delta
=
(\operatorname{id}\otimes\Delta)\Delta
\]
and
\[
(\varepsilon\otimes\operatorname{id})\Delta
=\operatorname{id}_C
=
(\operatorname{id}\otimes\varepsilon)\Delta,
\]
after the canonical identifications \(k\otimes_k C\cong C\cong C\otimes_k k\). Thus a coalgebra is a comonoid in the [[algebra-category-theory/monoidal-category|monoidal category]] of \(k\)-modules.

## How to read the axioms

If one writes \(\Delta(c)=\sum c_{(1)}\otimes c_{(2)}\) in Sweedler notation, coassociativity says that iterating \(\Delta\) has an unambiguous value
\(\sum c_{(1)}\otimes c_{(2)}\otimes c_{(3)}\). The counit equations say
\[
\sum\varepsilon(c_{(1)})c_{(2)}=c
=\sum c_{(1)}\varepsilon(c_{(2)}).
\]
These formulas are notation for identities of maps; they do not require a preferred finite expansion of \(\Delta(c)\).

## Morphisms and cocommutativity

A **coalgebra homomorphism** \(f:C\to D\) is a \(k\)-linear map satisfying
\[
\Delta_Df=(f\otimes f)\Delta_C,
\qquad
\varepsilon_Df=\varepsilon_C.
\]
The coalgebra is **cocommutative** when
\(\tau\Delta=\Delta\), where \(\tau(x\otimes y)=y\otimes x\).

## Duality with algebras

When \(C\) is finitely generated projective over \(k\), dualizing \(\Delta\) and
\(\varepsilon\) makes \(C^\vee=\operatorname{Hom}_k(C,k)\) an associative
unital algebra. Without finiteness or projectivity, the natural comparison
\(C^\vee\otimes C^\vee\to(C\otimes C)^\vee\) need not be an isomorphism, so
naive linear duality does not exchange arbitrary coalgebras and algebras.
Topological or finite-dual constructions are then needed.

## Examples

- Every set \(X\) gives a coalgebra with basis \(\{e_x:x\in X\}\),
  \(\Delta(e_x)=e_x\otimes e_x\), and \(\varepsilon(e_x)=1\).
- If \(A\) is a finite-dimensional \(k\)-algebra over a field, the dual
  vector space \(A^\vee\) is a coalgebra by transposing multiplication and
  the unit.

## References

1. Moss E. Sweedler, *Hopf Algebras*, W. A. Benjamin, 1969. Relevant: Chapter 1 on coalgebras and their dual algebras.
2. Christian Kassel, *Quantum Groups*, Graduate Texts in Mathematics 155, Springer, 1995. [Publisher record](https://doi.org/10.1007/978-1-4612-0783-2). Relevant: Chapter III, §1.
