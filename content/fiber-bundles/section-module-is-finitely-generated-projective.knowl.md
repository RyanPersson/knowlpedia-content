+++
id = "fiber-bundles/section-module-is-finitely-generated-projective"
title = "Section module is finitely generated projective"
kind = "theorem"
summary = "The theorem that smooth sections of a finite-rank vector bundle over a finite-dimensional manifold form a finite projective module."
aliases = ["finite projectivity of smooth sections", "Gamma E is projective"]
domains = ["fiber-bundles", "algebra-modules", "differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/vector-bundle", "fiber-bundles/module-of-smooth-sections", "algebra-modules/projective-module", "differential-geometry/algebra-of-smooth-functions"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) be a connected finite-dimensional Hausdorff second-countable smooth
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
No compactness hypothesis is required.

## Proof by a complementary bundle

The finite-dimensional vector-bundle embedding theorem gives a finite-rank
bundle \(F\) and an isomorphism
\[
E\oplus F\cong M\times\mathbb F^N.
\]
Equivalently, the finite-dimensional global-generator theorem produces
finitely many [[fiber-bundles/section-of-a-fiber-bundle|global sections]]
that span every fiber. This conclusion does not require a finite trivializing
cover; it follows from finite covering dimension together with a locally
finite trivialization and a smooth partition of unity. The generators define
a surjective
[[fiber-bundles/vector-bundle-morphism|vector bundle morphism]]
\[
M\times\mathbb F^N\longrightarrow E.
\]
Its kernel is a smooth [[fiber-bundles/vector-subbundle|vector subbundle]].
After choosing a [[fiber-bundles/bundle-metric|bundle metric]], the
[[linear-algebra/orthogonal-complement|orthogonal complement]] maps
isomorphically onto \(E\), recovering the displayed complement. Taking
smooth sections gives
\[
\Gamma(E)\oplus\Gamma(F)\cong C^\infty(M,\mathbb F)^N,
\]
which proves both projectivity and finite generation.

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
bundle, whereas freeness would give a global frame and trivialize the bundle.

For disconnected \(M\), the conclusion remains valid when the ranks of \(E\)
on its connected components are globally bounded. Without that bounded-rank
condition, a componentwise finite-rank bundle can have a section module that
is not finitely generated. If one replaces
\(C^\infty(M,\mathbb F)\) by functions vanishing at infinity, the
appropriate section module and projectivity statement must also be changed;
that is a different Serre–Swan formulation.

## References

1. Richard G. Swan, “Vector Bundles and Projective Modules,” *Transactions of the American Mathematical Society* 105 (1962), 264–277. [DOI record](https://doi.org/10.1090/S0002-9947-1962-0143225-6). Relevant: Theorem 1 and the compact-Hausdorff continuous model for section modules as finite projective modules.
2. Jet Nestruev, *Smooth Manifolds and Observables*, Springer, 2003. [DOI record](https://doi.org/10.1007/b98871). Relevant: Chapter 11, “Vector Bundles and Projective Modules.”
