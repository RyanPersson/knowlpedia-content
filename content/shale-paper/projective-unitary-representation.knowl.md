+++
id = "shale-paper/projective-unitary-representation"
title = "Projective unitary representation in the Shale paper"
kind = "knowl"
summary = "A group action by unitaries defined only up to phase (unitary rays)"
aliases = ["Shale-paper projective unitary representation"]
domains = ["shale-paper"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "shale-paper/projective-unitary-representation.md"
+++

A **projective unitary representation** assigns each \(g\in G\) a **unitary ray**
\(\overline{U}(g)=\{\alpha U(g):|\alpha|=1\}\), with multiplication holding up to a phase (a cocycle).
Equivalently, it is a homomorphism
\[
\overline U:G\longrightarrow PU(H)=U(H)/U(1)
\]
for a complex Hilbert space \(H\). After choosing a unitary representative \(U_g\) of each projective class, there is a function \(\omega:G\times G\to U(1)\) such that
\[
U_gU_h=\omega(g,h)U_{gh}.
\]
Associativity forces the cocycle identity
\[
\omega(g,h)\omega(gh,k)=\omega(h,k)\omega(g,hk).
\]
Changing the representatives \(U_g\) changes \(\omega\) by a coboundary but leaves \(\overline U\) unchanged.

## Remarks

**Key properties (paper use):**
- Shale's implementers \(Y(T)\) are unique only up to phase, so \(\overline{Y}\) is projective.
- In finite dimensions, \(\overline{Y}\) lifts to a genuine double-valued unitary representation (§5).
- More generally, a projective representation lifts to an ordinary unitary representation precisely when its multiplier class is trivial; it may instead lift after passing to a central extension of \(G\).

## Examples

- Spin representations are projective representations of rotation groups and ordinary representations of their double covers.
