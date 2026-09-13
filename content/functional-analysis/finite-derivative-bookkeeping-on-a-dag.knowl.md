+++
id = "functional-analysis/finite-derivative-bookkeeping-on-a-dag"
title = "Derivative requirements on a finite computation graph"
kind = "theorem"
summary = "A finite acyclic composition of operations with finite derivative requirements has a finite input requirement at each output order."
aliases = ["finite-stage derivative accounting"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["discrete-structures/directed-acyclic-graph", "functional-analysis/derivative-loss", "shared-foundations/recursion-on-natural-numbers", "real-analysis/maximum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Consider a finite [[discrete-structures/directed-acyclic-graph|directed acyclic graph]] whose vertices are intermediate smooth expressions. Suppose bounding output derivatives through order \(m\) at vertex \(v\) requires only derivatives through a finite order \(\phi_{vw}(m)\) of each input vertex \(w\to v\). Then every fixed output derivative order requires only finitely many derivatives of each original source.

## Recursive bound

For a source \(a\), let \(D_{v,a}(m)\) be a sufficient derivative order at that source. At source vertices set \(D_{a,a}(m)=m\) and \(D_{b,a}(m)=0\) for \(b\ne a\). In an order respecting the graph arrows, define
\[
D_{v,a}(m)=\max_{w\to v}D_{w,a}(\phi_{vw}(m)).
\]
Every maximum is finite and only finitely many operations are composed. For a fixed derivative loss \(d_{vw}\), take \(\phi_{vw}(m)=m+d_{vw}\).

## Separate from scale losses

The resulting number may grow with the number of correction stages. It does not by itself bound powers of a small parameter in the estimate. An operation requiring more input derivatives can still have the same explicit scale loss at every stage. Both kinds of bookkeeping must be proved for the actual operations on their actual domains.
