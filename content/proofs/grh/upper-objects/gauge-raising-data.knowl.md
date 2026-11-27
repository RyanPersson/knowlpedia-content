+++
id = "proofs/grh/upper-objects/gauge-raising-data"
title = "Data that raise the p-adic gauge by at most a factor"
kind = "definition"
summary = "For an abstract theta kernel and a prime p: the additive monoid of data whose jet maps multiply the p-adic gauge of Weyl-module vectors by at most max(c,0), uniformly in the finite adelic points."
aliases = ["raises gauges", "diagonal weight"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Kernel.raises", "New.weylGauge_add_le_max", "New.Kernel.smul_mem_raises", "New.Kernel.omega_mem_raises_iff", "New.diagonalWeight", "New.diagonalWeight_nonneg", "New.diagonalWeight_one"]
lean_files = ["src/New/UpperBound/Kernels/ThetaLiftGauge.lean"]
+++

Let \(E=E_s\) be the field of [[?lean:New.Parameters|parameters]] \(P\), \(p\) a prime with its fixed embedding \(\iota_p\colon\mathbb C\to\mathbb C_p\), and \(k\) a [[?lean:New.Kernel|theta kernel]] from rank \(n\) to rank \(n'\) with data space \(S\), action \(\omega\) of \(G\times G'\) (finite adelic points of the standard definite unitary groups) and jet map \(\operatorname{jet}\colon S\to\operatorname{Hom}(\mathcal V,\mathcal V')\), where \(\mathcal V,\mathcal V'\) are the Weyl modules with column numbers \(\kappa\) and determinant exponents \(e\), \(e'\). The [[?lean:New.weylGauge|gauge]] of \(\xi\in\mathcal V\) at \(g\in G\) is the \(p\)-adic sup norm of the coordinates of \(\rho_p(g)^{-1}(\iota_p\circ\xi)\), where \(\rho_p(g)\) is the action of \(g\) on \(\mathcal V\otimes\mathbb C_p\) through the embeddings \(z\mapsto\iota_p(\tau(\bar z))\) of \(E\) extended to the finite adeles.

**Definition.** For \(d\in G\), \(d'\in G'\) and \(c\in\mathbb R\), a datum \(\Phi\in S\) **raises gauges by at most \(c\) from \(d\) to \(d'\)** if for all \(g\in G\), \(h\in G'\), \(\xi\in\mathcal V\):
\[
\operatorname{gauge}_{hd'}\big(\operatorname{jet}(\omega(g,h)\Phi)\,\xi\big)\le\max(c,0)\cdot\operatorname{gauge}_{gd}(\xi).
\]

For a diagonal family \(u=(u_\tau)\), \(u_\tau\in\mathbb C_p^{\,n'}\), and a basis index \(i'\) of \(\mathcal V'\) (a family of fillings \(i'_\tau\)), the **diagonal weight** is \(\operatorname{dw}(u,i')=\prod_\tau\Big[\big(\prod_{b\in n'}\lvert u_{\tau,b}\rvert\big)^{e'_\tau}\cdot\prod_{\text{boxes of }i'_\tau}\lvert u_{\tau,\text{entry of the box}}\rvert\Big]\). It is \(\ge0\), and \(1\) for \(u=1\).

## Properties

1. The gauge is ultrametric in \(\xi\); hence the data raising gauges by at most \(c\) form an additive submonoid of \(S\) (the factor \(\max(c,0)\) makes \(0\) a member for every \(c\)).
2. If \(\Phi\) raises by at most \(B\) and \(\lvert\iota_pz\rvert\,B\le B'\), then \(z\Phi\) raises by at most \(B'\) (the jet map is linear and \(z\) scales gauges by \(\lvert\iota_pz\rvert\); \(\lvert\iota_p z\rvert\max(B,0)=\max(\lvert\iota_pz\rvert B,0)\)).
3. \(\omega(g_0,h_0)\Phi\) raises by at most \(B\) from \(g_0d\) to \(h_0d'\) if and only if \(\Phi\) does from \(d\) to \(d'\) (substitute \((g,h)\mapsto(gg_0,hh_0)\), a bijection).

## References

1. Lean: `New.Kernel.raises`, `New.Kernel.smul_mem_raises`, `New.Kernel.omega_mem_raises_iff`, `New.diagonalWeight` in `src/New/UpperBound/Kernels/ThetaLiftGauge.lean`.
