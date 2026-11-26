+++
id = "proofs/grh/reduction-zeros/main-theorems"
title = "The five final theorems"
kind = "theorem"
summary = "The Riemann hypothesis and the generalized Riemann hypothesis for Dirichlet L-functions, in five forms, deduced from the half-plane theorem."
aliases = ["Riemann hypothesis and generalized Riemann hypothesis", "final theorems"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["riemannHypothesis", "riemannZeta_eq_zero_re", "LFunction_ne_zero_of_half_lt_re", "LFunction_eq_zero_re", "LFunction_eq_zero_re_of_isPrimitive"]
lean_files = ["src/Main.lean"]
proof_status = "full"
+++

**Theorem.** The following five statements hold.

1. The [[proofs/grh/reduction-zeros/riemann-zeta-zeros-on-line|Riemann hypothesis]], in the form of the Mathlib library.
2. Every zero of the [[?c:Riemann zeta function|Riemann zeta function]] other than \(-2,-4,\dots\) (and other than the point \(1\)) has real part \(\tfrac12\).
3. The [[proofs/grh/reduction-zeros/dirichlet-l-nonvanishing-right-of-half|half-plane form of the generalized Riemann hypothesis]]: \(L(s,\chi)\ne0\) for every [[?c:Dirichlet character|Dirichlet character]] \(\chi\) and every \(s\) with \(\operatorname{Re}s>\tfrac12\), except at \(s=1\) for a principal character, where nothing is stated.
4. The [[proofs/grh/reduction-zeros/dirichlet-l-zeros-on-line|generalized Riemann hypothesis]]: every zero of every Dirichlet \(L\)-function \(L(s,\chi)\) with \(0<\operatorname{Re}s<1\) has real part \(\tfrac12\).
5. The generalized Riemann hypothesis for primitive Dirichlet characters.

## Proof

Statement 3 is the [[?lean:New.grh|half-plane theorem]], the result of the whole argument; it is proved in another chapter, and its last step is the [[proofs/grh/reduction-zeros/one-sided-criterion|one-sided criterion]] of this chapter.

Statement 1 follows from statement 3 by [[proofs/grh/reduction-zeros/zeta-zeros-on-line-from-half-plane|the passage to the critical line for \(\zeta\)]]. Statement 2 is the same proposition as statement 1. Statement 4 follows from statement 3 by [[proofs/grh/reduction-zeros/zeros-on-line-from-half-plane|the passage to the critical line for Dirichlet \(L\)-functions]]. Statement 5 is the special case of statement 4 in which \(\chi\) is primitive. \(\blacksquare\)

## Remarks

The logical order is: one-sided bound for a weighted prime sum (other chapters) \(\Rightarrow\) half-plane theorem (via the one-sided criterion) \(\Rightarrow\) statements 1, 2, 4, 5 (via the functional equation). The source file attributes the proof to Levent Alpöge, with Claude.

## References

1. Lean: `riemannHypothesis`, `riemannZeta_eq_zero_re`, `LFunction_ne_zero_of_half_lt_re`, `LFunction_eq_zero_re`, `LFunction_eq_zero_re_of_isPrimitive` in `src/Main.lean`.
