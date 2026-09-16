+++
id = "ergodic-theory/nonsingular-koopman-representation"
title = "Koopman representation of a nonsingular action"
kind = "construction"
summary = "A Radon–Nikodym weight makes pullback unitary when an action preserves only the measure class."
aliases = ["weighted Koopman representation"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-action", "harmonic-analysis/quasi-invariant-measure", "measure-theory/radon-nikodym-derivative", "measure-theory/l2-hilbert-space"]
+++

Let a countable discrete group act by measurable bijections \(T_g\) on a sigma-finite measure space and preserve its measure class: \((T_g)_*\mu\) and \(\mu\) have the same null sets. Its **nonsingular Koopman representation** is
\[
\kappa(g)f(x)=
\left(\frac{d(T_g)_*\mu}{d\mu}(x)\right)^{1/2}f(T_{g^{-1}}x).
\]
The square-root [[measure-theory/radon-nikodym-derivative|Radon–Nikodym weight]] gives unitarity; the derivative chain rule gives the representation law.

## Reduction to measure preservation

For a measure-preserving action, the derivative is one and this reduces to ordinary inverse pullback. In the general nonsingular case constants need not be fixed, so removing constants and using the probability-preserving fixed-vector criterion would not be justified.

## References

1. Jesse Peterson, [*Lecture notes on ergodic theory*](https://www.math.vanderbilt.edu/~peters10/teaching/Spring2011/ErgodicTheoryNotes.pdf), 2011. Definition 2.2.1.
