---
title: "Continuous function"
description: "A function where small changes in input produce small changes in output."
---

A function \(f: X \to Y\) between {{< knowl id="metric-space" section="topology" text="metric spaces" >}} is **continuous** if it is {{< knowl id="continuity-at-a-point" text="continuous at every point" >}} of its domain.

## Equivalent characterizations
For metric spaces \((X, d_X)\) and \((Y, d_Y)\), the following are equivalent:

1. **\(\varepsilon\)-\(\delta\) definition**: For every \(a \in X\) and \(\varepsilon > 0\), there exists \(\delta > 0\) such that \(d_X(x, a) < \delta\) implies \(d_Y(f(x), f(a)) < \varepsilon\).

2. **Sequential characterization**: For every convergent sequence \(x_n \to a\), we have \(f(x_n) \to f(a)\).

3. **Topological definition**: The preimage of every {{< knowl id="open-set" section="topology" text="open set" >}} is open.

## Properties
- Compositions of continuous functions are continuous.
- Continuous functions preserve {{< knowl id="compact-set" section="topology" text="compactness" >}} and {{< knowl id="connected-set" section="topology" text="connectedness" >}}.
- Continuous functions on compact sets are {{< knowl id="uniform-continuity" text="uniformly continuous" >}} ({{< knowl id="heine-cantor-theorem" section="topology" text="Heine-Cantor theorem" >}}).

## Examples
- Polynomials, exponentials, trigonometric functions on \(\mathbb{R}\).
- The projection maps \(\pi_i: \mathbb{R}^n \to \mathbb{R}\).
