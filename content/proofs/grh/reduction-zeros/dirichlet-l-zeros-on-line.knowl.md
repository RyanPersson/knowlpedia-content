+++
id = "proofs/grh/reduction-zeros/dirichlet-l-zeros-on-line"
title = "Critical-line form of the generalized Riemann hypothesis"
kind = "definition"
summary = "The statement that every zero of a Dirichlet L-function in the open critical strip has real part 1/2; also its restriction to primitive characters."
aliases = ["generalized Riemann hypothesis", "GRH", "DirichletLZerosOnLine", "PrimitiveDirichletLZerosOnLine"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["DirichletLZerosOnLine", "PrimitiveDirichletLZerosOnLine"]
lean_files = ["src/Statements.lean"]
+++

The **generalized Riemann hypothesis (critical-line form)** is the following statement: for every integer \(N\ge1\), every [[?c:Dirichlet character|Dirichlet character]] \(\chi\) modulo \(N\) with complex values and every \(s\in\mathbb{C}\) with \(0<\operatorname{Re}s<1\),
\[
L(s,\chi)=0\ \Longrightarrow\ \operatorname{Re}s=\tfrac12 ,
\]
where \(L(s,\chi)\) is the [[?c:Dirichlet L-function|Dirichlet \(L\)-function]] of \(\chi\).

The **generalized Riemann hypothesis for primitive characters** is the same statement restricted to [[?c:primitive Dirichlet character|primitive]] characters \(\chi\).

## Remarks

The first statement includes imprimitive characters; their \(L\)-functions have further zeros on the line \(\operatorname{Re}s=0\), which is why the strip is open. The case \(N=1\) concerns the [[?c:Riemann zeta function|Riemann zeta function]] in the strip.

## References

1. Lean: `DirichletLZerosOnLine`, `PrimitiveDirichletLZerosOnLine` in `src/Statements.lean`.
