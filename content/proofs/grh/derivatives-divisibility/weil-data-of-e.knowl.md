+++
id = "proofs/grh/derivatives-divisibility/weil-data-of-e"
title = "The idele alpha and the Weil data of E"
kind = "construction"
summary = "The finite idele alpha with component 1/P'(zeta) at the places dividing (1+sqrt(-d))/2 and 1 elsewhere, together with j = -1/sqrt(-d) and a splitting character, forms Weil data for E."
aliases = ["idele alpha", "Weil data of E"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.instWeilDataE", "New.Parameters.α", "New.diagonalAtPlaces", "New.Parameters.alpha_apply", "New.Parameters.inv_alpha_mem", "New.Parameters.q₁_mul_alpha_mem", "New.Parameters.v_alpha_mul_star_mul_relDifferentGen", "New.Parameters.v_neg_inv_sqrtNegDInE_mul_alpha_mul_star", "New.Parameters.exists_unit_prod_phi_eq_one_and_mul_star_eq", "New.Parameters.norm_zeta_sub_one_eq_one", "New.Parameters.norm_zeta_pow_eq_one", "New.Parameters.valuation_star_relDifferentGen", "New.Parameters.valuation_map_relDifferentGen", "New.Parameters.betaKInE_mem_or_star_mem", "New.Parameters.weilData_j_eq", "New.Parameters.phi_weilData_j", "New.Parameters.traceOne_eq_betaKInE", "New.Parameters.v_weilData_j_mul_alpha_mul_star", "New.Parameters.twelve_dvd_q₁"]
lean_files = ["src/New/Derivatives/Field/WeilData.lean"]
proof_status = "full"
+++

**Construction.** Let \(E=K(\zeta)\) be as in the [[proofs/grh/derivatives-divisibility/field-setting|field \(E\)]], \(\beta_K=(1+\sqrt{-d})/2\), and \(P'(\zeta)\) the generator of \(\mathfrak{D}_{E/K}\) from the [[proofs/grh/derivatives-divisibility/different-of-e|theorem on the different]]. The **idele \(\alpha\)** is the [[catalog/arithmetic/ideles-number-field-finite|finite idele]] of \(E\) with components
\[
\alpha_w=\begin{cases}P'(\zeta)^{-1}&\text{if }\beta_K\in w,\\ 1&\text{otherwise.}\end{cases}
\]
The **Weil data of \(E\)** are the triple \((\jmath,\alpha,\upsilon)\) with \(\jmath=-1/\sqrt{-d}\in E\) and \(\upsilon\) a chosen [[?lean:New.SplittingChar|splitting character]] of \(E\) (a unitary Hecke character with \(\upsilon(\bar x)=\upsilon(x)^{-1}\) and \(\upsilon(x)=\prod_\tau x_\tau/\lvert x_\tau\rvert\) on ideles whose finite part is a unit). They satisfy the axioms of [[?lean:New.WeilData|Weil data]]:

1. \(\bar\jmath=-\jmath\), and \(\Phi_\tau(\jmath)=i/\sqrt d\) has positive imaginary part for every \(\tau\in\Phi\);
2. (*self-duality*) at every finite place \(w\), \(v_w(\jmath\alpha\bar\alpha)=-v_w(\mathfrak{D}_{E/\mathbb{Q}})\);
3. \((1-\jmath^{-1})/2=\beta_K\) is an algebraic integer;
4. \(\upsilon\) takes the value \(-1\) at a uniformiser of every finite place \(w=\bar w\).

Moreover \(\alpha^{-1}\) and \(q_1\alpha\) are integral at every finite place, and \(\alpha\bar\alpha P'(\zeta)\) is a unit at every finite place.

## Proof

*\(\alpha\bar\alpha P'(\zeta)\) is a unit everywhere.* Complex conjugation maps \(\zeta\) to another primitive \(q_1\)-th root of unity, so \(\overline{P'(\zeta)}\) also generates \(\mathfrak{D}_{E/K}\) and \(v_{\bar w}(P'(\zeta))=v_w(P'(\zeta))\); hence \(v_w(\bar\alpha)=-v_w(P'(\zeta))\) if \(\bar\beta_K\in w\) and \(0\) otherwise. No \(w\) contains both \(\beta_K\) and \(\bar\beta_K=1-\beta_K\). If \(w\) contains neither, then \(P'(\zeta)\notin w\): indeed \(P'(\zeta)\mid q_1\), and every prime factor of \(q_1\) divides \((d+1)/4=\beta_K\bar\beta_K\), so \(P'(\zeta)\) divides a power of \(\beta_K\bar\beta_K\). In all three cases \(v_w(\alpha\bar\alpha P'(\zeta))=0\). The integrality of \(\alpha^{-1}\) is clear, and that of \(q_1\alpha\) follows from \(P'(\zeta)\mid q_1\).

*Axioms.* 1: \(\Phi_\tau(\sqrt{-d})=i\sqrt d\), as \(\Phi_\tau\) is the inclusion on \(K\). 2: \(\mathfrak{D}_{E/\mathbb{Q}}=(P'(\zeta)\sqrt{-d})\) and \(v_w(\alpha\bar\alpha)=-v_w(P'(\zeta))\). 3: \(\jmath^{-1}=-\sqrt{-d}\). 4 holds for [[?lean:New.Cohomology.upsilon_atUniformizer_eq_neg_one|every splitting character]].

*Existence of \(\upsilon\).* By the [[?lean:New.nonempty_splittingChar|existence theorem for splitting characters]] it suffices that every root of unity \(y\in E\) is \(\delta/\bar\delta\) for a unit \(\delta\) of \(\mathcal{O}_E\) with \(N_{E/K}(\delta)=\prod_w\Phi_w(\delta)=1\). The roots of unity of \(E\) are the powers of \(\zeta\); write \(y=\zeta^k\) and \(q_1=4m\) (\(12\mid q_1\)). Let \(i=\zeta^m\), so \(i^2=-1\), \(\bar i=-i\), and \(\eta=i(\zeta-1)\). Then \(\zeta\bar\eta=\zeta\cdot(-i)(\zeta^{-1}-1)=i(\zeta-1)=\eta\). Also \(N_{E/K}(\zeta)=1\) and \(N_{E/K}(\zeta-1)=\Phi_{q_1}(1)=1\), because \(q_1\) is not a prime power; so \(\eta\) is a unit of norm \(1\), and \(\delta=\eta^k\) works. \(\blacksquare\)

## References

1. Lean: `New.Parameters.α`, `New.Parameters.instWeilDataE`, `New.Parameters.v_alpha_mul_star_mul_relDifferentGen`, `New.Parameters.q₁_mul_alpha_mem`, `New.Parameters.exists_unit_prod_phi_eq_one_and_mul_star_eq`, `New.Parameters.phi_weilData_j`, `New.Parameters.traceOne_eq_betaKInE` in `src/New/Derivatives/Field/WeilData.lean`; `New.WeilData` in `src/Lib/Weil/Construction/WeilData.lean`.
