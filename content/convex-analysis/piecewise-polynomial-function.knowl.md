+++
id = "convex-analysis/piecewise-polynomial-function"
title = "Piecewise-polynomial function"
kind = "knowl"
summary = "A function represented by polynomial formulas on a finite semialgebraic cover."
aliases = ["piecewise polynomial", "piecewise-polynomial function"]
domains = ["convex-analysis", "algebra-rings"]
+++

A function \(f:\mathbb R^n\to\mathbb R\) is **piecewise polynomial** if there are finitely many closed [[convex-analysis/semialgebraic-set|semialgebraic sets]] \(S_1,\ldots,S_m\) covering \(\mathbb R^n\), and polynomials \(p_i\in\mathbb R[x_1,\ldots,x_n]\), such that \(f(x)=p_i(x)\) whenever \(x\in S_i\).

Because the sets cover the domain, the local formulas must agree on overlaps. With closed pieces this agreement implies that the resulting function is continuous. Pointwise maxima and minima of finitely many polynomial functions are basic examples.
