+++
id = "proofs/grh/upper-divisibility/data-of-a-weak-chain-datum-are-standard"
title = "The data of a weak chain datum are standard above a prime"
kind = "lemma"
summary = "For p different from N and prime to the modulus of the twist, the translated vacua in a weak chain datum are translates of the integral vacuum by points made integral above p by the level element; translations may be taken supported at M q."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsWeakChainDatum.translateDatum_mem_standardData", "New.Data.mem_integralAfter_of_mem_admissibleTranslations", "New.Data.exists_supported_translateDatum_eq", "New.Data.projOn_translateDatum", "New.Data.natCast_notMem_and_star_notMem_piNPlaces_of_ne"]
lean_files = ["src/New/UpperBound/Divisibility/ChainValuation.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]]. A tuple of translations \(x=(x_j)\) is [[?lean:New.Data.admissibleTranslations|admissible for a natural number \(q\)]] if every entry of \(\overline{\pi_M}\,x_j\) is integral at every finite place of \(E\) not containing \(q\) (here \(\overline{\pi_M}\) is the image of the element \(\bar\pi_M\) of \(K\)). For an integer \(\delta\) of \(K\) and a set \(S\) of places, \(x_j\) is **integral after \(\delta\) on \(S\)** if \(\delta x_j\) has entries integral at the places of \(S\).

**Lemma.**

1. If \(x\) is admissible for \(q\) and \(S\) is a set of places such that for each \(w\in S\): \(q\notin w\), and \(\delta=\bar\pi_M\) or \(\bar w\) is not a [[?lean:New.Data.IsChosen|chosen place]]; then each \(x_j\) is integral after \(\delta\) on \(S\).
2. If \(x\) is admissible for \(q\), there is \(x'\), admissible for \(q\) and vanishing at all places prime to \(Mq\), with the same [[?lean:New.Data.translateDatum|data]]: \(\Phi^{0}_{x,j}=\Phi^{0}_{x',j}\) for all \(j\).
3. Let \(\Psi\) be a [[?lean:New.Data.IsWeakChainDatum|weak chain datum]] for a twist \(\vartheta\) with modulus of norm \(\mathrm N\vartheta\), let \(p\ne N\) be a prime not dividing \(\mathrm N\vartheta\), and let \(\delta=\bar\pi_M\), or \(\delta\) arbitrary if \(p\nmid M\). Then for \(x\in\operatorname{supp}\Psi\) the datum \(\Phi^{0}_{x,j}\) lies in the [[?lean:New.Parameters.standardData|standard data]] for \(\delta\): the span of the translates of the integral vacuum by points that \(\delta\) makes integral above \(p\).
4. A place \(w\) above a prime \(p\ne N\) does not lie above \(N\), and \(\bar w\nmid\pi_N\).
5. Let \(S\) be a set of finite places and \(\mathrm{pr}_S\) the projection on the vacuum at \(S\): the mean, over integral vectors \(y\), of the Heisenberg translations by the part of \(y\) at \(S\) and the conjugate places. If \(x_j\) is integral at every place of \(S\) and at every conjugate of a place of \(S\), then \(\mathrm{pr}_S\Phi^{0}_{x,j}=\Phi^{0}_{x,j}\).

## Proof

(1) \(\overline{\pi_M}x_j\) is integral at \(w\). If \(\delta=\bar\pi_M\) this is the claim. Otherwise \(\bar w\) is not chosen, that is \(\pi_M\notin\bar w\), so \(\overline{\pi_M}\) is a unit at \(w\); then \(x_j\) is integral at \(w\) and so is \(\delta x_j\).

(2) Let \(S\) be the set of places containing \(Mq\); it is stable under conjugation. Write \(x_j=x_j^{S}+x_j^{S^{c}}\) (components at \(S\) and off \(S\)). Off \(S\), both \(q\) and \(M=\pi_M\bar\pi_M\) are units, so by (1) with \(\delta=1\), \(x_j^{S^{c}}\) is integral. The Heisenberg translation by an integral vector fixes the integral vacuum, and the translations by \(x_j^{S}\) and \(x_j^{S^{c}}\) compose without phase because their supports are disjoint and conjugation-stable (the pairing \(\overline{x^{S^{c}}}\cdot x^{S}\) vanishes). Hence translating the vacuum by \(x_j\) or by \(x'_j=x_j^{S}\) gives the same datum.

(3) The support of \(\Psi\) consists of translations admissible for \(\mathrm N\vartheta\cdot N\). A place \(w\) above \(p\) contains neither \(\mathrm N\vartheta\) (coprime to \(p\)) nor \(N\). If \(p\nmid M\), then \(\bar w\) (also above \(p\)) is not chosen. Apply (1) with \(S\) the places above \(p\).

(5) \(\Phi^{0}_{x,j}\) is the integral vacuum translated by \(x_j\). The projection multiplies a Heisenberg translate of a vector it fixes by the indicator that the translation is integral at \(S\) and its conjugates ([[?lean:New.Space.projOn_finHeisenbergOp|`projOn_finHeisenbergOp`]], quoted); it fixes the integral vacuum, since translations by integral vectors do, and the indicator is \(1\) by hypothesis.

(4) \(N\in w\) would give \(p\mid N\), so \(p=N\); a place dividing \(\pi_N\) contains \(N\), and \(N\) is fixed by conjugation. \(\blacksquare\)

*Status.* The definitions of admissible translations, standard data and the properties of Heisenberg translations of the vacuum are other areas' and are used as quoted; in (2) I followed the Lean computation `finHeisenbergOp_finHeisenbergOp` only at the level described.

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Divisibility/ChainValuation.lean`.
