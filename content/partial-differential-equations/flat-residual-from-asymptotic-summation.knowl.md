+++
id = "partial-differential-equations/flat-residual-from-asymptotic-summation"
title = "Flat residual from asymptotic summation"
kind = "theorem"
summary = "A realized field has an infinitely small residual when finite partial sums improve in order and the nonlinear comparison loses only fixed powers."
aliases = ["nonlinear flat-residual realization"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["asymptotics/shrinking-cutoff-asymptotic-summation", "partial-differential-equations/differential-polynomial-difference-estimate", "asymptotics/infinite-order-decay-with-derivatives", "asymptotics/parameter-choice-hierarchy"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(F\) be a fixed differential polynomial of finite order and degree whose coefficient jets grow at most as fixed powers of \(q^{-1}\). Suppose smooth finite states \(U^{[J]}\) and a smooth realization \(U\) on one domain satisfy
\[
|U-U^{[J]}|_m\le C_J q^{h_J-L_m},\qquad h_J\to\infty,
\]
near \(q=0\), and
\[
|U^{[J]}|_m\le C_{J,m}q^{-K_m}(1+|\log q|)^{P_{J,m}},
\]
\[
|F(U^{[J]})|_m\le C_{J,m}q^{\rho_J-K_m^F}(1+|\log q|)^{Q_{J,m}}+E_{J,m},\qquad \rho_J\to\infty.
\]
Assume \(L_m,K_m,K_m^F\) are independent of \(J\), and each fixed \(E_{J,m}\) is \(O(q^N)\) for every \(N\). Then \(F(U)\) has [[asymptotics/infinite-order-decay-with-derivatives|infinite-order decay with all derivatives]].

## Compare with one fixed stage

Fix an output derivative order \(m\) and target decay order \(N\). If \(F\) has order \(s\) and degree \(d\), choose \(J\) so large that the tail exponent \(h_J-L_{m+s}\) exceeds \(N\) plus the fixed coefficient loss and \((d-1)(K_{m+s}+1)\). Also require \(\rho_J-K_m^F>N\), with a positive margin to absorb logarithms. Keep this \(J\) fixed.

In a sufficiently small \(q\)-neighborhood, the difference jet is at most one and the fixed-stage logarithms fit within the allocated power margin. The differential-polynomial difference estimate gives \(|F(U)-F(U^{[J]})|_m=O(q^N)\). The fixed-stage residual and its fixed flat remainder have the same bound. The triangle inequality proves the claim.

The order of choices is \((m,N)\), then a finite \(J\), then a neighborhood and constants. This argument never sums the flat remainders \(E_{J,m}\) over stages; arbitrary stage-dependent flat errors need not form a convergent series.
