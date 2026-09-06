+++
id = "algebraic-geometry-foundations/quasi-coherent-sheaf"
title = "Quasi-coherent sheaf"
kind = "definition"
summary = "A sheaf of modules on a scheme that locally comes from a module on each affine chart."
aliases = ["quasicoherent sheaf", "QCoh"]
domains = ["algebraic-geometry-foundations", "langlands"]
prerequisites = ["algebraic-geometry-foundations/scheme", "algebraic-geometry-foundations/sheaf-of-modules"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be a scheme. A **quasi-coherent sheaf** on \(X\) is a sheaf
\(\mathcal F\) of \(\mathcal O_X\)-modules such that on every affine open
\(U=\operatorname{Spec}A\), the restriction \(\mathcal F|_U\) is isomorphic
to the sheaf \(\widetilde M\) associated to an \(A\)-module \(M\).

The category is denoted \(\operatorname{QCoh}(X)\). In derived algebraic
geometry the same notation often denotes a stable derived category rather
than its ordinary abelian heart.

## Examples

The structure sheaf \(\mathcal O_X\), [[fiber-bundles/vector-bundle|vector bundles]], and sheaves associated to
modules on an affine scheme are quasi-coherent. Coherent sheaves impose
additional finiteness conditions; see
[[algebraic-geometry-foundations/coherent-sheaf|coherent sheaf]].

## Geometric-Langlands warning

The early schematic slogan
\[
D\text{-}\operatorname{mod}(\operatorname{Bun}_G)
\simeq
\operatorname{QCoh}(\operatorname{LocSys}_{\widehat G})
\]
is correct for tori after suitable conventions but is too small on the
spectral side for general reductive \(G\). The corrected category uses
[[langlands/ind-coherent-sheaves-with-nilpotent-singular-support|ind-coherent
sheaves with nilpotent singular support]].

## References

1. Alexander Grothendieck, “Éléments de géométrie algébrique I,”
   *Publications Mathématiques de l’IHÉS* 4 (1960).
   [DOI](https://doi.org/10.1007/BF02684778).
