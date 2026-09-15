+++
id = "ergodic-theory/koopman-operator"
title = "Koopman operator"
kind = "definition"
summary = "The linear isometry that advances an observable by composition with a measure-preserving transformation."
aliases = ["composition Koopman operator"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-transformation", "measure-theory/l2-hilbert-space", "functional-analysis/unitary-operator"]
+++

The **forward Koopman operator** of a [[ergodic-theory/measure-preserving-transformation|probability-preserving transformation]] \(T\) is
\[
U_T:L^2(X,\mu)\longrightarrow L^2(X,\mu),\qquad U_Tf=f\circ T.
\]
It is a linear isometry. If \(T\) is invertible modulo null sets, it is [[functional-analysis/unitary-operator|unitary]], with \(U_T^{-1}f=f\circ T^{-1}\).

## Verification

Measure preservation gives \(\|U_Tf\|_2^2=\int|f|^2\circ T\,d\mu=\|f\|_2^2\). It also sends equality almost everywhere to equality almost everywhere, so the formula is independent of representatives. Composition respects linear combinations of functions without requiring any linear structure on \(X\).

## Direction of time

This convention gives \(U_T^nf=f\circ T^n\), as in time averages. For the left action \(n\mapsto T^n\), the [[ergodic-theory/koopman-representation|Koopman representation]] instead has \(\kappa(n)=U_T^{-n}\). Under noncommuting transformations, forward pullback reverses composition order.

## Noninvertible example

For the doubling map, \(U_T e_k=e_{2k}\). Odd Fourier frequencies are absent from its range. Thus it is an isometry that is not onto, and its nonnegative powers do not extend to a unitary representation of \(\mathbb Z\).

## References

1. Jesse Peterson, [*Lecture notes on ergodic theory*](https://www.math.vanderbilt.edu/~peters10/teaching/Spring2011/ErgodicTheoryNotes.pdf), 2011. §2.2.
