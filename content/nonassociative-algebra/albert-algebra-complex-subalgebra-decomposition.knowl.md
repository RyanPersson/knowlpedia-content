+++
id = "nonassociative-algebra/albert-algebra-complex-subalgebra-decomposition"
title = "Complex-subalgebra decomposition in the Albert algebra"
kind = "theorem"
summary = "A framed H_3(C) subalgebra of H_3(O) is encoded by three compatible real 2-planes in the octonions."
aliases = ["complex qutrit subalgebra normal form", "framed H3(C) subalgebra decomposition"]
domains = ["nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/jordan-subalgebra", "nonassociative-algebra/jordan-frame", "nonassociative-algebra/frame-decomposition-of-hermitian-jordan-algebras", "lie-groups/spin8-triality"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(B\subset H_3(\mathbb O)\) be a [[nonassociative-algebra/jordan-subalgebra|Jordan subalgebra]] isomorphic to
\(H_3(\mathbb C)\), and suppose that \(B\) contains the standard [[nonassociative-algebra/jordan-frame|Jordan frame]]
\((e_1,e_2,e_3)\). Relative to the standard frame decomposition there are
real two-dimensional subspaces \(V_{12},V_{23},V_{31}\subset\mathbb O\) such
that
\[
B=\bigoplus_{i=1}^3\mathbb R e_i
\oplus\xi_{12}(V_{12})
\oplus\xi_{23}(V_{23})
\oplus\xi_{31}(V_{31}).
\]
The Jordan-product closure of \(B\) forces the cyclic compatibility relations
\[
V_{12}V_{23}\subseteq V_{31}^*,\qquad
V_{23}V_{31}\subseteq V_{12}^*,\qquad
V_{31}V_{12}\subseteq V_{23}^*,
\]
with the precise placement of conjugations depending on the convention for
the maps \(\xi_{ij}\).

## A useful normal form

The \(\mathrm{Spin}(8)\) subgroup fixing the frame acts on the three
off-diagonal copies of \(\mathbb O\) through its vector and two half-spin
representations. After applying such an automorphism, one may arrange
\(V_{12}=\mathbb C\subset\mathbb O\). Choosing a unit vector
\(a\in V_{23}\) then gives
\[
B=\bigoplus_{i=1}^3\mathbb R e_i
\oplus\xi_{12}(\mathbb C)
\oplus\xi_{23}(\mathbb C a)
\oplus\xi_{31}(a^*\mathbb C).
\]
This is an intermediate normal form: a further frame-fixing automorphism can
take \(a\) to \(1\), turning \(B\) into the standard \(H_3(\mathbb C)\).

## Why the decomposition is useful

It converts an embedded [[nonassociative-algebra/jordan-algebra|Jordan algebra]] into linear data inside the octonions.
The [[nonassociative-algebra/frame-decomposition-of-hermitian-jordan-algebras|frame
decomposition]] supplies the six summands, while
[[lie-groups/spin8-triality|triality]] coordinates their transformation laws.
This is the key input to the transitivity theorem for complex-qutrit
subalgebras.

## References

1. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026, proof of Lemma 6. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
2. Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer, 2000, Chapters 5–7. [Publisher record](https://doi.org/10.1007/978-3-662-12622-6).
