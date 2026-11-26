+++
id = "proofs/grh/spanning-core/schur-bound-for-a-bessel-function"
title = "Schur bound for a Bessel function and its derivatives"
kind = "definition"
summary = "The L2 bound over the quotient by the unipotent group for integrals of a Bessel function against integrable functions, required also of its right derivatives of bounded order."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.SchurLe", "New.RealPlace.HasSchurBound"]
lean_files = ["src/New/Spanning/Bessel/Basic.lean"]
+++

Let \(G_1\), \(\mathsf U\), \(\mu\) (the [[?lean:New.besselQuotMeasure|measure for \(\mathsf U\backslash G_1\)]]) and \(\mathrm{rep}\colon U(\kappa)\to U(I)\) be as for [[proofs/grh/spanning-core/cut-pair-of-bessel-functions|cut pairs]], with Haar measure \(dy\) on \(G_1\).

1. A function \(W\colon G_1\to\mathbb{C}^I\) satisfies **Schur's bound with constant \(D\in[0,\infty]\)** if for every integrable \(\varphi\colon G_1\to\mathbb{C}\)
\[
\int\Bigl\lVert\int_{G_1}\varphi(y)\,W(\gamma y)\,dy\Bigr\rVert^2d\mu(\gamma)\ \le\ D\int_{G_1}\lvert\varphi(y)\rvert^2dy .
\]
2. \(W\) **has the Schur bound** with constants \(B\in\mathbb{R}\), \(D\in[0,\infty]\) (for the type \(\mathrm{rep}\)) if there is a family \(V_w\) of continuous functions \(G_1\to\mathbb{C}^I\), indexed by the finite words \(w\) in pairs \((a,b)\) of basis indices, with \(V_\emptyset=W\), such that for every \(w\):
   * (a) \(V_w\) is a [[?lean:New.IsBesselFunction|Bessel function of type \(\mathrm{rep}\)]];
   * (b) the \(V_{(a,b)w}\) are the coefficients of the right derivative of \(V_w\): if a curve \(\gamma(s)\) in \(G_1\) has matrix derivative \(\gamma'(t)=\gamma(t)X\) at \(t\), then \(V_w\circ\gamma\) is differentiable at \(t\) with derivative \(\sum_{a,b}X_{ab}\,V_{(a,b)w}(\gamma(t))\);
   * (c) if \(w\) has length at most \(2(\varrho+1)^2\), then \(V_w\) satisfies Schur's bound with constant \(B^{2\lvert w\rvert}D\).

## References

1. Lean: `New.SchurLe`, `New.RealPlace.HasSchurBound` in `src/New/Spanning/Bessel/Basic.lean`.
