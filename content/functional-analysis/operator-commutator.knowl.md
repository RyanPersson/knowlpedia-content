+++
id = "functional-analysis/operator-commutator"
title = "Commutator of possibly unbounded operators"
kind = "definition"
summary = "The difference of two operator products, defined only where both products make sense."
aliases = ["operator commutator", "commutator on a common domain", "AB minus BA"]
domains = ["functional-analysis"]
prerequisites = ["linear-algebra/hilbert-space", "functional-analysis/densely-defined-operator"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(A\) and \(B\) be linear operators on a [[linear-algebra/hilbert-space|Hilbert space]] \(H\), with possibly
proper domains. Their **operator commutator** is the operator
\[
[A,B]\xi=AB\xi-BA\xi
\]
with natural domain
\[
\operatorname{Dom}([A,B])=\operatorname{Dom}(AB)\cap\operatorname{Dom}(BA),
\]
where \(\operatorname{Dom}(AB)=\{\xi\in\operatorname{Dom}(B):B\xi\in
\operatorname{Dom}(A)\}\), and similarly for \(BA\). One may instead specify a
common subdomain \(E\) on which both products are defined; then the notation
\([A,B]|_E\) records that choice. Thus a commutator of
[[functional-analysis/densely-defined-operator|densely defined operators]] is
not determined by the formal expression alone: its domain is part of the
operator.

## Domain discipline

Even when \(B\) is a
[[functional-analysis/bounded-linear-operator|bounded operator]], the product
\(AB\) is defined only on vectors \(\xi\) for which \(B\xi\) lies in
\(\operatorname{Dom}(A)\). Boundedness of \(B\) does not by itself imply that
\(B\operatorname{Dom}(A)\subseteq\operatorname{Dom}(A)\). Consequently, algebraic
identities involving commutators must be checked on a domain invariant under
every operator product that occurs. This is the operator-domain convention used
in the standard treatment of unbounded operators.

## Spectral-triple convention

For a [[noncommutative-geometry/spectral-triple|spectral triple]]
\((\mathcal A,H,D)\), the algebra is represented by bounded operators
\(\pi(a)\). The usual convention requires
\(\pi(a)\operatorname{Dom}(D)\subseteq\operatorname{Dom}(D)\), so that
\([D,\pi(a)]\) is initially defined on all of \(\operatorname{Dom}(D)\). The
spectral-triple axiom then asks for this operator to have a
[[functional-analysis/bounded-commutator|bounded extension]]. A source that
writes simply \([D,a]\) is normally suppressing both the representation
\(\pi\) and this initial domain. Form or quadratic-form commutators are weaker
conventions and must be identified explicitly.

## Example and warning

On \(L^2(S^1)\), let \(D=-i\,d/dx\) with Sobolev domain \(H^1(S^1)\), and let
\(M_f\) multiply by a smooth function \(f\). Multiplication preserves
\(H^1(S^1)\), and on that domain
\[
[D,M_f]=-iM_{f'}.
\]
This calculation is legitimate because the domain invariance is known first.
Without it, the same formal subtraction could be defined only on a smaller
intersection, possibly one that is not dense.

## References

1. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1972. [Publisher record](https://doi.org/10.1016/B978-0-12-585001-8.X5001-6). Relevant: Chapter VIII on unbounded operators and their domains.
2. José M. Gracia-Bondía, Joseph C. Várilly, and Héctor Figueroa, *Elements of Noncommutative Geometry*, Birkhäuser, 2001. [DOI record](https://doi.org/10.1007/978-1-4612-0005-5). Relevant: §10.1 on spectral triples and bounded commutators.
