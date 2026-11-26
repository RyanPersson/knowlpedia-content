+++
id = "proofs/grh/reduction-main/theorem-c-integral-forms-long"
title = "Theorem C: integral forms are long"
kind = "theorem"
summary = "For independent target forms y_1..y_n with n >= (1 - 4/b^2) d_T, of index at most delta and covolume at most c in the target lattice: c + 2 delta >= d_T (h_main - 3 f a log^4 b)."
aliases = ["Theorem C", "integral forms are long", "integral_forms_long"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.integral_forms_long"]
lean_files = ["src/New/Determinant/Twist/LongForms.lean"]
proof_status = "full"
+++

**Theorem C (integral forms are long).** Let \(D\) be [[proofs/grh/reduction-main/data|data]], \(\mathcal T\) the target forms, of dimension \(d_T\), with the [[proofs/grh/reduction-main/target-lattice|target lattice]] \(L_D\). Let \(y_1,\dots,y_n\in\mathcal T\) be linearly independent with
\[
n\ \ge\ \Bigl(1-\frac4{b^2}\Bigr)d_T ,
\]
and suppose \(y\) has [[proofs/grh/reduction-main/index-bound|index at most \(\delta\)]] and [[proofs/grh/reduction-main/covolume-bound|covolume at most \(c\)]] in \(L_D\). Then
\[
c+2\delta\ \ge\ d_T\bigl(h_{\mathrm{main}}-3\,f\,a\,(\log b)^4\bigr),
\]
with the [[proofs/grh/reduction-main/main-amount-and-total-remainder|main amount \(h_{\mathrm{main}}\)]].

Explicitly, the hypotheses say: there are \(\delta_\ell\ge0\) with \(\sum\delta_\ell\log\ell\le\delta\) such that at each finite place \(\iota\mid\ell\) a matrix over \(\mathcal O_\iota\) with \(\lvert\det\rvert_\iota\ge\ell^{-\delta_\ell}\) takes \(y\) to forms all of whose lifts \(\Theta_\vartheta\), for \(m\)-fold twists \(\vartheta\) of modulus prime to \(\ell\), are integral at \(\iota\); and the Gram determinant of every conjugate of the untwisted lifts \(\Theta_1y_i\) has absolute value at most \(e^c\).

## Proof

Complete relative to [[proofs/grh/reduction-main/auxiliary-forms|auxiliary forms]], [[proofs/grh/reduction-main/inverse-ratio-height|the inverse ratio]] and the properties of the target lattice. Put \(F=fa\log^4b\).

Choose a family \(\theta\) with small ratios as in part (1) of the inverse ratio theorem; by its part (3), \(Z(1)/Z(\theta_\iota)\) has height at most \(b_{\mathrm{volume}}:=d_T(b+F-h_{\mathrm{main}})\). Choose \(e\), \(\gamma\) as in the theorem on auxiliary forms. Since the auxiliary forms span \(\mathcal T\), the independent family \(y\) can be completed to a basis \(y_1,\dots,y_n,z_1,\dots,z_{n'}\) of \(\mathcal T\) with all \(z_i\) auxiliary for \(\gamma\) (`New.exists_extend_basis_of_span_eq_top`); \(d_T=n+n'\).

We apply the theorem [[proofs/grh/reduction-main/covolume-add-index-nonneg|a twist for each prime]] to \(L_D\), with \(\xi_\iota=\theta_\iota\). Its hypotheses: the lifts \(\Theta_\vartheta\) are injective and \(Z(\vartheta)\) is the volume (target lattice, (3), (4)); \(\theta_\iota\) is allowed at \(\ell\) (small ratios, (i)); \(\gamma(\vartheta)\ne0\) and \(\gamma(\vartheta)\Theta_\vartheta z_i\) is integral where \(\vartheta\) is allowed, and \(\lVert\Theta_1z_i\rVert^2_\sigma\le e^{b_{\mathrm{short}}}\) with \(b_{\mathrm{short}}=2x_1^2b^2\) (definition of auxiliary); the family \(\lvert\gamma(\theta_\iota)\rvert^{-2}\) is the square of the family in part (a) of the lemma on auxiliary forms, so has height at most \(2m^2tx_1\le b=:b_{\mathrm{denom}}\). The theorem yields
\[
0\le c+2\delta+n'(2x_1^2b^2+b)+d_T(b+F-h_{\mathrm{main}}).
\]
By part (b) of that lemma, \(n'(2x_1^2b^2+b)\le d_Tb\). Hence \(c+2\delta\ge d_T(h_{\mathrm{main}}-F-2b)\ge d_T(h_{\mathrm{main}}-3F)\), as \(b\le F\).

## References

1. Lean: `New.Data.integral_forms_long` in `src/New/Determinant/Twist/LongForms.lean`.
