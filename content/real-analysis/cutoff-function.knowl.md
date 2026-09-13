+++
id = "real-analysis/cutoff-function"
title = "Smooth cutoff function"
kind = "definition"
summary = "A smooth function equal to one near a chosen set and supported in a specified open region."
aliases = ["cutoff", "cutoff function", "smooth cut-off"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/class-ck-map", "shared-foundations/support-of-a-function", "topology/neighborhood", "topology/open-set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(A\subseteq U\subseteq\mathbb R^n\), with \(U\) open. A **smooth cutoff for \(A\) supported in \(U\)** is a [[real-analysis/class-ck-map|smooth function]] \(\chi:\mathbb R^n\to[0,1]\) that equals \(1\) on a neighborhood of \(A\) and satisfies \(\operatorname{supp}\chi\subseteq U\).

## Compact and noncompact versions

When \(A\) is compact, one can choose \(\chi\) to have [[real-analysis/compactly-supported-function|compact support]] in \(U\). More generally, cutoffs adapted to unbounded regions need not have compact support. The support and plateau requirements must therefore be specified separately.

## One-dimensional transition

Let \(h(t)=e^{-1/t}\) for \(t>0\) and \(h(t)=0\) for \(t\le0\). Then
\[
\vartheta(t)=\frac{h(t)}{h(t)+h(1-t)}
\]
is smooth, equals \(0\) for \(t\le0\), and equals \(1\) for \(t\ge1\). The denominator is positive everywhere; smoothness of \(h\) at zero follows from the [[real-analysis/flat-exponential|flat-exponential construction]]. Translating and rescaling transitions produces plateaus with prescribed margins.

## References

- [Richard Schwartz, Partitions of Unity (Brown lecture notes)](https://www.math.brown.edu/reschwar/M114B/notes9.pdf).
