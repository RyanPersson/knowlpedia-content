---
title: "Heine-Cantor theorem"
description: "A continuous function on a compact metric space is uniformly continuous."
---

The **Heine-Cantor theorem** states: if \(f: K \to Y\) is a {{< knowl id="continuous-function" section="real-analysis" text="continuous function" >}} from a {{< knowl id="compact-set" text="compact" >}} {{< knowl id="metric-space" text="metric space" >}} \(K\) to a metric space \(Y\), then \(f\) is {{< knowl id="uniform-continuity" section="real-analysis" text="uniformly continuous" >}}.

## Statement
For every \(\varepsilon > 0\), there exists \(\delta > 0\) such that for all \(x, y \in K\):
$$
d_K(x, y) < \delta \implies d_Y(f(x), f(y)) < \varepsilon.
$$

The key point is that \(\delta\) depends only on \(\varepsilon\), not on the choice of points \(x, y\).

## Proof idea
1. Cover \(K\) with open balls where \(f\) varies by less than \(\varepsilon\).
2. By compactness, extract a finite subcover.
3. Use the {{< knowl id="lebesgue-number-lemma" text="Lebesgue number" >}} of the cover as \(\delta\).

## Classical version
A continuous function \(f: [a,b] \to \mathbb{R}\) is uniformly continuous.

## Counterexample
\(f(x) = 1/x\) on \((0,1]\) is continuous but not uniformly continuous (domain not compact).
