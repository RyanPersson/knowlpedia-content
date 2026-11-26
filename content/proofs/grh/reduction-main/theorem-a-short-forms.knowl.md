+++
id = "proofs/grh/reduction-main/theorem-a-short-forms"
title = "Theorem A (a): the source is spanned by integral forms with short lifts"
kind = "theorem"
summary = "The ramified source forms are spanned by forms integral at every finite place whose images under all translates of the normalised Poincaré map have lifts of squared norm at most exp(h_main - m rem + f a log^4 b) at every conjugate."
aliases = ["Theorem A", "short forms", "span_short_integralRamified_eq_top"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.span_short_integralRamified_eq_top"]
lean_files = ["src/New/Reduction/ShortAndEnough.lean"]
proof_status = "full"
+++

**Theorem A (a) (short forms).** Let \(D\) be [[proofs/grh/reduction-main/data|data]]. Let \(\mathcal S\) be the source, \(\mathcal S^{\mathrm{int}}\) its integral forms, \(\bar G\) the finite group and \(s\mathfrak p:\mathcal S\to\mathcal T\) the [[proofs/grh/reduction-main/normalized-poincare|normalised Poincaré maps]]; let \(\Theta_1\) be the chain of \(m\) lifts for the trivial twist and \(\lVert\cdot\rVert_\sigma^2\) the squared norm at \(\sigma\in\operatorname{Aut}(\mathbb C)\) of the [[proofs/grh/reduction-main/target-lattice|target lattice]]. Let \(h_{\mathrm{main}}\) and \(\mathrm{rem}\) be the [[proofs/grh/reduction-main/main-amount-and-total-remainder|main amount and total remainder]]. Then the complex vector space \(\mathcal S\) is spanned by the set of all \(\varphi\in\mathcal S^{\mathrm{int}}\) such that
\[
\lVert\Theta_1\,s\mathfrak p\,\varphi\rVert_\sigma^2\ \le\ \exp\bigl(h_{\mathrm{main}}-m\cdot\mathrm{rem}+f\,a\,(\log b)^4\bigr)\qquad\text{for all } s\in\bar G,\ \sigma\in\operatorname{Aut}(\mathbb C).
\]

## Proof

The proof is complete relative to four results of other chapters, quoted with their exact form:

- (i) [[?lean:New.Data.span_isShort_ramifiedSourceForms_eq_top|short source forms span]]: \(\mathcal S\) is spanned by the \(\varphi\in\mathcal S\) whose values are integral at every finite place and with \(\lVert\sigma(\varphi(g))\rVert^2\le\exp(E)\) for all \(\sigma\) and all finite adelic points \(g\), where \(E=fa\log^3b\) is the error unit;
- (ii) the seesaw identity in the form of property (2) of the normalised Poincaré maps;
- (iii) [[?lean:New.Data.weylNormSq_compositeLift_le|size of the composite lift]]: for a chain datum \(\Psi\) of the trivial twist, if all values of \(\sigma\varphi\) have squared norm \(\le e^{B}\), then all values of the \(\sigma\)-conjugate of \(B_{1,\Psi}\varphi\) have squared norm \(\le\exp(B+\beta)\), with
\[
\beta=h_{\mathrm{main}}-m\,\mathrm{rem}+2\sum_{\ell\in\mathcal P}\operatorname{gain}_\ell\log\ell+E ;
\]
- (iv) [[?lean:New.Data.normSqAt_goodProjTranslate_le|size of the good part]]: if all values of the \(\sigma\)-conjugate of \(\iota_1z\) have squared norm \(\le e^{B'}\), then \(\lVert\Theta_1(\#\bar G\,e_0\,s\,z)\rVert_\sigma^2\le\exp(x^{99}+B')\).

By (i) it suffices to show that every \(\varphi\) as in (i) lies in the set of the theorem. Such \(\varphi\) is in \(\mathcal S^{\mathrm{int}}\). Fix \(s,\sigma\) and put \(z=c_{ss}^{-1}\mathcal P\varphi\). By (ii) for the trivial twist, \(\iota_1z=B_{1,\Psi}\varphi\); by (iii) with \(B=E\) its conjugate values have squared norm \(\le\exp(E+\beta)\); by (iv), \(\lVert\Theta_1(\#\bar Ge_0sz)\rVert^2_\sigma\le\exp(x^{99}+E+\beta)\). Since \(s\mathfrak p\varphi=c_B\cdot\#\bar Ge_0sz\) with \(c_B\in\mathbb Q_{>0}\),
\[
\log\lVert\Theta_1s\mathfrak p\varphi\rVert_\sigma^2\le2\log c_B+x^{99}+E+\beta .
\]
By property (3) of [[proofs/grh/reduction-main/gain-normalisation|the gain normalisation]], \(2\log c_B\le-2\sum_{\ell\in\mathcal P}\operatorname{gain}_\ell\log\ell+2E+2b\). The gains cancel, leaving
\[
h_{\mathrm{main}}-m\,\mathrm{rem}+x^{99}+4E+2b\ \le\ h_{\mathrm{main}}-m\,\mathrm{rem}+fa\log^4b ,
\]
because \(x^{99}+4fa\log^3b+2b\le fa\log^4b\): each of \(x^{99}\), \(2b\) is at most \(fa\log^3b\) (as \(a=xb\), \(x^{99}\le b\)), and \(6\le\log b\).

## References

1. Lean: `New.Data.span_short_integralRamified_eq_top` in `src/New/Reduction/ShortAndEnough.lean`.
