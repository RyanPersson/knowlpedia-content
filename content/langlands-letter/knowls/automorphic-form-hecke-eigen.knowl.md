+++
id = "langlands-letter/knowls/automorphic-form-hecke-eigen"
title = "Automorphic form and Hecke eigenvalues"
kind = "knowl"
summary = "The historical passage from an automorphic form to unramified spherical Hecke eigencharacters and Satake parameters."
aliases = ["automorphic-form-hecke-eigen", "Automorphic Form and Hecke Eigenvalues"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/automorphic-form-hecke-eigen.md"
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/number-field", "algebraic-geometry-foundations/reductive-algebraic-group", "langlands/automorphic-form", "algebra-representation-theory/central-character", "langlands-letter/knowls/maximal-compact-hyperspecial", "algebra-representation-theory/character"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(F\) be a
[[algebra-fields-galois/number-field|number field]] and
\(G\) a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(F\)-group]]. An
[[langlands/automorphic-form|automorphic form]] is a suitably smooth,
finite, moderate-growth function on

\[
G(F)\backslash G(\mathbb A_F),
\]

usually with a prescribed
[[algebra-representation-theory/central-character|central character]]. At
an unramified finite place \(v\), a vector fixed by a
[[langlands-letter/knowls/maximal-compact-hyperspecial|hyperspecial
subgroup]] \(K_v\) is a **spherical Hecke eigenvector** if there is a
[[algebra-representation-theory/character|character]]

\[
\chi_v:\mathcal H(G(F_v),K_v)\longrightarrow\mathbb C
\]

such that \(T\phi=\chi_v(T)\phi\) for every spherical Hecke operator \(T\).

## Modern representation-theoretic formulation

The right translates of an eigenform can generate an
[[langlands/automorphic-representation|automorphic representation]]

\[
\pi\simeq\bigotimes_v'\pi_v.
\]

This is the
[[langlands/restricted-tensor-product-automorphic-representation|restricted
tensor product]] of the local components. For almost every finite \(v\),
\(\pi_v\) is
[[harmonic-analysis/unramified-representation-p-adic-group|unramified]] and
\(\pi_v^{K_v}\) is one-dimensional. The [[harmonic-analysis/hecke-algebra-locally-compact-group-pair|spherical Hecke algebra]] acts on
that line by \(\chi_v\). The
[[langlands-letter/knowls/spherical-hecke-algebra-satake|normalized Satake
isomorphism]] converts
\(\chi_v\) into the [[langlands/satake-parameter|Satake parameter]] of
\(\pi_v\).

## Three objects to distinguish

1. The automorphic form \(\phi\) is a vector in a function space.
2. The automorphic representation \(\pi\) is an irreducible global
   representation generated or detected by such vectors.
3. The Satake parameter is an unramified local
   [[langlands-letter/knowls/semisimple-element-and-class|semisimple]]
   [[algebra-groups/conjugacy-class|conjugacy class]].

A single form can be a simultaneous eigenvector at many places, while the
restricted tensor product records the entire automorphic representation.

## Relation to the letter

The letter moves directly from unramified Hecke eigencharacters to
semisimple dual-group classes. That is the seed of the modern local
parameter language, but it precedes [[langlands/l-packet|\(L\)-packets]],
[[langlands/refined-local-langlands-correspondence|refined local Langlands]],
and the global automorphic-spectrum formalism.

## References

1. A. Borel and H. Jacquet, “Automorphic forms and automorphic
   representations,” Proc. Sympos. Pure Math. 33, part 1, 1979.
2. Ichirō Satake, “Theory of spherical functions on reductive algebraic
   groups over \(p\)-adic fields,” *Publications Mathématiques de l'IHÉS*
   18 (1963), 5–69.
   [Numdam](https://www.numdam.org/item/PMIHES_1963__18__5_0/).
