+++
id = "proofs/grh/determinant-chain/fourier-transform-of-next-datum"
title = "Fourier transform of the next datum"
kind = "lemma"
summary = "The Fourier transform of a next datum is supported on block upper triangular matrices, and against a function that transforms by a primitive character of the determinant it may be replaced by the next datum of the Fourier transform, up to a Gauss sum."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Exchange.matrixFourier_nextDatum_fromBlocks", "New.Exchange.exists_sum_matrixFourier_nextDatum_eq"]
lean_files = ["src/New/Determinant/Chain/SquareLaw.lean"]
proof_status = "full"
+++

Let \(R\) be a finite commutative ring and \(\psi\colon R\to\mathbb{C}^\times\) a primitive [[?c:Additive character of a finite ring|additive character]] (a character of the additive group that is nontrivial on every nonzero ideal). The **Fourier transform** of \(f\colon M_{N\times a}(R)\to\mathbb{C}\) is the function on \(M_{a\times N}(R)\)
\[
\widehat f(\rho)=\sum_{v\in M_{N\times a}(R)}f(v)\,\psi(\operatorname{tr}(\rho v)),
\]
without normalising factor. A multiplicative character \(\chi\) of \(R\) is **primitive** if for every \(r\ne0\) there is \(c\in R\) with \(\chi(1+cr)\notin\{0,1\}\).

**Lemma.**

1. For \(p\colon M_{n\times a}(R)\to\mathbb{C}\) with [[proofs/grh/determinant-chain/point-datum-and-next-datum|next datum]] \(p^{+}\) on \(M_{(n\sqcup b)\times(a\sqcup b)}(R)\), and blocks \(A\in M_{a\times n}\), \(B\in M_{a\times b}\), \(C\in M_{b\times n}\), \(D\in M_{b\times b}\),
\[
\widehat{p^{+}}\begin{pmatrix}A&B\\C&D\end{pmatrix}=\begin{cases}\widehat p(-A)\,\psi(\operatorname{tr}D)&C=0,\\0&C\neq0.\end{cases}
\]
2. Let \(\psi\) and \(\chi\) be primitive and \(N,M,T\) finite index sets. There is \(\gamma\in\mathbb{C}\) with \(\lvert\gamma\rvert^2=(\#R)^{\#T(\#T+2\#N)}\) such that for every \(p\colon M_{M\times N}(R)\to\mathbb{C}\) and every \(L\colon M_{(N\sqcup T)\times(N\sqcup M\sqcup T)}(R)\to\mathbb{C}\) with \(L(kx)=\chi(\det k)L(x)\) for all \(k\in\mathrm{GL}_{N\sqcup T}(R)\),
\[
\sum_{x}\widehat{\overline{p^{+}}}(x)\,L(\iota\ \ x)=\gamma\sum_x\big(\widehat{\overline p}\big)^{+}(x)\,L(\iota\ \ x),
\]
the sums over \(x\in M_{(N\sqcup T)\times(M\sqcup T)}(R)\), with \(\iota=\begin{pmatrix}1\\0\end{pmatrix}\in M_{(N\sqcup T)\times N}(R)\).

## Proof

1. By the summation formula for the next datum and \(\operatorname{tr}\left(\begin{pmatrix}A&B\\C&D\end{pmatrix}\begin{pmatrix}\eta&s\\0&1\end{pmatrix}\right)=\operatorname{tr}(A\eta)+\operatorname{tr}(Cs)+\operatorname{tr}D\),
\[
\widehat{p^{+}}\begin{pmatrix}A&B\\C&D\end{pmatrix}=\Big(\sum_\eta p(-\eta)\psi(\operatorname{tr}(A\eta))\Big)\psi(\operatorname{tr}D)\cdot\frac{1}{\#M_{n\times b}(R)}\sum_{s}\psi(\operatorname{tr}(Cs)).
\]
The first factor is \(\widehat p(-A)\) (substitute \(\eta\mapsto-\eta\)). By orthogonality for the primitive character \(\psi\) ([[?lean:New.Exchange.sum_addChar_trace_mul|orthogonality along a matrix]]) the last sum is \(\#M_{n\times b}(R)\) if \(C=0\) and \(0\) otherwise.

2. By the [[?c:Gauss sum|Gauss sum]] identity for \(\chi\circ\det\) ([[?lean:New.Exchange.exists_matrixFourier_eq_mul_inv_det|Fourier transform of a function transforming by a primitive character of the determinant]]) there is \(G\in\mathbb{C}\) with \(\lvert G\rvert^2=(\#R)^{(\#T)^2}\) such that every \(S\colon M_{T\times T}(R)\to\mathbb{C}\) with \(S(gd)=\chi(\det g)S(d)\) for \(g\in\mathrm{GL}_T(R)\) has \(\widehat S(y)=G\,\chi^{-1}(\det y)\,S(1)\). Put \(\gamma=G\cdot\#M_{N\times T}(R)\); since \(\#M_{N\times T}(R)=(\#R)^{\#T\#N}\), \(\lvert\gamma\rvert^2=(\#R)^{(\#T)^2+2\#T\#N}\).

Let \(q=\widehat{\overline p}\) and \(K(\eta,s,d)=L\left(\iota\ \ \begin{pmatrix}\eta&s\\0&d\end{pmatrix}\right)\) for \(\eta\in M_{N\times M}\), \(s\in M_{N\times T}\), \(d\in M_{T\times T}\). For \(g\in\mathrm{GL}_T(R)\) the matrix \(u=\operatorname{diag}(1,g)\in\mathrm{GL}_{N\sqcup T}(R)\) has determinant \(\det g\), fixes \(\iota\), and replaces \(d\) by \(gd\); so \(K(\eta,s,gd)=\chi(\det g)K(\eta,s,d)\), and the Gauss sum identity at \(y=1\) gives \(\sum_dK(\eta,s,d)\psi(\operatorname{tr}d)=G\,K(\eta,s,1)\). Now by part 1 applied to \(\overline p\) (recall \(\overline{p^{+}}=\overline p^{\,+}\)), summing over the four blocks of \(x\) with \(C=0\),
\[
\sum_x\widehat{\overline{p^{+}}}(x)L(\iota\ x)=\sum_s\sum_\eta q(-\eta)\sum_dK(\eta,s,d)\psi(\operatorname{tr}d)=G\sum_s\sum_\eta q(-\eta)K(\eta,s,1),
\]
and the right side is \(G\cdot\#M_{N\times T}(R)\sum_xq^{+}(x)L(\iota\ x)\) by the summation formula for \(q^{+}\). \(\blacksquare\)

## References

1. Lean: `New.Exchange.matrixFourier_nextDatum_fromBlocks` in `src/New/Determinant/Chain/SquareLaw.lean`.
2. Lean: `New.Exchange.exists_sum_matrixFourier_nextDatum_eq` in `src/New/Determinant/Chain/SquareLaw.lean`.
