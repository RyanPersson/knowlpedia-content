+++
id = "ergodic-theory/koopman-representation"
title = "Koopman representation"
kind = "definition"
summary = "The unitary representation on observables obtained by inverse pullback of a measure-preserving left action."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-action", "measure-theory/l2-hilbert-space", "functional-analysis/unitary-operator", "algebra-representation-theory/group-representation"]
+++

For a [[ergodic-theory/measure-preserving-action|measure-preserving left action]] \(g\mapsto T_g\), its **Koopman representation** is
\[
\kappa:G\longrightarrow\mathcal U(L^2(X,\mu)),\qquad
(\kappa(g)f)(x)=f(T_{g^{-1}}x).
\]
It satisfies \(\kappa(e)=I\), \(\kappa(gh)=\kappa(g)\kappa(h)\), and each \(\kappa(g)\) is unitary. For topological groups we explicitly assume [[lie-groups/strongly-continuous-unitary-representation|strong continuity]] when invoking results that require it.

## Why the inverse is present

Applying two pullbacks yields
\[
\kappa(g)\kappa(h)f
=f\circ T_{h^{-1}}\circ T_{g^{-1}}
=f\circ T_{(gh)^{-1}}.
\]
The norm identity is \(\|f\circ T_{g^{-1}}\|_2=\|f\|_2\), and \(\kappa(g^{-1})\) is the inverse. This verifies all representation axioms.

## What it records

States are points of \(X\); vectors of the representation are observables. Nonconstant fixed vectors obstruct ergodicity, and matrix coefficients are correlations. The [[ergodic-theory/reduced-koopman-representation|reduced representation]] removes the constants that are always fixed; a nonzero finite-dimensional invariant subspace in that reduced representation obstructs weak mixing.

## References

1. Jesse Peterson, [*Lecture notes on ergodic theory*](https://www.math.vanderbilt.edu/~peters10/teaching/Spring2011/ErgodicTheoryNotes.pdf), 2011. §2.2.
