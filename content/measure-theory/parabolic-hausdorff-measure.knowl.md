+++
id = "measure-theory/parabolic-hausdorff-measure"
title = "Parabolic Hausdorff measure"
kind = "definition"
summary = "Hausdorff measure calculated with parabolic space-time scaling."
aliases = []
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/hausdorff-measure", "topology/parabolic-metric"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **parabolic Hausdorff measure** is [[measure-theory/hausdorff-measure|Hausdorff measure]] for the [[topology/parabolic-metric|parabolic metric]]. A common equivalent convention covers \(E\subset\mathbb R^n\times\mathbb R\) by cylinders of spatial radius \(r_j\) and time length \(r_j^2\), and sets
\[
\mathcal P^s(E)=\lim_{\delta\downarrow0}\inf\left\{\sum_jr_j^s:
E\subseteq\bigcup_jQ_{r_j},\ 0<r_j<\delta\right\}.
\]
The cylinder and metric-diameter versions are comparable up to constants and have the same null sets. State the convention if numerical normalization matters.

## Meaning of a null-set conclusion

The condition \(\mathcal P^1(E)=0\) says that arbitrarily fine parabolic covers can have arbitrarily small sum of radii. It does not say that \(E\) is empty. This distinction matters in partial-regularity statements for fluid equations.

## References

- [Lenya Ryzhik, Math 256B lecture notes (2024), §9, parabolic Hausdorff measure](https://virtualmath1.stanford.edu/~ryzhik/notes-256B-24.pdf).

## Fluid regularity

The [[fluid-dynamics/caffarelli-kohn-nirenberg-theorem|Caffarelli–Kohn–Nirenberg theorem]] controls the interior singular set of suitable three-dimensional Navier–Stokes solutions using this measure.
