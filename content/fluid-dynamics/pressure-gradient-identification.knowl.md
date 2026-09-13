+++
id = "fluid-dynamics/pressure-gradient-identification"
title = "Identifying pressure gradients without a pressure growth assumption"
kind = "theorem"
summary = "Time averaging the momentum equation puts a harmonic pressure-gradient difference in a global negative Sobolev space."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/canonical-pressure-from-integrable-stress", "partial-differential-equations/harmonic-sobolev-distribution-vanishes", "functional-analysis/sobolev-derivative-bound", "functional-analysis/test-function-space", "real-analysis/divergence-of-tensor", "measure-theory/mixed-lebesgue-norm", "functional-analysis/distribution", "functional-analysis/l1-negative-sobolev-bound"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

On \(\mathbb R^3\times(0,T)\), suppose \(w\in L^\infty_tL^2_x\), \(g\in L^\infty_tL^1_x\), and a distribution \(\pi\) satisfy
\[
\partial_t w+\operatorname{div}g=\nu\Delta w-\nabla\pi,\qquad \nabla\cdot w=0.
\]
Let \(\pi_*\) be the [[fluid-dynamics/canonical-pressure-from-integrable-stress|canonical pressure]] of \(g\). Then \(\nabla\pi=\nabla\pi_*\) in space-time distributions. No spatial growth assumption on \(\pi\) is required.

## Time-averaged global bound

For \(a\in C_c^\infty(0,T)\), integration against the time test function gives
\[
\int a\nabla\pi\,dt
=\nu\Delta\int aw\,dt+\int a'w\,dt-\operatorname{div}\int ag\,dt.
\]
The three terms belong to \(H^{-2}\), \(L^2\), and \(H^{-3}\), respectively, using \(L^1\subset H^{-2}\) in dimension three. Also \(\pi_*\in L^\infty_tH^{-2}_x\). Thus \(h_a=\int a(\nabla\pi-\nabla\pi_*)\,dt\) belongs to \(H^{-3}\).

Taking divergence of the equation yields \(\Delta\pi=-\sum_{i,j}\partial_i\partial_jg_{ij}=\Delta\pi_*\), so \(\Delta h_a=0\). The harmonic Sobolev vanishing theorem gives \(h_a=0\). Testing in space and then in time, and using density of finite sums of product test functions, proves the space-time claim. A time-dependent spatial constant in pressure is still allowed because its gradient is zero.
