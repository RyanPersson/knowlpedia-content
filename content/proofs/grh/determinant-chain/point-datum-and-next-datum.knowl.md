+++
id = "proofs/grh/determinant-chain/point-datum-and-next-datum"
title = "Point datum and next datum"
kind = "definition"
summary = "The indicator function of the inclusion matrix, and the weight on block upper triangular matrices built from a function on rectangular matrices."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Exchange.pointDatum", "New.Exchange.nextDatum", "New.Exchange.swapFirstTwo", "New.Exchange.sum_nextDatum_mul", "New.Exchange.star_nextDatum"]
lean_files = ["src/New/Determinant/Chain/SquareLaw.lean"]
+++

Let \(R\) be a finite [[?c:Commutative ring|commutative ring]] and \(a,b,n\) finite index sets. For a map \(u\colon m\to n\) of index sets the **inclusion matrix** \(\iota_u\in M_{n\times m}(R)\) has \(j\)-th column the standard basis vector of index \(u(j)\).

The **point datum** is the function \(M_{(a\sqcup b)\times a}(R)\to\mathbb{C}\) that is \(1\) at the inclusion matrix \(\begin{pmatrix}1\\0\end{pmatrix}\) of \(a\) in \(a\sqcup b\) and \(0\) elsewhere.

For a function \(p\colon M_{n\times a}(R)\to\mathbb{C}\) the **next datum** \(p^{+}\colon M_{(n\sqcup b)\times(a\sqcup b)}(R)\to\mathbb{C}\) is
\[
p^{+}\begin{pmatrix}\eta & s\\ C& D\end{pmatrix}=
\begin{cases}
p(-\eta)\,/\,\#M_{n\times b}(R) & \text{if } C=0 \text{ and } D=1,\\
0&\text{otherwise,}
\end{cases}
\]
where \(\eta\in M_{n\times a}(R)\), \(s\in M_{n\times b}(R)\), \(C\in M_{b\times a}(R)\), \(D\in M_{b\times b}(R)\).

## Properties

For every \(F\colon M_{(n\sqcup b)\times(a\sqcup b)}(R)\to\mathbb{C}\),
\[
\sum_{x}p^{+}(x)F(x)=\sum_{s\in M_{n\times b}(R)}\sum_{\eta\in M_{n\times a}(R)}\frac{p(-\eta)}{\#M_{n\times b}(R)}\,F\begin{pmatrix}\eta&s\\0&1\end{pmatrix},
\]
because a matrix is determined by its four blocks and \(p^{+}\) vanishes unless \(C=0\), \(D=1\). Complex conjugation commutes with the construction: \(\overline{p^{+}}=(\overline p)^{+}\).

The block order used with these data is the bijection \(a\sqcup(n\sqcup b)\to n\sqcup(a\sqcup b)\) that exchanges the first two blocks; it is the splitting \(\sigma\) in the [[proofs/grh/determinant-chain/square-law|square law]] of [[proofs/grh/determinant-chain/square-law-for-next-datum|the rule for a square]].

## References

1. Lean: `New.Exchange.pointDatum` in `src/New/Determinant/Chain/SquareLaw.lean`.
2. Lean: `New.Exchange.nextDatum` in `src/New/Determinant/Chain/SquareLaw.lean`.
3. Lean: `New.Exchange.swapFirstTwo` in `src/New/Determinant/Chain/SquareLaw.lean`.
4. Lean: `New.Exchange.sum_nextDatum_mul` in `src/New/Determinant/Chain/SquareLaw.lean`.
5. Lean: `New.Exchange.star_nextDatum` in `src/New/Determinant/Chain/SquareLaw.lean`.
