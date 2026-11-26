+++
id = "proofs/grh/spanning-mainterm/denominator-ideal"
title = "Denominator ideal of an element of a number field"
kind = "definition"
summary = "The ideal of the integers a such that a times nu is an algebraic integer."
aliases = ["denominator", "denominator of a number"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.denominator", "New.mem_denominator", "New.denominator_ne_bot"]
lean_files = ["src/New/Spanning/MainTerm/Frequencies.lean"]
+++

Let \(E\) be a [[algebra-fields-galois/number-field|number field]] with
[[algebra-fields-galois/ring-of-integers|ring of integers]] \(\mathcal O_E\), and let
\(\nu\in E\). The **denominator ideal of \(\nu\)** is

\[
  \mathfrak d(\nu)\;=\;\{\,a\in\mathcal O_E \;:\; a\nu\in\mathcal O_E\,\},
\]

an ideal of \(\mathcal O_E\). It is nonzero: writing \(\nu=a/b\) with \(a,b\in\mathcal O_E\),
\(b\ne0\), one has \(b\in\mathfrak d(\nu)\).

## Remarks

Equivalently \(\mathfrak d(\nu)=\mathcal O_E\cap\nu^{-1}\mathcal O_E\) for \(\nu\neq 0\), and
\(\mathfrak d(\nu)=\mathcal O_E\) exactly when \(\nu\) is an
[[algebra-fields-galois/algebraic-integer|algebraic integer]]. Its
[[algebra-fields-galois/ideal-norm|absolute norm]] \(N\mathfrak d(\nu)\) is the finite part of
the height used in the
[[proofs/grh/spanning-mainterm/sum-of-inverse-cubed-heights|sum over the frequencies]].

## References

1. Lean: `New.denominator`, `New.mem_denominator`, `New.denominator_ne_bot` in
   `src/New/Spanning/MainTerm/Frequencies.lean`.
