+++
id = "proofs/grh/derivatives-divisibility/frobenius-on-generators"
title = "Galois elements as powers of Frobenius: a criterion on generators"
kind = "lemma"
summary = "For a ring map from the integers of E to characteristic p, the Galois element of a place acts as the p^n-th power, possibly after complex conjugation, exactly when this holds at zeta and at the square root of -d; over a domain this means that the place and sign are the n-th power of the Frobenius element."
aliases = ["Frobenius element of E at p", "action of infinite places on finite places"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.forall_map_galOfPlaceInt_eq_pow_iff", "New.Parameters.map_galOfPlaceInt_eq_pow_iff_eq_frobElem_pow", "New.Parameters.map_galOfPlaceInt_zetaInt_inj", "New.Parameters.frobElem", "New.Parameters.galOfPlaceInt", "New.Parameters.IsIdOrConjWithSign", "New.Parameters.ringHom_ext_zetaInt_betaKInE", "New.Parameters.mem_asIdeal_smul_iff", "New.Parameters.chiK_pow_eq_one_or_neg_one"]
lean_files = ["src/New/Derivatives/Field/PrimeDecomposition.lean"]
proof_status = "full"
+++

**Definitions.** Let \(E=K(\zeta)\) with its group \(\Phi\) of infinite places and the automorphisms \(\sigma_v\in\operatorname{Gal}(E/K)\) (see the [[proofs/grh/reduction-main/field-e-and-its-places|field \(E\)]]). A *finite place* \(w\) of \(E\) is a nonzero prime ideal of \(\mathcal{O}_E\), \(\bar w\) its complex conjugate; it lies *above* the prime \(p\) if \(p\in w\). For an integer \(m\), \(\nu_m\in\Phi\) denotes the [[?lean:New.Parameters.placeOfInt|place named by \(m\)]] (the place of the class of \(m\) in \((\mathbb{Z}/q_1)^\times\) if \(m\) is prime to \(q_1\), the identity otherwise). An infinite place \(v\) acts on the finite places by \(v\bullet w=\sigma_v^{-1}(w)=\{x\in\mathcal{O}_E:\sigma_v(x)\in w\}\). For a prime \(p\), the **Frobenius element** is
\[
\operatorname{Frob}_p=\bigl(\nu_{\chi_K(p)p},\ \chi_K(p)\bigr)\in\Phi\times\mathbb{Z},
\]
the place named by the integer \(\chi_K(p)\,p\) and the Legendre symbol, in the product monoid. Let \((c,\varepsilon)\) be either \((\mathrm{id},1)\) or (complex conjugation, \(-1\)).

**Lemma.** Let \(p\) be a prime with \(p\nmid q_1\), \(R\) a commutative ring of characteristic \(p\), \(\varphi\colon\mathcal{O}_E\to R\) a ring homomorphism, \(n\ge0\) and \(v\in\Phi\).

1. \(\varphi(\sigma_vx)=\varphi(c\,x)^{p^n}\) for all \(x\in\mathcal{O}_E\) if and only if
\[
\varphi(\sigma_v\zeta)=\varphi(\sigma_u\zeta)\ \text{ for } u=\nu_{\varepsilon p^n},\qquad\text{and}\qquad\chi_K(p)^n\,\varepsilon\,\varphi(\sqrt{-d})=\varphi(\sqrt{-d}).
\]
2. If moreover \(R\) is an integral domain and \(p\nmid q_1d\), this holds if and only if \((v,\varepsilon)=\operatorname{Frob}_p^{\,n}\).

## Proof

1. In characteristic \(p\) the map \(x\mapsto\varphi(cx)^{p^n}\) is a ring homomorphism, and \(\mathcal{O}_E=\mathbb{Z}[\beta_K,\zeta]\) by the [[proofs/grh/derivatives-divisibility/different-of-e|theorem on the different]]; so it suffices to compare the two homomorphisms at \(\zeta\) and at \(\beta_K=(1+\sqrt{-d})/2\). At \(\zeta\): \(c\zeta=\zeta^{\varepsilon}\), so \((c\zeta)^{p^n}=\zeta^{\varepsilon p^n}=\sigma_u\zeta\), because \(\varepsilon p^n\) is prime to \(q_1\). At \(\beta_K\): \(p\ne2\) (as \(2\mid q_1\)), so \(2\) is invertible in \(R\) and one may compare at \(\sqrt{-d}=2\beta_K-1\). Now \(\sigma_v\) fixes \(\sqrt{-d}\in K\), \(c\sqrt{-d}=\varepsilon\sqrt{-d}\), and \(\varphi(\sqrt{-d})^{p^n}=\chi_K(p)^n\varphi(\sqrt{-d})\). Indeed \(\varphi(\sqrt{-d})^{p}=(-d)^{(p-1)/2}\varphi(\sqrt{-d})\), and in characteristic \(p\): if \(p\ne d\), [[?c:Euler's criterion|Euler's criterion]] gives \((-d)^{(p-1)/2}=\left(\frac{-d}{p}\right)\), and \(\left(\frac{-d}{p}\right)=\left(\frac{-1}{p}\right)\left(\frac{d}{p}\right)=\left(\frac{p}{d}\right)=\chi_K(p)\) by [[?c:quadratic reciprocity|quadratic reciprocity]], as \(d\equiv3\pmod4\); if \(p=d\), both \((-d)^{(p-1)/2}\) and \(\chi_K(p)\) vanish in \(R\). Iterating \(n\) times gives the claim (the source proves this as [[?lean:New.eq_map_betaK_pow_iff|a lemma on \(\beta_K\)]]).

2. Since \(p\nmid q_1\), \(\varphi(\zeta)\) is a primitive \(q_1\)-th root of unity in the domain \(R\), and \(\sigma_t\zeta=\zeta^{a_t}\) with \(a_t\) the class naming \(t\); so \(\varphi(\sigma_v\zeta)=\varphi(\sigma_u\zeta)\) iff \(v=u\). Since \(\varphi(\sqrt{-d})^2=-d\ne0\) in \(R\) and \(1\ne-1\) in \(R\), the second condition says \(\varepsilon=\chi_K(p)^n\) (both are \(\pm1\)). Together: \((v,\varepsilon)=(\nu_{\chi_K(p)^np^n},\chi_K(p)^n)=\operatorname{Frob}_p^n\). \(\blacksquare\)

## References

1. Lean: `New.Parameters.forall_map_galOfPlaceInt_eq_pow_iff`, `New.Parameters.map_galOfPlaceInt_eq_pow_iff_eq_frobElem_pow`, `New.Parameters.frobElem` in `src/New/Derivatives/Field/PrimeDecomposition.lean`.
