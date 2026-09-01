+++
id = "fiber-bundles/nonabelian-cech-h1-principal-bundles"
title = "Nonabelian Čech H1 and principal bundles"
kind = "theorem"
summary = "Nonabelian Čech 1-cohomology classifies principal G-bundles as a pointed set."
aliases = ["Čech classification of principal bundles", "nonabelian H1 of a manifold", "principal bundles classified by H1"]
domains = ["fiber-bundles", "topology"]
prerequisites = ["fiber-bundles/principal-g-bundle"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(M\) be a smooth manifold and \(G\) a Lie group. Regard
\(U\mapsto C^\infty(U,G)\) as a sheaf of groups. Then the nonabelian Čech set

\[
\check H^1\!\left(M,C^\infty(-,G)\right)
\]

is naturally identified with the set of isomorphism classes of smooth
[[fiber-bundles/principal-g-bundle|principal \(G\)-bundles]] over \(M\). Its
distinguished point is the class of the trivial bundle \(M\times G\).

## A fixed cover

On an open cover \(\mathcal U=\{U_i\}\), let \(Z^1(\mathcal U,G)\) be the set
of [[fiber-bundles/smooth-g-valued-cech-1-cocycle|smooth \(G\)-valued Čech
\(1\)-cocycles]]. The group of \(0\)-cochains

\[
C^0(\mathcal U,G)=\prod_i C^\infty(U_i,G)
\]

acts by

\[
(h\cdot g)_{ij}=h_i^{-1}g_{ij}h_j.
\]

The orbit set \(Z^1(\mathcal U,G)/C^0(\mathcal U,G)\) classifies principal
\(G\)-bundles equipped with trivializations over that cover. Passing through
common refinements removes the choice of cover and gives the displayed Čech
set.

## Why it is usually not a group

For nonabelian \(G\), multiplying two cocycles componentwise need not produce
a cocycle, so the orbit set has no natural group law in general. It is a
[[shared-foundations/pointed-set|pointed set]], with the trivial cocycle as
basepoint.

The cocycles and \(0\)-cochains retain more structure as a
[[fiber-bundles/cech-cocycle-groupoid|Čech cocycle groupoid]]: cocycles are
objects, and a family \(h_i\) satisfying
\(g'_{ij}=h_i^{-1}g_{ij}h_j\) is a morphism \(g\to g'\). Automorphisms in this
groupoid recover the gauge transformations of the glued bundle.

## The abelian case

If \(G\) is abelian, cocycles and coboundaries form abelian groups, so
\(\check H^1(M,C^\infty(-,G))\) is an abelian group. For \(G=U(1)\), principal
\(U(1)\)-bundles correspond to complex [[fiber-bundles/line-bundle|line
bundles]], the group law is tensor product, and the first
[[fiber-bundles/chern-class|Chern class]] gives, for a smooth manifold,

\[
\{\text{complex line bundles over }M\}/\cong
\;\cong\; H^2(M;\mathbb Z).
\]

## References

1. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: classification by transition functions and classifying spaces.
2. Jean-Luc Brylinski, *Loop Spaces, Characteristic Classes and Geometric Quantization*, Birkhäuser, 1993. [DOI record](https://doi.org/10.1007/978-0-8176-4731-5). Relevant: Čech descriptions of bundles and line bundles.
