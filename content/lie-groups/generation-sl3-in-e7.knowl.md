+++
id = "lie-groups/generation-sl3-in-e7"
title = "Generation sl3 in e7"
kind = "theorem"
summary = "A good Standard Model subalgebra of e7 has centralizer sl3 plus a two-dimensional center, with a unique sl3 subalgebra."
aliases = ["generation sl3", "generation algebra in e7", "sl3 gen"]
domains = ["lie-groups", "mathematical-physics"]
prerequisites = ["lie-groups/good-standard-model-embedding-in-e7", "lie-groups/centralizer-of-a-lie-subalgebra", "lie-groups/lie-subalgebra", "lie-groups/lie-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Fix a [[lie-groups/good-standard-model-embedding-in-e7|good embedding]]
\(\mathfrak g_{\mathrm{SM}}\subset\mathfrak e_7\). Its [[lie-groups/centralizer-of-a-lie-subalgebra|centralizer]] satisfies
\[
C_{\mathfrak e_7}(\mathfrak g_{\mathrm{SM}})
\cong \mathfrak{sl}_3(\mathbb C)\oplus\mathbb C^2,
\]
and it contains exactly one [[lie-groups/lie-subalgebra|Lie subalgebra]] isomorphic to \(\mathfrak{sl}_3(\mathbb C)\). This unique subalgebra is the **generation \(\mathfrak{sl}_3\)**, denoted \(\mathfrak{sl}_3^{\mathrm{gen}}\).

The displayed formula is an isomorphism of [[lie-groups/lie-algebra|Lie algebras]]: the two summands commute, and \(\mathbb C^2\) is abelian.

## Why the sl3 is unique

For any subalgebra \(\mathfrak a\cong\mathfrak{sl}_3\) inside
\(\mathfrak{sl}_3\oplus\mathbb C^2\), projection to the abelian factor has abelian image. Since \(\mathfrak{sl}_3\) is simple and perfect, that projection vanishes. Thus \(\mathfrak a\) lies in the first summand, and equality follows from dimension.

## Root-system description

For a compatible Cartan description of the regular \(\mathfrak g_{\mathrm{SM}}\), the [[lie-groups/centralizer-of-a-regular-reductive-subalgebra|regular-centralizer formula]] selects the roots orthogonal to the Standard Model [[lie-groups/root-subsystem|root subsystem]]. They form a subsystem of type \(A_2\), producing \(\mathfrak{sl}_3^{\mathrm{gen}}\); the remaining two orthogonal Cartan directions give the abelian factor.

## Intrinsic status

Once the particular good embedded subalgebra \(\mathfrak g_{\mathrm{SM}}\subset\mathfrak e_7\) is fixed, \(\mathfrak{sl}_3^{\mathrm{gen}}\) is intrinsic: no [[lie-groups/cartan-subalgebra|Cartan subalgebra]] or root labeling is required to characterize it. A Cartan choice is needed only to split it into the [[lie-groups/generation-plane|generation plane]] and six [[lie-groups/root-space|root spaces]] or to name the three [[lie-groups/generation-sl2-subalgebras|generation \(\mathfrak{sl}_2\) subalgebras]].

## References

1. John C. Baez, “Three Generations in E7,” 2026, Proposition 1. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
2. Benjamin Nasmith, “An Exceptional Combinatorial Sequence and Standard Model Particles,” 2020, §6. [arXiv:2012.03933](https://arxiv.org/abs/2012.03933).
3. E. B. Dynkin, “Semisimple Subalgebras of Semisimple Lie Algebras,” *American Mathematical Society Translations*, Series 2, 6 (1957), 111–244.
