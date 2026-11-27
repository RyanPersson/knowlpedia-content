+++
id = "proofs/grh/spanning-unfolding-a/bessel-quotient-as-union-of-class-quotients"
title = "The quotient [R] modulo the level is the disjoint union of the quotients U_c backslash R(F_infinity)"
kind = "theorem"
summary = "Integrals over [R] of functions right invariant under J' = R(A_f) cap J are vol(J') times the sum over classes of integrals over U_c backslash R(F_infinity) along the class sections."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.exists_integral_besselMeasure_eq_sum", "New.Filling.Fits.isCutoff_sum_classWeight", "New.Filling.Fits.exists_ratBessel_mul_mem_coset", "New.Filling.Fits.eq_and_exists_classUnipotent_of_mem_coset", "New.Filling.Fits.exists_eq_unipotent_mul_inclX", "New.Filling.Fits.sourceFn_mul_of_mem_stdPrincipalLevel", "New.Filling.Fits.adelicToFin_adelicEquiv_mem_besselU"]
lean_files = ["src/New/Spanning/Unfolding/SeriesPeriod.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity (with fixed Weil data), \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], and \(V\) with grading \(Y\) a space [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fitting]] \(S\). Let \(R(F)\) be the rational points of the Bessel group \(R(\mathbb A)\) ([[?lean:New.Grading.ratBessel|rational Bessel group]]), \([R]=R(F)\backslash R(\mathbb A)\) with its [[?lean:New.Grading.besselMeasure|quotient measure]], and \(J'=R(\mathbb A_f)\cap J_M\).

1. *(Orbits.)* For every \(r\in R(\mathbb A)\) there are \(\gamma\in R(F)\) and a class \(c\) with \((\gamma r)_f\in x_cJ_M\). If \(g_f\in x_dJ_M\), \(\gamma\in R(F)\) and \((\gamma g)_f\in x_cJ_M\), then \(c=d\) and \(\gamma\) is the image of an element of \(\mathsf U_c(M)\).
2. *(Cutoff.)* The sum \(\sum_c\omega_c\) of the [[proofs/grh/spanning-unfolding-a/class-sections-and-class-weights|class weights]] is a cutoff for the action of \(R(F)\) on \(R(\mathbb A)\): \(\sum_{\gamma\in R(F)}\sum_c\omega_c(\gamma r)=1\) for all \(r\).
3. *(Integration.)* There is a real constant \(\operatorname{vol}_{J'}\ne0\) such that for every measurable \(F\) on \(R(\mathbb A)\) that is left \(R(F)\)-invariant, right \(J'\)-invariant and integrable on \([R]\): each \(s\mapsto\beta_c(\theta(s))F(s,x_c)\) is integrable on \(R(F_\infty)\), and
\[
\int_{[R]}F=\operatorname{vol}_{J'}\sum_c\int_{R(F_\infty)}\beta_c(\theta(s))\,F(s,x_c)\,ds .
\]
4. *(Level of the source function.)* If \(k\in J'\), then \((1,k)=u\cdot j_Y(1,a)\) with \(u\in U(\mathbb A)\), \(\chi_R(u)=1\), and \(a\) in the source level. Consequently, if \(\jmath c_Y=-(M\varpi)^{-1}\) and \(\psi\) is an [[?c:Algebraic modular form|algebraic form]] fixed by the source level, the source function \(\mathcal W_{t,\eta\psi}\) is right invariant under \(J'\).

## Proof

**1.** *Existence.* Write \(r=n\cdot j_Y(a)\) with \(n\in U(\mathbb A)\), \(a\in H(\mathbb A)\). Decompose \(a_f\eta=\delta\,c_{\mathrm{out}}\,k\) with \(\delta\) a rational point of \(H\), \(c\) a class and \(k\) in the source level (definition of the classes as [[?c:Double coset|double cosets]]). By [[?c:Strong approximation for unipotent groups|strong approximation]] for the unipotent group ([[?lean:New.Filling.exists_besselU_approx|strong approximation for \(\mathsf U\)]]) there is a rational \(u\in\mathsf U\) with \(y^{-1}n_f^{-1}u_f\,y\in K(M)\), where \(y=\iota(a_f\eta)\) and \(n_f\) is the finite part of \(n\) in the lattice basis. Then \(\gamma=\delta^{-1}u^{-1}\in R(F)\), and by property 2 of class sections the condition \((\gamma r)_f\in x_cJ_M\) reads \(h_c^{-1}\iota(\eta)\psi((\gamma r)_f)\in K(M)\); computing with \(\psi(g_f)=\iota(\eta)^{-1}\alpha(g)_f\iota(\eta)\) this element is \(\iota(k)\) times the inverse of the approximation error, and \(\iota(k)\in K(M)\) because the source level is the preimage of \(K(M)\).
*Uniqueness.* Let \(\gamma\) be the image of a rational \(\sigma\); it lies in the Bessel subgroup of \(S\). The two conditions give \(h_c^{-1}\sigma_fh_d\in K(M)\). A rational element of the Bessel subgroup with this property has \(c=d\) and lies in \(\mathsf U_c(M)\) ([[?lean:New.Filling.eq_and_mem_classUnipotent_of_besselS|terms of the Bessel subgroup at the identity]]).

**2.** By 1 (existence) we may assume \(r_f\in x_dJ_M\) for some \(d\). By 1 (uniqueness), \(\omega_c(\gamma r)\ne0\) forces \(c=d\) and \(\gamma\) in the image of \(\mathsf U_d(M)\). For \(u\in\mathsf U_d(M)\), property 3 of class sections gives \((ur)_f\in x_dJ_M\) and \(\omega_d(ur)=\beta_d(\theta(u_\infty r_\infty))\). So the sum is \(\sum_{u\in\mathsf U_d(M)}\beta_d(\theta(u_\infty r_\infty))=1\).

**3.** By 2, \(\int_{[R]}F=\int_{R(\mathbb A)}\bigl(\sum_c\omega_c\bigr)F=\sum_c\int_{R(\mathbb A)}\omega_cF\) ([[?lean:New.IsCutoff.integral_orbitMeasure|integral over a quotient through a cutoff]]; each \(\omega_cF\) is integrable, being dominated by \((\sum_c\omega_c)\lvert F\rvert\)). The function \(\omega_cF\) vanishes off \(R(F_\infty)\times x_cJ'\) and on this set equals \(\beta_c(\theta(s))F(s,x_c)\), by the right \(J'\)-invariance of \(F\). For such functions, \(\int_{R(\mathbb A)}=\operatorname{vol}_{J'}\int_{R(F_\infty)}\) with a nonzero constant ([[?lean:New.Grading.exists_integral_eq_mul_integral_besselReal|integration over a coset of the level]]), together with the integrability of the function of \(s\).

**4.** Let \(a\) be the finite component of the Levi part of \((1,k)\) and \(u=(1,k\,j_Y(a)^{-1})\in U(\mathbb A)\). In the lattice basis of \(S\), \(\psi(u_f)\) lies in the unipotent group (the Bessel subgroup, which contains \(\iota(\eta)\), normalises it) and \(\psi(u_f)\iota(a)=\psi(k)\in K(M)\). The Levi factor of an element of a unitary level lies in that level ([[?lean:New.mem_unitaryLevel_of_besselU_mul|the Levi factor of an element of a unitary level]]), so \(\iota(a)\in K(M)\), i.e. \(a\) is in the source level, and then \(\psi(u_f)\in K(M)\). The unipotent character is trivial on unipotent elements conjugate into \(K(M)\) ([[?lean:New.Filling.unipotentChar_eq_of_mem_principalLevel|the unipotent character on the principal level]]), and \(u\) has trivial real part, so \(\chi_R(u)\) equals the finite unipotent character of \(u\), which is \(1\).
For the consequence: \(\mathcal W(r\,(1,k))=\mathcal W(r\,u\,j_Y(1,a))\); translation by \(a\) fixes \(\eta\psi\) (\(a\) is in the source level and \(\eta\) is central); and \(\mathcal W(ru)=\chi_R(ru)\cdot(\text{coefficient at the Levi part of }r)=\chi_R(r)\chi_R(u)\cdots=\mathcal W(r)\) by the proposition on the [[proofs/grh/spanning-unfolding-a/bessel-character-extends-generic-character|Bessel character]].

## References

1. Lean: `New.Filling.Fits.exists_integral_besselMeasure_eq_sum` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
2. Lean: `New.Filling.Fits.isCutoff_sum_classWeight` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
3. Lean: `New.Filling.Fits.exists_ratBessel_mul_mem_coset` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
4. Lean: `New.Filling.Fits.eq_and_exists_classUnipotent_of_mem_coset` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
5. Lean: `New.Filling.Fits.exists_eq_unipotent_mul_inclX` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
6. Lean: `New.Filling.Fits.sourceFn_mul_of_mem_stdPrincipalLevel` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
7. Lean: `New.Filling.Fits.adelicToFin_adelicEquiv_mem_besselU` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
