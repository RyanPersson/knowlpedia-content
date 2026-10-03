+++
id = "ergodic-theory/measure-preserving-transformation"
title = "Measure-preserving transformation"
kind = "definition"
summary = "A measurable self-map whose inverse images preserve the measure of every event."
aliases = ["probability-preserving transformation", "pmp transformation"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["probability/probability-space", "measure-theory/measurable-function", "measure-theory/pushforward-measure"]
+++

A **probability-measure-preserving transformation** of a [[probability/probability-space|probability space]] \((X,\Sigma,\mu)\) is a [[measure-theory/measurable-function|measurable]] map \(T:X\to X\) such that
\[
\mu(T^{-1}E)=\mu(E)\qquad(E\in\Sigma).
\]
Equivalently, its [[measure-theory/pushforward-measure|pushforward]] satisfies \(T_*\mu=\mu\). Here \(T^{-1}E\) means a preimage and does not assume an inverse map.

## Invertibility and integration

An invertible transformation has a measurable inverse, possibly after discarding null sets. Measure preservation implies
\[
\int_X f\circ T\,d\mu=\int_X f\,d\mu
\]
for nonnegative measurable or integrable \(f\). This identity makes composition well defined on almost-everywhere equivalence classes.

## Examples

Permutations preserve uniform probability on a finite set. The [[ergodic-theory/doubling-map|doubling map]] preserves circle probability without being invertible modulo null sets.
