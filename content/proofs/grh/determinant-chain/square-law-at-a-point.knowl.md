+++
id = "proofs/grh/determinant-chain/square-law-at-a-point"
title = "The square law at a point"
kind = "lemma"
summary = "The square law evaluated on block determinant functions concentrated at one matrix gives an identity between single values."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Exchange.SquareLaw.card_mul_apply_fromRows_eq", "New.Exchange.sum_inv_det_mul_eq_card_mul"]
lean_files = ["src/New/Determinant/Chain/SquareLaw.lean"]
proof_status = "full"
+++

**Lemma.** Let \(R\) be a finite commutative ring, \(\chi\) a multiplicative character of \(R\), \(\sigma\colon b\sqcup a\to n\) a bijection of finite index sets, and let \(L,L'\) satisfy the [[proofs/grh/determinant-chain/square-law|square law]] with constant \(c\) for \(\chi,\sigma\). Use \(\sigma\) to write an \(a\times n\) matrix as \((x_1\ x_2)\) with \(x_1\in M_{a\times b}(R)\), \(x_2\in M_{a\times a}(R)\), and an \(n\times b\) matrix as \(\begin{pmatrix}y_1\\ y_2\end{pmatrix}\) with \(y_1\in M_{b\times b}(R)\), \(y_2\in M_{a\times b}(R)\). Then for every \(w\in M_{a\times b}(R)\)
\[
\#\mathrm{GL}_b(R)\cdot L'\begin{pmatrix}1\\-w\end{pmatrix}\;=\;c\cdot\#\mathrm{GL}_a(R)\cdot L\,(w\ \ 1).
\]

## Proof

Let \(\delta\) be the indicator function of \(w\) on \(M_{a\times b}(R)\), and put
\[
\Phi(x_1\ x_2)=\chi^{-1}(\det x_2)\,\delta(x_2^{-1}x_1),\qquad
\Psi\begin{pmatrix}y_1\\y_2\end{pmatrix}=\chi^{-1}(\det y_1)\,\delta(-y_2y_1^{-1}),
\]
both read as \(0\) when the square block is not invertible (then \(\chi^{-1}\) of the determinant is \(0\)). These block determinant functions are matched for \(\chi,\sigma\) over \(R\) ([[?lean:New.Rows.areMatched_block|block determinant functions are matched]]; the proof is Jacobi's identity for complementary minors). The third clause of the square law gives
\[
\sum_{y_1}\chi^{-1}(\det y_1)\sum_{y_2}\delta(-y_2y_1^{-1})\,L'\begin{pmatrix}y_1\\y_2\end{pmatrix}
= c\sum_{x_2}\chi^{-1}(\det x_2)\sum_{x_1}\delta(x_2^{-1}x_1)\,L(x_1\ x_2).
\]
For invertible \(y_1=g\) the inner sum on the left has the single term \(y_2=-wg\), and \(\begin{pmatrix}g\\-wg\end{pmatrix}=\begin{pmatrix}1\\-w\end{pmatrix}g\), so by clause 2 the inner sum is \(\chi(\det g)\,L'\begin{pmatrix}1\\-w\end{pmatrix}\). Likewise for invertible \(x_2=g\) the inner sum on the right has the single term \(x_1=gw\), and by clause 1 it equals \(\chi(\det g)\,L(w\ 1)\).

Finally, if \(f\colon M_{a\times a}(R)\to\mathbb{C}\) satisfies \(f(g)=\chi(\det g)\,v\) for all invertible \(g\), then \(\sum_u\chi^{-1}(\det u)f(u)=\#\mathrm{GL}_a(R)\cdot v\): non-invertible \(u\) have non-unit determinant, where \(\chi^{-1}\) vanishes, and each invertible \(u\) contributes \(\chi(\det u)^{-1}\chi(\det u)v=v\). Applying this on both sides gives the claim. \(\blacksquare\)

## References

1. Lean: `New.Exchange.SquareLaw.card_mul_apply_fromRows_eq` in `src/New/Determinant/Chain/SquareLaw.lean`.
2. Lean: `New.Exchange.sum_inv_det_mul_eq_card_mul` in `src/New/Determinant/Chain/SquareLaw.lean`.
