+++
id = "shale-paper/weyl-ccr-quantization"
title = "Weyl CCR Quantization"
kind = "definition"
summary = "A regular unitary representation of the Weyl relations for a real symplectic space."
aliases = ["weyl-ccr-quantization", "Weyl CCR Quantization"]
domains = ["shale-paper"]
prerequisites = ["shale-paper/symplectic-hilbert-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "shale-paper/weyl-ccr-quantization.md"
+++

Let \((K,B)\) be a real [[shale-paper/symplectic-hilbert-space|symplectic
Hilbert space]]. A **Weyl representation** of \((K,B)\) on a complex Hilbert
space \(\mathcal H\) is a map
\[
V:K\longrightarrow U(\mathcal H)
\]
satisfying the **Weyl relations**
\[
V(z_1)V(z_2)=e^{-iB(z_1,z_2)/2}\,V(z_1+z_2).
\]
It is **regular** if, for every \(z\in K\), the one-parameter unitary group
\(t\mapsto V(tz)\) is strongly continuous. A regular Weyl representation is
the exponentiated form of a quantization of the canonical commutation
relations.

## Infinitesimal generators

Regularity is what permits the field operators to be defined. By Stone's
theorem, for each \(z\in K\) there is a unique self-adjoint operator \(R(z)\)
such that
\[
V(tz)=e^{itR(z)}.
\]
In particular \(V(z)=e^{iR(z)}\). The unbounded operators \(R(z)\) need not
share a domain, so the Weyl relations are the domain-free formulation of the
canonical commutation relations.

## Continuity convention

For unitary-valued maps, strong and weak continuity of each one-parameter
subgroup are equivalent. Regularity may equivalently be stated as weak
continuity of \(V\) on every finite-dimensional subspace of \(K\); this implies, and in
this setting is equivalent to, the one-parameter condition above. Compare
[[shale-paper/weak-continuity|weak continuity of a representation]].

## Examples

For the Schrödinger representation on \(L^2(\mathbb R)\), let \(Q\) be
multiplication by \(x\) and let \(P=-i\,d/dx\). With
\[
B\bigl((q,p),(q',p')\bigr)=q p'-p q',
\]
the unitaries
\[
V(q,p)=e^{i(qQ+pP)}
\]
give a regular Weyl representation with the phase convention used above.
