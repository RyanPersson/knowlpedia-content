+++
id = "ergodic-theory/kolmogorov-sinai-entropy"
title = "Kolmogorov–Sinai entropy"
kind = "definition"
summary = "The supremum of information production rates over finite measurable observations of a system."
aliases = ["metric entropy", "measure-theoretic entropy", "Kolmogorov-Sinai entropy"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measurable-partition", "probability/shannon-entropy", "ergodic-theory/measure-preserving-system"]
+++

For a [[ergodic-theory/measurable-partition|finite measurable partition]] \(\mathcal P\), define its entropy by
\[
H_\mu(\mathcal P)=-\sum_{P\in\mathcal P}\mu(P)\log\mu(P),\qquad0\log0=0.
\]
Its entropy rate under a [[ergodic-theory/measure-preserving-system|probability-preserving transformation]] is
\[
h_\mu(T,\mathcal P)=\lim_{n\to\infty}\frac1nH_\mu\left(\bigvee_{j=0}^{n-1}T^{-j}\mathcal P\right).
\]
Subadditivity makes this limit exist. The **Kolmogorov–Sinai entropy** is \(h_\mu(T)=\sup_{\mathcal P}h_\mu(T,\mathcal P)\), over all finite measurable partitions. Natural logarithms measure entropy in nats per step.

## Meaning and invariance

The partition describes a finite-resolution observation. Its entropy rate measures how much additional information is needed per time step to record long orbit names. Measurable conjugacy preserves every such observation process and therefore preserves \(h_\mu(T)\).

## Bernoulli example

For a Bernoulli shift on a finite alphabet with probabilities \(p_j\), the coordinate partition generates the system and independence gives \(h_\mu(T)=-\sum_jp_j\log p_j\), by the generator theorem.
