+++
id = "fiber-bundles/section-module-is-finitely-generated-projective"
title = "Section module is finitely generated projective"
kind = "definition"
summary = "The theorem that smooth sections of a finite-rank vector bundle over a compact manifold form a finite projective module."
aliases = ["finite projectivity of smooth sections", "Gamma E is projective"]
domains = ["fiber-bundles", "algebra-modules", "differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be a compact smooth
[[fiber-bundles/smooth-manifold|manifold]], let
\(\mathbb F\in\{\mathbb R,\mathbb C\}\), and let \(E\to M\) be a smooth
finite-rank \(\mathbb F\)-[[fiber-bundles/vector-bundle|vector bundle]]. The
**finite-projectivity theorem for the section module** states that the
[[fiber-bundles/module-of-smooth-sections|module of smooth sections]]
\(\Gamma^\infty(M,E)\) is a finitely generated
[[algebra-modules/projective-module|projective module]] over
[[differential-geometry/algebra-of-smooth-functions|\(C^\infty(M,\mathbb F)\)]]. Equivalently, there are an integer \(N\), another
\(C^\infty(M,\mathbb F)\)-module \(Q\), and an isomorphism
\[
\Gamma^\infty(M,E)\oplus Q\cong C^\infty(M,\mathbb F)^N.
\]
Compactness guarantees the finite global construction used below.

## Proof by a complementary bundle

A finite trivializing cover and a subordinate smooth partition of unity
produce finitely many [[fiber-bundles/section-of-a-fiber-bundle|global sections]] that span every fiber. They define a
surjective
[[fiber-bundles/vector-bundle-morphism|vector bundle morphism]]
\[
M\times\mathbb F^N\longrightarrow E.
\]
After choosing a [[fiber-bundles/bundle-metric|bundle metric]], its kernel is
a smooth [[fiber-bundles/vector-subbundle|vector subbundle]] and the
[[linear-algebra/orthogonal-complement|orthogonal complement]] maps isomorphically onto \(E\). Thus there is a vector
bundle \(F\) with
\[
E\oplus F\cong M\times\mathbb F^N.
\]
Taking smooth sections gives
\[
\Gamma(E)\oplus\Gamma(F)\cong C^\infty(M,\mathbb F)^N,
\]
which proves both projectivity and finite generation
[Nestruev, Chapter 11](https://doi.org/10.1007/b98871).

## Idempotent form

The splitting determines a smooth idempotent matrix
\[
p\in M_N(C^\infty(M,\mathbb F)),
\qquad p^2=p,
\]
such that
\[
\Gamma^\infty(M,E)\cong p\,C^\infty(M,\mathbb F)^N.
\]
Conversely, the pointwise images of such an idempotent form a smooth bundle;
this is the
[[fiber-bundles/serre-swan-idempotent-construction|Serre–Swan idempotent construction]]. The theorem in the core is therefore one direction of the
smooth Serre–Swan equivalence.

## Examples and scope

For the trivial rank-\(r\) bundle,
\(\Gamma^\infty(M,M\times\mathbb F^r)\cong
C^\infty(M,\mathbb F)^r\), which is free. The Möbius
[[fiber-bundles/line-bundle|line bundle]] over \(S^1\) gives a projective
module that is not free: projectivity records the existence of a complementary
bundle, whereas freeness would give a global frame and trivialize the bundle
[Nestruev, Chapter 11](https://doi.org/10.1007/b98871).

The compact hypothesis makes the finite-cover proof immediate. Extensions to
noncompact finite-dimensional manifolds use finite-covering-dimension or
bundle-embedding results instead. If one replaces \(C^\infty(M)\) by functions
vanishing at infinity, the appropriate section module and projectivity
statement must also be changed; this is a different Serre–Swan formulation
[Nestruev, Chapter 11](https://doi.org/10.1007/b98871).

## References

1. Richard G. Swan, “Vector Bundles and Projective Modules,” *Transactions of the American Mathematical Society* 105 (1962), 264–277. [DOI record](https://doi.org/10.1090/S0002-9947-1962-0143225-6). Relevant: Theorem 1 and the compact-Hausdorff continuous model for section modules as finite projective modules.
2. Jet Nestruev, *Smooth Manifolds and Observables*, Springer, 2003. [DOI record](https://doi.org/10.1007/b98871). Relevant: Chapter 11, “Vector Bundles and Projective Modules.”
