+++
id = "proofs/grh/derivatives-divisibility/cm-curve-setting"
title = "The CM lattice, its theta function and the ring of integral series in y"
kind = "notation"
summary = "Notation for a lattice with complex multiplication, the functions theta, x, y, the series g = -log theta, the ring of integral series in y and its formal parameter T, with the facts imported from the library."
aliases = ["CM lattice notation", "ring of integral series in y"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = []
lean_files = ["src/New/Derivatives/FormalGroup/FrobeniusCongruence.lean", "src/New/Derivatives/FormalGroup/Exponent.lean"]
+++

**Notation (the CM lattice).** Work in the [[proofs/grh/derivatives-divisibility/p-adic-setting|\(p\)-adic setting]], with the prime \(d\equiv 7\pmod 8\), \(K=\mathbb{Q}(\sqrt{-d})\) and the place \(\iota_p\colon\mathbb{C}\to\mathbb{C}_p\). A [[?lean:New.CMLattice|CM lattice]] \(C\) consists of a [[?c:lattice in the complex plane|lattice]] \(\Lambda\subset\mathbb{C}\) that is stable under multiplication by the [[algebra-fields-galois/ring-of-integers|ring of integers]] \(\mathcal{O}_K\), a point \(t\in\mathbb{C}\) with \(2t\in\Lambda\), \(t\notin\Lambda\) and \(\omega t,\bar\omega t\notin\Lambda\) for \(\omega=(1+\sqrt{-d})/2\), and a number \(a_1\) with \(a_1^2=12\wp(t)\); the lattice is scaled so that \(\wp''(t)=2\). Here \(\wp\) is the [[?c:Weierstrass elliptic function|Weierstrass function]] of \(\Lambda\). Write \(A\) for the area of a fundamental parallelogram of \(\Lambda\), \(H(l,z)=\pi\,\bar l\,z/A\), and \(\chi_\sigma(l)=1\) if \(l\in2\Lambda\), \(\chi_\sigma(l)=-1\) otherwise. The [[?lean:PeriodPair.σ|normalised sigma function]] \(\sigma\) of \(\Lambda\) is an odd entire function with \(\sigma'(0)=1\) and
\[
\sigma(z+l)=\chi_\sigma(l)\,\exp\bigl(H(l,z)+\tfrac12H(l,l)\bigr)\,\sigma(z)\qquad(l\in\Lambda).
\]
It is *not* the classical [[?c:Weierstrass sigma function|Weierstrass sigma function]] \(\sigma_W\): the two differ by a factor \(\exp(cz^2)\) with a constant \(c\) depending on \(\Lambda\). The following functions and series are attached to \(C\).

* \(\theta\) is the [[?lean:New.CMLattice.θ|theta function of \(C\)]]: \(\theta(z)=(T_t\sigma)(z)/(T_t\sigma)(0)\), where \((T_uf)(z)=\exp\bigl(-H(u,z)-\tfrac12H(u,u)\bigr)f(z+u)\) is the twisted translation of degree one by \(u\); so \(\theta(0)=1\), and \(\theta\) is even.
* \(x(z)=\wp(z+t)-\wp(t)\) and \(y(z)=\tfrac12\bigl(\wp'(z+t)-a_1x(z)\bigr)\); they satisfy \(y^2+a_1xy=x^3+x\), \(x'=2y+a_1x\) and \(y'=1+3x^2-a_1y\).
* The same letters \(\theta,x,y\) denote the Taylor series at \(0\), read in \(\mathbb{C}_p[\![z]\!]\) through \(\iota_p\). Then \(x=z^2+\cdots\) and \(y=z+\cdots\).
* \(g=-\log\theta\in\mathbb{C}_p[\![z]\!]\), with \(g(0)=0\), so \(\theta=\exp(-g)\); it has no linear term and \(g''=g''(0)+x\).
* \(\mathcal{O}[\![y]\!]\subset\mathbb{C}_p[\![z]\!]\) is the ring of all \(G(y)\) with \(G\) an integral series in one variable.
* The **formal parameter** \(T\) is the part of \(y\) in the degrees \(\equiv 1 \pmod{q_p-1}\); it has the form \(z+\cdots\) and \(\mathcal{O}[\![y]\!]=\mathcal{O}[\![T]\!]\).

## Facts imported from the library

The following statements, proved in the supporting library, are used in this chapter (always for a prime \(d\equiv7\pmod 8\)).

1. [[?lean:New.CMLattice.taylorVia_translatedX_mem_integralSeriesRing|\(x\in\mathcal{O}[\![y]\!]\)]], and [[?lean:New.CMLattice.derivative_mem_integralSeriesRing|\(\mathcal{O}[\![y]\!]\) is stable under \(d/dz\)]]; \(\lvert\iota_p a_1\rvert\le 1\).
2. [[?lean:New.CMLattice.norm_coeff_le_one_of_lt|Integrality in low degrees]]: a series in \(\mathcal{O}[\![y]\!]\) has integral coefficients in the degrees \(<q_p\).
3. [[?lean:New.CMLattice.rescale_mem_range_seriesToCp|Integrality after scaling]]: if \(\lvert\varpi\rvert\le p^{-\rho_p}\) and \(H\in\mathcal{O}[\![y]\!]\), then \(H(\varpi z)\) is integral.
4. [[?lean:New.CMLattice.exists_scaled_formalParam|The scaled parameter]]: there are \(\varpi\in\mathbb{C}_p\) with \(\lvert\varpi\rvert=p^{-\rho_p}\) and an integral series \(Y\) with \(T(\varpi z)=\varpi\,Y(z)\) and \(Y\equiv\sum_{j\ge 0}z^{q_p^{\,j}}\pmod{\pi_p}\).
5. [[?lean:New.CMLattice.derivative_derivative_negLogTheta|\(g''=g''(0)+x\)]], and [[?lean:New.CMLattice.norm_sqrt_mul_coeff_two_negLogTheta_le_one|\(\lvert\iota_p(\sqrt{-d})\,g''(0)\rvert\le 1\)]].
6. For every \(\zeta\in\mathbb{C}_p\) with \(\zeta^{q_p-1}=1\), [[?lean:New.CMLattice.expSubst_rescale_sub_mem_of_pow_eq_one|\(\exp\bigl(\zeta^{-(p+1)}g(\zeta z)-g(z)\bigr)\in\mathcal{O}[\![y]\!]\)]].
7. Closure properties of \(B=\mathcal{O}[\![y]\!]\): if \(m\) is prime to \(p\), \(h(0)=0\) and \(\exp(h)^m\in B\), then [[?lean:New.IsSeriesGenerator.expSubst_mem_of_pow_mem|\(\exp(h)\in B\)]]; if \(c\ne 0\), \(\lvert c\rvert\le p^{-1/(p-1)}\), \(h(0)=0\) and \(\exp(ch)=1+cH\) with \(H\in B\), then [[?lean:New.IsSeriesGenerator.mem_of_expSubst_smul_eq|\(h\in B\)]].

## References

1. Lean: `New.CMLattice`, `New.CMLattice.θ`, `New.CMLattice.translatedX`, `New.CMLattice.translatedY` in `src/Lib/CM/Sigma/Basic.lean`; `New.CMLattice.negLogTheta` in `src/Lib/CM/Integrality/LogTheta.lean`; `New.CMLattice.integralSeriesRing` in `src/Lib/CM/FormalGroup/IntegralParameter.lean`; `New.CMLattice.formalParam` in `src/Lib/CM/FormalGroup/FormalParameter.lean`.
