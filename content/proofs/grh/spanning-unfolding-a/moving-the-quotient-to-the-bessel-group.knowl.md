+++
id = "proofs/grh/spanning-unfolding-a/moving-the-quotient-to-the-bessel-group"
title = "Moving the quotient by U_c from G(F_infinity) to R(F_infinity)"
kind = "lemma"
summary = "For a form y of type e and principal level and a U_c-invariant W on R(F_infinity), the integral over U_c backslash G_infinity of (int_R e(g_0^-1 s^-1 x) W(s) ds) y(x, x_c) equals the integral over U_c backslash R(F_infinity) of W(s) y(s g_0, x_c)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.integral_classCutoff_integral_mul"]
lean_files = ["src/New/Spanning/Unfolding/SeriesPeriod.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity, \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], and \(V\) with grading \(Y\) a space [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fitting]] \(S\). Let \(c\) be a class, \(e\) a continuous integrable function on \(G_\infty\), \(g_0\in G_\infty\), \(y\) a [[?lean:New.Space.IsForm|form]] of type \(e\) on \(V\) that is right invariant under the principal level \(J_M\), and \(W\) a measurable function on \(R(F_\infty)\) with \(W(u_\infty s)=W(s)\) for \(u\in\mathsf U_c(M)\), such that \(s\mapsto\beta_c(\theta(s))W(s)\) is integrable on \(R(F_\infty)\). Then
\[
\int_{G_\infty}\beta_c(\theta(x))\Bigl(\int_{R(F_\infty)}e(g_0^{-1}s^{-1}x)\,W(s)\,ds\Bigr)y(x,x_c)\,dx=\int_{R(F_\infty)}\beta_c(\theta(s))\,W(s)\,y(sg_0,x_c)\,ds .
\]
(Integrals against \(\beta_c\) are integrals over the quotients by \(\mathsf U_c(M)\).)

## Proof

Put \(F(s,x)=W(s)\,e(g_0^{-1}s^{-1}x)\,y(x,x_c)\) on \(R(F_\infty)\times G_\infty\).

*Invariance.* For \(u\in\mathsf U_c(M)\): \(F(u_\infty s,u_\infty x)=F(s,x)\). Indeed \(W\) is invariant, the argument of \(e\) is unchanged, and \(y(u_\infty x,x_c)=y(x,x_c)\) because \(u\cdot(x,x_c)=(u_\infty x,x_c)(1,k)\) with \(k\in J_M\) (property 3 of [[proofs/grh/spanning-unfolding-a/class-sections-and-class-weights|class sections]]), \(y\) is left invariant under rational points and right invariant under \(J_M\).

*Integrability.* \(y\) is bounded, \(e\) is integrable and \(\beta_cW\) is integrable, so \(\beta_c(\theta(s))F(s,x)\) is integrable on the product.

*Swap.* The translates of \(\beta_c\circ\theta\) under \(\mathsf U_c(M)\) sum to \(1\) (property 4 of class sections). By the general statement on [[?lean:New.integral_cutoff_swap|moving a quotient from one variable to the other]] (for a countable group \(\Lambda\) mapping to a subgroup \(R\subseteq G\), a weight with translates summing to one, and \(F\) on \(R\times G\) invariant under the diagonal action: \(\int_{\Lambda\backslash G}\int_RF=\int_{\Lambda\backslash R}\int_GF\)),
\[
\int_{G_\infty}\beta_c(\theta(x))\int_{R(F_\infty)}F(s,x)\,ds\,dx=\int_{R(F_\infty)}\beta_c(\theta(s))\int_{G_\infty}F(s,x)\,dx\,ds .
\]
*The kernel reproduces \(y\).* Since \(y\) is of type \(e\) and \(e\) is integrable, \(y(g)=\int_{G_\infty}e(z)\,y(g\,(z,1))\,dz\). With \(g=(sg_0,x_c)\) and the substitution \(x=sg_0z\): \(\int_{G_\infty}e(g_0^{-1}s^{-1}x)\,y(x,x_c)\,dx=y(sg_0,x_c)\). Hence \(\int F(s,x)\,dx=W(s)\,y(sg_0,x_c)\).

## References

1. Lean: `New.Filling.Fits.integral_classCutoff_integral_mul` in `src/New/Spanning/Unfolding/SeriesPeriod.lean`.
