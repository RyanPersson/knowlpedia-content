+++
id = "ergodic-theory/essentially-free-action"
title = "Essentially free action"
kind = "definition"
summary = "An action for which almost every point has trivial stabilizer."
aliases = ["essential freeness", "free action modulo null sets"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-action", "measure-theory/standard-probability-space"]
+++

A measurable action of a countable discrete group \(G\) on a [[measure-theory/standard-probability-space|standard probability space]] is **essentially free** if
\[
\mu\{x:T_gx=x\}=0\qquad(g\ne e).
\]
Since \(G\) is countable, this is equivalent to almost every point having trivial stabilizer.

## Examples

An irrational circle rotation gives an essentially free \(\mathbb Z\)-action: no nonzero power fixes a point. A cycle of length \(n\) is ergodic as a \(\mathbb Z\)-system but not essentially free, since \(T^n\) is the identity. The action of \(\mathbb Z/n\mathbb Z\) by translation on itself is free; the acting group matters.
