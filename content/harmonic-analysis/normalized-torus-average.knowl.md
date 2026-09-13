+++
id = "harmonic-analysis/normalized-torus-average"
title = "Normalized torus average"
kind = "definition"
summary = "Integration over a lattice cell divided by its volume gives a translation-invariant probability average."
aliases = ["normalized Haar average on a torus", "torus mean"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["topology/flat-torus", "linear-algebra/lattice-fundamental-domain", "measure-theory/lebesgue-integral", "linear-algebra/determinant", "real-analysis/change-of-variables-formula"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For an integrable function on the [[topology/flat-torus|flat torus]] \(\mathbb R^n/B\mathbb Z^n\), its **normalized torus average** is
\[
\langle f\rangle=\frac1{|\det B|}\int_{B[0,1)^n}f([x])\,dx
=\int_{[0,1)^n}f([By])\,dy.
\]
In particular \(\langle1\rangle=1\). The same integral results from any measurable fundamental domain.

## Translation invariance

Translating the domain and partitioning it into lattice translates of pieces of the original domain shows \(\langle f(\cdot+a)\rangle=\langle f\rangle\). Thus this is the probability normalization of [[harmonic-analysis/haar-measure|Haar measure]] on the torus. On the unit torus a smooth function's average is its [[harmonic-analysis/zero-fourier-mode|zero Fourier mode]]. Averaging independent auxiliary variables does not mean averaging physical coordinates after an auxiliary map has been evaluated.
