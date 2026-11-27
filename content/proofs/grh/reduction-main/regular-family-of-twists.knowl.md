+++
id = "proofs/grh/reduction-main/regular-family-of-twists"
title = "Ratios of Hecke L-values, main pairs, families with small ratios and regular families of twists"
kind = "definition"
summary = "The ratio of twisted to untwisted Hecke L-values of a pair; ramified and main pairs; the denominator budget; families of m-fold twists, one for each finite place of C, with small ratios, and regular families."
aliases = ["CriticalPair.ratio", "IsRamified", "IsMainPair", "denominatorBudget", "ClearsProjection", "HasDenominatorsLe", "IsDenominatorBound", "IsNegligible", "HasSmallRatios", "IsRegularFamily", "goodLift", "regular family", "small ratios"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.CriticalPair.ratio", "New.Data.RankOneIndex", "New.Data.goodLift", "New.Data.CriticalPair.IsRamified", "New.Data.CriticalPair.IsMainPair", "New.Data.CriticalPair.IsMainPair.isRamified", "New.Data.denominatorBudget", "New.Data.ClearsProjection", "New.Data.HasDenominatorsLe", "New.Data.IsDenominatorBound", "New.Data.IsNegligible", "New.Data.HasSmallRatios", "New.Data.IsRegularFamily"]
lean_files = ["src/New/Determinant/Twist/FitTwists.lean"]
+++

Let \(D\) be [[proofs/grh/reduction-main/data|data]]. A [[?lean:New.Data.CriticalPair|pair]] \(p=(\nu,z)\) consists of an integer \(1\le z\le t\) and an automorphic character \(\nu\) of \(\mathrm U(1)(\mathbb A)\) of weight \(-c\), with \(z\le c(v)\le4b\) at every infinite place \(v\), and tame part supported on the chosen places. \(L^{S}(z,\mu)\) denotes the [[?lean:New.AutChar.L|partial Hecke \(L\)-function]] of the character \(x\mapsto\mu(x/\bar x)\) of \(E\), without the Euler factors at the places of \(S\) and their conjugates; \(\mathrm{Ch}\) is the set of [[?lean:New.Data.IsChosen|chosen places]] (those dividing \(\pi_M\)).

**Ratio.** For a pair \(p=(\nu,z)\), a [[proofs/grh/reduction-main/twist|tame character]] \(\vartheta\) with modulus \(Q\) and a sign \(\epsilon=\pm1\) (default \(1\)),
\[
\operatorname{ratio}(p,\vartheta,\epsilon):=\frac{\bigl\lvert L^{\mathrm{Ch}\cup Q}\bigl(z,(\nu\vartheta^{\epsilon})^{-1}\bigr)\bigr\rvert}{\bigl\lvert L^{\mathrm{Ch}}(z,\nu^{-1})\bigr\rvert}\ \in\mathbb R_{\ge0}\subset\mathbb C
\]
(with the convention \(u/0=0\)).

**Ramified and main pairs.** \(p\) is *ramified* if its tame part is nontrivial exactly at the chosen places. \(p\) is a *main pair for \(j\)* if: \(2\le z\) and the index set with four blocks of sizes \(12,4,4\) and \(\max(2z-20,0)\) has \(2z\) elements, which holds exactly when \(z\ge10\) ([[?lean:New.Data.CriticalPair.HasLiftRank|lift rank condition]]; it is implied by \(m<z\)); \(m<z\le r\); \(1\le j\le m\); the tame part of \(\nu\) is \(\omega^j\) ([[proofs/grh/reduction-main/lift-characters|\(\omega\)]]); and \(\kappa_j(v)+r-t\le c(v)\le\kappa_j(v)\) at every infinite place \(v\). A main pair is ramified, because \(\omega_w^j\ne1\) exactly at the chosen places for \(1\le j\le m\) ([[?lean:New.Data.chiMLocal_zpow_ne_one_iff_isChosen|order of \(\omega\)]]).

**Good lift.** For a tame character \(\vartheta\) and \(j\), the *good lift* is the [[?lean:New.Data.singleLift|single theta lift]] \(W_j\to V\) for \(\vartheta\) restricted to the [[?lean:New.Data.goodForms|good forms]] on \(W_j\); its image is the *space of lifts* \(Z_{\vartheta,j}\).

**Denominator budget.** \(\operatorname{budget}:=\dfrac{f\,a\,(\log b)^3}{m\,k}\).

**Denominators at one place.** Let \(\iota\mid\ell\), \(\vartheta\) a twist, \(j\ge0\), \(\beta\in\mathbb R\). We say the *denominators are at most \(\beta\)* at \((\iota,\vartheta,j)\) if

1. (*clearing the projection*) there is an endomorphism \(\Lambda\) of \(Z_{\vartheta,j}\) with \(\lvert\det\Lambda\rvert_\iota\ge\exp(-\dim Z_{\vartheta,j}\cdot r\beta)\) such that \(\Lambda(\mathrm{pr}\,y)\) is integral at \(\iota\) for every form \(y\) on \(V\) that is integral at \(\iota\) and [[?lean:New.DescentPair.IsOrthogonalToFalseLifts|orthogonal to the false lifts]] taken for the good-forms idempotent \(e_0\) and the subspace \(Z_{\vartheta,j}^{\perp}\) (the forms in \(Z_{\vartheta,j}^\perp\), in the image of \(e_0\), killed by the Hecke polynomial at its test value at some split place off the level), \(\mathrm{pr}\) being the orthogonal projection onto \(Z_{\vartheta,j}\); and
2. for every main pair \(p\) for \(j\) and any two [[?lean:New.DescentPair.IsTestForm|test forms]] \(\Xi,\Xi'\) for the lift of \(\nu\vartheta\) from \(\mathrm U(1)\) to the definite space of rank \(2z\), the inner product of their projections to the line of the lifted form has \(\lvert\cdot\rvert_\iota\le e^\beta\).

**Families.** Let \(\theta=(\theta_\iota)_\iota\) be a family of [[proofs/grh/reduction-main/m-fold-twist|\(m\)-fold twists]], one for each [[proofs/grh/reduction-main/prime-padic-iso|finite place \(\iota\mid\ell\) of \(\mathbb C\)]].

- \(\theta\) **has small ratios** if (i) \(\gcd(\ell,\mathrm{Nm}\,Q(\theta_\iota))=1\) for all \(\iota\mid\ell\), and (ii) for every \(1\le j\le m\), every ramified pair \(p\) and every sign \(\epsilon\), the family \(\iota\mapsto\operatorname{ratio}(p,\theta_\iota^{\,j},\epsilon)^{-1}\) has [[proofs/grh/reduction-main/height-bound|height at most \(x_1\)]].
- \(\theta\) is **regular** if it has small ratios and, for every \(1\le j\le m\), there are real numbers \(\gamma_\ell\) with \(\sum_{\ell\in T}\gamma_\ell\le\operatorname{budget}\) for every finite set \(T\) of primes, such that at every \(\iota\mid\ell\) the denominators at \((\iota,\theta_\iota^{\,j},j)\) are at most \(\gamma_\ell\).

A family of reals \(e_\ell\ge0\) is called *negligible with exponent \(C\)* if \(\sum_{\ell\in T}e_\ell\log\ell\le x^C\) for all finite sets \(T\) of primes.

Regular families exist: [[?lean:New.exists_isRegularFamily|existence of regular families]].

## References

1. Lean: the declarations in the front matter, in `src/New/Determinant/Twist/FitTwists.lean`.
