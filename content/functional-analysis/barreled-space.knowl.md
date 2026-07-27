+++
id = "functional-analysis/barreled-space"
title = "Barreled space"
kind = "definition"
summary = "A locally convex space in which every closed, convex, balanced, absorbing set is a zero-neighborhood."
aliases = ["barrelled space"]
domains = ["functional-analysis"]
section_mode = "progressive"
+++

Let \(E\) be a Hausdorff [[functional-analysis/locally-convex-space|locally convex space]]. A **barrel** in \(E\) is a closed, [[convex-analysis/convex-set|convex]], [[convex-analysis/balanced-and-absorbing-sets|balanced, and absorbing]] subset of \(E\). The space \(E\) is **barreled** if every barrel is a [[topology/neighborhood|neighborhood]] of \(0\). Thus a set satisfying the algebraic size and symmetry conditions, together with topological closedness, cannot be anomalously thin near the origin. This property is unchanged by the alternative British spelling **barrelled**.

## Equivalent characterizations

A Hausdorff locally convex space \(E\) is barreled exactly when every lower-semicontinuous [[convex-analysis/seminorm|seminorm]] on \(E\) is continuous. It is also equivalent to the following uniform-boundedness formulation: every pointwise bounded subset of the [[functional-analysis/topological-dual|topological dual]] \(E'\) is [[functional-analysis/equicontinuous-family-linear-maps|equicontinuous]]. These equivalences explain why barrels, rather than arbitrary absorbing sets, occur in the definition [Schaefer–Wolff, Chapter III, §4](https://doi.org/10.1007/978-1-4612-1468-7).

## Uniform boundedness and examples

If \(E\) is barreled and \(F\) is locally convex, every [[real-analysis/pointwise-bounded-family|pointwise bounded family]] of [[functional-analysis/continuous-linear-map|continuous linear maps]] from \(E\) to \(F\) is equicontinuous. This is the locally convex Banach–Steinhaus principle. Every [[linear-algebra/banach-space|Banach space]] and every [[functional-analysis/frechet-space|Fréchet space]] is barreled by the [[topology/baire-category-theorem|Baire category theorem]]. [[functional-analysis/inductive-limit-locally-convex-spaces|Locally convex inductive limits]] of barreled spaces, including [[functional-analysis/lf-space|LF-spaces]], are also barreled.

## Conventions and nearby notions

Some authors build Hausdorffness into “locally convex space”; it is stated explicitly here. Requiring only barrels that absorb every bounded subset gives the weaker notion of a quasibarreled or infrabarreled space. Barreledness does not itself imply metrizability, completeness, or bornologicality, although familiar function spaces often possess several of these properties simultaneously.

## References

1. Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces*, 2nd ed., Springer, 1999. [Springer DOI record](https://doi.org/10.1007/978-1-4612-1468-7). Relevant: Chapter III, §4 on barreled spaces and uniform boundedness.
2. Nicolas Bourbaki, *Topological Vector Spaces: Chapters 1–5*, Springer, 2003. [Springer DOI record](https://doi.org/10.1007/978-3-642-61715-7). Relevant: Chapter III on spaces of continuous linear maps and equicontinuity.
