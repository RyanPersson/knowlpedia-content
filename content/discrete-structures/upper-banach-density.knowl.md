+++
id = "discrete-structures/upper-banach-density"
title = "Upper Banach density"
kind = "definition"
summary = "The limiting maximal proportion of a set of integers in long intervals."
aliases = []
domains = ["discrete-structures"]
section_mode = "progressive"
prerequisites = ["shared-foundations/integers", "shared-foundations/cardinality"]
+++

For [[shared-foundations/integers|\(E\subseteq\mathbb Z\)]], its **upper Banach density** is
\[
d^*(E)=\limsup_{N\to\infty}\ \sup_{m\in\mathbb Z}
\frac{|E\cap\{m,m+1,\ldots,m+N-1\}|}{N}.
\]
It measures the greatest density that persists in arbitrarily long intervals, allowing their starting positions to vary.

## Comparison with ordinary upper density

For \(E\subseteq\mathbb N\), the ordinary upper density is \(\limsup_N |E\cap\{1,\ldots,N\}|/N\), which cannot exceed \(d^*(E)\). The two can differ: a set containing arbitrarily long intervals separated by sufficiently large gaps has upper Banach density one but can have ordinary upper density zero.

Both positive-density notions imply the existence of arbitrarily long arithmetic progressions by Szemerédi's theorem.
