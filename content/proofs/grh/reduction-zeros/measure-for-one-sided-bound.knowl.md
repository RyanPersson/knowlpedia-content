+++
id = "proofs/grh/reduction-zeros/measure-for-one-sided-bound"
title = "The nonnegative measure attached to a one-sided bound"
kind = "lemma"
summary = "A one-sided exponential bound on a function of exponential growth turns K/(s - beta) minus its transform into the Laplace transform of a nonnegative measure."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_measure_laplace_eq", "New.exists_mul_exp_le"]
lean_files = ["src/Lib/Analytic/Landau.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E\colon\mathbb{R}\to\mathbb{R}\) be [[measure-theory/measurable-function|measurable]] with \(\lvert E(v)\rvert\le Ce^{v}\) for \(v\ge0\), let \(\beta>0\), and suppose \(E(v)\le e^{(\beta-1)v}\) for all sufficiently large \(v\). Then:

1. there is a real \(K\) with \(E(v)e^{v}\le Ke^{\beta v}\) for all \(v>0\);
2. the measure \(\mu\) on \((0,\infty)\) with density \(Ke^{\beta v}-E(v)e^{v}\ge0\) satisfies, for every \(s\) with \(\operatorname{Re}s>\beta+2\): \(\int e^{-(\operatorname{Re}s)v}\,d\mu(v)<\infty\) and
\[
\int e^{-sv}\,d\mu(v)=\frac{K}{s-\beta}-\int_0^\infty E(v)\,e^{(1-s)v}\,dv .
\]

## Proof

1. Let \(E(v)\le e^{(\beta-1)v}\) for \(v\ge Y\), where we may take \(Y\ge0\). Put \(K=\max(1,\lvert C\rvert e^{2Y})\). For \(v\ge Y\): \(E(v)e^{v}\le e^{\beta v}\le Ke^{\beta v}\). For \(0<v\le Y\): \(E(v)e^{v}\le\lvert C\rvert e^{2v}\le\lvert C\rvert e^{2Y}\le K\le Ke^{\beta v}\).

2. The density is nonnegative by 1. For \(\operatorname{Re}s>\beta+2\) both \(Ke^{(\beta-s)v}\) and \(E(v)e^{(1-s)v}\) are integrable on \((0,\infty)\) (the second because \(\lvert E(v)e^{(1-s)v}\rvert\le Ce^{(2-\operatorname{Re}s)v}\)). Their difference is \(e^{-sv}\) times the density, so \(e^{-sv}\) is \(\mu\)-integrable and
\(\int e^{-sv}d\mu=K\int_0^\infty e^{(\beta-s)v}dv-\int_0^\infty E(v)e^{(1-s)v}dv\), where the first integral is \(1/(s-\beta)\). \(\blacksquare\)

## References

1. Lean: `New.exists_mul_exp_le`, `New.exists_measure_laplace_eq` in `src/Lib/Analytic/Landau.lean`.
