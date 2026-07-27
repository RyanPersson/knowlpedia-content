+++
id = "algebra-commutative/hilbert-basis-corollary"
title = "Hilbert basis corollary"
kind = "knowl"
summary = "Polynomial rings (and finitely generated algebras) over a Noetherian ring are Noetherian."
aliases = ["hilbert-basis-corollary", "Hilbert basis corollary"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/hilbert-basis-corollary.md"
+++

**Hilbert basis theorem (iterated form).** Let \(R\) be a [[algebra-commutative/noetherian-ring|Noetherian ring]]. For every integer \(n\ge 0\), the polynomial ring \(R[x_1,\ldots,x_n]\) is Noetherian. Hence every ideal in this ring is finitely generated. Moreover, every finitely generated \(R\)-algebra is Noetherian, because it is a quotient of some \(R[x_1,\ldots,x_n]\).

In particular, if \(k\) is a [[algebra-rings/field|field]], then \(k[x_1,\ldots,x_n]\) and each quotient \(k[x_1,\ldots,x_n]/I\) are Noetherian.

## Examples
1. **Polynomial rings over a field.**
   For a field \(k\), the ring \(k[x,y,z]\) is Noetherian, so every ideal—not merely one given by a finite list—is finitely generated.

2. **Polynomial rings over the integers.**
   Since \(\mathbb Z\) is Noetherian, \(\mathbb Z[x_1,\dots,x_n]\) is Noetherian. In particular, ideals like \((2,\; x^2,\; xy) \subset \mathbb Z[x,y]\) are finitely generated (here by three explicit generators).

3. **Coordinate rings are Noetherian.**
   Over a field \(k\), the quotient ring \(k[x,y]/(x^2+y^2-1)\) is Noetherian, because it is a quotient of the Noetherian ring \(k[x,y]\).
