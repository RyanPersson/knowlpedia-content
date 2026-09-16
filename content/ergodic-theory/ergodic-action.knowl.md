+++
id = "ergodic-theory/ergodic-action"
title = "Ergodic group action"
kind = "definition"
summary = "A measure-preserving action whose jointly invariant measurable events have probability zero or one."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-action", "ergodic-theory/invariant-sigma-algebra"]
+++

A [[ergodic-theory/measure-preserving-action|measure-preserving action]] \(G\curvearrowright(X,\mu)\) is **ergodic** if any measurable \(E\) satisfying
\[
\mu(T_g^{-1}E\triangle E)=0\qquad\text{for every }g\in G
\]
has probability zero or one.

## Joint invariance

All group elements enter the definition. Individual generators can fail to be ergodic while their joint action is ergodic. For example, the two irrational translations along the separate coordinates of a two-torus jointly have only constant invariant functions; see [[ergodic-theory/gaussian-integer-translations|Gaussian-integer translations]].
