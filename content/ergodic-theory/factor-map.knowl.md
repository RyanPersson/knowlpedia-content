+++
id = "ergodic-theory/factor-map"
title = "Factor of a probability-preserving system"
kind = "definition"
summary = "A measurable probability-preserving quotient compatible with dynamics."
aliases = ["measurable factor", "factor system"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-system", "measure-theory/pushforward-measure"]
+++

A **factor map** between [[ergodic-theory/measure-preserving-system|probability-preserving systems]] \((X,\mu,T)\) and \((Y,\nu,S)\) is a measurable map \(p:X\to Y\) such that
\[
p_*\mu=\nu,\qquad p\circ T=S\circ p\quad\text{almost everywhere}.
\]
The target system is a **factor** of the source. For a group action the intertwining identity is required for every group element.

## Observable interpretation

Pullback \(f\mapsto f\circ p\) embeds \(L^2(Y,\nu)\) isometrically into \(L^2(X,\mu)\) as an invariant space of observables. On standard spaces, factors can equivalently be described by invariant sub-sigma-algebras modulo null sets.

An arbitrary invariant Hilbert subspace need not define a factor: the corresponding bounded observables must also retain multiplication and complex conjugation.
