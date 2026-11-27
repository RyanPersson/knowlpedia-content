+++
id = "proofs/grh/upper-seesaw/unfolding-stages"
title = "The functions of the unfolding"
kind = "construction"
summary = "The functions W_k on the unitary groups of the tower Y_k left by k unfolding steps of the chain of lifts, with outer variables g_k."
aliases = ["unfold stage", "moved datum", "outer variables"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.movedDatum", "New.Data.twistedPairWeil_movedDatum", "New.Data.constTermAtStringMap_movedDatum", "New.Data.unfoldStageOn", "New.Data.unfoldStage", "New.Data.unfoldStageOn_succ", "New.Data.unfoldStageOn_update", "New.Data.unfoldStage_update", "New.Data.isEquivariant_unfoldStageOn", "New.Data.continuous_unfoldStage", "New.Data.fixesLeft_ratBessel_unfoldStage", "New.Data.integral_unfoldStageOn", "New.Data.inclXFin_mem_chosenLevel"]
lean_files = ["src/New/UpperBound/Seesaw/UnfoldingStages.lean"]
+++

Let \(D\) be the [[?lean:New.Data|data]], \(\vartheta\) a
[[?lean:New.Data.TameChar|tame character]], \(\varphi\) a
[[?lean:New.Data.SourceForm|source form]] on \(U(X_0)\) and \(t\) a linear form on its values. Let
\(G_k=U(Y_k)(\mathbb{A})\) with the [[proofs/grh/upper-seesaw/tower-gradings-and-evaluated-data|grading]]
\(\mathcal{Y}_k\) (\(k\le m-1\)) and Bessel subgroup \(R_k\le G_k\). Fix **outer variables**
\(g_k=(\xi_k,y_k)\in G_k\) (archimedean and finite parts) for all \(k\). Let \(F_k\) be the
[[?lean:New.Data.datumY|datum of lift \(k+1\)]] on \(\operatorname{Hom}(Y_k,Y_{k+1})\) and
\(\mu_{k+1}\) the [[?lean:New.Data.chainChar|character of lift \(k+1\)]].

The **moved datum** is \(F_k^{g}=\omega_{\mu_{k+1}}(g_k,1)F_k\) (twisted Weil action, normalised by
the rank twist of \(\mu_{k+1}\)); acting on it by \((g,h)\) is acting on \(F_k\) by \((gg_k,h)\).

The **functions of the unfolding** are defined recursively:

* \(\mathcal{W}^{R}_0\) on \(R_0\) is the [[?lean:New.Grading.sourceFn|source function]] of
  \((t,\varphi)\): \(\mathcal{W}^{R}_0(u\,g)=\psi_U(u)\,t\bigl(\varphi(g)\bigr)\) for \(u\) in the unipotent radical and \(g\in U(X_0)(\mathbb{A})\) (the string of \(Y_0\) has odd length \(m-1\), so here every element of the unipotent radical raises grades by at least two), where \(\psi_U\) is the unipotent character of the grading and \(t(\varphi(g))\) stands for the coefficient \(t\bigl(\rho(g_\infty)^{-1}\varphi(g_f)\bigr)\) of the algebraic form;
* \(\mathcal{W}_{k+1}\) on \(G_{k+1}\) is the [[?lean:New.Grading.unfoldStep|unfolding step]]
  applied to \(\mathcal{W}^{R}_k\) and the moved datum:
  \[
  \mathcal{W}_{k+1}(h)=\int_{[R_k]}\mathcal{W}^{R}_k(r)\;c_{\operatorname{sh}}\bigl(F_k^{g};r,h\bigr)\,dr ,
  \]
  the integral over \(R_k\) modulo its rational points, where
  \(c_{\operatorname{sh}}(F;r,h)\) is the
  [[?lean:New.Grading.constTermAtStringMap|constant term at the shift]] \(T\colon Y_k\to Y_{k+1}\):
  the mean, over adelic matrices \(v\) modulo rational ones, of the theta value of
  \(\varrho(T)\,\omega_{\mu_{k+1}}(r,h)F\) translated by the part of \(v\) of positive degree;
* \(\mathcal{W}^{R}_{k+1}(\gamma)=\mathcal{W}_{k+1}(\gamma g_{k+1})\) for \(\gamma\in R_{k+1}\), as long as \(k+1\le m-1\).

Thus \(\mathcal{W}^{R}_k\) is defined for \(0\le k\le m-1\) and \(\mathcal{W}_{k+1}\) for \(0\le k\le m-1\); in the step to \(\mathcal{W}_{k+1}\) the target \(Y_{k+1}\) carries the grading \(\mathcal{Y}_{k+1}\) for \(k+1\le m-1\) and, for the terminal function \(\mathcal{W}_m\), the last grading of \(Y_m\) (empty string), for which no restricted function is formed.

## Properties

1. \(\mathcal{W}_{k+1}\) depends only on \(g_0,\dots,g_k\).
2. \(\mathcal{W}^{R}_k\) is [[?lean:New.Grading.IsEquivariant|equivariant]] on \(R_k\): continuous, left invariant under the rational points, and
   \(\mathcal{W}^{R}_k(ur)=\psi_U(u)\,\mathcal{W}^{R}_k(r)\) for \(u\) in the subgroup \(U^{\ge2}\) of elements \(u\in R_k\) such that \(u-1\) (in rational coordinates) raises grades by at least two. When the string length is odd, \(U^{\ge2}\) is the whole unipotent radical; for a positive even string length there are directions of degree one, for which no transformation law is asserted. \(\mathcal{W}_{k+1}\) is continuous and left invariant under the
   rational points of \(R_{k+1}\).
3. (**One unfolding step.**) Here \(R_{k+1}(F)=\Gamma_{Y_{k+1}}\cap R_{k+1}\) denotes the rational points of the Bessel subgroup: the intersection with the rational unitary group, which is defined over the totally real field \(F=E^{+}\). Let \(z\) be an [[langlands/automorphic-form|automorphic]], [[?c:Rapidly decreasing automorphic function|rapidly decreasing]] function on
   \(G_{k+1}\). Then \(\mathcal{W}_{k+1}z\) is integrable on \(R_{k+1}(F)\backslash G_{k+1}\) and
   \[
   \int_{[R_k]}\mathcal{W}^{R}_k(r)\int_{[G_{k+1}]}\theta\bigl(\omega_{\mu_{k+1}}(rg_k,h)F_k\bigr)z(h)\,dh\,dr
   =\int_{R_{k+1}(F)\backslash G_{k+1}}\mathcal{W}_{k+1}(h)z(h)\,dh .
   \]
   That is: pairing the previous function with the [[?c:Theta lift|theta lift]] of \(z\) to \(G_k\), translated by
   \(g_k\), unfolds to pairing \(\mathcal{W}_{k+1}\) with \(z\). (This is the general unfolding
   identity of `Lib/Weil/Periods/Unfolding` applied to the tower; its proof is not reproduced.)
4. The embedding of the finite points of \(U(X_k)\) into those of \(U(Y_k)\) maps the level of
   \(X_k\) into the chosen level (the chosen places do not lie above \(N\); cf.
   [[proofs/grh/upper-seesaw/glued-level-congruences|congruence levels of the glued lattice]]).

## References

1. Lean: `New.Data.unfoldStageOn`, `New.Data.unfoldStage`, `New.Data.integral_unfoldStageOn` and the lemmas listed in the front matter, in `src/New/UpperBound/Seesaw/UnfoldingStages.lean`.
2. B. Wang, *Global theta lifting and periods associated to nilpotent orbits*, 2025; Gomez–Zhu, *Local theta lifting of generalized Whittaker models*, 2014 (cited in the head of `SeesawIdentity.lean` as related work for the unfolding).
