+++
id = "langlands-letter/knowls/spherical-hecke-algebra-satake"
title = "Spherical Hecke algebra and Satake isomorphism"
kind = "knowl"
summary = "The commutative unramified Hecke algebra and its normalized identification with the representation ring of the dual group."
aliases = ["spherical-hecke-algebra-satake", "Spherical Hecke Algebra and Satake Isomorphism"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/spherical-hecke-algebra-satake.md"
section_mode = "progressive"
+++

Let \(F\) be a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]], let \(G/F\) be
[[algebraic-geometry-foundations/unramified-reductive-group|unramified]],
and let \(K\) be a
[[langlands-letter/knowls/maximal-compact-hyperspecial|hyperspecial
subgroup]]. With [[harmonic-analysis/haar-measure|Haar measure]] normalized by
\(\operatorname{vol}(K)=1\), the **spherical Hecke algebra**

\[
\mathcal H(G(F),K)
=
C_c^\infty(K\backslash G(F)/K)
\]

has [[harmonic-analysis/convolution-on-locally-compact-group|convolution]]
product and unit \(\mathbf 1_K\). It is commutative.

## Split Satake isomorphism

If \(G\) is [[langlands-letter/knowls/split-reductive-group|split]] with
split [[langlands-letter/knowls/maximal-torus-weight-lattice|maximal torus]]
\(T\) and [[lie-groups/weyl-group|Weyl group]] \(W\), the
normalized Satake transform gives

\[
\mathcal H(G(F),K)
\otimes_\mathbb Z\mathbb C
\cong
\mathbb C[X_*(T)]^W
\cong
\mathbb C[X^*(\widehat T)]^W
\cong
R(\widehat G)\otimes_\mathbb Z\mathbb C.
\]

The lattice is \(X_*(T)=X^*(\widehat T)\), not
\(X_*(\widehat T)\). The normalization includes the square root of the
[[harmonic-analysis/parabolic-modulus-character|modulus character]],
equivalently a \(\rho\)-shift.

For an unramified nonsplit group,
[[langlands-letter/knowls/frobenius-unramified|Frobenius]] acts on the
[[langlands-letter/knowls/langlands-dual-group|dual root datum]] and the
invariant algebra is described through the corresponding
[[langlands/l-group|\(L\)-group]] fiber.

## Eigencharacters

If \(\pi\) is an irreducible
[[harmonic-analysis/unramified-representation-p-adic-group|unramified
representation]], then
\(\dim\pi^K=1\). Its Hecke character corresponds under Satake to a
[[langlands/satake-parameter|semisimple Satake parameter]]. Conversely,
that class determines the spherical [[algebra-representation-theory/irreducible-representation|irreducible representation]].

## Integral and normalization issues

The normalized isomorphism can require adjoining \(q^{1/2}\). An
unnormalized Satake transform is defined over a smaller coefficient ring but
shifts the recorded parameter. Arithmetic applications must specify this
choice before comparing
[[langlands-letter/knowls/frobenius-unramified|Galois Frobenius
eigenvalues]].

## Relation to the letter

The letter describes the target as invariants in the
[[algebra-representation-theory/group-algebra|group algebra]] of its
[[langlands-letter/knowls/dual-lattice|dual lattice]]. Modern dual-group
language identifies that invariant algebra with the
[[algebra-representation-theory/representation-ring|representation ring]]
of \(\widehat G\).

## References

1. Ichirō Satake, “Theory of spherical functions on reductive algebraic
   groups over \(p\)-adic fields,” *PMIHÉS* 18 (1963), 5–69.
   [Numdam](https://www.numdam.org/item/PMIHES_1963__18__5_0/).
2. A. Borel, “Automorphic \(L\)-functions,” Proc. Sympos. Pure Math. 33,
   part 2, 1979.
