+++
id = "ergodic-theory/measure-preserving-action"
title = "Measure-preserving group action"
kind = "definition"
summary = "A left group action by probability-preserving measurable maps."
aliases = ["probability-measure-preserving action", "pmp action"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["algebra-groups/group", "probability/probability-space", "ergodic-theory/measure-preserving-transformation"]
+++

A **measure-preserving left action** of a group \(G\) on a [[probability/probability-space|probability space]] \((X,\Sigma,\mu)\) is a family of measurable maps \(T_g:X\to X\) satisfying
\[
T_e=\mathrm{id},\qquad T_{gh}=T_g\circ T_h,\qquad
\mu(T_g^{-1}E)=\mu(E)
\]
for all \(g,h\in G\) and \(E\in\Sigma\). Each \(T_g\) is automatically invertible, with inverse \(T_{g^{-1}}\).

## Measurability conventions

For a discrete group, measurability of each map suffices. For a locally compact group acting on a standard Borel model, one usually requires joint measurability of \((g,x)\mapsto T_gx\). Whenever a topological representation theorem is used, the associated Koopman representation is assumed strongly continuous.

Actions may also be defined by maps modulo null sets, with the laws holding almost everywhere for each pair \(g,h\). For uncountable groups this does not assert a single conull set on which every law holds simultaneously.
