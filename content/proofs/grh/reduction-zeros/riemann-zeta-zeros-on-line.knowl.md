+++
id = "proofs/grh/reduction-zeros/riemann-zeta-zeros-on-line"
title = "The Riemann hypothesis as stated here"
kind = "definition"
summary = "The statement that every zero of the Riemann zeta function other than the trivial zeros has real part 1/2."
aliases = ["Riemann hypothesis", "RiemannZetaZerosOnLine"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["RiemannZetaZerosOnLine"]
lean_files = ["src/Statements.lean"]
+++

The **Riemann hypothesis** is the following statement about the [[?c:Riemann zeta function|Riemann zeta function]] \(\zeta\): for every \(s\in\mathbb{C}\) with \(\zeta(s)=0\), if \(s\) is not one of the trivial zeros \(-2,-4,-6,\dots\) (that is, \(s\ne-2(n+1)\) for all integers \(n\ge0\)) and \(s\neq1\), then
\[
\operatorname{Re}s=\tfrac12 .
\]

## Remarks

* The function \(\zeta\) has a pole at \(1\). The source works with a function defined on all of \(\mathbb{C}\), whose value at \(1\) is a convention; the clause \(s\ne1\) removes that point.
* The statement is word for word the proposition called `RiemannHypothesis` in the Mathlib library; `RiemannZetaZerosOnLine` in `Statements.lean` repeats it.

## References

1. Lean: `RiemannZetaZerosOnLine` in `src/Statements.lean`; `RiemannHypothesis` in Mathlib.
