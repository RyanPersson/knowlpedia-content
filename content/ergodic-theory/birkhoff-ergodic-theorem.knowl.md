+++
id = "ergodic-theory/birkhoff-ergodic-theorem"
title = "Birkhoff pointwise ergodic theorem"
kind = "theorem"
summary = "Time averages of an integrable observable converge almost everywhere to conditional expectation on invariant events."
aliases = ["pointwise ergodic theorem", "Birkhoff ergodic theorem"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/time-average", "ergodic-theory/invariant-sigma-algebra", "probability/conditional-expectation", "measure-theory/l1-function"]
+++

For a probability-preserving transformation \(T\) and \(f\in L^1(X,\mu)\), the **Birkhoff pointwise ergodic theorem** states
\[
\frac1N\sum_{n=0}^{N-1}f(T^nx)
\longrightarrow \mathbb E[f\mid\mathcal I_T](x)
\quad\text{for almost every }x.
\]
Here \(\mathcal I_T\) is the [[ergodic-theory/invariant-sigma-algebra|invariant sigma-algebra]]. Invertibility is not required. If \(T\) is ergodic, the limit is \(\int_X f\,d\mu\).

## Visit frequencies

Taking \(f=1_E\) in an ergodic system identifies the asymptotic fraction of visits to \(E\) with \(\mu(E)\). The exceptional null set may depend on \(E\) or \(f\); the theorem does not give a single exceptional set valid for all measurable observables at once.

## Why this differs from mean convergence

The [[ergodic-theory/von-neumann-mean-ergodic-theorem|mean ergodic theorem]] concerns Hilbert-space norm convergence. Birkhoff's theorem concerns individual trajectories. A proof uses the [[ergodic-theory/maximal-ergodic-theorem|maximal ergodic inequality]] to control exceptional sets, not merely the \(L^2\) projection argument.

## References

1. Jesse Peterson, [*Lecture notes on ergodic theory*](https://www.math.vanderbilt.edu/~peters10/teaching/Spring2011/ErgodicTheoryNotes.pdf), 2011. §2.5.
2. Anders Karlsson, [“A proof of the subadditive ergodic theorem”](https://unige.ch/math/folks/karlsson/subaddnew.pdf), §1, Birkhoff theorem for a measure-preserving transformation without an invertibility assumption.
