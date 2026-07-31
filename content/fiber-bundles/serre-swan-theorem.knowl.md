+++
id = "fiber-bundles/serre-swan-theorem"
title = "Serre–Swan theorem"
kind = "theorem"
summary = "On a finite-dimensional smooth manifold, taking smooth sections gives an equivalence between vector bundles and finitely generated projective modules."
aliases = ["Serre-Swan correspondence", "Serre-Swan duality", "vector bundles versus projective modules", "categorical Serre-Swan equivalence"]
domains = ["fiber-bundles", "algebra-category-theory"]
section_mode = "progressive"
+++

Let \(M\) be a connected finite-dimensional Hausdorff second-countable
[[fiber-bundles/smooth-manifold|smooth manifold]], and let
\(\mathbb F\in\{\mathbb R,\mathbb C\}\). The **smooth Serre–Swan theorem**
states that the functor
\[
E\longmapsto\Gamma^\infty(M,E)
\]
from the
[[fiber-bundles/category-of-vector-bundles-over-a-manifold|fixed-base
category \(\mathbf{Vect}_{\mathbb F}(M)\)]] of finite-rank smooth
[[fiber-bundles/vector-bundle|\(\mathbb F\)-vector bundles]] and bundle maps
covering \(\operatorname{id}_M\) to the
[[algebra-modules/category-of-finitely-generated-projective-modules|category
\(\mathbf{Proj}(C^\infty(M,\mathbb F))\)]] is an
[[algebra-category-theory/equivalence-of-categories|equivalence of
categories]]. Thus every
[[fiber-bundles/section-module-is-finitely-generated-projective|section
module is finitely generated projective]], every such module is the
[[fiber-bundles/module-of-smooth-sections|module of smooth sections]] of a
vector bundle, and module homomorphisms arise uniquely from vector-bundle maps
over \(M\). No compactness hypothesis is needed for this smooth formulation
over the algebra of all smooth functions.

## The two constructions

Finite dimensionality and paracompactness imply that a finite-rank bundle
\(E\) admits a finite-rank complementary bundle \(F\):
\[
E\oplus F\cong M\times\mathbb F^N
\]
for some finite \(N\). Equivalently, finitely many global sections generate
every fiber of \(E\). This uses the finite-dimensional vector-bundle
embedding/global-generator theorem, not a finite trivializing cover.
Taking sections expresses \(\Gamma^\infty(M,E)\) as a direct summand of the
finite-rank free \(C^\infty(M,\mathbb F)\)-module
\(C^\infty(M,\mathbb F)^N\), hence as a finitely generated
[[algebra-modules/projective-module|projective module]].

Conversely, a finitely generated projective module is represented by an idempotent matrix \(p\in M_N(C^\infty(M))\). Evaluating \(p\) pointwise gives a smoothly varying family of projections, whose images form a [[fiber-bundles/vector-subbundle|vector subbundle]] of \(M\times\mathbb F^N\). This [[fiber-bundles/projective-module-bundle-reconstruction|idempotent reconstruction]] is inverse to taking sections up to [[algebra-category-theory/natural-isomorphism|natural isomorphism]] [Swan, §§1–3](https://doi.org/10.1090/S0002-9947-1962-0143225-6).

## Categorical content

The theorem is stronger than a bijection of isomorphism classes. It identifies
morphisms covering \(\operatorname{id}_M\) and their compositions, so direct
sums, direct summands, and isomorphisms agree on the geometric and algebraic
sides. In particular, bundle automorphisms over \(M\) correspond exactly to
invertible \(C^\infty(M)\)-linear endomorphisms of the section module.

This equivalence explains why vector bundles define classes in topological \(K\)-theory and why finitely generated projective modules play the role of vector bundles in noncommutative geometry.

## Classical compact smooth formulation

The theorem is often stated first for a **compact** smooth manifold \(M\):
taking smooth sections gives an equivalence between finite-rank smooth vector
bundles on \(M\) and finitely generated projective
\(C^\infty(M,\mathbb F)\)-modules. Compactness makes the elementary proof
especially direct: choose a finite trivializing cover and a subordinate
partition of unity to construct finitely many global generators.

This familiar compact statement remains part of the theorem; the opening
formulation records its finite-dimensional noncompact extension. On a
noncompact manifold the finite global complement follows from finite covering
dimension and the smooth vector-bundle embedding theorem, rather than from a
finite trivializing cover. Changing the coefficient algebra to functions
vanishing at infinity gives a different version and changes the appropriate
section module.

## Variants and scope

**Warning.** Several results are called the Serre–Swan theorem. For a compact
Hausdorff space \(X\),
[[fiber-bundles/complex-vector-bundle|complex vector bundles]] correspond to
finitely generated projective modules over \(C(X)\). Compactness is essential
to that formulation with the algebra of continuous functions. It is not
required for the displayed smooth theorem over
\(C^\infty(M,\mathbb F)\), whose finite-dimensional manifold hypotheses
supply the needed finite-rank complement.

Connectedness is used only to keep rank constant without extra notation. For
a disconnected finite-dimensional Hausdorff second-countable manifold, the
same equivalence holds between bundles whose componentwise ranks are globally
bounded and finitely generated projective
\(C^\infty(M,\mathbb F)\)-modules. Allowing unbounded ranks across components
produces section modules that need not be finitely generated.

“Serre–Swan duality” is common terminology, but the result is a covariant equivalence produced by the section functor, not a contravariant duality.

There is also a sheaf-level form:
[[fiber-bundles/vector-bundles-and-locally-free-sheaves|taking sections over
all open subsets identifies finite-rank vector bundles with finite-rank
locally free \(C^\infty_M(\mathbb F)\)-module sheaves]]. That sheaf
equivalence records local triviality directly; the global finite-projective
theorem additionally uses the finite-dimensional global-generator result.

## References

1. Richard G. Swan, “Vector Bundles and Projective Modules,” *Transactions of the American Mathematical Society* 105 (1962), 264–277. [DOI record](https://doi.org/10.1090/S0002-9947-1962-0143225-6). Relevant: §§1–3, finite-type bundles, projective section modules, and reconstruction.
2. José M. Gracia-Bondía, Joseph C. Várilly, and Héctor Figueroa, *Elements of Noncommutative Geometry*, Birkhäuser, 2001. [DOI record](https://doi.org/10.1007/978-1-4612-0005-5). Relevant: chapter 2, projective modules as noncommutative vector bundles and the Serre–Swan correspondence.
3. Jet Nestruev, *Smooth Manifolds and Observables*, Springer, 2003. [DOI record](https://doi.org/10.1007/b98871). Relevant: Chapter 11, finite-dimensional manifolds, vector-bundle complements, and projective modules of smooth sections.
