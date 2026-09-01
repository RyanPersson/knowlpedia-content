+++
id = "fiber-bundles/universal-characteristic-class"
title = "Universal characteristic class"
kind = "definition"
summary = "A cohomology class on a classifying space whose pullbacks assign a natural characteristic class to every principal bundle."
aliases = ["characteristic class on BG", "universal cohomological characteristic class"]
domains = ["fiber-bundles", "topology"]
prerequisites = ["topology/topological-group", "fiber-bundles/classifying-space-bg", "fiber-bundles/classifying-map-of-a-principal-bundle"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a [[topology/topological-group|topological group]], let \(R\) be a coefficient ring, and choose a [[fiber-bundles/classifying-space-bg|classifying space]] \(BG\). A **universal characteristic class of degree \(n\)** is a class
\[
c\in H^n(BG;R).
\]
For a principal \(G\)-bundle \(P\to B\) over a paracompact base and a [[fiber-bundles/classifying-map-of-a-principal-bundle|classifying map]] \(f_P:B\to BG\), its associated characteristic class is
\[
c(P):=f_P^*c\in H^n(B;R).
\]
Because any two classifying maps for \(P\) are homotopic, \(c(P)\) is independent of the choice of \(f_P\).

## Naturality and universality

If \(g:B'\to B\), then
\[
c(g^*P)=g^*c(P),
\]
so a universal class determines a natural [[fiber-bundles/characteristic-class|characteristic class]] of principal \(G\)-bundles. Conversely, in the standard homotopy-theoretic setting, every such cohomological natural assignment is obtained by evaluating it on the universal bundle \(EG\to BG\).

Changing the model of \(BG\) transports \(c\) through a [[topology/homotopy-equivalence|homotopy equivalence]] and therefore does not change the resulting assignment.

## Standard examples

The universal [[fiber-bundles/stiefel-whitney-class|Stiefel–Whitney classes]] lie in \(H^i(BO(n);\mathbb Z/2)\), the universal Chern classes in \(H^{2i}(BU(n);\mathbb Z)\), and the universal Pontryagin classes in \(H^{4i}(BO(n);\mathbb Z)\). Pulling them back along classifying maps gives the corresponding classes of real or [[fiber-bundles/complex-vector-bundle|complex vector bundles]] through their frame bundles.

The phrase “universal Chern class” names one of these specific universal classes; it is an example, not a synonym for an arbitrary class in \(H^*(BG;R)\).

## Scope and conventions

The definition depends on a cohomology theory and coefficients. This knowl uses ordinary singular cohomology, but generalized cohomology theories give analogous universal classes in \(h^n(BG)\). A class for \(G\)-bundles can also be transported along a homomorphism \(H\to G\) by the induced map \(BH\to BG\).

**Warning.** Not every element of \(H^*(B;\!R)\) is a characteristic class of a bundle on \(B\); it must arise by pullback from the fixed universal class. Likewise, [[fiber-bundles/chernweil-form|Chern–Weil forms]] represent certain real universal classes but do not by themselves encode all torsion characteristic classes.

## References

1. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Annals of Mathematics Studies 76, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: Chapter 4, universal bundles and characteristic classes.
2. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: Chapter 14, characteristic classes and universal constructions.
