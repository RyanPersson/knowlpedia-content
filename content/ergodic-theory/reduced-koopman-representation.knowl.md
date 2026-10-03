+++
id = "ergodic-theory/reduced-koopman-representation"
title = "Reduced Koopman representation"
kind = "definition"
summary = "The Koopman representation restricted to mean-zero observables."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/koopman-representation", "linear-algebra/orthogonal-complement"]
+++

Given a [[ergodic-theory/koopman-representation|Koopman representation]] \(\kappa\), its **reduced Koopman representation** is the restriction \(\kappa_0=\kappa|_{L^2_0}\), where
\[
L^2_0(X,\mu)=\left\{f\in L^2(X,\mu):\int_X f\,d\mu=0\right\},
\qquad L^2=\mathbb C1\oplus L^2_0.
\]
Both summands are invariant because a probability-preserving action fixes constants and preserves integrals.

## Ergodicity and irreducibility

Ergodicity means \(\kappa_0\) has no nonzero fixed vectors. It does not mean that \(\kappa_0\) is [[lie-groups/irreducible-unitary-representation|irreducible]]: an irrational rotation has many invariant Fourier lines and is still ergodic.

## Terminology

Some sources use “[[ergodic-theory/koopman-representation|Koopman representation]]” for this restriction. In these knowls, the unqualified representation acts on all of \(L^2\), and “reduced” explicitly removes constants.

## References

1. Jesse Peterson, [*Lecture notes on ergodic theory*](https://www.math.vanderbilt.edu/~peters10/teaching/Spring2011/ErgodicTheoryNotes.pdf), 2011. §2.2.
