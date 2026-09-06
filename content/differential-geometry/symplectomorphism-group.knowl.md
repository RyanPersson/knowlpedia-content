+++
id = "differential-geometry/symplectomorphism-group"
title = "Symplectomorphism group"
kind = "definition"
summary = "The group of all self-symplectomorphisms of a fixed symplectic manifold."
aliases = ["group of symplectomorphisms", "Symp(M, omega)", "symplectic diffeomorphism group"]
domains = ["differential-geometry", "algebra-groups"]
prerequisites = ["differential-geometry/symplectic-manifold", "differential-geometry/category-of-symplectic-manifolds", "differential-geometry/symplectic-isotopy", "differential-geometry/hamiltonian-diffeomorphism"]
dependency_review_count = 1
section_mode = "progressive"
+++

For a fixed [[differential-geometry/symplectic-manifold|symplectic manifold]] \((M,\omega)\), its **symplectomorphism group** is
\[
\operatorname{Symp}(M,\omega)
=\{\phi\in\operatorname{Diff}(M):\phi^*\omega=\omega\}.
\]
Composition is the group operation. The inverse of a form-preserving diffeomorphism again preserves the form, so this is the automorphism group of \((M,\omega)\) in the [[differential-geometry/category-of-symplectic-manifolds|maximal symplectic subgroupoid]].

With the \(C^\infty\) topology, the path component of the identity is denoted
\[
\operatorname{Symp}_0(M,\omega).
\]
Its elements are exactly the endpoints of [[differential-geometry/symplectic-isotopy|symplectic isotopies]] beginning at the identity. The [[differential-geometry/hamiltonian-diffeomorphism|Hamiltonian diffeomorphism group]] \(\operatorname{Ham}(M,\omega)\) is a normal subgroup of \(\operatorname{Symp}_0(M,\omega)\), and [[differential-geometry/flux-homomorphism|flux]] measures the difference between these groups on a closed manifold.

## Noncompact manifolds

When \(M\) is noncompact, support conventions are essential. One commonly uses
\[
\operatorname{Symp}_c(M,\omega),
\]
the subgroup of compactly supported symplectomorphisms, and its identity component through compactly supported symplectic isotopies. This need not agree with taking the identity component in the unrestricted group and then intersecting with compactly supported maps. Any notation involving a subscript \(0\) or \(c\) should therefore be read with its path and support convention stated.

## Examples

The linear symplectic group \(\operatorname{Sp}(2n,\mathbb R)\) embeds in \(\operatorname{Symp}(\mathbb R^{2n},\omega_0)\), but the latter also contains nonlinear symplectomorphisms. For a symplectic surface, symplectomorphisms are precisely orientation-preserving diffeomorphisms preserving the area form; preserving orientation alone is weaker.

## References

1. Augustin Banyaga, *The Structure of Classical Diffeomorphism Groups*, Kluwer Academic Publishers, 1997. [DOI record](https://doi.org/10.1007/978-1-4757-0185-3). Relevant: Chapters 7–8, symplectic and Hamiltonian diffeomorphism groups.
2. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: Chapter 10.
