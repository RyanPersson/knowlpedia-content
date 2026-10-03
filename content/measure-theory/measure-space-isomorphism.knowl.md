+++
id = "measure-theory/measure-space-isomorphism"
title = "Isomorphism of probability spaces modulo null sets"
kind = "definition"
summary = "A probability-preserving measurable bijection between conull parts of two spaces."
aliases = ["measure isomorphism", "probability-space isomorphism"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["probability/probability-space", "measure-theory/almost-everywhere", "measure-theory/measurable-function"]
+++

An **isomorphism modulo null sets** between [[probability/probability-space|probability spaces]] \((X,\Sigma,\mu)\) and \((Y,\mathcal T,\nu)\) is a bijection \(b:X_0\to Y_0\) between measurable subsets of measure one such that \(b,b^{-1}\) are measurable and
\[
\mu(b^{-1}E)=\nu(E)\qquad(E\subseteq Y_0\text{ measurable}).
\]
Maps agreeing [[measure-theory/almost-everywhere|almost everywhere]] represent the same isomorphism.

## What is preserved

Integration, measurable events modulo null sets, and \(L^p\) norms are preserved. Topology, distance, and linear coordinates are additional structures that this definition need not preserve. Compatibility with dynamics is the extra requirement in [[ergodic-theory/measurable-conjugacy|measurable conjugacy]].
