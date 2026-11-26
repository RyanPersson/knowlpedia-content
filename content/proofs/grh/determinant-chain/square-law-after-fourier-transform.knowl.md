+++
id = "proofs/grh/determinant-chain/square-law-after-fourier-transform"
title = "The square law after Fourier transform"
kind = "lemma"
summary = "For primitive characters, the rule for a square holds between the Fourier transforms of the weights, with a constant of known modulus in place of the group orders."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Exchange.SquareLaw.exists_sum_matrixFourier_eq_sum_nextDatum"]
lean_files = ["src/New/Determinant/Chain/SquareLaw.lean"]
proof_status = "full"
+++

**Lemma.** Let \(R\) be a finite commutative ring, \(\psi\) a primitive additive character and \(\chi\) a primitive multiplicative character of \(R\) (as in [[proofs/grh/determinant-chain/fourier-transform-of-next-datum|Fourier transform of the next datum]]), and \(N,T\) finite index sets. There is \(\gamma\in\mathbb{C}\) with
\[
\lvert\gamma\rvert^{2}\cdot(\#R)^{\#T(\#T+2\#N)}=1
\]
such that the following holds for all \(c\in\mathbb{C}\), all \(p\colon M_{(N\sqcup T)\times N}(R)\to\mathbb{C}\) and all
\[
L\colon M_{(N\sqcup T)\times(N\sqcup(N\sqcup T)\sqcup T)}(R)\to\mathbb{C},\qquad L'\colon M_{(N\sqcup(N\sqcup T)\sqcup T)\times(N\sqcup T)}(R)\to\mathbb{C}
\]
satisfying the [[proofs/grh/determinant-chain/square-law|square law]] with constant \(c\) for \(\chi\) and the splitting of \(N\sqcup(N\sqcup T)\sqcup T\) into the middle block and the two outer blocks: with \(\iota'\) the inclusion matrix of \(N\sqcup T\) in \((N\sqcup T)\sqcup T\) and \(\iota\) that of \(N\) in \(N\sqcup T\),
\[
\sum_{y\in M_{N\times(N\sqcup T)}(R)}\widehat{\overline p}(y)\,L'\begin{pmatrix}y\\ \iota'\end{pmatrix}
=\gamma\,c\sum_{x\in M_{(N\sqcup T)\times((N\sqcup T)\sqcup T)}(R)}\widehat{\overline{p^{+}}}(x)\,L(\iota\ \ x).
\]

## Proof

Apply [[proofs/grh/determinant-chain/square-law-for-next-datum|the rule for a square]] with \(n=N\), \(a=N\sqcup T\), \(b=T\) to the weight \(q=\widehat{\overline p}\). Here \(a\) and \(n\sqcup b\) are both \(N\sqcup T\), so the two group orders agree and cancel (they are nonzero), giving
\[
\sum_yq(y)L'\begin{pmatrix}y\\ \iota'\end{pmatrix}=c\sum_xq^{+}(x)L(\iota\ x).
\]
By part 2 of [[proofs/grh/determinant-chain/fourier-transform-of-next-datum|Fourier transform of the next datum]] (with \(M=N\sqcup T\); its hypothesis on \(L\) is the first clause of the square law) there is \(\gamma_0\) with \(\lvert\gamma_0\rvert^2=(\#R)^{\#T(\#T+2\#N)}>0\) and \(\sum_x\widehat{\overline{p^{+}}}(x)L(\iota\ x)=\gamma_0\sum_xq^{+}(x)L(\iota\ x)\). Take \(\gamma=\gamma_0^{-1}\). \(\blacksquare\)

## References

1. Lean: `New.Exchange.SquareLaw.exists_sum_matrixFourier_eq_sum_nextDatum` in `src/New/Determinant/Chain/SquareLaw.lean`.
