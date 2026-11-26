+++
id = "proofs/grh/reduction-zeros/zero-forces-large-tail-integral"
title = "A zero in the box forces a large tail integral"
kind = "theorem"
summary = "Three-lines argument: for a primitive character of conductor at most T^2, a zero of L with real part at least 1/2 + 9 delta and bounded height forces J(chi, T) > T^(2 delta) for large T."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.eventually_rpow_lt_thetaTailIntegral", "New.three_lines_bound_of_LFunction_eq_zero", "New.norm_mul_mollifier_sub_le", "New.norm_gaussianMellin_mul_LFunction_le"]
lean_files = ["src/Lib/Analytic/QuadraticTwist.lean"]
proof_status = "full"
+++

**Theorem (three lines).** Let \(j\in\{0,1\}\), \(\delta>0\) and \(H\in\mathbb{R}\). There is \(T_0\) such that for all \(T\ge T_0\) the following holds. Let \(\chi\ne1\) be a [[?c:primitive Dirichlet character|primitive]] Dirichlet character of conductor \(q\le T^{2}\) with \(\chi(-1)=(-1)^{j}\). If \(L(s,\chi)=0\) for some \(s\) with \(\operatorname{Re}s\ge\tfrac12+9\delta\) and \(\lvert\operatorname{Im}s\rvert\le H\), then the [[proofs/grh/reduction-zeros/theta-tail-integral-and-mollifier|tail integral]] satisfies
\[
J(\chi,T)>T^{2\delta}.
\]

More precisely there is a constant \(C=C(j)\) such that for \(\delta>0\), \(T>0\), \(\chi\) as above with \(q\le T^2\) and \(J(\chi,T)\le T^{2\delta}\), every zero \(s\) of \(L(\cdot,\chi)\) with \(\tfrac12+9\delta\le\operatorname{Re}s\le1\) has \(\lvert\Gamma_j(s)\rvert^{2}\le C\,T^{-2\delta}\).

## Proof

Let \(G\) bound \(\lvert\Gamma_j\rvert\) on the strip \(\tfrac12\le\operatorname{Re}z\le2\), and \(C=9+G^{2}\). Assume \(J=J(\chi,T)\le T^{2\delta}\). Note \(T\ge1\) because \(1\le q\le T^{2}\). Let \(\mathcal{M}\) be the mollifier of \(\chi\) and
\[
\Psi(z)=\Gamma_j(z)L(z,\chi)\mathcal{M}(z)-\Gamma_j(z)^{2}.
\]
It is holomorphic on \(\operatorname{Re}z>0\) and bounded on the strip (\(\Gamma_jL\) is a Mellin transform bounded there, by [[proofs/grh/reduction-zeros/riemann-formula-for-character|Riemann's formula]]).

*Right line \(\operatorname{Re}z=2\).* By the [[proofs/grh/reduction-zeros/mellin-of-theta-series|Mellin transforms]], \(\Gamma_j(z)/L(z,\chi)-\mathcal{M}(z)=\int_0^{1/T}\theta_{\mu\chi}(u)u^{z-1/2}du/u\), of absolute value \(\le\int_0^{1/T}3e^{-u}du\le3/T\); and \(\lvert\Gamma_j(z)L(z,\chi)\rvert=\lvert\int_0^\infty\theta_\chi(u)u^{z-1/2}du/u\rvert\le\int_0^\infty3e^{-u}du=3\). As \(L(z,\chi)\ne0\),
\[
\lvert\Psi(z)\rvert=\lvert\Gamma_jL\rvert\cdot\lvert\mathcal{M}-\Gamma_j/L\rvert\le9/T\le C\,T^{-1}.
\]

*Left line \(\operatorname{Re}z=\tfrac12\).* By Riemann's formula and its fold, using \(q^{-1/2}\ge1/T\),
\[
\lvert\Gamma_j(z)L(z,\chi)\rvert\le\int_0^\infty\lvert\theta_\chi\rvert\frac{du}u=2\int_{q^{-1/2}}^\infty\lvert\theta_\chi\rvert\frac{du}u\le2\int_{1/T}^\infty\lvert\theta_\chi\rvert\frac{du}u\le2J .
\]
Also \(\lvert\mathcal{M}(z)\rvert\le J\). Hence \(\lvert\Psi(z)\rvert\le2T^{4\delta}+G^{2}\le C\,T^{4\delta}\).

*Interpolation.* Let \(s\) be a zero with \(\tfrac12+9\delta\le\operatorname{Re}s\le1\), and \(\omega=(\operatorname{Re}s-\tfrac12)/\tfrac32\ge6\delta\). By the [[?c:Hadamard three-lines theorem|three-lines theorem]],
\[
\lvert\Gamma_j(s)\rvert^{2}=\lvert\Psi(s)\rvert\le(CT^{4\delta})^{1-\omega}(CT^{-1})^{\omega}=C\,T^{4\delta-\omega(1+4\delta)}\le C\,T^{-2\delta},
\]
since \(4\delta-\omega(1+4\delta)\le4\delta-6\delta=-2\delta\) and \(T\ge1\).

*Conclusion.* A zero of \(L(\cdot,\chi)\) has \(\operatorname{Re}s\le1\) ([[?c:non-vanishing of Dirichlet L-functions on the line Re s = 1|non-vanishing on \(\operatorname{Re}s\ge1\)]]). On the compact rectangle \(\tfrac12\le\operatorname{Re}s\le1\), \(\lvert\operatorname{Im}s\rvert\le H\), \(\lvert\Gamma_j\rvert\ge c>0\). Choose \(T_0\) with \(CT^{-2\delta}<c^{2}\) for \(T\ge T_0\). Then \(J\le T^{2\delta}\) would give \(c^{2}\le\lvert\Gamma_j(s)\rvert^2\le CT^{-2\delta}<c^2\). \(\blacksquare\)

## References

1. Lean: `New.three_lines_bound_of_LFunction_eq_zero`, `New.eventually_rpow_lt_thetaTailIntegral` in `src/Lib/Analytic/QuadraticTwist.lean`.
