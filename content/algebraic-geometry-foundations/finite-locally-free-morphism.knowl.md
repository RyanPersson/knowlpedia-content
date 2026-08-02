+++
id = "algebraic-geometry-foundations/finite-locally-free-morphism"
title = "Finite locally free morphism"
kind = "definition"
summary = "A scheme morphism whose direct-image algebra is locally a finite-rank free module."
aliases = ["finite flat morphism of finite presentation", "finite locally free map"]
domains = ["algebraic-geometry-foundations"]
section_mode = "progressive"
+++

A [[algebraic-geometry-foundations/morphism-of-schemes|morphism of schemes]] \(f:X\to S\) is **finite locally free** if every point of \(S\) has an affine neighborhood \(U=\operatorname{Spec}R\) for which
\[
f^{-1}(U)=\operatorname{Spec}A
\]
and \(A\) is a finite free \(R\)-module. Equivalently, \(f\) is
[[algebraic-geometry-foundations/finite-morphism|finite]],
[[algebraic-geometry-foundations/flat-morphism|flat]], and locally of finite
presentation.

## Rank and base change

The module rank defines a locally constant function on \(S\). If the rank is the constant \(d\), one says that \(f\) has degree \(d\). Finite locally free morphisms are preserved by [[algebraic-geometry-foundations/base-change|base change]].

For a finite field extension \(L/k\), the map \(\operatorname{Spec}L\to\operatorname{Spec}k\) is finite locally free of rank \([L:k]\). In particular, \(\operatorname{Spec}\mathbb C\to\operatorname{Spec}\mathbb R\) has rank \(2\); this is the base morphism used in [[algebraic-geometry-foundations/weil-restriction|Weil restriction]] from \(\mathbb C\) to \(\mathbb R\).

## References

1. The Stacks Project Authors, *Morphisms of Schemes*, Lemma 29.48.2 and Section 29.48, “Finite locally free morphisms.” [Stacks Project](https://stacks.math.columbia.edu/tag/02K9).
2. Alexander Grothendieck and Jean Dieudonné, *Éléments de géométrie algébrique IV*, §6.1.
