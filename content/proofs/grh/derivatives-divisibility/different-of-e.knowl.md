+++
id = "proofs/grh/derivatives-divisibility/different-of-e"
title = "The different of E = K(zeta) and its imaginary generator"
kind = "theorem"
summary = "The value at zeta of the derivative of the q1-th cyclotomic polynomial generates the different of E over K, the integers of E are O_K[zeta], and the different of E over Q has a purely imaginary generator delta_E whose absolute values at the infinite places multiply to the f-th power of the root discriminant."
aliases = ["generator of the different of E", "imaginary generator of the different", "delta_E"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.relDifferentGen", "New.Parameters.relDifferent_spec", "New.Parameters.differentIdeal_eq_span_and_adjoin_eq_top", "New.Parameters.eval_derivative_cyclotomic_dvd_q₁", "New.Parameters.map_differentIdeal_adjoin_eq_span", "New.Parameters.span_derivative_cyclotomic_dvd_differentIdeal", "New.Parameters.adjoin_betaKInE_zetaInt_eq_top", "New.Parameters.differentIdeal_eq_span_relDifferentGen_mul", "New.Parameters.conductor_mem_differentIdeal", "New.Parameters.deltaE", "New.Parameters.differentGenPhase", "New.Parameters.star_deltaE", "New.Parameters.differentIdeal_eq_span_deltaE", "New.Parameters.prod_deltaE_eq_rootDiscr_pow", "New.Parameters.infinitePlace_apply_deltaE", "New.Parameters.exists_unit_mul_relDifferentGen_real", "New.Parameters.exists_unit_mul_zetaInt_sub_real", "New.Parameters.zetaInt", "New.Parameters.betaKInE", "New.Parameters.sqrtNegDInE", "New.Parameters.map_differentIdeal_eq_span_sqrtNegDInE"]
lean_files = ["src/New/Derivatives/Field/PrimeDecomposition.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E=K(\zeta)\), \(K=\mathbb{Q}(\sqrt{-d})\), \(\zeta\) of order \(q_1\), be as in the [[proofs/grh/reduction-main/field-e-and-its-places|field \(E\)]], with \(f\) infinite places. Let \(\Phi_{q_1}\) be the [[algebra-fields-galois/cyclotomic-polynomial|cyclotomic polynomial]], \(\beta_K=(1+\sqrt{-d})/2\), and
\[
P'(\zeta):=\Phi_{q_1}'(\zeta)\in\mathcal{O}_E .
\]

1. \(P'(\zeta)\) divides \(q_1\) in \(\mathcal{O}_E\).
2. \(P'(\zeta)\) generates the [[?c:different ideal|different]] \(\mathfrak{D}_{E/K}\), and \(\mathcal{O}_E=\mathcal{O}_K[\zeta]=\mathbb{Z}[\beta_K,\zeta]\). The same holds with \(\zeta\) replaced by any primitive \(q_1\)-th root of unity of \(\mathcal{O}_E\).
3. \(\mathfrak{D}_{E/\mathbb{Q}}=(P'(\zeta)\sqrt{-d})\); in particular \(q_1d\in\mathfrak{D}_{E/\mathbb{Q}}\).
4. There is a unit \(c\in\mathcal{O}_E\) with \(c\bar c=1\) such that \(cP'(\zeta)\) is fixed by complex conjugation. For a fixed such \(c\), the element
\[
\delta_E=c\,P'(\zeta)\sqrt{-d}
\]
satisfies \(\bar\delta_E=-\delta_E\) and \(\mathfrak{D}_{E/\mathbb{Q}}=(\delta_E)\).
5. For each infinite place \(v\), \(\lvert\delta_E\rvert_v=\lvert P'(\zeta)\rvert_v\sqrt d\), where \(\lvert x\rvert_v=\lvert\Phi_v(x)\rvert\); and \(\prod_v\lvert\delta_E\rvert_v=\mathrm{rd}_E^{\,f}\), where \(\mathrm{rd}_E=\lvert D_E\rvert^{1/[E:\mathbb{Q}]}\) is the [[?c:root discriminant|root discriminant]].

Moreover \(E\) contains a primitive root of unity of order \(5040\) (as \(5040\mid q_1\)).

## Proof

1. Write \(X^{q_1}-1=\Phi_{q_1}Q\). Differentiating at the root \(\zeta\) of \(\Phi_{q_1}\) gives \(q_1\zeta^{q_1-1}=P'(\zeta)Q(\zeta)\); multiply by \(\zeta\).

2. Let \(z\) be a primitive \(q_1\)-th root of unity and \(y=\Phi_{q_1}'(z)\). The ring of integers of \(\mathbb{Q}(z)\) is \(\mathbb{Z}[z]\) ([[?c:ring of integers of a cyclotomic field|integers of a cyclotomic field]]), so by the [[?c:Euler–Dedekind formula for the different|formula for the different of a monogenic order]] (conductor times different equals the ideal of the derivative of the minimal polynomial) the different of \(\mathbb{Q}(z)\), extended to \(\mathcal{O}_E\), is \((y)\). The different of \(K\) is \((\sqrt{-d})\), since \(\mathcal{O}_K=\mathbb{Z}[\beta_K]\). As \(y\mid q_1\), \(\sqrt{-d}\mid d\) and \(\gcd(q_1,d)=1\), the two extended differents are coprime; for linearly disjoint subfields with coprime differents, [[?c:different of a compositum with coprime differents|the extended different of one divides the relative different over the other]]: \((y)\mid\mathfrak{D}_{E/K}\). Finally \(E=K(z)\), \(z\) is a root of \(\Phi_{q_1}\in\mathcal{O}_K[X]\), and in general \(\mathfrak{D}_{E/K}\mid\mathfrak{c}\,\mathfrak{D}_{E/K}=(m'(z))\mid(y)\) for the minimal polynomial \(m\) of \(z\) over \(K\) and the conductor \(\mathfrak{c}\) of \(\mathcal{O}_K[z]\); so [[?lean:New.differentIdeal_eq_span_of_dvd|all these ideals are equal and \(\mathfrak{c}=1\)]]: \(\mathfrak{D}_{E/K}=(y)\) and \(\mathcal{O}_E=\mathcal{O}_K[z]\). With \(\mathcal{O}_K=\mathbb{Z}[\beta_K]\) this gives \(\mathcal{O}_E=\mathbb{Z}[\beta_K,\zeta]\).

3. By transitivity of the different in \(\mathbb{Q}\subset K\subset E\), \(\mathfrak{D}_{E/\mathbb{Q}}=\mathfrak{D}_{E/K}\cdot\mathfrak{D}_{K/\mathbb{Q}}\mathcal{O}_E\). Then use 1 and \(\sqrt{-d}\mid d\).

4. \(P'(\zeta)=\prod_{a\ne\zeta}(\zeta-a)\) over the other primitive \(q_1\)-th roots of unity \(a\). As \(q_1\) is even, each is \(a=\zeta^{2e+1}\). Let \(i\in\mathcal{O}_E\) with \(i^2=-1\), \(\bar i=-i\), and \(u=i\,\bar\zeta^{\,e+1}\); then \(u\bar u=1\) and \(u(\zeta-a)=i(\bar\zeta^{\,e}-\zeta^e)\) is a product of two purely imaginary elements, hence real. Let \(c\) be the product of these \(u\). Then \(\bar\delta_E=cP'(\zeta)\cdot\overline{\sqrt{-d}}=-\delta_E\), and \(\delta_E\) generates \(\mathfrak{D}_{E/\mathbb{Q}}\) by 3, as \(c\) is a unit.

5. \(\lvert\Phi_v(c)\rvert^2=\Phi_v(c\bar c)=1\) and \(\lvert\Phi_v(\sqrt{-d})\rvert=\sqrt d\). The square of \(\prod_v\lvert\delta_E\rvert_v\) is \(\lvert N_{E/\mathbb{Q}}(\delta_E)\rvert\), the absolute norm of the different, which is \(\lvert D_E\rvert=\mathrm{rd}_E^{2f}\) since \([E:\mathbb{Q}]=2f\). \(\blacksquare\)

## References

1. Lean: `New.Parameters.relDifferentGen`, `New.Parameters.relDifferent_spec`, `New.Parameters.adjoin_betaKInE_zetaInt_eq_top`, `New.Parameters.differentIdeal_eq_span_relDifferentGen_mul`, `New.Parameters.deltaE`, `New.Parameters.star_deltaE`, `New.Parameters.differentIdeal_eq_span_deltaE`, `New.Parameters.prod_deltaE_eq_rootDiscr_pow`, `New.Parameters.infinitePlace_apply_deltaE` in `src/New/Derivatives/Field/PrimeDecomposition.lean`.
