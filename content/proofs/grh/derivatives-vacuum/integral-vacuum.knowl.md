+++
id = "proofs/grh/derivatives-vacuum/integral-vacuum"
title = "The integral vacuum"
kind = "definition"
summary = "The vacuum of a hermitian space of rank n over E multiplied by the n-th power of the vacuum scale, a fixed nonzero number that makes the rank-one vacuum integral with bounded conjugates."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.intVacuum", "New.Parameters.vacuumScale", "New.Parameters.IsVacuumScale", "New.Parameters.isVacuumScale_vacuumScale", "New.Parameters.vacuumBoundConst", "New.Parameters.vacuumScale_ne_zero"]
lean_files = ["src/New/Derivatives/Vacuum/IntegralVacuum.lean"]
+++

Let \(P\) be [[?lean:New.Parameters|parameters]] and \(s\in\mathbb{N}\). By [[proofs/grh/derivatives-vacuum/integral-vacuum-in-rank-one|the integral vacuum in rank one]] fix once and for all

* the **vacuum bound constant** \(C_{\mathrm{vac}}\in\mathbb{N}\) (a constant \(C\) as in that theorem; it depends only on \(P\)), and
* for each \(s\) the **vacuum scale** \(c_{\mathrm{vac}}=c_{\mathrm{vac}}(s)\in\mathbb{C}^\times\): a number \(c\) with properties (a) and (b) of that theorem for the constant \(C_{\mathrm{vac}}\).

For a [[?lean:New.Space|hermitian space]] \(V\) over \(E\) with finite index set \(n\), the **integral vacuum** is
\[ \theta^\circ=\theta^\circ_V=c_{\mathrm{vac}}^{\,\lvert n\rvert}\cdot\mathrm{vac}_V\in\mathcal{S}(V), \]
where \(\mathrm{vac}_V\) is the [[?lean:New.Space.vacElem|vacuum]] of \(V\).

## References

1. Lean: `New.Parameters.intVacuum`, `New.Parameters.vacuumScale`, `New.Parameters.IsVacuumScale`, `New.Parameters.isVacuumScale_vacuumScale`, `New.Parameters.vacuumBoundConst`, `New.Parameters.vacuumScale_ne_zero` in `src/New/Derivatives/Vacuum/IntegralVacuum.lean`.
