+++
id = "proofs/grh/upper-divisibility/gauge-and-size-of-the-restriction-to-y-m"
title = "Gauge and size of the restriction to Y_m"
kind = "lemma"
summary = "Restriction from X_m to Y_m keeps p-adic gauge bounds (with a diagonal base point at the primes dividing pi_N) and multiplies squared norms by at most exp(x^70) times N to minus the sum of the branch exponents."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.GaugeLe.restrictToY_of_diag", "New.Data.GaugeLe.restrictToY", "New.Data.weylNormSq_restrictToY_le"]
lean_files = ["src/New/UpperBound/Divisibility/ChainValuation.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]]. The [[?lean:New.Data.restrictToY|restriction to \(Y_m\)]] of a form \(\varphi\) on \(X_m\) is
\[
(\operatorname{res}\varphi)(g)=a\cdot\mathcal B\,\varphi\bigl(\operatorname{diag}(g,1)\bigr),\qquad a=\prod_{\tau\in\Phi}\tau(\bar\pi_N)^{-n_\tau},
\]
where \(Y_m\subset X_m\) is the orthogonal complement of the last basis vector, \(\mathcal B\) is the [[?lean:New.Data.branching|branching map]] (an integer matrix from the Weyl module of the weight on \(X_m\) to that of the weight on \(Y_m\)), and \(n_\tau\) is the [[?lean:New.Data.branchExponent|branch exponent]]: the sum of the entries of the weight on \(X_m\) at \(\tau\) minus that of the weight on \(Y_m\).

**Lemma.** Let \(p\) be a prime, \(\iota\colon\mathbb{C}\to\mathbb{C}_p\), \(w_\tau\) the prime induced by \(\tau\).

1. Let \(d\in G_f(X_m)\) be such that for each \(\tau\), its component at \(\overline{w_\tau}\) (read in \(\mathbb{C}_p\) through \(\iota\circ\tau\circ\mathrm{conj}\)) is \(\operatorname{diag}(1,\dots,1,N)\) if \(\overline{w_\tau}\mid\pi_N\) and \(1\) otherwise. If \(\varphi\) has gauge at most \(c\) at base point \(d\), then \(\operatorname{res}\varphi\) has gauge at most \(c\) at base point \(1\).
2. If \(p\ne N\) and \(\varphi\) has gauge at most \(c\) at base point \(1\), so has \(\operatorname{res}\varphi\).
3. For every ring endomorphism \(\sigma\) of \(\mathbb{C}\), every \(\varphi\) and \(h\in G_f(Y_m)\):
\[
\lVert\sigma(\operatorname{res}\varphi(h))\rVert^{2}\le\exp\Bigl(x^{70}-\sum_\tau n_\tau\log N\Bigr)\,\lVert\sigma(\varphi(\operatorname{diag}(h,1)))\rVert^{2}.
\]

## Proof

(1) The gauge of \(\operatorname{res}\varphi(g)\) at \(g\) is the norm of \(g^{-1}\) acting (weight on \(Y_m\)) on \(\iota(a)\mathcal B\,\iota\varphi(\operatorname{diag}(g,1))\). At \(\tau\), \((\operatorname{diag}(g,1)d)^{-1}\) is the block matrix \(\operatorname{diag}(g^{-1},s_\tau)\) with \(s_\tau=\det(d_\tau)^{-1}\in\{N^{-1},1\}\). The branching map intertwines: \(\mathcal B\circ\rho_{X}(\operatorname{diag}(g^{-1},s))=\prod_\tau s_\tau^{n_\tau}\cdot\rho_Y(g^{-1})\circ\mathcal B\) ([[?lean:New.IsBranchingMap.mul_weylRep|`IsBranchingMap.mul_weylRep`]], quoted). The element \(\iota\tau(\bar\pi_N)\) has the absolute value of \(N\) if \(\overline{w_\tau}\mid\pi_N\) and is a unit otherwise (the primes dividing \(\pi_N\) are split of degree one above \(N\)), so \(\lvert\iota a\rvert_p=\lvert\prod_\tau s_\tau^{n_\tau}\rvert_p\). Hence the gauge of \(\operatorname{res}\varphi(g)\) at \(g\) equals the norm of \(\mathcal B\) applied to \((\operatorname{diag}(g,1)d)^{-1}\cdot\iota\varphi(\operatorname{diag}(g,1))\), and an integer matrix does not increase the maximum norm; the latter vector has norm at most \(c\) by hypothesis.

(2) For \(p\ne N\) no \(\overline{w_\tau}\) divides \(\pi_N\) ([[proofs/grh/upper-divisibility/data-of-a-weak-chain-datum-are-standard|part 4 there]]), so \(d=1\) satisfies the hypothesis of (1).

(3) \(\lvert\sigma\tau(\bar\pi_N)\rvert^{2}=N\) because \(\pi_N\bar\pi_N=N\) and embeddings of the CM field commute with conjugation; so \(\lvert\sigma(a)\rvert^{2}=N^{-\sum n_\tau}\). The integer matrix \(\mathcal B\) commutes with \(\sigma\) and multiplies squared norms by at most \(\exp(x^{70})\) ([[?lean:New.IsBranchingMap.weylNormSq_le|`IsBranchingMap.weylNormSq_le`]], quoted). \(\blacksquare\)

*Status.* The intertwining property and the norm bound of the branching map are quoted from the file defining it.

## References

1. Lean: `New.Data.GaugeLe.restrictToY_of_diag`, `New.Data.GaugeLe.restrictToY`, `New.Data.weylNormSq_restrictToY_le` in `src/New/UpperBound/Divisibility/ChainValuation.lean`.
