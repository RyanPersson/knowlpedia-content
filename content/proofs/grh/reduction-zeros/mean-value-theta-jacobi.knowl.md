+++
id = "proofs/grh/reduction-zeros/mean-value-theta-jacobi"
title = "A mean value estimate for theta series with Jacobi symbols"
kind = "theorem"
summary = "The sum over v up to T^2 of |theta_v(u)|^2, with coefficients alpha_n (-v/n odd part), is O(T^2 u^(-2 delta)) for u >= 1/T; consequently the sum of the tail integrals is O(T^(2+delta))."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.sum_sq_thetaSeries_jacobiSym_le", "New.exists_summable_mul_norm_sum_jacobiSym_le", "New.exists_summable_ge_of_isSquare", "New.exists_summable_ge_of_isSquare_ordCompl", "New.exists_abs_gaussianMonomial_le_rpow", "New.exists_mul_abs_gaussianMonomial_mul_le", "New.sum_integral_norm_thetaSeries_div_le", "New.sum_thetaTailIntegral_le"]
lean_files = ["src/Lib/Analytic/QuadraticTwist.lean"]
proof_status = "full"
+++

**Theorem (mean value).** Let \(j\in\{0,1\}\) and \(\delta>0\). There is a constant \(C=C(j,\delta)\) such that for all \(T>0\) and all sequences \(\alpha\) with \(\lvert\alpha_n\rvert\le1\), writing \(c_v(n)=\alpha_n\,(-v/n^{\circ})\) (Jacobi symbol, \(n^\circ\) the odd part of \(n\)) and \(\theta_v=\theta_{c_v}\) for the [[proofs/grh/reduction-zeros/theta-series-of-coefficients|theta series]] of parity \(j\):

1. for all \(u\ge1/T\): \(\displaystyle\sum_{1\le v\le T^{2}}\lvert\theta_v(u)\rvert^{2}\le C\,T^{2}u^{-2\delta}\);
2. \(\displaystyle\sum_{1\le v\le T^{2}}\int_{1/T}^\infty\lvert\theta_v(u)\rvert\frac{du}u\le\frac{\sqrt C}{\delta}\,T^{2+\delta}\);
3. \(\displaystyle\sum_{1\le v\le T^{2}}J(c_v,T)\le\frac{2\sqrt C}{\delta}\,T^{2+\delta}\), with \(J\) the [[proofs/grh/reduction-zeros/theta-tail-integral-and-mollifier|tail integral]].

The sums are over all integers \(v\), prime or not.

## Proof

*Expansion.* Since \((-v/n^\circ)(-v/m^\circ)=(-v/(nm)^\circ)\) and the series converge absolutely,
\[
\sum_{v\le T^2}\lvert\theta_v(u)\rvert^2=\sum_{n,m\ge1}\alpha_n\overline{\alpha_m}\;u\,w_j(nu)w_j(mu)\sum_{v\le T^{2}}\Bigl(\frac{-v}{(nm)^{\circ}}\Bigr).
\]
It suffices to find a summable family \(M(n,m)\ge0\), depending only on \(j,\delta\), with
\[
u\,\lvert w_j(nu)\rvert\lvert w_j(mu)\rvert\,\Bigl\lvert\sum_{v\le T^{2}}\Bigl(\frac{-v}{(nm)^{\circ}}\Bigr)\Bigr\rvert\le M(n,m)\,T^{2}u^{-2\delta}\qquad(u\ge1/T); \tag{1}
\]
then 1 holds with \(C=\sum M(n,m)\).

*Decay of the weight.* For every \(A>0\), \(\lvert w_j(x)\rvert\le3e^{-2x}\le3e^{-x}\le3A^{A}x^{-A}\) for \(x>0\) (from \((x/A)^{A}\le e^{x}\)). Hence \(u\lvert w_j(nu)\rvert\lvert w_j(mu)\rvert\le C_A\,u^{1-2A}(nm)^{-A}\).

*Pairs with \((nm)^{\circ}\) a square.* Bound the inner sum by \(T^{2}\) and take \(A=\tfrac12+\delta\): the left side of (1) is at most \(C_A\,u^{-2\delta}(nm)^{-1/2-\delta}\,T^2\). The terms \((nm)^{-\sigma}\), \(\sigma=\tfrac12+\delta>\tfrac12\), over such pairs have a summable majorant \(W\): if \(k\,nm=r^{2}\) with \(k\in\{1,2\}\), put \(g=\gcd(kn,r)\), \(kn=bg\), \(r=cg\) with \(\gcd(b,c)=1\); then \(bm=c^{2}g\), so \(b\mid g\), \(g=ab\), and \(kn=ab^{2}\), \(m=ac^{2}\), \(knm=(abc)^{2}\). Each triple \((a,b,c)\) determines \((n,m)\), and \(\sum_{a,b,c}(abc)^{-2\sigma}=\zeta(2\sigma)^{3}<\infty\). If \((nm)^\circ\) is a square then \(nm\) or \(2nm\) is a square, according to the parity of the exponent of \(2\); so \(W=W_1+2^{\sigma}W_2\) works.

*Other pairs.* By the [[proofs/grh/reduction-zeros/jacobi-symbol-sums|bound for Jacobi symbol sums]] the inner sum is at most \(2(1+2/\delta)(nm)^{1/2+\delta/2}\). With \(A=\tfrac32+\delta\) the left side of (1) is at most a constant times \(u^{-2-2\delta}(nm)^{-1-\delta/2}\), and \(u^{-2}\le T^{2}\). The family \(n^{-1-\delta/2}m^{-1-\delta/2}\) is summable.

2. By the [[linear-algebra/cauchy-schwarz-inequality|Cauchy–Schwarz inequality]] over the at most \(T^{2}\) values of \(v\) and part 1, \(\sum_v\lvert\theta_v(u)\rvert\le\sqrt{T^{2}\cdot CT^{2}u^{-2\delta}}=\sqrt C\,T^{2}u^{-\delta}\) for \(u\ge1/T\). Integrate: \(\int_{1/T}^\infty u^{-\delta-1}du=T^{\delta}/\delta\).

3. \(J(c_v,T)\) is the sum of the tail integrals for \(c_v\) and for \(\mu c_v\); the latter has the same form with \(\alpha\) replaced by \(\alpha\mu\). Apply 2 twice. \(\blacksquare\)

## Remarks

The source describes part 1 as a form of an estimate of Elliott, replacing Heath-Brown's quadratic large sieve: the coefficients are bounded, the weight is fixed, and the effective length \(1/u\) of the sums is at most \(T\), the square root of the range of \(v\).

## References

1. Lean: `New.sum_sq_thetaSeries_jacobiSym_le`, `New.sum_integral_norm_thetaSeries_div_le`, `New.sum_thetaTailIntegral_le` and the auxiliary declarations in the front matter, in `src/Lib/Analytic/QuadraticTwist.lean`.
2. Named in the head of the Lean file: M. Jutila, *On mean values of Dirichlet polynomials with real characters*, Acta Arith. 27 (1975); D. R. Heath-Brown, *A mean value estimate for real character sums*, Acta Arith. 72 (1995).
