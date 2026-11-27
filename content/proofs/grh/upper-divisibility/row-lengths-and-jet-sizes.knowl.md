+++
id = "proofs/grh/upper-divisibility/row-lengths-and-jet-sizes"
title = "Row lengths of the lift diagrams and growth of the jet size"
kind = "lemma"
summary = "Each row of the Young diagram of a lift is at most its main length plus an explicit slack; adding e boxes to a row of length r raises the jet size by at most e(log(r+e+1) + log(M/Omega)); the conjugates of the level element have squared absolute value M."
aliases = ["row main length", "row slack"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.rowMainLength", "New.Data.rowSlack", "New.Data.diagramWeight_le_rowMainLength_add_rowSlack", "New.Data.jetSize_le_add", "New.Data.norm_map_star_piMBar_sq"]
lean_files = ["src/New/UpperBound/Size/Estimates.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]]. For an infinite place \(\tau\) and a row index \(i\ge0\) define the **main length** and the **slack** of row \(i\):
\[
\operatorname{main}(\tau,i)=\begin{cases}c(\tau,1)&i=0\\ w(\tau)&0<i<k\\ 0&i\ge k,\end{cases}\qquad
\operatorname{slack}(i)=\begin{cases}b+\lfloor a/\lfloor x_1\rfloor\rfloor+(\Delta/2)^2&i=0\\ (\Delta/2)^2&i>0,\end{cases}
\]
where \(c(\tau,h)\) is the [[?lean:New.Data.columnCount|number of columns of height \(h\)]] of the weight at \(\tau\) (so \(c(\tau,1)=a\) at an a-place and \(0\) elsewhere), \(w\) is the [[?lean:New.Data.weight|weight]] and \(\Delta/2=r^{8}\) is half the gap.

**Lemma.**

1. Let \(j<m\) and let \(\lambda\) be the Young diagram at \(\tau\) with \(c(\tau,h)\) columns of height \(h\) for each \(h<n_{j+1}\). Then row \(i\) of \(\lambda\) has length at most \(\operatorname{main}(\tau,i)+\operatorname{slack}(i)\).
2. Let \(s_\infty(l)=\log l!+l\log(M/\Omega)\) be the [[?lean:New.Data.jetSize|jet size]]. If \(l\le r'+e\) then \(s_\infty(l)\le s_\infty(r')+e\bigl(\log(r'+e+1)+\log(M/\Omega)\bigr)\).
3. Let \(\bar\pi_M\) be the [[?lean:New.Data.piMBar|integer of \(K\) of norm \(M\)]] of the data, \(K\subset\mathbb{C}\). For every automorphism \(\sigma\) of \(\mathbb{C}\), \(\lvert\sigma(\overline{\bar\pi_M})\rvert^{2}=M\).

## Proof

(1) By [[?lean:New.Data.liftDiagram_le|`liftDiagram_le`]] (quoted) row \(i\) has length at most \(c(\tau,1)+\kappa_{j+1}(\tau)\) for \(i=0\), at most \(\kappa_{j+1}(\tau)\) for \(0<i<k\), and at most \(m\Delta\) otherwise, where \(\kappa_{j+1}(\tau)\le w(\tau)+m\Delta+\Delta/2\) is the lift weight. Moreover \(w(\tau)\le b+\lfloor a/\lfloor x_1\rfloor\rfloor\) and \(m\Delta+\Delta/2\le(\Delta/2)^2\) (a size comparison of the data). The three cases follow by linear arithmetic.

(2) \(l!\le(r'+e)!=r'!\,(r'+1)\cdots(r'+e)\le r'!\,(r'+e+1)^{e}\), and \(l\log(M/\Omega)\le(r'+e)\log(M/\Omega)\) because \(M\ge\Omega\).

(3) The map \(z\mapsto\sigma(\bar z)\) is an embedding \(\iota\) of \(K\) in \(\mathbb{C}\), and complex conjugation of \(\mathbb{C}\) commutes with every embedding of the imaginary quadratic field \(K\), so \(\lvert\iota(\bar z)\rvert=\lvert\iota(z)\rvert\). Hence \(\lvert\iota(\bar\pi_M)\rvert^2=\lvert\iota(\bar\pi_M\overline{\bar\pi_M})\rvert=M\). \(\blacksquare\)

*Status.* In (1) the bound for the rows by the lift weights and the two numerical comparisons are quoted.

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Size/Estimates.lean`.
