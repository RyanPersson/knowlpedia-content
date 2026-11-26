+++
id = "proofs/grh/upper-divisibility/hecke-transfer-through-the-chain"
title = "Hecke transfer through the lifts at a marked prime"
kind = "theorem"
summary = "At a marked prime, p to the transfer exponent times the chain of lifts after the Hecke operator of index r is a p-integral combination of Hecke operators of index at most r after the chain."
aliases = ["Hecke transfer"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsWeakChainDatum.exists_hecke_transfer", "New.Data.IsWeakChainDatum.exists_sum_heckeSplit_chain_eq_pow_smul", "New.Data.IsWeakChainDatum.exists_sum_heckeSplit_lift_eq_pow_smul", "New.Data.IsWeakChainDatum.exists_sum_heckeSplit_lift_eq_smul", "New.Data.IsWeakChainDatum.exists_heckePolyOp_lift", "New.Data.heckePolyOp_mul_apply", "New.Data.pow_mul_pow_choose_two_dvd", "New.Data.mul_le_transferExponent", "New.Data.IsMarked.norm_baseChange_atUniformizer", "New.Data.IsMarked.exists_q_eq_sq", "New.Data.IsMarked.charUnramifiedAt_rankTwist", "New.Data.IsMarked.notMem_asIdeal", "New.Data.IsWeakChainDatum.projOn_translateDatum_eq_self", "New.Data.IsWeakChainDatum.liftKernel_omega_translateDatum_of_mem_maxCompactAt"]
lean_files = ["src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]], \(\vartheta\) a twist, \(\Psi\) a [[?lean:New.Data.IsWeakChainDatum|weak chain datum]] for \(\vartheta\), \(p\) a prime not dividing the norm of the modulus of \(\vartheta\), \(\iota\colon\mathbb{C}\to\mathbb{C}_p\), \(O_\iota\) the ring of \(p\)-integral complex numbers, \(\Lambda\) a [[proofs/grh/upper-divisibility/marked-set-of-primes|marked set]] and \(\mathfrak l\in\Lambda\), of norm \(q\). For \(x\in\operatorname{supp}\Psi\) let \(\Theta_{x,e}\) be the lift \(X_e\to X_{e+1}\) with datum the translated vacuum \(\Phi^{0}_{x,e}\), and \(F_{x,e}=\Theta_{x,e-1}\circ\cdots\circ\Theta_{x,0}\). Let \(T_i\) be the Hecke operator of the double coset of \(\operatorname{diag}(\varpi1_i,1)\) at \(\mathfrak l\) (on forms on any \(X_e\)), and \(T(U)=\sum_i(-U)^{i}q^{\binom i2}T_i\) the [[?lean:New.heckePolyOp|Hecke polynomial]].

**Theorem.**

1. \(q=z^{2}\) with \(z=p^{h}\), \(2h\le f\). The primes \(\mathfrak l,\bar{\mathfrak l}\) contain none of: the norm of the modulus, \(\pi_M\), \(\bar\pi_M\), \(N\). The base change of the character of each lift (twisted by the splitting character according to the rank) is unramified at \(\mathfrak l\), and its value at a uniformiser at \(\mathfrak l\) is a \(p\)-adic unit.
2. For \(x\in\operatorname{supp}\Psi\), \(\Phi^{0}_{x,e}\) is the vacuum at \(\mathfrak l\), and it is fixed by \(\omega(1,b)\) for \(b\) in the maximal compact subgroup at \(\mathfrak l\) of the group of \(X_{e+1}\).
3. (**One lift.**) There is a polynomial \(R\in O_\iota[U]\) with \(R(0)=1\), independent of \(x\), such that \(\Theta_{x,e}\) maps forms spherical at \(\mathfrak l\) to forms spherical at \(\mathfrak l\) and
\[
T(U)\,\Theta_{x,e}\varphi=R(U)\cdot\Theta_{x,e}\,T\bigl(z^{t+1}U\bigr)\varphi\qquad(U\in\mathbb{C}).
\]
Consequently there are \(c_{i,i'}\in O_\iota\), independent of \(x\), with \(\sum_{i'\le i}c_{i,i'}T_{i'}\Theta_{x,e}\varphi=z^{(t+1)i}q^{\binom i2}\,\Theta_{x,e}T_i\varphi\) for \(i\le n_e\); and for \(i\le\mathfrak r\) the same with the factor \(p^{f\mathfrak rt}\) on the right (with other \(p\)-integral coefficients).
4. (**The chain.**) For every \(e\) there are \(c_i\in O_\iota\), independent of \(x\), such that on forms spherical at \(\mathfrak l\)
\[
\sum_{i\le\mathfrak r}c_i\,T_iF_{x,e}\varphi=p^{\,ef\mathfrak rt}\,F_{x,e}T_{\mathfrak r}\varphi .
\]
For \(e=j+1\le m\) one may replace \(p^{ef\mathfrak rt}\) by \(p^{\nu_p}\), \(\nu_p=\mathfrak rf(n_m+\mathfrak r)\) the [[proofs/grh/upper-divisibility/classes-of-primes|transfer exponent]], keeping \(p\)-integral coefficients; for \(j\ge m\) the identity with \(p^{\nu_p}\) still holds with complex coefficients.

## Proof

(1) The order \(o\) of \(u(-p)\) is even and \(q=p^{o}\) ([[proofs/grh/upper-divisibility/orbits-at-an-exceptional-prime|orbits]]); \(o\le\lvert\Phi\rvert=f\). \(\mathfrak l\) and \(\bar{\mathfrak l}\) contain \(p\), which is prime to the modulus and to \(MN=\pi_M\bar\pi_MN\). The tame part of the lift characters is supported at the chosen places and the modulus, so the characters are unramified at \(\mathfrak l\). The \(p\)-adic absolute value of the value at a uniformiser is \(p\) to the difference of the sums of the weights \(\kappa_e(\tau)\) over the places inducing \(\mathfrak l\) and those inducing \(\bar{\mathfrak l}\), which is \(0\) by the [[proofs/grh/upper-divisibility/properties-of-marked-sets|balance]].

(2) By the [[proofs/grh/upper-divisibility/data-of-a-weak-chain-datum-are-standard|integrality lemma]], \(x_e\) is integral at \(\mathfrak l,\bar{\mathfrak l}\), so the projection on the vacuum at \(\mathfrak l\) fixes \(\Phi^{0}_{x,e}\). On a vector that is the vacuum at \(\mathfrak l\), the maximal compact subgroup acts through the character of the determinant, which is unramified, hence trivially ([[?lean:New.pairWeil_eq_smul_of_projOn_eq|`pairWeil_eq_smul_of_projOn_eq`]], quoted).

(3) The identity for the Hecke polynomials is the transfer of spherical Hecke operators through a theta lift whose datum is the vacuum at a split place, for ranks \(n_{e+1}=n_e+(t+1)\) ([[?lean:New.hecke_transfer_of_pairing|`hecke_transfer_of_pairing`]], quoted): with \(\chi\) the unit value of the lift character at the uniformiser and Frobenius values \(z^{n_i}\chi\) on \(X_i\), it gives \(R(U)=\prod_{k\le t}\bigl(1-q^{k}z^{n_e}\chi U\bigr)\) and the rescaling \(q^{t+1}z^{n_e}\chi/(z^{n_{e+1}}\chi)=z^{t+1}\). The coefficients of \(R\) are \(p\)-integral and \(R(0)=1\), so \(R\) is invertible as a power series over \(O_\iota\); dividing by \(R\) and comparing the coefficients of \(U^{i}\) gives the second statement, with \(c_{i,i'}=(-1)^{i+i'}q^{\binom{i'}2}[U^{i}](R^{-1}U^{i'})\); only \(i'\le i\) contribute. Finally \(z^{(t+1)i}q^{\binom i2}=p^{h(ti+i^{2})}\) divides \(p^{f\mathfrak rt}\) for \(i\le\mathfrak r\le t\), as \(h(ti+i^2)\le2h\mathfrak rt\le f\mathfrak rt\); and \(\mathfrak r\le k\le n_e\).

(4) Induction on \(e\); for \(e=0\) take \(c_i=[i=\mathfrak r]\). Apply \(\Theta_{x,e}\) to the identity for \(e\), multiply by \(p^{f\mathfrak rt}\) and move each \(T_i\) (\(i\le\mathfrak r\)) through \(\Theta_{x,e}\) by (3): the new coefficients are \(c'_{i'}=\sum_{i'\le i\le\mathfrak r}c_id_{i,i'}\). For \(e\le m\): \(ef\mathfrak rt\le\mathfrak rf\cdot mt\le\mathfrak rf(n_m+\mathfrak r)=\nu_p\), so multiplying by the integer power \(p^{\nu_p-ef\mathfrak rt}\) keeps integrality; for larger \(e\) the same factor is a power of \(p\) with integer exponent of either sign. \(\blacksquare\)

*Status.* The transfer of Hecke polynomials through a lift (`hecke_transfer_of_pairing`) is the main quoted input; the power-series step uses [[?lean:New.sum_coeff_invOfUnit_smul_eq|`sum_coeff_invOfUnit_smul_eq`]], also quoted. The remaining steps were checked against the Lean proofs.

## References

1. Lean: `New.Data.IsWeakChainDatum.exists_hecke_transfer` and the lemmas listed in the front matter, in `src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean`.
