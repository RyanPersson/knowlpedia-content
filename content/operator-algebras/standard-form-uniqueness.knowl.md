+++
id = "operator-algebras/standard-form-uniqueness"
title = "Uniqueness of standard form"
kind = "definition"
summary = "A normal isomorphism between von Neumann algebras in standard form has a unique cone-preserving unitary implementation."
aliases = ["spatial uniqueness of standard form"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/standard-form", "operator-algebras/von-neumann-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((M,H,J_M,P_M)\) and \((N,K,J_N,P_N)\) be
[[operator-algebras/standard-form|standard forms]] of [[operator-algebras/von-neumann-algebra|von Neumann algebras]].
The **uniqueness of standard form** says that every normal
\(*\)-isomorphism \(\alpha:M\to N\) has a unique unitary \(U:H\to K\)
such that
\[
\alpha(x)=UxU^*\quad(x\in M),\qquad U(P_M)=P_N.
\]
This unitary automatically intertwines the modular conjugations,
\[
UJ_M=J_NU.
\]
Thus the self-dual cones remove the freedom ordinarily present in spatial
implementations. Normality, the full standard-form axioms, and preservation
of the distinguished cones are part of the theorem.

## Canonical consequences

Taking \(M=N\) shows that every normal automorphism of \(M\) acts canonically
on the standard [[linear-algebra/hilbert-space|Hilbert space]]. If \(U_\alpha\) and \(U_\beta\) implement
normal automorphisms \(\alpha\) and \(\beta\), uniqueness gives
\[
U_{\alpha\circ\beta}=U_\alpha U_\beta.
\]
The identity automorphism is implemented by the identity unitary. Hence the
normal [[algebra-groups/automorphism-group|automorphism group]] of \(M\) acquires an honest unitary
representation, not merely a projective one.

The same uniqueness makes standard form functorial: composing normal
\(*\)-isomorphisms composes their canonical spatial implementations.
Changing to another standard form changes this representation only by the
unique cone-preserving unitary equivalence.

## Why the cone condition matters

A faithful
[[operator-algebras/normal-representation|normal representation]] by itself
has no comparable uniqueness.
For example, an algebra may be represented with additional multiplicity,
and unitaries in its commutant can alter a spatial implementation without
changing the induced algebra map. Even inside a standard representation,
an implementing unitary multiplied by a suitable commutant unitary can
implement the same isomorphism while failing to preserve the
[[operator-algebras/natural-positive-cone|natural positive cone]].

The cone condition selects exactly one implementation. Compatibility with
[[operator-algebras/modular-conjugation|modular conjugation]] is then a
consequence rather than an independent choice.

## References

1. Uffe Haagerup, “The Standard Form of von Neumann Algebras,” *Mathematica Scandinavica* 37 (1975), 271–283. [Journal and DOI record](https://doi.org/10.7146/math.scand.a-11606). Relevant: Theorem 2.3 on the unique unitary implementation of normal \(*\)-isomorphisms between standard forms.
