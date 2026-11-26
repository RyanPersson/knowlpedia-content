+++
id = "proofs/grh/upper-divisibility/mark-operator"
title = "Elementary divisors of the scaled Hecke operator at a marked prime"
kind = "theorem"
summary = "The scaled Hecke operator at a marked prime preserves the integral source forms and is onto modulo p^j up to colength at most (12 A_l/(m p) + j/(m^2 f)) times the dimension."
aliases = ["mark operator"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsMarked.isOntoUpToColength_scaledHeckeOperator", "New.Data.isLargeDegree_of_le_card", "New.Data.three_mul_divisorConstant_le"]
lean_files = ["src/New/UpperBound/Divisibility/MarkOperator.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]], \(p\) a prime, \(\iota\colon\mathbb{C}\to\mathbb{C}_p\), \(\Lambda\) a [[proofs/grh/upper-divisibility/marked-set-of-primes|marked set]], \(\mathfrak l\in\Lambda\) and \(j_0\in\mathbb{N}\). Let \(\widetilde T_{\mathfrak l}=p^{A_{\mathfrak l}}T_{\mathfrak l,\mathfrak r}\) be the [[proofs/grh/upper-divisibility/scaled-hecke-operator|scaled Hecke operator]] and \(\mathcal M\) the module of integral source forms over \(O_\iota\). Then \(\widetilde T_{\mathfrak l}\mathcal M\subset\mathcal M\), and there is a natural number
\[
e\le\Bigl(\frac{12A_{\mathfrak l}}{mp}+\frac{j_0}{m^{2}f}\Bigr)\dim_{\mathbb{C}}\mathcal S
\]
such that every finite family in \(\mathcal M\) is carried into \(\widetilde T_{\mathfrak l}\mathcal M+p^{j_0}\mathcal M\) by a square matrix over \(O_\iota\) whose determinant divides \(p^{e}\).

## Proof

Let \(o_0=o_0(p)\) (odd, \(\le\mathfrak r\)), \(g=u(-p)\) of order \(o\), and \(N\) the order of \(g^{o_0}\); as \(o_0\mid o\) (reduction modulo \(q_0\) is a homomorphism), \(o=o_0N\). Choose an a-place \(\tau\) inducing \(\mathfrak l\). By the [[proofs/grh/upper-divisibility/frobenius-cycle-of-a-marked-prime|proposition on the Frobenius cycle]], \(t(i)=g^{o_0i}\tau\) enumerates bijectively the set \(Q\) of a-places inducing \(\mathfrak l\) or \(\bar{\mathfrak l}\), and the letter embeddings form a Frobenius cycle \(T\) with prime \(p\), exponent \(o_0\), even letters \(\{i:w_{t(i)}=\mathfrak l\}\). Hence \(A_{\mathfrak l}=a\cdot\lvert\{\text{even letters}\}\rvert\), and the even letters are half of all: \(N=2\ell\).

*Size conditions with \(\theta=1/(m^{2}f)\).* \(0<o_0\le\mathfrak r\), so \(\mathfrak r>0\); \(2\mathfrak r\le k\) and \(\theta\le1\) are size comparisons. \(q=P^{N}=p^{o}\ge3^{m}\) because \(m\mid o\) ([[proofs/grh/upper-divisibility/orbits-at-an-exceptional-prime|orbits]]) and \(p\ge13\); and \(a^{4}\le e^{5\log b}\le e^{m}\le3^{m}\). Finally \(\log q=o_0N\log p\le o_0N\log x_1\), \(P^{3\mathfrak r}\le x_1^{3o_0\mathfrak r}\le x_1^{3l_0^{2}}\le\sqrt b\) ([[?lean:New.Data.x₁_pow_le_sqrt_b|`x₁_pow_le_sqrt_b`]]), \(N\le f\), and then \((Nk\log q/\theta)^{5}P^{3\mathfrak r}\le a\) is a size comparison (quoted from `le_of_hasLogBound`).

*The constant.* \(c=Na\bigl(P^{-2\mathfrak r}+\mathfrak r^{2}/(kP)\bigr)\). Since \(m\le p^{\mathfrak r}\) and \(p\le p^{\mathfrak r}\): \(mp\le p^{2\mathfrak r}\le P^{2\mathfrak r}\). Since \(\mathfrak r^{2}m\le k\) (size comparison) and \(p\le P\): \(\mathfrak r^{2}/(kP)\le1/(mp)\). So \(3c\le3\cdot2\ell a\cdot\dfrac{2}{mp}=\dfrac{12a\ell}{mp}=\dfrac{12A_{\mathfrak l}}{mp}\).

Now apply the [[proofs/grh/upper-divisibility/elementary-divisors-of-the-scaled-hecke-operator-given-a-frobenius-cycle|bound given a Frobenius cycle]] with this \(T\), \(t\), \(\theta\): the colength exponent is at most \((3c+\theta j_0)\dim\mathcal S\le(12A_{\mathfrak l}/(mp)+j_0/(m^{2}f))\dim\mathcal S\). \(\blacksquare\)

*Status.* Numerical comparisons proved in Lean by `le_of_hasLogBound` are asserted; the main input is the quoted theorem on elementary divisors.

## Remarks

The head of the source file relates this to known results on slopes of \(T_p\) and integral scalings of Hecke operators (Arsovski 2019; Liu–Truong–Xiao–Zhao 2023; Fakhruddin–Pilloni 2021), as related work, not as sources for this statement.

## References

1. Lean: `New.Data.IsMarked.isOntoUpToColength_scaledHeckeOperator`, `New.Data.isLargeDegree_of_le_card`, `New.Data.three_mul_divisorConstant_le` in `src/New/UpperBound/Divisibility/MarkOperator.lean`.
