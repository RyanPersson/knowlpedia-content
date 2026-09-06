+++
id = "nonassociative-algebra/octonion-algebra"
title = "Octonion algebra"
kind = "definition"
summary = "The eight-dimensional real alternative normed division algebra."
aliases = ["octonions", "Cayley numbers", "Cayley algebra", "𝕆"]
domains = ["nonassociative-algebra"]
prerequisites = ["nonassociative-algebra/real-normed-division-algebra", "nonassociative-algebra/alternative-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

The **octonion algebra** \(\mathbb O\) is the eight-dimensional [[nonassociative-algebra/real-normed-division-algebra|real normed division algebra]]. It is unital, noncommutative, and nonassociative, but it is [[nonassociative-algebra/alternative-algebra|alternative]]. By [[nonassociative-algebra/hurwitz-theorem|Hurwitz's theorem]], it is unique up to isomorphism among eight-dimensional real normed division algebras.

## A multiplication table from the Fano plane

As a real [[linear-algebra/vector-space|vector space]],
\[
 \mathbb O=\mathbb R1\oplus\bigoplus_{i=1}^{7}\mathbb R e_i,
 \qquad e_i^2=-1.
\]
An oriented Fano plane specifies the remaining products: if \((e_i,e_j,e_k)\) occur in the chosen cyclic order on a line, then \(e_i e_j=e_k\), cyclic permutations have the same sign, and reversing the order changes the sign. Different consistent orientations give isomorphic algebras, but formulas quoted from different sources can differ by basis and sign conventions.

## Conjugation and division

For \(x=x_0+\sum_i x_i e_i\), define
\[
 x^*=x_0-\sum_i x_i e_i.
\]
Then \(xx^*=x^*x=\lVert x\rVert^2 1\), where \(\lVert x\rVert^2=\sum_{i=0}^7x_i^2\), and \(\lVert xy\rVert=\lVert x\rVert\lVert y\rVert\). Thus \(x^{-1}=x^*/\lVert x\rVert^2\) for \(x\ne0\). See [[nonassociative-algebra/octonion-conjugation-norm-and-inner-product|octonion conjugation, norm, and inner product]].

## Exceptional symmetry

The real algebra automorphism group of \(\mathbb O\) is the [[lie-groups/compact-exceptional-lie-group-g2|compact exceptional Lie group \(G_2\)]], whose [[lie-groups/lie-algebra|Lie algebra]] is [[lie-groups/exceptional-lie-algebra-g2|\(\mathfrak g_2\)]]. Choosing an embedded copy of \(\mathbb C\) reduces this symmetry to the [[nonassociative-algebra/su3-stabilizer-of-a-complex-octonion-subalgebra|pointwise stabilizer \(SU(3)\)]]. The octonions also form the coefficient algebra for the [[nonassociative-algebra/exceptional-jordan-algebra|exceptional Jordan algebra]].

## Convention warning

Over a general field, an *octonion algebra* can mean any eight-dimensional unital [[nonassociative-algebra/composition-algebra|composition algebra]], including split forms with zero divisors. Here \(\mathbb O\) means the positive-definite real division algebra unless a base field or split form is explicitly named.

## References

1. John C. Baez, “The Octonions,” *Bulletin of the American Mathematical Society* **39** (2002), 145–205. [DOI record](https://doi.org/10.1090/S0273-0979-01-00934-X).
2. John H. Conway and Derek A. Smith, *On Quaternions and Octonions*, A K Peters, 2003. [DOI record](https://doi.org/10.1201/9781439864180).
3. Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer, 2000. [DOI record](https://doi.org/10.1007/978-3-662-12622-6). Relevant: Chapter 1.
