+++
id = "real-analysis/equicontinuity-pointwise-bounded-uniform-bounded"
title = "Equicontinuity + pointwise boundedness implies uniform boundedness on compact sets"
kind = "knowl"
summary = "On a compact metric space, an equicontinuous, pointwise bounded family of real-valued functions is uniformly bounded."
aliases = ["equicontinuity-pointwise-bounded-uniform-bounded", "Equicontinuity + pointwise boundedness implies uniform boundedness on compact sets"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/equicontinuity-pointwise-bounded-uniform-bounded.md"
+++

Let \((K,d)\) be a [[topology/compact-set|compact]] [[topology/metric-space|metric space]] and let \(\mathcal F\subseteq C(K,\mathbb R)\). If \(\mathcal F\) is [[real-analysis/equicontinuous-family|equicontinuous]] and [[real-analysis/pointwise-bounded-family|pointwise bounded]], meaning
\[
\sup_{f\in\mathcal F}|f(x)|<\infty
\quad\text{for every }x\in K,
\]
then \(\mathcal F\) is [[real-analysis/uniformly-bounded-family|uniformly bounded]]. Thus there is \(M<\infty\) such that
\[
|f(x)|\le M
\quad\text{for every }f\in\mathcal F\text{ and }x\in K.
\]

## Remarks

This lemma is a standard step in the proof of the [[real-analysis/arzela-ascoli-theorem|Arzelà–Ascoli theorem]].
