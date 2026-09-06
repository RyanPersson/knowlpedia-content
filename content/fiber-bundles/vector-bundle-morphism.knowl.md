+++
id = "fiber-bundles/vector-bundle-morphism"
title = "Vector bundle morphism"
kind = "definition"
summary = "A smooth map between total spaces of vector bundles that covers a base map and is linear on each fiber."
aliases = ["fiberwise linear bundle map"]
domains = ["fiber-bundles", "category-theory"]
prerequisites = ["fiber-bundles/complex-vector-bundle", "fiber-bundles/smooth-map"]
dependency_review_count = 1
section_mode = "progressive"
legacy_source_path = "fiber-bundles/vector-bundle-morphism.md"
+++

Let \(\pi_E:E\to M\) and \(\pi_F:F\to N\) be smooth real or [[fiber-bundles/complex-vector-bundle|complex vector bundles]]. A **vector bundle morphism** (also called a *fiberwise linear bundle map*) from \(E\) to \(F\) is a pair \((\Phi,f)\) consisting of a [[fiber-bundles/smooth-map|smooth map]] \(\Phi:E\to F\) and a smooth map \(f:M\to N\) such that:

1. **Covers the base map:** \(\pi_F\circ \Phi = f\circ \pi_E\).

2. **Fiberwise linearity:** for every \(x\in M\), the induced map on fibers
   \[
   \Phi_x:E_x\to F_{f(x)},\qquad \Phi_x(v):=\Phi(v),
   \]
   is \(\mathbb F\)-linear (with \(\mathbb F=\mathbb R\) or \(\mathbb C\) according to the bundles).

If \(M=N\) and \(f=\mathrm{id}_M\), one often says \(\Phi:E\to F\) is a *bundle map over \(M\)*.

Composition of vector bundle morphisms is defined by composition of the total-space maps and the base maps, and yields a category of smooth vector bundles and bundle morphisms.

## Fixed-base and varying-base categories

There are two useful categorical conventions.

- In the [[fiber-bundles/category-of-vector-bundles-over-a-manifold|
  fixed-base category]] \(\mathbf{Vect}_{\mathbb F}(M)\), every object lies
  over one chosen \(M\), and every morphism covers
  \(\operatorname{id}_M\).
- In the varying-base category, objects may lie over different manifolds and
  \((\Phi,f):E\to F\) may cover an arbitrary smooth map \(f:M\to N\).

Only the first convention sends sections covariantly by simple
postcomposition:
\[
s\longmapsto\Phi\circ s.
\]
When \(f\ne\operatorname{id}_M\), \(\Phi\circ s\) lies over \(f\), rather than
being a section of \(F\to N\). A common alternative is to express a
varying-base map as a bundle map \(E\to f^*F\) over \(M\).

## Examples
1. **Differential of a smooth map.** For any smooth map \(f:M\to N\), the differential
   \[
   df:TM\to TN
   \]
   is a vector bundle morphism covering \(f\) between the [[fiber-bundles/tangent-bundle|tangent bundles]].

2. **Projection from a direct sum.** For bundles \(E,F\to M\), the projection \(\mathrm{pr}_E:E\oplus F\to E\) is a bundle morphism over \(\mathrm{id}_M\), fiberwise the linear projection \(E_x\oplus F_x\to E_x\).

3. **Inclusion of a subbundle.** If \(E\subseteq F\) is a [[fiber-bundles/vector-subbundle|smooth vector subbundle]] over the same base \(M\), then the inclusion map \(E\hookrightarrow F\) is a vector bundle morphism over \(\mathrm{id}_M\).

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: smooth vector bundles and bundle homomorphisms.
2. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: bundle maps and pullback bundles.
