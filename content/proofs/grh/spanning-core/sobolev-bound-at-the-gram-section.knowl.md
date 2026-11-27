+++
id = "proofs/grh/spanning-core/sobolev-bound-at-the-gram-section"
title = "The L2 bound at the Gram section via Sobolev's inequality"
kind = "theorem"
summary = "For a function with the Schur bound, the convolution with a compactly supported weight has bounded mean square over the orbit of gamma_Z under the fixer of the frame, at the price of a power of the size bound P."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.RealPlace.lintegral_gramSection_integral_le", "New.RealPlace.lintegral_gramSection_le_of_hasDerivWords", "New.RealPlace.HasDerivWords", "New.RealPlace.HasDerivWords.exists_hasDerivAt_gramSection_mul", "New.RealPlace.exists_hasDerivAt_gramSection_mul_norm_le", "New.RealPlace.hasDerivWords_integral", "New.RealPlace.convolutionWeight", "New.RealPlace.norm_convolutionWeight_le", "New.RealPlace.exists_real_coordinates", "New.RealPlace.exists_real_coordinates_mapsTo_ball", "New.RealPlace.sobolev_const_mul_le_pow"]
lean_files = ["src/New/Spanning/Bessel/SobolevBound.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(G_1\) be the real unitary group of a shape, of rank \(r\), \(n=\varrho+1\), and \(P\ge8r\). Let \(F\colon G_1\to\mathbb{C}^I\) [[proofs/grh/spanning-core/schur-bound-for-a-bessel-function|have the Schur bound]] with constants \(P\) and \(D\) for a type \(\mathrm{rep}\). Let \(Z\) be a \((\varrho+1)\times(\varrho+1)\) matrix and \(c>0\) such that every \(Y\) with \(\lVert Y-Z\rVert<P^{-6}\) is [[proofs/grh/spanning-core/open-cell-of-frame-matrices|bounded in the cell]] by \(P\) and has \(\mathsf g(Y)\ge c\). Let \(\varphi\colon G_1\to\mathbb{C}\) be measurable, integrable, and zero at every \(y\) with \(\lVert y\rVert>P^{20}\). Then
\[
\int_{\lVert u\rVert\le P^{20}}\Bigl\lVert\int_{G_1}\varphi(y)\,F\bigl(\gamma_Z(uh)^{-1}y\bigr)\,dy\Bigr\rVert^2d\mu_c(h,u)\ \le\ P^{2000n^2}\,D\int_{G_1}\lvert\varphi\rvert^2 ,
\]
with the [[proofs/grh/spanning-core/integral-over-the-section-orbit|fixer measure \(\mu_c\)]] on \(U(\kappa)\times\mathsf U^0\) and the [[proofs/grh/spanning-core/gram-section|Gram section]] \(\gamma_Z\).

**Intermediate statement (derivative words).** A family \((V_w)\) of functions \(G_1\to\mathbb{C}^I\) indexed by words in a finite alphabet \(L\) **has derivative words with constant \(\Lambda\)** if along every curve \(\gamma\) in \(G_1\) with \(\gamma'=\gamma X\) and \(\lVert X\rVert\le C\) near \(t\), \(V_w\circ\gamma\) is differentiable at \(t\) with derivative of norm at most \(\Lambda C\sum_{l\in L}\lVert V_{lw}(\gamma(t))\rVert\). If this holds with \(\Lambda\ge0\), \(\lvert L\rvert\Lambda\le P^{44}\), the \(V_w\) are measurable with \(\lVert V_w\rVert\) left \(S\)-invariant, and \(\int\lVert V_w\rVert^2d\mu\le K\) for all words of length \(\le2n^2\), then (with \(Z,c,P\) as above)
\[
\int_{\lVert u\rVert\le P^{20}}\bigl\lVert V_\emptyset\bigl(\gamma_Z(uh)^{-1}\bigr)\bigr\rVert^2d\mu_c\le P^{550n^2}K .
\]

## Proof

*Outline.*

*Step 1 (logarithmic derivative of the section).* If \(p(t)\) is a curve of matrices with \(\lVert p'\rVert\le P^2/4\), \(p(t)\) bounded in the cell by \(P\ge8\), and \(\lVert k\rVert\le P^{20}\), then \(g(s)=\gamma_{p(s)}k\) satisfies \(g'(t)=g(t)A\) with \(\lVert A\rVert\le P^{85}\): by the [[proofs/grh/spanning-core/bounds-for-the-gram-section|bounds for the Gram section]], \(\lVert\gamma_{p(t)}\rVert\le P^{18}\) and the derivative of the section has norm \(\le P^{25}\), so \(\lVert g'\rVert\le P^{25}P^2P^{20}\) and \(\lVert g^{-1}\rVert=\lVert g\rVert\le P^{18}P^{20}\).

*Step 2 (Sobolev on a cube).* Choose real linear coordinates \(x\in\mathbb{R}^{2n^2}\mapsto Z+e(x)\) on the matrices, preserving Lebesgue measure, in which the coordinate vectors have norm \(\le P^2/4\) and the cube \([0,P^{-8}]^{2n^2}\) maps into the ball of radius \(P^{-6}\) about \(Z\) (real and imaginary parts of the entries; uses \(P\ge8r\)). Put \(f_w(x,\omega)=V_w(\gamma_{Z+e(x)}(uh)^{-1})\) for \(\omega=(h,u)\) in the fixer ball. By Step 1 and the derivative-word hypothesis, each partial derivative of \(f_w\) in \(x\) is bounded by \(\Lambda P^{85}\sum_l\lVert f_{lw}\rVert\). The library inequality `New.sobolev_trace_cube` (Sobolev trace at the corner of a cube: let \(0<\varepsilon\le1\), let \(d\) be the number of real coordinates, and suppose that for almost all \(\omega\) every partial derivative of \(f_w\) on the cube \([0,\varepsilon]^d\) exists and has norm at most \(\Lambda'\sum_l\lVert f_{lw}\rVert\), and that \(\int_{[0,\varepsilon]^d}\!\int\lVert f_w(x,\omega)\rVert^2d\omega\,dx\le K'\) for all words of length at most \(d\); then \(\int\lVert f_\emptyset(0,\omega)\rVert^2d\omega\le\bigl(\tfrac2\varepsilon(1+(\lvert L\rvert\Lambda')^2)\bigr)^dK'\)) is applied with \(\varepsilon=P^{-8}\), \(d=2n^2\), \(\Lambda'=\Lambda P^{85}\), and \(a=\tfrac2\varepsilon(1+(\lvert L\rvert\Lambda P^{85})^2)\); it is not reproved here. The integrals over the cube are bounded, after the measure preserving change of variables, by [[proofs/grh/spanning-core/integral-over-the-section-orbit|the orbit integral lemma]] with \(Q\) the ball: at most \((2P^2)^{2n^2}K\). Since \(a\cdot2P^2\le P^{275}\) when \(\lvert L\rvert\Lambda\le P^{44}\), the total is \(\le(P^{275})^{2n^2}K=P^{550n^2}K\). This proves the intermediate statement.

*Step 3 (derivatives of convolutions).* Let \((V_w)\) be the family given by the Schur bound of \(F\) (\(V_\emptyset=F\), words in pairs \((a,b)\) of basis indices). For words \(i\) in the letters \(((a,b),c,d)\) define weights \(\psi_\emptyset=\varphi\), \(\psi_{((a,b),c,d)i}(y)=\psi_i(y)\,(y^{-1})_{ad}\,y_{cb}/R^2\) with \(R=P^{20}\), and \(W_i(g)=\int\psi_i(y)V_{\bar i}(gy)\,dy\), \(\bar i\) the word of first components. Since \(\varphi\) vanishes where \(\lVert y\rVert>R\) and \(\lVert y^{-1}\rVert=\lVert y\rVert\), \(\lvert\psi_i\rvert\le\lvert\varphi\rvert\). Differentiating under the integral sign (the \(V_w\) are bounded, the \(\psi_i\) integrable) and using \(\frac{d}{dt}(\gamma(t)y)=\gamma(t)y\cdot(y^{-1}Xy)\) and the chain rule (b) of the Schur bound, the derivative of \(W_i\circ\gamma\) is \(\sum_{l=((a,b),c,d)}R^2X_{dc}\,W_{li}(\gamma)\); so \((W_i)\) has derivative words with \(\Lambda=R^2=P^{40}\), and the number of letters is \(r^4\le P^4\). The norms \(\lVert W_i\rVert\) are left \(S\)-invariant because the \(V_w\) are Bessel functions (library statement `New.IsBesselFunction.enorm_integral_besselS_mul`). By part (c) of the Schur bound, for \(\lvert i\rvert\le2n^2\), \(\int\lVert W_i\rVert^2d\mu\le P^{2\lvert i\rvert}D\int\lvert\psi_i\rvert^2\le P^{4n^2}D\int\lvert\varphi\rvert^2=:K\). The intermediate statement gives the bound \(P^{550n^2}P^{4n^2}D\int\lvert\varphi\rvert^2\le P^{2000n^2}D\int\lvert\varphi\rvert^2\). \(\blacksquare\)

## References

1. Lean: `New.RealPlace.lintegral_gramSection_integral_le`, `New.RealPlace.lintegral_gramSection_le_of_hasDerivWords`, `New.RealPlace.hasDerivWords_integral`, `New.RealPlace.exists_hasDerivAt_gramSection_mul_norm_le` in `src/New/Spanning/Bessel/SobolevBound.lean`.
