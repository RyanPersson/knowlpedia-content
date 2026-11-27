+++
id = "proofs/grh/spanning-unfolding-a/folding-of-poincare-series"
title = "Folding: pairing a form of principal level with a Poincaré series"
kind = "theorem"
summary = "The integral over Gamma backslash G of a form z of principal level times P_phi is vol(J_M) times the sum over classes of integrals over G_infinity of beta_c (sum_i phi_(c,i) W_i) z(x, x_c)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.integral_mul_poincareSeries_eq_sum_classes"]
lean_files = ["src/New/Spanning/Unfolding/PoincareSeries.lean"]
proof_status = "full"
+++

**Theorem (folding).** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity, \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], \(V\) a space [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fitting]] \(S\), and \(z\) a [[?lean:New.Space.IsForm|form]] on \(V\) (of any type) that is right invariant under the principal level \(J_M\). Then for every \(\varphi\in\mathbb C^{\{(c,i)\}}\)
\[
\int_{\Gamma\backslash G}z(g)\,\mathcal P_\varphi(g)\,d\dot g=\operatorname{vol}(J_M)\sum_{c}\int_{G_\infty}\beta_c(\theta(x))\Bigl(\sum_i\varphi_{(c,i)}W_i(\theta(x))\Bigr)z(x,x_c)\,dx,
\]
where the sum is over the classes \(c\), \(x_c\in G_f\) is the class point, \(\theta\) the identification of \(G_\infty\) with \(\prod_vG_1\), \(\beta_c\) the [[?lean:New.Filling.classCutoff|class cutoff]], \(W_i\) the coordinates of the full Bessel function, and \(\operatorname{vol}(J_M)\) the [[harmonic-analysis/haar-measure|Haar measure]] of \(J_M\) in \(G_f\).

## Proof

By the theorem on [[proofs/grh/spanning-unfolding-a/unfolding-of-poincare-series|unfolding]], the left side is \(\sum_c\sum_i\varphi_{(c,i)}\int_Gz\,B_{(c,i)}\). Fix \(c\). By definition \(B_{(c,i)}(g)=\beta_c(\theta(g_\infty))W_i(\theta(g_\infty))\cdot\mathbf 1_{J_M}(x_c^{-1}g_f)\). If \(x_c^{-1}g_f\in J_M\), then \(z(g)=z(g_\infty,x_c)\) because \(z\) is right \(J_M\)-invariant. Hence
\[
\sum_i\varphi_{(c,i)}z(g)B_{(c,i)}(g)=A(g_\infty)\,\chi(g_f),\qquad A(x)=\beta_c(\theta(x))\Bigl(\sum_i\varphi_{(c,i)}W_i(\theta(x))\Bigr)z(x,x_c),\quad\chi(k)=\mathbf 1_{J_M}(x_c^{-1}k).
\]
The Haar measure of \(G\) is the product of those of \(G_\infty\) and \(G_f\), so the integral over \(G\) is \(\int_{G_\infty}A\cdot\int_{G_f}\chi\), and \(\int_{G_f}\chi=\operatorname{vol}(x_cJ_M)=\operatorname{vol}(J_M)\) by left invariance. (The exchange of the finite sum over \(i\) with the integral uses the integrability of \(zB_{(c,i)}\), from the proposition on [[proofs/grh/spanning-unfolding-a/convergence-of-poincare-series|convergence]].)

## References

1. Lean: `New.Filling.Fits.integral_mul_poincareSeries_eq_sum_classes` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
