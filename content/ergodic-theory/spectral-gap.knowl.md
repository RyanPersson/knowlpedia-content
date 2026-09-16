+++
id = "ergodic-theory/spectral-gap"
title = "Spectral gap of a probability-preserving action"
kind = "definition"
summary = "Uniform displacement of every mean-zero observable by some element of a fixed finite set."
aliases = ["Koopman spectral gap"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/reduced-koopman-representation", "harmonic-analysis/almost-invariant-vectors"]
+++

A [[ergodic-theory/measure-preserving-action|probability-preserving action]] of a discrete group \(G\) has a **spectral gap** if there are a finite nonempty set \(F\subseteq G\) and \(\varepsilon>0\) such that
\[
\max_{g\in F}\|\kappa_0(g)f-f\|_2\geq\varepsilon\|f\|_2
\qquad(f\in L^2_0(X,\mu)).
\]
Equivalently, the reduced Koopman representation has no almost-invariant unit vectors. This condition in particular implies ergodicity.

## Quantitative averaging

Enlarge \(F\) to a finite symmetric set of size \(m\), and set
\[
M=\frac1m\sum_{g\in F}\kappa_0(g),\qquad B=\tfrac12(I+M).
\]
Then \(B\) is a positive self-adjoint contraction and
\[
\langle(I-M)f,f\rangle=\frac1{2m}\sum_{g\in F}\|\kappa_0(g)f-f\|_2^2
\geq\frac{\varepsilon^2}{2m}\|f\|_2^2.
\]
Hence \(\|B^n f\|_2\leq(1-\varepsilon^2/(4m))^n\|f\|_2\). This gives a rate for this averaging operator, not automatically for arbitrary orbit averages.

## References

1. Jesse Peterson, [*Lecture notes on ergodic theory*](https://www.math.vanderbilt.edu/~peters10/teaching/Spring2011/ErgodicTheoryNotes.pdf), 2011. §2.2.1, discussion after Theorem 2.2.8.
