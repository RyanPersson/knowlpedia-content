+++
id = "ergodic-theory/measure-preserving-system"
title = "Probability-preserving dynamical system"
kind = "definition"
summary = "A probability space together with a measure-preserving transformation."
aliases = ["measure-preserving dynamical system", "pmp system"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["probability/probability-space", "ergodic-theory/measure-preserving-transformation"]
+++

A **probability-preserving dynamical system** is a quadruple \((X,\Sigma,\mu,T)\), where \((X,\Sigma,\mu)\) is a [[probability/probability-space|probability space]] and \(T\) is a [[ergodic-theory/measure-preserving-transformation|measure-preserving transformation]]. The system is invertible when \(T\) is invertible modulo null sets.

## Iteration

The iterates satisfy \(T^0=\mathrm{id}\) and \(T^{m+n}=T^mT^n\) for \(m,n\geq0\). Invertibility extends these laws to all integers, giving a [[ergodic-theory/measure-preserving-action|measure-preserving action]] of \(\mathbb Z\).

## Statistical questions

Ergodic theory asks how [[ergodic-theory/time-average|orbit averages]], invariant events, and correlations reflect the long-term behavior of the system. The probability measure is part of the data: the same map can be ergodic for one invariant probability measure and nonergodic for another.
