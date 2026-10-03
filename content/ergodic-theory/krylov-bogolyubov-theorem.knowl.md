+++
id = "ergodic-theory/krylov-bogolyubov-theorem"
title = "Krylov–Bogolyubov existence theorem"
kind = "theorem"
summary = "Every continuous map of a nonempty compact metric space has an invariant Borel probability measure."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/invariant-probability-measure", "topology/continuous-map", "topology/compact-set", "topology/metric-space"]
+++

Every continuous self-map \(T:X\to X\) of a nonempty compact metric space admits an [[ergodic-theory/invariant-probability-measure|invariant Borel probability measure]]. This is the compact-space **Krylov–Bogolyubov existence theorem**.

## Empirical-measure proof

Choose \(x\in X\) and put \(\mu_N=N^{-1}\sum_{j=0}^{N-1}\delta_{T^jx}\). Probabilities on a compact metric space have a weakly convergent subsequence: convergence here means convergence of the integral of every continuous function. For any such subsequential limit \(\mu\) and \(f\in C(X)\),
\[
\int(f\circ T-f)\,d\mu_N=\frac{f(T^Nx)-f(x)}N\longrightarrow0.
\]
Continuity permits passage to the limit, giving \(\int f\circ T\,d\mu=\int f\,d\mu\), hence invariance. The theorem establishes existence; it does not assert uniqueness or convergence of the entire empirical-measure sequence.
