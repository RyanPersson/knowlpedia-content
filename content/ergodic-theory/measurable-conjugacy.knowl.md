+++
id = "ergodic-theory/measurable-conjugacy"
title = "Measurable conjugacy"
kind = "definition"
summary = "An isomorphism of probability spaces intertwining their transformations."
aliases = ["measure-theoretic conjugacy", "isomorphism of measure-preserving systems"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/measure-space-isomorphism", "ergodic-theory/measure-preserving-system"]
+++

A **measurable conjugacy** between probability-preserving systems \((X,\mu,T)\) and \((Y,\nu,S)\) is an [[measure-theory/measure-space-isomorphism|isomorphism modulo null sets]] \(b:X\to Y\) such that
\[
b\circ T=S\circ b\quad\text{almost everywhere}.
\]
Thus \(S=bTb^{-1}\) wherever the representatives are defined.

## Consequences

Conjugacy preserves ergodicity, mixing, and distributions of time averages. Pullback \(Wf=f\circ b\) is a unitary \(L^2(Y,\nu)\to L^2(X,\mu)\) intertwining the forward Koopman operators. The converse implication from an arbitrary unitary intertwiner to measurable conjugacy is generally false: the function-algebra structure carries additional information.
