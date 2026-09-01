+++
id = "noncommutative-geometry/unitary-equivalence-spectral-triples"
title = "Unitary equivalence of spectral triples"
kind = "definition"
summary = "Two spectral triples are unitarily equivalent when a unitary identifies their algebra representations and Dirac operators."
aliases = ["isomorphic spectral triples", "unitarily equivalent triples"]
domains = ["noncommutative-geometry", "operator-algebras"]
prerequisites = ["noncommutative-geometry/spectral-triple", "operator-algebras/star-isomorphism", "linear-algebra/surjective-linear-isometry"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Two [[noncommutative-geometry/spectral-triple|spectral triples]]
\((\mathcal A_1,H_1,D_1)\) and \((\mathcal A_2,H_2,D_2)\), with
representations \(\pi_1,\pi_2\), are **unitarily equivalent** if there are a
[[operator-algebras/star-isomorphism|star-isomorphism]]
\(\alpha:\mathcal A_1\to\mathcal A_2\) and a unitary, hence a
[[linear-algebra/surjective-linear-isometry|surjective linear isometry]],
\(U:H_1\to H_2\) such that
\[
U\pi_1(a)U^*=\pi_2(\alpha(a)),\qquad
UD_1U^*=D_2
\]
for every \(a\in\mathcal A_1\). The second equality includes
\(U\operatorname{Dom}(D_1)=\operatorname{Dom}(D_2)\). If the algebras are
already identified, one usually takes \(\alpha\) to be the identity.

## Preserved structure

Unitary conjugation preserves self-adjointness, spectrum with multiplicity,
compactness of the resolvent, and norms of commutators:
\[
[D_2,\pi_2(\alpha(a))]
=U[D_1,\pi_1(a)]U^*.
\]
It therefore preserves summability and the Connes metric after states are
transported by \(\alpha\). This is the basic sameness relation for changing a
Hilbert-space realization without changing the represented metric data.

## Additional structures

For even triples, equivalence also requires
\(U\Gamma_1U^*=\Gamma_2\). For real triples it requires
\(UJ_1U^*=J_2\), with the algebra isomorphism understood in the represented
left and right actions. Omitting these equations identifies the underlying
ungraded complex triples but need not identify their parity or real
structures.

## Examples and distinctions

Changing an [[linear-algebra/orthonormal-basis|orthonormal basis]] of \(H\)
conjugates all represented data and gives a unitarily equivalent triple.
Likewise, a spin-preserving isometry of closed spin manifolds induces a
unitary equivalence of their canonical spectral triples.

Equality of spectra of \(D_1\) and \(D_2\) alone is not enough: an isospectral
unitary need not intertwine the algebra representations. Morita equivalence
is also weaker and more flexible; it may change the Hilbert-space module
rather than identify it by one unitary.

## References

1. Walter D. van Suijlekom, *Noncommutative Geometry and Particle Physics*, 2nd ed., Springer, 2025. [Publisher chapter](https://doi.org/10.1007/978-3-031-59120-4_2). Relevant: §2.2.1, Definition 2.24 on unitary equivalence of finite spectral triples.
2. Alain Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-hosted book](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Relevant: Part VI on spectral triples, their represented data, and unitary changes of realization.
