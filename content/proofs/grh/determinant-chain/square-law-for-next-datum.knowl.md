+++
id = "proofs/grh/determinant-chain/square-law-for-next-datum"
title = "The rule for a square"
kind = "lemma"
summary = "The square law written out for a weight p on one side and its next datum on the other."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Exchange.SquareLaw.sum_eq_nextDatum"]
lean_files = ["src/New/Determinant/Chain/SquareLaw.lean"]
proof_status = "full"
+++

**Lemma (rule for a square).** Let \(R\) be a finite commutative ring, \(\chi\) a multiplicative character of \(R\), and \(a,b,n\) finite index sets. Let
\[
L\colon M_{(n\sqcup b)\times(n\sqcup a\sqcup b)}(R)\to\mathbb{C},\qquad L'\colon M_{(n\sqcup a\sqcup b)\times a}(R)\to\mathbb{C}
\]
satisfy the [[proofs/grh/determinant-chain/square-law|square law]] with constant \(c\) for \(\chi\) and the splitting of \(n\sqcup a\sqcup b\) into the block \(a\) and the block \(n\sqcup b\) (so the roles of "\(b\)" and "\(a\)" in the definition are played by \(a\) and \(n\sqcup b\)). Let \(\iota_a=\begin{pmatrix}1\\0\end{pmatrix}\in M_{(a\sqcup b)\times a}(R)\) and \(\iota_n=\begin{pmatrix}1\\0\end{pmatrix}\in M_{(n\sqcup b)\times n}(R)\) be the inclusion matrices. Then for every \(p\colon M_{n\times a}(R)\to\mathbb{C}\), with [[proofs/grh/determinant-chain/point-datum-and-next-datum|next datum]] \(p^{+}\),
\[
\#\mathrm{GL}_a(R)\sum_{y\in M_{n\times a}(R)}p(y)\,L'\begin{pmatrix}y\\ \iota_a\end{pmatrix}
\;=\;c\cdot\#\mathrm{GL}_{n\sqcup b}(R)\sum_{x\in M_{(n\sqcup b)\times(a\sqcup b)}(R)}p^{+}(x)\,L\,(\iota_n\ \ x).
\]

## Proof

Fix \(\eta\in M_{n\times a}(R)\) and \(s\in M_{n\times b}(R)\), and let \(w=\begin{pmatrix}\eta\\0\end{pmatrix}\in M_{(n\sqcup b)\times a}(R)\). In the block order \(a,\ n\sqcup b\) the matrix \(\begin{pmatrix}1\\-w\end{pmatrix}\) is, in the order \(n,a,b\) of the rows, the matrix \(\begin{pmatrix}-\eta\\ \iota_a\end{pmatrix}\); and \((w\ \ 1)\) is, in the order \(n,a,b\) of the columns, the matrix \(\left(\iota_n\ \ \begin{pmatrix}\eta&0\\0&1\end{pmatrix}\right)\). Let \(u=\begin{pmatrix}1&s\\0&1\end{pmatrix}\in\mathrm{GL}_{n\sqcup b}(R)\), of determinant \(1\). Then \(u\,\iota_n=\iota_n\) and \(u\begin{pmatrix}\eta&0\\0&1\end{pmatrix}=\begin{pmatrix}\eta&s\\0&1\end{pmatrix}\), so by the first clause of the square law and [[proofs/grh/determinant-chain/square-law-at-a-point|the square law at the point \(w\)]]
\[
\#\mathrm{GL}_a(R)\,L'\begin{pmatrix}-\eta\\ \iota_a\end{pmatrix}
= c\,\#\mathrm{GL}_{n\sqcup b}(R)\,L\left(\iota_n\ \ \begin{pmatrix}\eta&s\\0&1\end{pmatrix}\right)\qquad\text{for all }\eta,s.
\]
Multiply by \(p(-\eta)/\#M_{n\times b}(R)\) and sum over \(\eta\) and \(s\). On the left the summand does not depend on \(s\), so the sum over \(s\) cancels the denominator and, after the substitution \(y=-\eta\), gives the left side of the claim. On the right the sum is \(\sum_x p^{+}(x)L(\iota_n\ x)\) by the summation formula for the next datum. \(\blacksquare\)

## References

1. Lean: `New.Exchange.SquareLaw.sum_eq_nextDatum` in `src/New/Determinant/Chain/SquareLaw.lean`.
