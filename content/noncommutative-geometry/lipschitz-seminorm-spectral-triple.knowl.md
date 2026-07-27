+++
id = "noncommutative-geometry/lipschitz-seminorm-spectral-triple"
title = "Spectral Lipschitz seminorm"
kind = "definition"
summary = "The extended seminorm that measures an algebra element by the norm of its commutator with a spectral triple's Dirac operator."
aliases = ["commutator Lipschitz seminorm", "Dirac Lipschitz seminorm"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
+++

Let \((\mathcal A,H,D)\) be a [[noncommutative-geometry/spectral-triple|spectral triple]], with \(\mathcal A\) represented on \(H\). Its **spectral Lipschitz seminorm** is
\[
L_D(a)=\lVert[D,a]\rVert,\qquad a\in\mathcal A,
\]
where \([D,a]\) denotes its [[functional-analysis/bounded-commutator|bounded extension]]. On a larger ambient \(C^*\)-algebra one may set \(L_D(a)=+\infty\) when no bounded extension exists. The triangle inequality and Leibniz estimate
\[
L_D(ab)\leq L_D(a)\lVert b\rVert+\lVert a\rVert L_D(b)
\]
make \(L_D\) an extended Leibniz seminorm. It can vanish on nonscalar elements commuting with \(D\), so it need not be a norm modulo the scalars.

## Metric role

The unit ball \(\{a=a^*:L_D(a)\leq1\}\) is the set over which the
[[noncommutative-geometry/connes-distance|Connes spectral distance]] takes its
supremum. Only differences of states are evaluated, so adding a scalar to
\(a\) does not change that distance. If the kernel of \(L_D\) on the
self-adjoint part consists exactly of scalars, the induced quotient seminorm
separates states; additional compactness conditions are needed for its metric
to induce the [[functional-analysis/weak-star-topology|weak-star topology]]
[Rieffel, §§1–2](https://doi.org/10.4171/DM/68).

The seminorm isolates the first-order metric information of a spectral triple.
Summability, grading, real structure, and regularity may affect other parts
of the geometry but are not ingredients in this definition.

## Canonical example

For the canonical spin spectral triple of a closed Riemannian spin manifold
\(M\), Clifford multiplication gives
\[
[\not D,f]=c(df),\qquad
L_{\not D}(f)=\sup_{x\in M}|df_x|.
\]
Thus \(L_{\not D}\) is the classical Lipschitz seminorm on smooth functions,
and its completion recovers ordinary Lipschitz functions. This identity is
the analytic input behind the recovery of Riemannian geodesic distance
[Connes, Chapter VI, §1](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).

A bounded operator commuting with \(D\) has seminorm zero, even when it is not
scalar. Such a [[operator-algebras/commutant|commutant]] element is therefore
a decisive obstruction to
obtaining a genuine metric on all states.

## Conventions and scope

Some authors define \(L_D\) only on the self-adjoint part of a dense
order-unit space; others define it on the complex algebra and restrict only
when constructing a metric. “Lipschitz ball” may mean the unit ball itself,
its image modulo scalars, or a norm-bounded slice. These sets have different
compactness properties.

For a [[noncommutative-geometry/nonunital-spectral-triple|nonunital or locally compact spectral triple]],
the unit ball is usually
too large to be compact without a choice of base state, localization, or
additional properness condition. The formula for \(L_D\) remains meaningful,
but compact quantum metric-space conclusions do not follow automatically.

## References

1. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-hosted text](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Relevant: Chapter VI, §1 on the distance formula and Dirac commutator norm.
2. M. A. Rieffel, “Metrics on State Spaces,” *Documenta Mathematica* 4 (1999), 559–600. [DOI record](https://doi.org/10.4171/DM/68). Relevant: §§1–2 on Lipschitz seminorms, quotient seminorms, and metrics on state spaces.
