+++
id = "proofs/grh/derivatives-divisibility/exponent-on-one-curve"
title = "The exponent on one curve"
kind = "theorem"
summary = "At a non-split prime, theta(varpi z) is an integral series times exp(c_varpi Xi), where Xi is integral and congruent modulo pi_p to a combination of the monomials (z^(p^e) z)^(p^j) with e in I_p; at an inert prime the leading coefficients are units."
aliases = ["exponent on one curve"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.exists_exponent_tsum", "New.CMLattice.exists_smul_negLogThetaPart_sub_rescale_eq", "New.CMLattice.exists_smul_rescale_negLogThetaPart_sub_rescale_eq", "New.CMLattice.exists_functional_equation_exponentSeries", "New.CMLattice.norm_coeff_exponentSeries_sub_le", "New.CMLattice.exists_seriesToCp_eq_exponentSeries_of_inert", "New.CMLattice.exists_seriesToCp_eq_exponentSeries_of_ramified", "New.CMLattice.norm_coeff_exponentSeries_eq_one", "New.CMLattice.exists_eq_exponentSeries_dvd_sub_tsum_of_inert", "New.CMLattice.exists_exponentSeries_tsum_of_ramified", "New.CMLattice.exists_congruencePart_eq_smul_formalParam_pow_add", "New.exists_congruencePart_eq_smul_X_pow_add", "New.norm_piPrime_mul_pow_leastFlatDegree_div", "New.norm_piPrime_pow_div_le", "New.C_dvd_pow_sub_primePowerSeries_odd_mul_even", "New.C_dvd_sq_sub_primePowerSeries_univ_sq", "New.ramified_or_inert", "New.reducePiPrime", "New.summable_smul_X_pow_mul_X_pow"]
lean_files = ["src/New/Derivatives/FormalGroup/Exponent.lean"]
proof_status = "full"
+++

**Theorem (the exponent on one curve).** Let \(d\equiv 7\pmod 8\) be a prime, \(C\) a CM lattice for \(K=\mathbb{Q}(\sqrt{-d})\) with theta function \(\theta\) (see the [[proofs/grh/derivatives-divisibility/cm-curve-setting|CM lattice]]), and \(p\) a prime with \(\chi_K(p)\ne1\) and a \(p\)-adic place \(\iota_p\). In the notation of the [[proofs/grh/derivatives-divisibility/p-adic-setting|\(p\)-adic setting]], there are \(\varpi\in\mathbb{C}_p\), integral series \(\Xi,W\in\mathcal{O}[[z]]\) in one variable, and numbers \(\lambda_{e,j}\in\mathcal{O}\) \((e,j\ge 0)\) such that

1. \(\lvert\varpi\rvert=p^{-\rho_p}\) and \(\Xi(0)=0\);
2. \(\theta(\varpi z)=W\cdot\exp(c_\varpi\,\Xi)\), with \(c_\varpi=\varpi^{p+1}/p\);
3. \(\displaystyle\Xi\equiv\sum_{e\in I_p^\circ}\ \sum_{j\ge0}\lambda_{e,j}\,\bigl(z^{p^e}\cdot z\bigr)^{p^j}\pmod{\pi_p}\);
4. if \(p\) is inert in \(K\), then \(\lambda_{e,0}\) is a unit of \(\mathcal{O}\) for every odd \(e\).

More precisely one can take \(\lambda_{e,j}=\lambda\) for all \(e,j\) with one unit \(\lambda\) if \(p\) is inert; and \(\lambda_{0,0}=\lambda/2\), \(\lambda_{0,j}=\lambda\) \((j\ge1)\), \(\lambda_{e,j}=2\lambda\) \((e\ge1)\) with some \(\lambda\in\mathcal{O}\) if \(p=d\).

## Proof

Write \(\pi=\iota_p\pi_p\), \(q=q_p\), and let \(g^\flat\), \(i_0\), \(\Xi_1\) be as in the [[proofs/grh/derivatives-divisibility/exponent-series|exponent series]]. By fact 4 of the setting choose \(\varpi\) with \(\lvert\varpi\rvert=p^{-\rho_p}\) and an integral \(Y\) with \(T(\varpi z)=\varpi Y\) and \(Y\equiv\sum_{j}z^{q^j}\pmod\pi\). Then \(\lvert\varpi\rvert^{q-1}=\lvert\pi\rvert\). By property 3 of the exponent series, \(\theta(\varpi z)=W\exp(c_\varpi\Xi_1)\) with \(W\) integral. It remains to show that \(\Xi_1\) is integral (then \(\Xi=\Xi_1\); it has no constant term) and to determine it modulo \(\pi\).

**Step 2: the functional equation.** By the [[proofs/grh/derivatives-divisibility/frobenius-congruence-for-theta|Frobenius congruence]], \(q\,g(z)-g(\pi z)=\pi G\) with \(G\in\mathcal{O}[[y]]=\mathcal{O}[[T]]\). Taking on both sides the parts in the degrees \(\equiv p+1\equiv i_0\pmod{q-1}\) gives \(q\,g^\flat(z)-g^\flat(\pi z)=\pi G^\flat\). Write \(G=F(T)\) with \(F\) integral. Since \(T\) has terms only in degrees \(\equiv1\pmod{q-1}\), \(G^\flat=F^\flat(T)\), where \(F^\flat\) is the part of \(F\) in the degrees \(\equiv i_0\); and as \(i_0<q-1\), \(F^\flat=l\,X^{i_0}+X^{i_0+q-1}F'\) with \(l\in\mathcal{O}\), \(F'\) integral. So
\[
q\,g^\flat(z)-g^\flat(\pi z)=\pi\bigl(l\,T^{i_0}+T^{i_0+q-1}H'\bigr),\qquad H'\in\mathcal{O}[[T]] .
\]
Replace \(z\) by \(\varpi z\); with \(f=g^\flat(\varpi z)\), \(T(\varpi z)=\varpi Y\), and \(H'(\varpi z)\) integral (fact 3),
\[
q\,f(z)-f(\pi z)=\pi\varpi^{i_0}\bigl(l\,Y^{i_0}+\varpi^{q-1}R\bigr),\qquad R=Y^{i_0+q-1}H'(\varpi z)\in\mathcal{O}[[z]] .
\]
Divide by \(-q\,c_\varpi\) and compare coefficients of \(z^n\): with \(u=-\pi\varpi^{i_0}/(q\,c_\varpi)\),
\[
\Bigl(1-\frac{\pi^n}{q}\Bigr)\,[z^n]\Xi_1=u\,l\,[z^n]Y^{i_0}+u\,\varpi^{q-1}\,[z^n]R .
\]
The number \(u\) has norm \(1\): if \(p\) is inert, \(\pi=p\), \(i_0=p+1\), \(q=p^2\) and \(u=-1\); if \(p=d\), \(q=p\), \(i_0=2\) and \(u=-\pi/\varpi^{p-1}\) with \(\lvert\varpi\rvert^{p-1}=\lvert\pi\rvert\). As \(\lvert\varpi^{q-1}\rvert=\lvert\pi\rvert\), with \(\lambda=ul\in\mathcal{O}\):
\[
\Bigl(1-\frac{\pi^n}{q}\Bigr)\,[z^n]\Xi_1\equiv\lambda\,[z^n]Y^{i_0}\pmod{\pi}\qquad\text{for all } n ,\tag{FE}
\]
where a congruence modulo \(\pi\) between elements of \(\mathbb{C}_p\) means that the difference has norm at most \(\lvert\pi\rvert\).

**Step 3: solving (FE).** For \(n>2\), \(\pi^n/q=\pm\pi^{n-2}\) has norm at most \(\lvert\pi\rvert<1\), so \(1-\pi^n/q\) is a unit congruent to \(1\), and (FE) gives \([z^n]\Xi_1\equiv\lambda[z^n]Y^{i_0}\). For \(n<i_0\), \([z^n]\Xi_1=0\) and (FE) gives the same congruence.

*Inert case.* Here \(i_0=p+1>2\), so every \(n\) is covered: \(\Xi_1\) is congruent coefficientwise to the integral series \(\lambda Y^{p+1}\); hence \(\Xi_1\) is integral and \(\Xi\equiv\lambda Y^{p+1}\pmod\pi\). Now \(q=p^2\), so \(Y\equiv P_{\mathrm{even}}:=\sum_{i\ \mathrm{even}}z^{p^i}\). Modulo \(\pi\) the ring has characteristic \(p\) (as \(\pi\mid p\)), so \(P_{\mathrm{even}}^{\,p}\equiv P_{\mathrm{odd}}:=\sum_{i\ \mathrm{odd}}z^{p^i}\) and
\[
Y^{p+1}\equiv P_{\mathrm{odd}}P_{\mathrm{even}}=\sum_{e\ \mathrm{odd}}\ \sum_{j\ge 0}\bigl(z^{p^e}z\bigr)^{p^j},
\]
because each exponent \(p^a+p^b\) with \(a\) odd and \(b\) even is \((p^e+1)p^j\) for exactly one pair (\(j=\min(a,b)\), \(e=\lvert a-b\rvert\), which is odd), and for odd \(p\) distinct pairs \((e,j)\) give distinct degrees. This is 3 with \(\lambda_{e,j}=\lambda\).

*Ramified case \(p=d\).* Here \(i_0=2\), and only \(n=2\) is left. There \(1-\pi^2/q=1-(-p)/p=2\), so (FE) reads \(2\,\xi\equiv\lambda c\) with \(\xi=[z^2]\Xi_1\), \(c=[z^2]Y^2\). Since \(Y\equiv P:=\sum_{i\ge 0}z^{p^i}\) and \([z^2]P^2=1\), \(c\equiv1\). As \(2\) is a unit,
\[
\xi-\lambda\bigl(c-\tfrac12\bigr)=\tfrac12\bigl((2\xi-\lambda c)+\lambda(1-c)\bigr)\equiv0 .
\]
So \(\Xi_1\) is integral and \(\Xi\equiv\lambda\,(Y^2-\tfrac12z^2)\equiv\lambda\,(P^2-\tfrac12z^2)\pmod\pi\). In \(P^2=\sum_{a,b}z^{p^a+p^b}\) the degree \((p^e+1)p^j\) occurs with coefficient \(1\) if \(e=0\) (\(a=b=j\)) and \(2\) if \(e\ge1\); subtracting \(\tfrac12z^2\) changes the coefficient at \((e,j)=(0,0)\) to \(\tfrac12\). This is 3 with the stated \(\lambda_{e,j}\), and \(I_d^\circ\) is all of \(\mathbb{N}\).

**Step 4: the unit (inert case).** The coefficient of \(z^{p+1}\) in \(\Xi_1=-(p/\varpi^{p+1})\,g^\flat(\varpi z)\) is \(-p\,g_{p+1}\). Comparing the coefficients of \(z^{p-1}\) in \(g''=g''(0)+x\) gives \((p+1)\,p\,g_{p+1}=[z^{p-1}]x\), which is [[proofs/grh/derivatives-divisibility/supersingular-coefficient-unit|a unit]]; and \(p+1\) is a unit. So \([z^{p+1}]\Xi\) is a unit. The coefficient of \(z^{p+1}\) in \(P_{\mathrm{odd}}P_{\mathrm{even}}\) is \(1\), so \(\lambda\equiv[z^{p+1}]\Xi\pmod\pi\); as \(\lvert\pi\rvert<1\), \(\lambda\) is a unit. \(\blacksquare\)

## Remarks

The head of the source file lists earlier bounds for one curve at inert primes, which are not used: Bannai–Kobayashi (algebraic theta functions and \(p\)-adic interpolation of Eisenstein–Kronecker numbers), Bannai–Kobayashi–Yasuda (radius of convergence of the \(p\)-adic sigma function), Fujiwara (divisibilities of special values of real analytic Eisenstein series).

## References

1. Lean: `New.CMLattice.exists_exponent_tsum` and the lemmas before it in `src/New/Derivatives/FormalGroup/Exponent.lean`; the combinatorics of \(\sum z^{p^i}\) is in `src/Lib/General/Algebra/SeriesCongruences.lean` (`New.primePowerSeries`, `New.hasSum_primePowerSeries_odd_mul_even`, `New.hasSum_primePowerSeries_univ_sq_sub`).
