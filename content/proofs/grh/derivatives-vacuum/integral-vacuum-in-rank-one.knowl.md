+++
id = "proofs/grh/derivatives-vacuum/integral-vacuum-in-rank-one"
title = "The integral vacuum in rank one"
kind = "theorem"
summary = "For every s a nonzero multiple of the vacuum of the standard space of rank one has values at finite points that are integral at every prime and whose conjugates over K are at most exp(C q1^2), with C depending only on the parameters."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.exists_mul_vacElem_integral_bounded", "New.Parameters.exists_norm_gal_torsion_value_le", "New.Parameters.sq_q₁_pow_card_infinitePlace_le"]
lean_files = ["src/New/Derivatives/Vacuum/IntegralVacuum.lean"]
proof_status = "outline"
+++

Let \(P\) be [[?lean:New.Parameters|parameters]]. For \(s\in\mathbb{N}\) let \(E=E_s\), \(q_1=q_1(s)\), and let \(\mathrm{vac}\) be the [[?lean:New.Space.vacElem|vacuum]] of the [[?lean:New.stdSpace|standard space]] of rank one over \(E\).

**Theorem.** There is \(C\in\mathbb{N}\), depending only on \(P\), such that for every \(s\) there is \(c\in\mathbb{C}^\times\) with:

(a) for every prime \(p\), every \(p\)-adic place \(\iota_p\) of \(\mathbb{C}\) and every finite adele \(x\) of \(E\): \(\lvert\iota_p(c\cdot\mathrm{vac}(x_f))\rvert_p\le1\);

(b) for every automorphism \(\sigma\) of \(\mathbb{C}\) over \(K\) and every \(x\): \(\lvert\sigma(c\cdot\mathrm{vac}(x_f))\rvert\le\exp(C\,q_1^2)\).

## Proof

*A uniform bound for torsion values.* There is \(M\ge0\), depending only on \(P\), with
\[ \bigl\lvert\sigma\bigl((\tau^{(1)}_{x\Omega_0}\theta_{\mathcal{E}})(0)\bigr)\bigr\rvert\le M\qquad(\sigma\in\operatorname{Aut}(\mathbb{C}/K),\ x\in K). \]
Indeed, by [[?lean:New.CMLattice.complex_multiplication_theta|complex multiplication for theta functions]], \(\sigma\) maps the Taylor series at \(0\) of the translate of \(\theta_{\mathcal{E}}\) by \(x\Omega_0\) to that of the translate of the theta function of the conjugate lattice \(\mathcal{E}^\sigma\) by some point \(x'\Omega\) (\(x'\in K\) close to \(\beta x\), which exists as \(K\) is dense in its finite adeles). Comparing constant terms, the conjugate is a degree-one torsion value of the theta function of \(\mathcal{E}^\sigma\), and these are bounded uniformly over all CM lattices for \(d\) by a Lib lemma (Lean `New.CMLattice.exists_norm_twistedTranslate_theta_le`; asserted here).

*The vector \(F\).* Fix \(s\), write \(N=q_1\), and let \(F\) be a [[proofs/grh/derivatives-vacuum/existence-of-theta-products|theta product]] of level one for \((\mathcal{E},\Omega_0)\) on the rank-one standard space. By [[proofs/grh/derivatives-vacuum/vacuum-as-sum-of-translates|the vacuum as a sum of translates]], \(c\cdot\mathrm{vac}=\sum_{j\in\Gamma}h(a_j)\varrho(b_f)F\) with \(c\ne0\), \(\lvert\Gamma\rvert=(N^2)^{f}\). Evaluating at \(x_f\) (Lean `New.Space.exists_sum_finHeisenbergOp_apply_eq`): there are finite adeles \(w_j,y_j\) with
\[ c\cdot\mathrm{vac}(x_f)=\sum_{j\in\Gamma}\psi(w_j)\,F((y_j)_f), \]
where \(\psi\) is the self-dual additive character of the finite adeles, whose values are roots of unity.

*(a).* The values \(F(y_f)\) are \(p\)-integral (condition 4 of a theta product) and roots of unity are units, so the sum is \(p\)-integral.

*(b).* Fix \(\sigma\) and \(z\). The values of \(F\) at finite points are values at \(0\) of rational translates of \(\Theta_F\) (Lean `New.Space.range_apply_finVec_eq_range_ratShift_entireTheta`), so \(F(z_f)=\theta(\varrho((-\gamma)_f)F)\) for some \(\gamma\in E\), and by condition 2
\[ \lvert\sigma F(z_f)\rvert=\prod_{k<N}\bigl\lvert\sigma\,\vartheta_{k,-\gamma}(0)\bigr\rvert^{N}\le (e^{M})^{N\cdot N}, \]
each factor being a torsion value as above (\(\kappa_k(-\gamma)\in K\)) and \(M\le e^M\). Since \(\sigma\) maps roots of unity to roots of unity,
\[ \lvert\sigma(c\,\mathrm{vac}(x_f))\rvert\le\lvert\Gamma\rvert\,e^{MN^2}=(N^2)^{f}e^{MN^2}. \]
The number of infinite places is \(f\le N\) (it is at most \(\varphi(q_1)\)) and \(N\le e^{N}\), so \((N^2)^f\le e^{2N^2}\). Hence (b) holds with \(C=\lceil M\rceil+2\).

## References

1. Lean: `New.Parameters.exists_mul_vacElem_integral_bounded`, `New.Parameters.exists_norm_gal_torsion_value_le`, `New.Parameters.sq_q₁_pow_card_infinitePlace_le` in `src/New/Derivatives/Vacuum/IntegralVacuum.lean`.
