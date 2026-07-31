+++
id = "differential-geometry/chronological-and-causal-future"
title = "Chronological and causal future"
kind = "definition"
summary = "The sets reachable from an event by future-directed timelike or causal curves."
aliases = ["chronological future", "causal future", "chronological past", "causal past", "I plus", "J plus"]
domains = ["differential-geometry", "mathematical-physics"]
section_mode = "progressive"
+++

Let \((M,g)\) be a time-oriented [[differential-geometry/lorentzian-manifold|Lorentzian manifold]]. The **chronological future** and **causal future** of \(p\in M\) are
\[
I^+(p)=\{q\in M:\text{a future-directed timelike curve runs from \(p\) to \(q\)}\},
\]
\[
J^+(p)=\{p\}\cup
\{q\in M:\text{a future-directed [[differential-geometry/causal-curve|causal curve]] runs from \(p\) to \(q\)}\}.
\]
The chronological and causal pasts \(I^-(p)\) and \(J^-(p)\) are defined with past-directed curves.

For \(A\subseteq M\), set
\[
I^\pm(A)=\bigcup_{p\in A}I^\pm(p),
\qquad
J^\pm(A)=\bigcup_{p\in A}J^\pm(p).
\]
One always has \(I^\pm(p)\subseteq J^\pm(p)\). The chronological future is open, whereas the causal future need not be closed without additional causal hypotheses.

The intersection \(J^+(p)\cap J^-(q)\) is the [[differential-geometry/causal-diamond|causal diamond]] between \(p\) and \(q\).

## References

1. Barrett O'Neill, *Semi-Riemannian Geometry With Applications to Relativity*, Academic Press, 1983. [Publisher record](https://doi.org/10.1016/C2009-0-03118-3). Relevant: Chapter 14.
2. Ettore Minguzzi, “Lorentzian causality theory,” *Living Reviews in Relativity* 22 (2019), article 3. [Journal record](https://doi.org/10.1007/s41114-019-0019-x).
