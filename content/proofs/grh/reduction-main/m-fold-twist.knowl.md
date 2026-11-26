+++
id = "proofs/grh/reduction-main/m-fold-twist"
title = "m-fold twist"
kind = "definition"
summary = "A twist whose tame part has nontrivial n-th power at every place of its modulus for all n from 1 to m, so that its first m powers are twists."
aliases = ["MFoldTwist", "m-fold twists"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.MFoldTwist", "New.Data.MFoldTwist.powTwist", "New.Data.MFoldTwist.toTwist_one", "New.Data.toAutChar_one_and_toTwist_one_and_Q_one"]
lean_files = ["src/New/Reduction/Data/LevelAndTwists.lean", "src/New/Determinant/Twist/FitTwists.lean"]
+++

Let \(D\) be [[proofs/grh/reduction-main/data|data]] with number of lifts \(m\). An **\(m\)-fold twist** is a [[proofs/grh/reduction-main/twist|twist]] \(\vartheta\), with modulus \(Q\) and tame part \(\psi\), such that
\[
\psi_w^{\,n}\ne1\qquad\text{for all } w\in Q\ \text{and all } 1\le n\le m .
\]
Then for \(1\le n\le m\) the power \(\vartheta^n\) is a twist. The trivial twist is an \(m\)-fold twist (its modulus is empty). In a chain of lifts, lift \(j\) uses the power \(\vartheta^j\).

## References

1. Lean: `New.Data.MFoldTwist`, `New.Data.MFoldTwist.powTwist` in `src/New/Reduction/Data/LevelAndTwists.lean`; `New.Data.MFoldTwist.toTwist_one` in `src/New/Determinant/Twist/FitTwists.lean`.
