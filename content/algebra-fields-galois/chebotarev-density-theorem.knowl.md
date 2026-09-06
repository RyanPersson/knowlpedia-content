+++
id = "algebra-fields-galois/chebotarev-density-theorem"
title = "Chebotarev density theorem"
kind = "theorem"
summary = "Frobenius conjugacy classes of unramified primes are equidistributed in a finite Galois group."
aliases = ["Chebotarev theorem", "Chebotarev density"]
domains = ["algebra-fields-galois", "number-theory", "langlands"]
section_mode = "progressive"
prerequisites = ["langlands-letter/knowls/galois-extension-and-group", "algebra-fields-galois/number-field", "algebra-fields-galois/galois-group", "algebra-groups/conjugacy-class", "langlands-letter/knowls/frobenius-unramified"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(L/K\) be a finite
[[langlands-letter/knowls/galois-extension-and-group|Galois extension]] of
[[algebra-fields-galois/number-field|number fields]]
with [[algebra-fields-galois/galois-group|Galois group]] \(G\), and let
\(C\subseteq G\) be a
[[algebra-groups/conjugacy-class|conjugacy class]]. The **Chebotarev density
theorem** says that the unramified finite places \(v\) of \(K\) whose
[[langlands-letter/knowls/frobenius-unramified|Frobenius conjugacy class]]
\(\operatorname{Frob}_v\) equals \(C\) have natural density

\[
\frac{|C|}{|G|}.
\]

In particular, every conjugacy class occurs at infinitely many unramified
places.

## Consequence for Galois representations

Frobenius elements at unramified places are dense, up to conjugacy, in the
finite quotients of the
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]].
Consequently two continuous semisimple \(\ell\)-adic representations with
equal [[linear-algebra/characteristic-polynomial|characteristic polynomials]]
of Frobenius at all but finitely many places are isomorphic. This
is the uniqueness mechanism behind
[[langlands/compatible-system-of-galois-representations|compatible systems]]
and many formulations of [[langlands/local-global-compatibility|local–global
compatibility]].

## Function fields

There is a corresponding theorem for
[[algebra-fields-galois/global-function-field|global function fields]]. When the
constant field grows inside \(L\), Frobenius classes and degrees satisfy a
compatibility condition; equidistribution is stated degree by degree in the
permitted congruence classes.  Omitting this constant-field qualification can
make the naive number-field wording false.

## References

1. Nikolai G. Chebotarev, “Die Bestimmung der Dichtigkeit einer Menge von
   Primzahlen, welche zu einer gegebenen Substitutionsklasse gehören,”
   *Mathematische Annalen* 95 (1926), 191–228.
   [EuDML](https://eudml.org/doc/159182).
2. Jean-Pierre Serre, *Lectures on \(N_X(p)\)*, Research Notes in Mathematics
   11, CRC Press, 2012, §3.
