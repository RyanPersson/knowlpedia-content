+++
id = "proofs/grh/spanning-unfolding-b/square-sum-of-the-induced-character"
title = "The conjugation mean of the unipotent character has square sum at most two"
kind = "theorem"
summary = "The sum over the residue group of the squared absolute values of the conjugation mean of the reduced unipotent character is at most 2."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.sum_norm_reducedCharMean_sq_le", "New.Filling.extendedBesselChar_toPlaces_eq_reducedChar", "New.Filling.integral_extendedBesselChar_conj_eq", "New.Filling.sum_sq_norm_integral_extendedBesselChar_conjugate_le", "New.Filling.inv_ideleM_mem_integralOff"]
lean_files = ["src/New/Spanning/Unfolding/Moments.lean"]
proof_status = "outline"
+++

**Theorem (the induced character).** Let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over a CM field \(E\) with [[?lean:New.WeilData|Weil data]], and \(\bar\psi^\natural_{\mathsf U}\) the [[proofs/grh/spanning-unfolding-b/reduced-unipotent-character|conjugation mean of the reduced character]]. Then
\[
\sum_{s\in\bar G}\bigl\lvert\bar\psi^\natural_{\mathsf U}(s)\bigr\rvert^2\le2 .
\]

## Proof

The proof passes to the product \(F_T\) of the completions of \(E\) at the set \(T\) of the chosen places and their conjugates; \(M^{-1}\) is integral off \(T\), because the idempotent of the places off \(T\) vanishes modulo all places of \(T\) and is therefore divisible by \(M\) (condition 4 of a filling datum). Let \(K_T\) be the group of integral points of the unitary group over \(F_T\) and \(K_T(M)\) its congruence subgroup. The structure is as follows; the steps marked (cited) rest on results of other areas that are only quoted here.

1. (cited) There is a [[?lean:New.Filling.IsFillingData|filling datum at \(T\)]], a large lattice datum of modulus \(M\) with a Haar measure \(\mu\) on the group over \(F_T\) ([[?lean:New.Filling.exists_isFillingData|existence]]).
2. Let \(\chi_M\) be the [[?lean:New.Floors.IntegralPlace.extendedBesselChar|extended Bessel character]]: \(\chi_M(uk)=\psi(\sigma(u)/M)\) for \(u\) unipotent and \(k\in K_T(M)\), and \(0\) off \(\mathsf{U}K_T(M)\). For \(l\in K\) with component \(l_T\): \(\chi_M(l_T)=\bar\psi_{\mathsf U}(\bar l)\). If \(\bar l=\bar k\) with \(k\) integral unipotent, then \(k_T^{-1}l_T\in K_T(M)\) and the value is \(\psi_{\mathsf U}(k)\); if \(\chi_M(l_T)\ne0\), then \(l_T\in uK_T(M)\) with \(u\) unipotent over \(F_T\), and \(u\) lifts to an integral unipotent element with the same reduction as \(l\). Both directions use (cited) that reductions agree exactly when components at \(T\) are congruent modulo \(M\), and that elements over \(F_T\) lift to elements integral off \(T\).
3. For \(l\in K\): \(\int_{K_T}\chi_M(y\,l_T\,y^{-1})\,d\mu(y)=\mu(K_T)\cdot\bar\psi^\natural_{\mathsf U}(\bar l)\). Indeed, choosing lifts \(\sigma(g)\in K\) of all \(g\in\bar G\) (reduction is onto by admissibility) and using the invariance of \(\mu\) on \(K_T\), \(\lvert\bar G\rvert\) times the integral is the integral of \(\sum_g\chi_M\bigl((\sigma(g)_Ty)\,l_T\,(\sigma(g)_Ty)^{-1}\bigr)\), and by step 2 the sum equals \(\lvert\bar G\rvert\,\bar\psi^\natural_{\mathsf U}(\bar l)\) for every \(y\in K_T\).
4. (cited) Put \(a(z)=\int_{K_T}\chi_M(yzy^{-1})d\mu(y)\). It is constant on the cosets \(\sigma(s)_TK_T(M)\), which are disjoint for distinct \(s\in\bar G\). Hence \(\sum_s\lvert a(\sigma(s)_T)\rvert^2\mu(K_T(M))\le\int\lvert a\rvert^2d\mu\), and the mass estimate for large lattice data ([[?lean:New.Floors.IntegralPlace.IsLargeLatticeData.massIntegral_le_main_add_error|main term plus error]]) bounds this integral by \(\mu(K_T)\mu(K_T(M))(\mu(K_T)+2^{-n})\le2\mu(K_T)^2\mu(K_T(M))\); the rank condition it needs, \(n+2\cdot10^9n^4\le k\), follows from the size conditions \(10^{10}n^4\le n^6\), \(3n^6+12\le n^7\le k\).
5. Combining 3 and 4: \(\mu(K_T)^2\sum_s\lvert\bar\psi^\natural_{\mathsf U}(s)\rvert^2\le2\mu(K_T)^2\), and \(\mu(K_T)>0\).

*What is asserted without proof here:* the existence and properties of the filling datum at \(T\) (steps 1, 2, 4), in particular the mass estimate of step 4, which is the analytic heart; they are proved in the parts of the development on the main term and on two frames at one place. I read the Lean proofs of the five declarations listed for this knowl verbatim; the definitions of the objects over \(F_T\) were not opened.

## References

1. Lean: `New.Filling.sum_norm_reducedCharMean_sq_le`, `New.Filling.extendedBesselChar_toPlaces_eq_reducedChar`, `New.Filling.integral_extendedBesselChar_conj_eq`, `New.Filling.sum_sq_norm_integral_extendedBesselChar_conjugate_le` in `src/New/Spanning/Unfolding/Moments.lean`.
