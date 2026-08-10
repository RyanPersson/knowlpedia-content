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

Let \(F\) be nonarchimedean, let \(G/F\) be unramified, and let \(K\) be a
hyperspecial subgroup. With [[harmonic-analysis/haar-measure|Haar measure]] normalized by
\(\operatorname{vol}(K)=1\), the **spherical Hecke algebra**

\[
\mathcal H(G(F),K)
=
C_c^\infty(K\backslash G(F)/K)
\]

has convolution product and unit \(\mathbf 1_K\). It is commutative.

## Split Satake isomorphism

If \(G\) is split with split maximal torus \(T\) and [[lie-groups/weyl-group|Weyl group]] \(W\), the
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
modulus character, equivalently a \(\rho\)-shift.

For an unramified nonsplit group, Frobenius acts on the dual root datum and
the invariant algebra is described through the corresponding \(L\)-group
fiber.

## Eigencharacters

If \(\pi\) is an irreducible unramified representation, then
\(\dim\pi^K=1\). Its Hecke character corresponds under Satake to a
[[langlands/satake-parameter|semisimple Satake parameter]]. Conversely,
that class determines the spherical [[algebra-representation-theory/irreducible-representation|irreducible representation]].

## Integral and normalization issues

The normalized isomorphism can require adjoining \(q^{1/2}\). An
unnormalized Satake transform is defined over a smaller coefficient ring but
shifts the recorded parameter. Arithmetic applications must specify this
choice before comparing Galois Frobenius eigenvalues.

## Relation to the letter

The letter describes the target as invariants in the group algebra of its
[[langlands-letter/knowls/dual-lattice|dual lattice]]. Modern dual-group language identifies that invariant algebra
with the representation ring of \(\widehat G\).

## References

1. Ichirō Satake, “Theory of spherical functions on reductive algebraic
   groups over \(p\)-adic fields,” *PMIHÉS* 18 (1963), 5–69.
   [Numdam](https://www.numdam.org/item/PMIHES_1963__18__5_0/).
2. A. Borel, “Automorphic \(L\)-functions,” Proc. Sympos. Pure Math. 33,
   part 2, 1979.
