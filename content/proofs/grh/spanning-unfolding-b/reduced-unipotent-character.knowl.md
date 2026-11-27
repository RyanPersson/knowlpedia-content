+++
id = "proofs/grh/spanning-unfolding-b/reduced-unipotent-character"
title = "The unipotent character on the residue group and its conjugation mean"
kind = "definition"
summary = "The unipotent character read on reductions of integral unipotent elements and extended by zero, and its mean over conjugates in the residue group."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.reducedChar", "New.Filling.reducedCharMean", "New.Filling.reducedCharMean_conj"]
lean_files = ["src/New/Spanning/Unfolding/Moments.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] with residue group \(\bar G\), lattice stabiliser \(K\), and [[proofs/grh/spanning-unfolding-b/unipotent-character-agreement-stability|unipotent character]] \(\psi_{\mathsf U}\).

* The **reduced character** \(\bar\psi_{\mathsf U}\colon\bar G\to\mathbb{C}\) is defined by \(\bar\psi_{\mathsf U}(s)=\psi_{\mathsf U}(k)\) if \(s=\bar k\) for some \(k\in K\cap\mathsf{U}\) (one such \(k\) being fixed for each \(s\)), and \(\bar\psi_{\mathsf U}(s)=0\) if \(s\) is not the reduction of an integral unipotent element.
* Its **conjugation mean** is
\[
\bar\psi^\natural_{\mathsf U}(s)=\frac1{\lvert\bar G\rvert}\sum_{g\in\bar G}\bar\psi_{\mathsf U}(gsg^{-1}).
\]
It is a class function on \(\bar G\).

## Remarks

The value \(\psi_{\mathsf U}(k)\) does not depend on the choice of \(k\) with \(\bar k=s\): two choices differ by an element of \(K(M)\), on which cosets the character is constant ([[proofs/grh/spanning-unfolding-b/unipotent-character-on-level-cosets|constancy on level cosets]], with \(g=1\)). The Lean definition picks \(k\) by choice and does not need this.

## References

1. Lean: `New.Filling.reducedChar`, `New.Filling.reducedCharMean`, `New.Filling.reducedCharMean_conj` in `src/New/Spanning/Unfolding/Moments.lean`.
