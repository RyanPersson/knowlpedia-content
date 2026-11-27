+++
id = "proofs/grh/derivatives-divisibility/decomposition-of-primes-in-e"
title = "Decomposition of primes in E = K(zeta)"
kind = "theorem"
summary = "For a prime p not dividing q1 d and a place w of E above p, an infinite place v fixes w, or sends it to its conjugate, exactly when (v,1), or (v,-1), is a power of the Frobenius element; the norm of w is p to the order of that element, and p is unramified."
aliases = ["prime decomposition in E", "decomposition group via Frobenius element"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.smul_eq_iff_exists_frobElem_pow", "New.Parameters.smul_eq_self_iff_exists_frobElem_pow", "New.Parameters.smul_eq_star_iff_exists_frobElem_pow", "New.Parameters.q_eq_pow_orderOf_frobElem", "New.Parameters.natCast_notMem_sq", "New.Parameters.intValuation_natCast_eq_exp_neg_one", "New.Parameters.exists_gal_smul_mem_iff", "New.Parameters.exists_smul_eq_or_star", "New.Parameters.exists_mk_galOfPlaceInt_eq_pow_of_smul_eq", "New.Parameters.smul_eq_self_iff_of_inert", "New.Parameters.smul_eq_star_iff_of_inert", "New.Parameters.q_eq_pow_lcm_of_inert", "New.Parameters.natCast_dvd_pow_sub_galOfPlaceInt_star", "New.Parameters.not_dvd_q₁_mul_d_of_inert", "New.Parameters.frobElem_eq_one", "New.Parameters.smul_ne_star", "New.Parameters.chiK_eq_one_of_modEq_one", "New.Parameters.betaKInE_mul_star_notMem_of_star_eq", "New.Parameters.not_dvd_q₁_of_star_eq", "New.Parameters.natCast_eq_neg_one_of_star_eq"]
lean_files = ["src/New/Derivatives/Field/PrimeDecomposition.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E=K(\zeta)\) be as in the [[proofs/grh/reduction-main/field-e-and-its-places|field \(E\)]], \(p\) a prime, and \(w,w'\) finite places of \(E\) above \(p\). Let \(v\bullet w\) and \(\operatorname{Frob}_p\) be as in the [[proofs/grh/derivatives-divisibility/frobenius-on-generators|criterion on generators]].

1. (*Transitivity.*) There is \(v\in\Phi\) with \(w'=v\bullet w\) or \(w'=\overline{v\bullet w}\).

Suppose \(p\nmid q_1d\). Then:

2. \(v\bullet w=w\) if and only if \((v,1)=\operatorname{Frob}_p^{\,n}\) for some \(n\ge 0\); and \(v\bullet w=\bar w\) if and only if \((v,-1)=\operatorname{Frob}_p^{\,n}\) for some \(n\).
3. \(Nw=p^{m}\), where \(m\) is the order of \(\operatorname{Frob}_p\).
4. \(p\notin w^2\): \(p\) is unramified in \(E\).

**Corollaries.**

* (*Inert primes.*) If \(\chi_K(p)=-1\), then \(p\nmid q_1d\) and \(\operatorname{Frob}_p=(\nu_{-p},-1)\): \(v\bullet w=w\) iff \(v=\nu_{-p}^{\,n}\) with \(n\) even; \(v\bullet w=\bar w\) iff \(v=\nu_{-p}^{\,n}\) with \(n\) odd; \(Nw=p^{\operatorname{lcm}(o,2)}\) with \(o\) the order of \(\nu_{-p}\). Moreover, for odd \(n\) and every \(y\in\mathcal{O}_E\), \(y^{p^n}\equiv\sigma_{\nu_{-p^n}}(\bar y)\pmod{p\,\mathcal{O}_E}\).
* (*Primes \(\equiv1\).*) If \(p\equiv1\pmod{q_1d}\), then \(\operatorname{Frob}_p=1\); so \(v\bullet w\ne\bar w\) for all \(v\), \(v\bullet w=w\) only for \(v=1\), and \(Nw=p\).
* (*Self-conjugate places.*) If \(\bar w=w\), then \(\beta_K\bar\beta_K\notin w\) for \(\beta_K=(1+\sqrt{-d})/2\), \(p\nmid q_1\), and \(p\equiv-1\pmod{2^{s+1}}\), \(s\) being the level.

## Proof

1. \(\operatorname{Gal}(E/\mathbb{Q})\) acts transitively on the primes above \(p\) ([[?c:transitivity of the Galois group on primes above a prime|standard]]); take \(\sigma\) with \(\sigma x\in w\iff x\in w'\). The embedding \(\Phi_1\circ\sigma\) induces some place \(v\), so it equals \(\Phi_v=\Phi_1\circ\sigma_v\) or its complex conjugate; thus \(\sigma=\sigma_v\) or \(\sigma=\sigma_v\circ(\text{conjugation})\).

2. Let \((c,\varepsilon)\) be \((\mathrm{id},1)\) or (conjugation, \(-1\)); the claim is \(v\bullet w=c^{-1}(w)\iff\exists n\,(v,\varepsilon)=\operatorname{Frob}_p^n\). If \(v\bullet w=c^{-1}(w)\), then \(\sigma_v\circ c^{-1}\) maps \(w\) into \(w\) and induces an endomorphism of the finite field \(\mathcal{O}_E/w\) over \(\mathbb{F}_p\), which is a [[algebra-fields-galois/frobenius-endomorphism|power of Frobenius]]: \(\sigma_vx\equiv(cx)^{p^n}\pmod w\) for all \(x\). By the criterion (part 2, with \(R=\mathcal{O}_E/w\)), \((v,\varepsilon)=\operatorname{Frob}_p^n\). Conversely, if \(\sigma_vx\equiv(cx)^{p^n}\pmod w\), then \(\sigma_vx\in w\iff cx\in w\).

3. \(Nw=p^{f_w}\) and \(f_w\mid n\) iff \(x^{p^n}\equiv x\pmod w\) for all \(x\), iff \(\operatorname{Frob}_p^n=1\) (criterion with \(v=1\), \(c=\mathrm{id}\)). So \(f_w\) is the order.

4. If \(p\in w^2\), then \(w\) divides \(\mathfrak{D}_{E/\mathbb{Q}}\) ([[?c:ramified primes divide the different|ramified primes divide the different]]), which contains \(q_1d\) by the [[proofs/grh/derivatives-divisibility/different-of-e|theorem on the different]]; then \(q_1d\in w\cap\mathbb{Z}=p\mathbb{Z}\), a contradiction.

*Inert primes.* [[?lean:New.Parameters.chiK_eq_one_of_dvd|Primes dividing \(q_1\) have \(\chi_K=1\)]] and \(\chi_K(d)=0\), so \(p\nmid q_1d\); \(\operatorname{Frob}_p^n=(\nu_{-p}^n,(-1)^n)\), and the order of a pair is the lcm of the orders. The congruence is part 1 of the criterion with \(R=\mathcal{O}_E/p\mathcal{O}_E\), conjugation, \(v=\nu_{-p^n}\): the first condition is trivial and \(\chi_K(p)^n(-1)=1\).

*Primes \(\equiv1\).* Then \(\chi_K(p)=1\) and \(\nu_p=1\).

*Self-conjugate places.* \(\bar\beta_K=1-\beta_K\); if \(\beta_K\bar\beta_K\in w=\bar w\), both factors lie in \(w\), and so does their sum \(1\). [[?lean:New.Parameters.dvd_d_add_one_div_four_of_dvd_q₁|Every prime dividing \(q_1\) divides \((d+1)/4\)]]\(\,=\beta_K\bar\beta_K\); hence \(p\nmid q_1\). For the congruence note \(1\bullet w=w=\bar w\). If \(p\) splits (\(p\neq d\)), part 2 gives \(-1=1^n\), impossible. If \(p=d\): as in 2, \(x\equiv\bar x^{\,d^n}\pmod w\) for some \(n\), and part 1 of the criterion with the injectivity at \(\zeta\) gives \(1=\nu_{-d^n}\), so \(d^n\equiv-1\pmod{q_0}\), which is [[?lean:New.Parameters.d_pow_ne_neg_one|impossible for the parameters]]. So \(p\) is inert and \(1=\nu_{-p}^{\,n}\) with \(n\) odd. The class \(u\) of \(-p\) in \((\mathbb{Z}/2^{s+1})^\times\), a group of order \(2^s\), then satisfies \(u^n=1=u^{2^s}\) with \(\gcd(n,2^s)=1\), so \(u=1\). \(\blacksquare\)

## References

1. Lean: `New.Parameters.smul_eq_iff_exists_frobElem_pow`, `New.Parameters.q_eq_pow_orderOf_frobElem`, `New.Parameters.intValuation_natCast_eq_exp_neg_one`, `New.Parameters.exists_smul_eq_or_star`, `New.Parameters.smul_eq_self_iff_of_inert`, `New.Parameters.smul_eq_star_iff_of_inert`, `New.Parameters.q_eq_pow_lcm_of_inert`, `New.Parameters.natCast_dvd_pow_sub_galOfPlaceInt_star`, `New.Parameters.smul_ne_star`, `New.Parameters.natCast_eq_neg_one_of_star_eq` in `src/New/Derivatives/Field/PrimeDecomposition.lean`.
