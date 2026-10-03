+++
id = "ergodic-theory/minimal-system"
title = "Minimal topological dynamical system"
kind = "definition"
summary = "A continuous dynamical system in which every forward orbit is dense."
aliases = ["minimality of a transformation"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["topology/continuous-map", "topology/compact-set", "algebra-groups/orbit"]
+++

A [[topology/continuous-map|continuous map]] \(T:X\to X\) on a nonempty compact metric space is **minimal** if every forward orbit \(\{T^nx:n\geq0\}\) is dense in \(X\). Equivalently, there is no proper nonempty closed set \(F\) with \(T(F)\subseteq F\).

## Relation to probability

Minimality concerns every point and the topology. Ergodicity concerns invariant events modulo null sets for one invariant measure. Irrational circle rotations have both properties, but minimality alone does not guarantee a unique invariant probability measure.
