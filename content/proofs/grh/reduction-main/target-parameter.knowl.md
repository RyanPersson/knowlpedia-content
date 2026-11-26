+++
id = "proofs/grh/reduction-main/target-parameter"
title = "The row parameter at an infinite place"
kind = "definition"
summary = "The integer sequence (k/2 - 1, k/2 - 2, ..., 1 - k/2; Delta/2 - kappa_1, Delta/2 - kappa_2, ...) from which the Harish-Chandra parameters of the unitary groups in the chain are read off."
aliases = ["targetParameter", "row parameter"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.targetParameter", "New.Data.targetParameter_eq"]
lean_files = ["src/New/Reduction/Data/LevelAndTwists.lean"]
+++

Let \(D\) be [[proofs/grh/reduction-main/data|data]] with source rank \(k\) (even), half gap \(\Delta/2\) and shifted weights \(\kappa^{(i)}\), lift weights \(\kappa_j\) ([[proofs/grh/reduction-main/data-derived-quantities|derived quantities]]). The **row parameter** at an infinite place \(v\) of \(E\) is the sequence of integers \(\lambda_v(i)\), \(i=0,1,2,\dots\):
\[
\lambda_v(i)=\begin{cases}\dfrac k2-1-i,& i<k-1,\\[2mm]-\kappa^{(2(i+1-k)+1)}(v)=\dfrac\Delta2-\kappa_{\,i+2-k}(v),& i\ge k-1.\end{cases}
\]
So the first \(k-1\) entries are \(\tfrac k2-1,\dots,1-\tfrac k2\), followed by \(-\kappa_{1/2},-\kappa_{3/2},\dots\) with \(\kappa_{u}=\kappa+(u+\tfrac12)\Delta\). The equality of the two expressions in the second case is the identity \(\kappa+(2(i+1-k)+2)\tfrac\Delta2=\kappa_{i+2-k}-\tfrac\Delta2\). The parameter is not doubled.

## References

1. Lean: `New.Data.targetParameter`, `New.Data.targetParameter_eq` in `src/New/Reduction/Data/LevelAndTwists.lean`.
