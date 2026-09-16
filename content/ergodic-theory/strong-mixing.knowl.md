+++
id = "ergodic-theory/strong-mixing"
title = "Strong mixing"
kind = "definition"
summary = "Asymptotic independence of an event and a distant-time event."
aliases = ["mixing transformation", "strongly mixing system"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-system"]
+++

A [[ergodic-theory/measure-preserving-system|probability-preserving transformation]] \(T\) is **strongly mixing** if
\[
\mu(T^{-n}A\cap B)\longrightarrow\mu(A)\mu(B)
\quad(n\to\infty)
\]
for every measurable \(A,B\). For a noncompact locally compact group action, replace \(T^n\) by \(T_g\) and let \(g\) leave every compact subset of the group.

## Observables

Equivalently, \(\langle U_T^nf,h\rangle\to0\) for every mean-zero \(f,h\in L^2\). This follows from the event formulation by approximation with simple functions. Hence \(U_T^nf\) converges weakly to zero on \(L^2_0\), even though \(\|U_T^nf\|_2=\|f\|_2\). Unitarity and mixing are compatible.

## Examples

The [[ergodic-theory/cat-map|cat map]], [[ergodic-theory/bernoulli-shift|Bernoulli shifts]], and the [[ergodic-theory/doubling-map|doubling map]] are mixing. Rotations of a nontrivial compact abelian group are not mixing.

## References

1. Jesse Peterson, [*Lecture notes on ergodic theory*](https://www.math.vanderbilt.edu/~peters10/teaching/Spring2011/ErgodicTheoryNotes.pdf), 2011. §§1.7 and 2.2.
