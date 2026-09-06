+++
id = "fiber-bundles/section-of-a-vector-bundle"
title = "Section of a vector bundle"
kind = "definition"
summary = "A smooth choice of one vector in every fiber of a smooth vector bundle."
aliases = ["vector bundle section", "smooth vector bundle section"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/vector-bundle", "fiber-bundles/section-of-a-fiber-bundle", "fiber-bundles/smooth-map", "linear-algebra/vector-space"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\pi:E\to M\) be a smooth [[fiber-bundles/vector-bundle|vector bundle]]. A **section of \(E\)** is a smooth [[fiber-bundles/section-of-a-fiber-bundle|section]] \(s:M\to E\); equivalently,
\[
\pi\circ s=\operatorname{id}_M,
\qquad s(x)\in E_x
\]
for every \(x\in M\). A local section over an open subset \(U\subseteq M\) is defined similarly as a [[fiber-bundles/smooth-map|smooth map]] \(s:U\to E\) with values \(s(x)\in E_x\). Because each fiber is a [[linear-algebra/vector-space|vector space]], sections can be added and multiplied by smooth scalar functions pointwise. The resulting space of global smooth sections is denoted \(\Gamma^\infty(M,E)\), or simply \(\Gamma(E)\).

## Local description

In a [[fiber-bundles/local-trivialization|local trivialization]] \(E|_U\cong U\times\mathbb F^r\), a section is uniquely represented by a smooth map \(U\to\mathbb F^r\), hence by \(r\) smooth component functions. On an overlap, these component functions transform by the bundle [[fiber-bundles/transition-function|transition function]]. This compatibility is what distinguishes a section from an arbitrary collection of fiber vectors.

A section is determined by its restrictions to an [[topology/open-cover|open cover]]. Conversely, local sections that agree on overlaps glue to a unique global section. These facts make sections naturally sheaf-like, although this knowl concerns sections of a bundle rather than the abstract notion of a sheaf section.

## Algebraic structure

If \(s,t\in\Gamma^\infty(M,E)\) and \(f\in C^\infty(M)\), then
\[
(s+t)(x)=s(x)+t(x),
\qquad
(fs)(x)=f(x)s(x).
\]
Thus \(\Gamma^\infty(M,E)\) is a module over the [[differential-geometry/algebra-of-smooth-functions|algebra of smooth functions]]. [[fiber-bundles/bundle-morphism|Bundle morphisms]] over \(M\) induce [[algebra-modules/module-homomorphism|module homomorphisms]] on sections by pointwise composition.

## Examples

Sections of the [[fiber-bundles/tangent-bundle|tangent bundle]] are smooth [[fiber-bundles/vector-field|vector fields]], while sections of the [[fiber-bundles/cotangent-bundle|cotangent bundle]] are smooth one-forms. Every vector bundle has the [[fiber-bundles/zero-section|zero section]], so—unlike a general fiber bundle—the existence of a global section does not imply triviality. A rank-\(r\) vector bundle is trivial precisely when it admits \(r\) global sections that form a basis in every fiber.

## References

1. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 10, vector bundles and local frames.
2. L. W. Tu, *Differential Geometry: Connections, Curvature, and Characteristic Classes*, Springer, 2017. [DOI record](https://doi.org/10.1007/978-3-319-55092-8). Relevant: Chapter 1, vector bundles and sections.
