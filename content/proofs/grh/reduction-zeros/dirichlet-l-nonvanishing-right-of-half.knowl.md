+++
id = "proofs/grh/reduction-zeros/dirichlet-l-nonvanishing-right-of-half"
title = "Half-plane form of the generalized Riemann hypothesis"
kind = "definition"
summary = "The statement that no Dirichlet L-function vanishes at a point of real part greater than 1/2, the pole of a principal character excepted."
aliases = ["half-plane form of GRH", "DirichletLNonvanishingRightOfHalf"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["DirichletLNonvanishingRightOfHalf"]
lean_files = ["src/Statements.lean"]
+++

The **half-plane form of the generalized Riemann hypothesis** is the following statement: for every integer \(N\ge 1\), every [[?c:Dirichlet character|Dirichlet character]] \(\chi\) modulo \(N\) with complex values, and every \(s\in\mathbb{C}\) with \(\operatorname{Re}s>\tfrac12\) such that \(\chi\) is not [[?c:principal Dirichlet character|principal]] or \(s\neq 1\),
\[
L(s,\chi)\neq 0 ,
\]
where \(L(s,\chi)\) is the [[?c:Dirichlet L-function|Dirichlet \(L\)-function]] of \(\chi\).

## Remarks

* The character need not be [[?c:primitive Dirichlet character|primitive]]. Here \(L(s,\chi)\) is the [[complex-analysis/analytic-continuation|analytic continuation]] of \(\sum_{n\ge1}\chi(n)n^{-s}\); it is entire if \(\chi\) is not principal and has a simple pole at \(s=1\) (and no other pole) if \(\chi\) is principal. At that pole nothing is asserted.
* For \(N=1\) the only character is the principal one and \(L(s,\chi)\) is the [[?c:Riemann zeta function|Riemann zeta function]].
* This statement is proved as `New.grh`; see [[?lean:New.grh|the half-plane theorem]]. The other forms of the hypothesis follow from it by [[proofs/grh/reduction-zeros/zeros-on-line-from-half-plane|the reflection \(s\mapsto 1-s\)]].

## References

1. Lean: `DirichletLNonvanishingRightOfHalf` in `src/Statements.lean`.
