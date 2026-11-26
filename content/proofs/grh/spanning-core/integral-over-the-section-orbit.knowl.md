+++
id = "proofs/grh/spanning-core/integral-over-the-section-orbit"
title = "Integrals over the orbit of the Gram section are bounded by integrals over the quotient"
kind = "lemma"
summary = "For a weight invariant under the Bessel subgroup, its integral at gamma_Z (u h)^-1 over a bounded set of Z and over the fixer of the frame is at most (2P^2)^(2n^2) times its integral over the quotient by the unipotent group."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.RealPlace.lintegral_lintegral_gramSection_le", "New.Shape.fixerMeasure", "New.Shape.fixerBall"]
lean_files = ["src/New/Spanning/Bessel/SobolevBound.lean"]
proof_status = "full"
+++

**Notation.** For \(c\in\mathbb{R}\) let \(\mu_c\) be the measure \(c_G\,c^{\,k-1}\,dh\,du\) on \(U(\kappa)\times\mathsf U^0\) (Haar probability measure on \(U(\kappa)\), Haar measure on \(\mathsf U^0\), and \(c_G\) the [[proofs/grh/spanning-core/local-bounds-of-a-bessel-function|open cell constant]]) — the **fixer measure**; and for \(R\in\mathbb{R}\) let the **fixer ball** be the set of \((h,u)\) with \(\lVert u\rVert\le R\).

**Lemma.** Let \(P\ge1\), \(c>0\), and let \(Q\) be a measurable set of \((\varrho+1)\times(\varrho+1)\) matrices such that every \(Z\in Q\) is [[proofs/grh/spanning-core/open-cell-of-frame-matrices|bounded in the cell]] by \(P\) and has [[proofs/grh/spanning-core/frame-discriminant|\(\mathsf g(Z)\)]] \(\ge c\). Let \(w\colon G_1\to[0,\infty]\) be measurable and invariant under left translation by the Bessel subgroup \(S\). Then, with \(\gamma_Z\) the [[proofs/grh/spanning-core/gram-section|Gram section]] and \(n=\varrho+1\),
\[
\int_Q\int w\bigl(\gamma_Z\,(u\,h)^{-1}\bigr)\,d\mu_c(h,u)\,dZ\ \le\ (2P^2)^{2n^2}\int w\,d\mu ,
\]
where \(\mu\) is the measure for \(\mathsf U\backslash G_1\).

## Proof

Choose a measurable cutoff \(\chi\ge0\) on \(G_1\) with \(\int_{\mathsf U^0}\chi(u\gamma)\,du=1\) for all \(\gamma\) (it exists: library statement `New.RealPlace.isUnimodularHaar_besselHaar₀`), and let \(\chi_Q=\chi\cdot1_{\{\gamma:\,Z(\gamma)\in Q\}}\). We compare both sides with \(\int_{G_1}\chi_Qw\,d\gamma\).

*Upper bound.* By the [[proofs/grh/spanning-core/unfolding-bound-on-the-real-group|unfolding bound]] with \(\varphi=\chi_Q\), \(K=1\), \(R=P^2\) (its third hypothesis is the complement there, because \(\chi_Q(y)\neq0\) implies that \(Z(y)\in Q\) is bounded in the cell by \(P\)): \(\int\chi_Qw\,d\gamma\le(2P^2)^{2n^2}\int w\,d\mu\).

*Lower bound.* By the [[proofs/grh/spanning-core/mean-value-inequality-over-the-gram-section|mean value inequality]] for \(f=\chi_Qw\),
\[
\int_\Omega c_G\,\mathsf g(Z)^{k-1}\int_{R^\circ}\!\!\int_{R^\circ}(\chi_Qw)(s'\gamma_Zs)\,ds'\,ds\,dZ\le\int\chi_Qw\,d\gamma .
\]
Fix \(Z\in Q\subseteq\Omega\) and \(r\in R^\circ\). For \(s'=u'h'\in R^\circ\): the frame Gram matrix of \(s'\gamma_Zr\) is \(Z\in Q\) (elements of \(R^\circ\) fix the frame, and \(Z(\gamma_Z)=Z\)), and \(w(s'\gamma_Zr)=w(\gamma_Zr)\) since \(R^\circ\subseteq S\). Hence \(\int_{R^\circ}(\chi_Qw)(s'\gamma_Zr)\,ds'=w(\gamma_Zr)\int\!\!\int\chi(u'h'\gamma_Zr)\,du'\,dh'=w(\gamma_Zr)\). Since \(ds\) is invariant under inversion ([[proofs/grh/spanning-core/coordinates-on-frames-over-a-gram-matrix|coordinates lemma]], part 4), the inner double integral equals \(\int\!\!\int w(\gamma_Z(uh)^{-1})\,du\,dh\). Finally \(\mathsf g(Z)\ge c\) on \(Q\), so the density \(c_G\mathsf g(Z)^{k-1}\) is at least that of \(\mu_c\). \(\blacksquare\)

## References

1. Lean: `New.RealPlace.lintegral_lintegral_gramSection_le`, `New.Shape.fixerMeasure`, `New.Shape.fixerBall` in `src/New/Spanning/Bessel/SobolevBound.lean`.
