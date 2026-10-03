+++
id = "ergodic-theory/observable"
title = "Observable of a measurable dynamical system"
kind = "definition"
summary = "A measurable function recording a quantity along the states of a dynamical system."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-system", "measure-theory/measurable-function", "measure-theory/lp-space"]
+++

An **observable** on a measurable dynamical system is a [[measure-theory/measurable-function|measurable function]] \(f:X\to\mathbb C\) (or \(\mathbb R\)). In probability-preserving dynamics it is usually considered modulo almost-everywhere equality in a specified function space, such as \(L^1\), \(L^2\), or \(L^\infty\).

## Reading a trajectory

The sequence \(f(x),f(Tx),f(T^2x),\ldots\) records the observable along the orbit of \(x\). Indicator functions record visits to events. Coordinates record positions, while nonlinear observables can detect quantities such as radius or energy that coordinate functions alone miss.

The [[ergodic-theory/koopman-operator|Koopman operator]] evolves these functions linearly even when the state dynamics is nonlinear.
