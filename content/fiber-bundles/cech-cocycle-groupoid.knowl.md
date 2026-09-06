+++
id = "fiber-bundles/cech-cocycle-groupoid"
title = "Čech cocycle groupoid"
kind = "definition"
summary = "The groupoid whose objects are Čech cocycles and whose morphisms are changes of local trivialization."
aliases = ["cocycle groupoid", "groupoid of Cech cocycles", "descent cocycle groupoid"]
domains = ["fiber-bundles", "category-theory", "topology"]
prerequisites = ["fiber-bundles/smooth-g-valued-cech-1-cocycle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Fix an open cover \(\mathcal U=\{U_i\}\) and a Lie group \(G\). The **Čech
cocycle groupoid** has [[fiber-bundles/smooth-g-valued-cech-1-cocycle|smooth
\(G\)-valued Čech \(1\)-cocycles]] \(g=\{g_{ij}\}\) as objects. A morphism
\(g\to g'\) is a family of smooth maps \(h_i:U_i\to G\) such that

\[
g'_{ij}=h_i^{-1}g_{ij}h_j
\]

on every overlap. Composition is induced by pointwise multiplication of the
families \(\{h_i\}\), with order determined by this convention.

## Why it is a groupoid

Every morphism is invertible because each \(h_i\) is group-valued. Passing to
isomorphism classes gives the [[shared-foundations/pointed-set|pointed set]]
of nonabelian Čech \(H^1\), while retaining the groupoid also retains the
automorphisms of each cocycle. For a cocycle defining a principal bundle,
these automorphisms correspond to its gauge transformations.

## Relation to bundle classification

The gluing construction identifies this groupoid with the groupoid of
principal \(G\)-bundles equipped with trivializations over \(\mathcal U\).
Refining covers gives the cover-independent descent description.

## References

1. Jean-Luc Brylinski, *Loop Spaces, Characteristic Classes and Geometric Quantization*, Birkhäuser, 1993. [DOI record](https://doi.org/10.1007/978-0-8176-4731-5). Relevant: Čech cocycles, descent, and bundle classification.
