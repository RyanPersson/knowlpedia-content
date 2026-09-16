+++
id = "ergodic-theory/space-average"
title = "Space average of an observable"
kind = "definition"
summary = "The expectation of an integrable observable under the chosen probability measure."
aliases = ["ensemble average of an observable"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/observable", "probability/expectation"]
+++

The **space average** of an integrable [[ergodic-theory/observable|observable]] \(f\) on \((X,\Sigma,\mu)\) is its [[probability/expectation|expectation]]
\[
\langle f\rangle_\mu=\int_X f\,d\mu.
\]
It averages over states distributed according to \(\mu\). For an event indicator \(f=1_E\), this average is \(\mu(E)\).

## Relation to time averages

A [[ergodic-theory/time-average|time average]] samples one orbit. The two notions are defined independently; [[ergodic-theory/birkhoff-ergodic-theorem|Birkhoff's theorem]] identifies typical limiting time averages with space averages when the system is ergodic.
