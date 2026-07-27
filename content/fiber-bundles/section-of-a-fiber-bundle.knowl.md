+++
id = "fiber-bundles/section-of-a-fiber-bundle"
title = "Section of a fiber bundle"
kind = "definition"
summary = "A smooth right inverse to a fiber-bundle projection, selecting one point in every fiber."
aliases = ["smooth section", "global section", "cross-section", "section of a smooth fiber bundle", "bundle section"]
domains = ["fiber-bundles"]
section_mode = "progressive"
+++

Let \(\pi:E\to M\) be a [[fiber-bundles/smooth-fiber-bundle|smooth fiber bundle]]. A **smooth global section** of \(\pi\) is a [[fiber-bundles/smooth-map|smooth map]] \(s:M\to E\) satisfying
\[
\pi\circ s=\operatorname{id}_M.
\]
Equivalently, \(s(x)\in E_x=\pi^{-1}(x)\) for every \(x\), and this choice varies smoothly with \(x\). A **local section over** an open set \(U\subseteq M\) is a smooth map \(s:U\to E\) with \(\pi\circ s=\operatorname{id}_U\). A fiber bundle always has local sections near each base point, but it need not have a global section.

## Local description and constructions

Under a local trivialization \(\Phi:\pi^{-1}(U)\to U\times F\), every local section has the form
\[
\Phi(s(x))=(x,f(x))
\]
for a smooth map \(f:U\to F\), and every such \(f\) defines a local section. Local representatives on overlaps satisfy the transition-function rule for the bundle.

Sections pull back along smooth maps: if \(f:N\to M\), then \(x\mapsto(x,s(f(x)))\) is a section of the [[fiber-bundles/pullback-bundle|pullback bundle]] \(f^*E\to N\).

## Examples and obstructions

For the product bundle \(M\times F\to M\), every smooth map \(f:M\to F\) gives the section \(x\mapsto(x,f(x))\).

For a vector bundle, the zero vector in each fiber defines a canonical global section. Sections of the [[fiber-bundles/tangent-bundle|tangent bundle]] are vector fields.

A principal bundle admits a global section exactly when it is trivial, as expressed by the [[fiber-bundles/trivial-principal-bundle-criterion-global-section-principal-bundle-is-trivial|global-section triviality theorem]] and its converse. The Hopf principal circle bundle is a standard bundle with no global section.

## Conventions and scope

“Section” and “cross-section” are synonymous here. The adjective “global” distinguishes a section on all of \(M\) from one defined only on an open subset.

**Warning.** A set-theoretic choice of one point per fiber is not a smooth section unless the resulting map is smooth. A section of a sheaf is a different categorical notion, although bundles and sheaves of their sections are closely related.

## References

1. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: chapter 10, smooth bundles and sections.
2. D. Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-4008-0). Relevant: chapters 1–2, bundle maps, local triviality, and sections.
