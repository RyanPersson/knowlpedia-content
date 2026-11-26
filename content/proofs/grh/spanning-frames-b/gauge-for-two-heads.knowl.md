+++
id = "proofs/grh/spanning-frames-b/gauge-for-two-heads"
title = "A gauge in which two sequences are heads"
kind = "lemma"
summary = "For any two sequences of nonzero complex numbers there is a size L at least rho making both heads, and its powers are paid by the head weights."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Floors.IsCutBessel.exists_gauge_isHead", "New.Floors.IsCutBessel.max_pow_le_mul_max_one_pow", "New.Floors.IsCutBessel.headWeight_succ_of_le", "New.Floors.IsCutBessel.isHead_gauge_iff"]
lean_files = ["src/New/Spanning/Frames/RealShells.lean"]
proof_status = "full"
+++

**Lemma.** In the [[proofs/grh/spanning-frames-b/real-place-setting|notation at a real place]], let \(F\) be a [[proofs/grh/spanning-frames-b/cut-bessel-function-real|cut Bessel function]] of box radius \(\rho\), let \(j,K\ge0\) and let \(p,q\) be sequences of nonzero complex numbers. There is a real number \(L\ge\rho\) such that

1. \(p\) and \(q\) are heads of length \(j\) for the gauge \(\Gamma_L\), that is, \(\lvert p_0\cdots p_{l-1}\rvert^{-1}\le L\) and \(\lvert q_0\cdots q_{l-1}\rvert^{-1}\le L\) for \(l\le j\);
2. for every real \(R\) such that \(\lvert p_0\cdots p_{l-1}\rvert\le R\) and \(\lvert q_0\cdots q_{l-1}\rvert\le R\) for all \(l\le j\),
\[
L^{K}\le\rho^{K}\,\mathrm{w}_{R,K,j}(p)\,\mathrm{w}_{R,K,j}(q).
\]

## Proof

Induction on \(j\). For \(j=0\) take \(L=\rho\): the empty product is \(1\), \(1\le\rho\), and both weights are \(1\).

Let \(L\) serve for \(j\), and put \(x=p_0\cdots p_j\), \(y=q_0\cdots q_j\), \(L'=\max(L,\lvert x\rvert^{-1},\lvert y\rvert^{-1})\). Then \(L'\ge L\ge\rho\) and 1 holds for \(j+1\). For 2, let \(R\) bound the partial products up to length \(j+1\); in particular \(\lvert x\rvert,\lvert y\rvert\le R\), so the weights of length \(j+1\) are those of length \(j\) times \(\max(1,\lvert x\rvert^{-1})^K\), resp. \(\max(1,\lvert y\rvert^{-1})^K\). For real \(\Lambda_0\ge1\) and \(u\ge 0\) one has \(\max(\Lambda_0,u)\le\Lambda_0\max(1,u)\), hence \(\max(\Lambda_0,u)^K\le B\max(1,u)^K\) whenever \(\Lambda_0^K\le B\). Applying this twice (first with \(\Lambda_0=L\ge1\), \(u=\lvert x\rvert^{-1}\), then with \(\Lambda_0=\max(L,\lvert x\rvert^{-1})\), \(u=\lvert y\rvert^{-1}\)) and the induction hypothesis,
\[
L'^{K}\le\rho^{K}\mathrm{w}_{R,K,j}(p)\mathrm{w}_{R,K,j}(q)\max(1,\lvert x\rvert^{-1})^{K}\max(1,\lvert y\rvert^{-1})^{K}=\rho^K\mathrm{w}_{R,K,j+1}(p)\mathrm{w}_{R,K,j+1}(q).
\]

## References

1. Lean: `New.Floors.IsCutBessel.exists_gauge_isHead` in `src/New/Spanning/Frames/RealShells.lean`.
