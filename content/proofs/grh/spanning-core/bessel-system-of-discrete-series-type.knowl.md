+++
id = "proofs/grh/spanning-core/bessel-system-of-discrete-series-type"
title = "Bessel system of discrete series type"
kind = "definition"
summary = "A Bessel system whose full function is the Bessel average of the discrete series coefficient of a parameter l, with values in the representation of U(X_0) of a given weight."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DiscreteSeries.UnitarySignFrame", "New.Filling.IsDiscreteSeriesBessel"]
lean_files = ["src/New/Spanning/Bessel/LargeFunction.lean"]
+++

Let \(\mathfrak s\) be a shape with real unitary group \(G_1\) and form \(J\), and \(\varepsilon\) a sign vector on the basis indices. A **unitary sign frame** is a unitary matrix \(p\) with \(p^*Jp=\operatorname{diag}(\varepsilon)\) (a [[?lean:New.SignFrame|sign frame]] that is unitary); it identifies \(G_1\) with the group \(U(\varepsilon)\) of [[?lean:New.USign|\(\operatorname{diag}(\varepsilon)\)]] by \(g\mapsto p^{-1}gp\).

Fix a unitary sign frame, a [[proofs/grh/spanning-core/bessel-system|Bessel system]] \(B\) for \((\mathfrak s,b,f)\), a doubled Harish-Chandra parameter \(l\) for \(\varepsilon\), and a weight \(kw\colon\mathbb{N}\to\mathbb{N}\). The system \(B\) **is of discrete series type \((l,kw)\)** if

1. \(\deg=\) [[?lean:New.weylDimensionPoly|Weyl's dimension polynomial]] at \(l\);
2. up to an invertible change of coordinates of the value space, \(\mathrm{rep}(g)\) is the transpose of the [[?lean:New.schur|Schur matrix]] of weight \(kw\) at \(g^{\mathsf T}\), for \(g\in U(\kappa)\);
3. the full function \(W\) is fixed by right convolution with the kernel [[?lean:New.HCParam.dsKernel|\(e_\lambda=\deg_\lambda\overline{c_\lambda}\)]] carried to \(G_1\) by the frame: \(\int e_\lambda(x)\,W(y\,x)\,dx=W(y)\);
4. there are a real \(c\), a point \(x\in G_1\) and a vector \(v\) such that for all \(y\) the [[proofs/grh/spanning-core/bessel-period-group-and-average|Bessel integrand]] is integrable over \(R\) and \(W(y)=c\cdot\mathcal W_{x,v}(y)\), the Bessel average.

## References

1. Lean: `New.DiscreteSeries.UnitarySignFrame`, `New.Filling.IsDiscreteSeriesBessel` in `src/New/Spanning/Bessel/LargeFunction.lean`.
