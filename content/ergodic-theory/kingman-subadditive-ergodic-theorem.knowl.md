+++
id = "ergodic-theory/kingman-subadditive-ergodic-theorem"
title = "Kingman subadditive ergodic theorem"
kind = "theorem"
summary = "Normalized integrable subadditive orbit costs have an invariant almost-everywhere limit."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/subadditive-cocycle", "measure-theory/l1-function"]
+++

Let \(T\) preserve a probability measure and let \((a_n)\) be a real [[ergodic-theory/subadditive-cocycle|subadditive cocycle]] with \(a_n\in L^1\) for every \(n\geq1\). Assume
\[
\inf_{n\geq1}\frac1n\int_Xa_n\,d\mu>-\infty.
\]
Then \(a_n/n\) converges almost everywhere and in \(L^1\) to an integrable invariant function \(a_\infty\), and
\[
\int a_\infty\,d\mu=\inf_{n\geq1}\frac1n\int a_n\,d\mu.
\]
If \(T\) is ergodic, this limit is the displayed constant almost everywhere.

## Applications

Additive orbit sums recover Birkhoff's theorem. Logarithms of matrix-product norms give asymptotic growth rates and are a starting point for the multiplicative ergodic theorem. The lower-bound hypothesis here ensures a finite integrable limit; more general versions can allow a limit of \(-\infty\).

## References

1. Anders Karlsson, [“A proof of the subadditive ergodic theorem”](https://unige.ch/math/folks/karlsson/subaddnew.pdf), §1, theorem attributed to Kingman (1968).
