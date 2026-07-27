+++
id = "algebra-commutative/nullstellensatz-corollary"
title = "Nullstellensatz corollary: maximal ideals are points"
kind = "knowl"
summary = "Over an algebraically closed field, maximal ideals of a polynomial ring are exactly the ideals of points."
aliases = ["nullstellensatz-corollary", "Nullstellensatz corollary: maximal ideals are points"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/nullstellensatz-corollary.md"
+++

Let \(k\) be an algebraically closed [[algebra-rings/field|field]]. The weak Nullstellensatz states that every maximal ideal \(\mathfrak m\subset k[x_1,\dots,x_n]\) has the form
\[
\mathfrak m = (x_1-a_1,\dots,x_n-a_n).
\]
for a unique point \(a=(a_1,\dots,a_n)\in k^n\). Thus the [[algebra-commutative/maximal-spectrum|maximal spectrum]] of \(k[x_1,\dots,x_n]\) is naturally identified with \(k^n\), and the [[algebra-commutative/residue-field|residue field]] at every maximal ideal is canonically \(k\).

## Geometric interpretation

Under this identification, the subspace topology induced from the [[algebra-commutative/zariski-topology|Zariski topology]] on [[algebra-commutative/prime-spectrum|Spec]] agrees with the usual “vanishing set” Zariski topology on \(k^n\).

## Examples
1. **One variable.**
   In \(\mathbb C[x]\), every maximal ideal is of the form \((x-a)\) for a unique \(a \in \mathbb C\).

2. **Two variables.**
   In \(\mathbb C[x,y]\), the ideal \((x-1,\; y+2)\) is maximal and corresponds to the point \((1,-2) \in \mathbb C^2\).

3. **A non-maximal ideal and the points above it.**
   In \(\mathbb C[x]\), the ideal \((x^2+1)\) is not maximal because \(x^2+1=(x-i)(x+i)\). The maximal ideals containing \((x^2+1)\) are \((x-i)\) and \((x+i)\), corresponding to the two points \(i\) and \(-i\).
