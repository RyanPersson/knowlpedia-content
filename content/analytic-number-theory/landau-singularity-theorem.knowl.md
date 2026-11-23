+++
id = "analytic-number-theory/landau-singularity-theorem"
title = "Landau’s theorem for Dirichlet series"
kind = "theorem"
summary = "A Dirichlet series with nonnegative coefficients has a singularity at its finite real abscissa of convergence."
aliases = ["Landau's theorem", "Landau’s singularity theorem"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["complex-analysis/analytic-continuation"]
+++

Let \(F(s)=\sum_{n\ge1}a_n n^{-s}\) with \(a_n\ge0\). Suppose the boundary of its half-plane of convergence is \(\operatorname{Re}s=\sigma_c\), with \(\sigma_c\) finite. **Landau’s theorem** says that \(F\) has a singularity at the real point \(\sigma_c\). No holomorphic [[complex-analysis/analytic-continuation|continuation]] through a neighborhood of that point exists.

## How positivity helps

For a real \(s_0>\sigma_c\), expand \(n^{s_0-s}=\exp((s_0-s)\log n)\). When \(s<s_0\) is real, all the terms in the resulting double sum are nonnegative. If \(F\) were holomorphic across \(\sigma_c\), its Taylor expansion could then force convergence of the original series to the left of \(\sigma_c\).

Chojecki invokes this idea to explain a reduction from zeros to an estimate. The specific prime sum and the quantifiers on its range belong to the [[analytic-number-theory/windowed-landau-criterion|windowed criterion]].

## References

- Kiran Kedlaya, [Notes on analytic number theory, Theorem 2.4 and proof](https://kskedlaya.org/ant/part-1-3.html).
