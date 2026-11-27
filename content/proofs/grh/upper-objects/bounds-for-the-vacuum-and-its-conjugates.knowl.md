+++
id = "proofs/grh/upper-objects/bounds-for-the-vacuum-and-its-conjugates"
title = "Uniform bounds for the values of the moved vacuum and of its Galois conjugates"
kind = "lemma"
summary = "On a definite space of rank n the values of the vacuum moved by any Weil operator are at most exp((2d+6)(q_1 n+1)^2); under a jet conjugation the translates of the moved integral vacuum have values at most exp(C_P (q_1 n+1)^2)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.norm_omega_vac_le", "New.Parameters.IsJetConjugation.norm_map_intVacuum_le", "New.Parameters.norm_vacuumFn_vecAtPoint_le", "New.Parameters.exists_intCast_eq_norm_archCoords_sq", "New.Parameters.one_le_norm_archCoords_sub", "New.exp_neg_pi_div_mul_sq_le", "New.sqrt_mul_sq_add_le_of_le"]
lean_files = ["src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean"]
proof_status = "outline"
+++

Let \(E=E_s\), \(K=\mathbb Q(\sqrt{-d})\), \(q_1=q_1(s)\), and let \(W\) be a definite [[?lean:New.Space|space]] over \(E\) with index set \(n\): a Gram matrix \(J\) and a point \(x\in\mathrm{GL}_n(\mathbb A_E)\) with \(x^*Jx=1\). For \(\gamma\in E^n\) let \(\gamma_W=x^{-1}\gamma\) and \(\lVert\gamma\rVert_W\) the Euclidean length of the archimedean components of \(\gamma_W\) (in \(\mathbb C^{\Phi\times n}\)). Call \(\gamma\) *\(W\)-integral* if the finite components of \(\alpha^{-1}\gamma_W\) are integral, \(\alpha\) the idele of the Weil data.

**Lemma.**

1. \(\lvert\mathrm{vac}_{\mathrm{fn}}(\gamma_W)\rvert\le\exp(-\pi\lVert\gamma\rVert_W^2/\sqrt d)\) for the [[?lean:New.vacuumFn|vacuum function]], which moreover vanishes unless \(\gamma\) is \(W\)-integral.
2. If \(\gamma\) is \(W\)-integral then \(\lVert\gamma\rVert_W^2\in\mathbb Z\); two distinct \(W\)-integral vectors have \(\lVert\gamma-\delta\rVert_W\ge1\).
3. For every space \(V\) with all signs \(+1\), every adelic point \(g\) of its unitary group and every adelic vector \(y\): \(\lvert(\omega(g)\mathrm{vac})(y)\rvert\le\exp\big((2d+6)(q_1\lvert n\rvert+1)^2\big)\).
4. Let \(V\) be standard and \(L\) a [[proofs/grh/upper-objects/jet-conjugation|jet conjugation]] for \((V,\sigma,t,b)\). For every finite adelic vector \(x\), finite point \(g\) and adelic vector \(y\): \(\big\lvert L\big(\varrho(\hat x)\omega(g)v^{\mathrm{int}}\big)(y)\big\rvert\le\exp\big(C_P(q_1\lvert n\rvert+1)^2\big)\), where \(v^{\mathrm{int}}=\varsigma^{\lvert n\rvert}\mathrm{vac}\) is the [[?lean:New.Parameters.intVacuum|integral vacuum]] and \(C_P\) is the [[?lean:New.Parameters.constantBound|constant bound]] of \(P\) (a sum of the constant \(C_0\) below, \(2d+6\) and a nonnegative term).

## Proof

*1.* The vacuum function is \(\exp(-\sum_{i,w}\pi\operatorname{Im}(w(\jmath))\lvert\gamma_{W,i,w}\rvert^2)\) times a factor of absolute value \(\le1\) (a phase on the lattice, \(0\) off it), and \(\operatorname{Im}w(\jmath)=1/\sqrt d\) for the element \(\jmath\) of the Weil data.

*2.* Let \(h=\gamma^*J\gamma\in E\). Its image at each infinite place \(w\) is \(\sum_i\lvert\gamma_{W,i,w}\rvert^2\), and its finite adele is \(\sum_i\overline{\gamma_{W,i}}\gamma_{W,i}\). If \(\gamma\) is \(W\)-integral this lies in \(\alpha\bar\alpha\hat{\mathcal O}\), and \(\alpha\bar\alpha\) times a generator of the relative different of \(E/K\) is a unit at every place (property of the Weil data of \(E_s\)); so \(h\) times that generator is integral and \(\operatorname{Tr}_{E/K}(h)\) is an integer of \(K\). It equals \(\sum_w w(h)=\lVert\gamma\rVert_W^2\), which is real; a real integer of the imaginary quadratic field \(K\) is a rational integer. For the second claim, \(\gamma-\delta\) is \(W\)-integral and nonzero, so \(\lVert\gamma-\delta\rVert_W^2\) is a positive integer.

*3.* Put \(W=V\cdot g\) (the moved space) and \(f=\varrho(y)\omega(g)\mathrm{vac}\); then \((\omega(g)\mathrm{vac})(y)=\theta(f)\). By the Lean statement `hasSum_dataInner` (cited: \(\lvert\theta f\rvert^2=\sum_{\gamma\in E^n}\langle f,\varrho(\gamma_V)f\rangle\), a theta series of matrix coefficients) and since \(\lvert\langle f,\varrho(\gamma_V)f\rangle\rvert=\lvert\mathrm{vac}_{\mathrm{fn}}(\gamma_W)\rvert\) (translation by \(y\) only contributes a phase), by 1
\[
\lvert\theta f\rvert^2\le\sum_{\gamma\ W\text{-integral}}e^{-\pi\lVert\gamma\rVert_W^2/\sqrt d}\le e^{\sqrt d\,D^2}\sum_{\gamma\ W\text{-integral}} e^{-D\lVert\gamma\rVert_W},
\]
using \(e^{-\pi t^2/a}\le e^{aD^2}e^{-Dt}\) for \(a>0\) (complete the square, \(\pi\ge\tfrac14\)), with \(D=\dim+1\), \(\dim=2f_E\lvert n\rvert\) the real dimension. The archimedean coordinates of the \(W\)-integral \(\gamma\) are \(1\)-separated by 2, so a packing bound (Lean: `tsum_le_of_separated`, cited) gives \(\sum_{\gamma\ W\text{-integral}} e^{-D\lVert\gamma\rVert}\le3^{\dim}e^{\dim}\le e^{2\dim}e^{\dim}\). Since \(f_E\le q_1\), \(\dim\le2q_1\lvert n\rvert\), and \(\sqrt d(\dim+1)^2+3\dim\le2(2d+6)(q_1\lvert n\rvert+1)^2\).

*4.* By the [[proofs/grh/upper-objects/existence-of-jet-conjugation|vacuum formula]] (with \(R=\emptyset\)), \(L(\mathrm{vac})=c\,\omega(u)\mathrm{vac}\), so \(L(v^{\mathrm{int}})=a\,\omega(u)\mathrm{vac}\) with \(a=\sigma(\varsigma^{\lvert n\rvert})c\). By the values formula, \(L(v^{\mathrm{int}})(\hat w)=\sigma(v^{\mathrm{int}}(\widehat{w'}))\) for \(bw'=w\) (\(b\) is a unit), and the conjugates over \(K\) of the values of the integral vacuum at finite points are at most \(e^{C_0q_1^2\lvert n\rvert}\) (Lean: `New.Parameters.norm_gal_intVacuum_le`, another area; cited). A bound for a datum at all finite points bounds its squared norm (Lean: `norm_dataInner_self_le`, cited), and \(\omega(u)\mathrm{vac}\) is a unit vector; hence \(\lvert a\rvert\le e^{C_0q_1^2\lvert n\rvert}\). Next, \(L\varrho(\hat x)\omega(g)v^{\mathrm{int}}=\varrho(\widehat{bx})L\omega(g)v^{\mathrm{int}}\), and \(L\omega(g)=(\text{multiplier ratio of absolute value }1)\cdot\omega(g)L\) on the finite part (Lean: `ScalesTranslations.map_omega`, cited). So the value at \(y\) has absolute value \(\lvert a\rvert\cdot\lvert\omega(gu)\mathrm{vac}(y+\widehat{bx})\rvert\le e^{C_0q_1^2\lvert n\rvert}e^{(2d+6)(q_1\lvert n\rvert+1)^2}\) by 3, and \(q_1^2\lvert n\rvert\le(q_1\lvert n\rvert+1)^2\). \(\square\)

## References

1. Lean: `New.Parameters.norm_omega_vac_le`, `New.Parameters.IsJetConjugation.norm_map_intVacuum_le` in `src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean`.
