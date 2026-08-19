+++
id = "complex-analysis/upper-semicontinuous-function"
title = "Upper-semicontinuous function"
kind = "definition"
summary = "A function whose value at a limit point is at least the limsup of nearby values."
aliases = ["upper semicontinuity", "usc function"]
domains = ["complex-analysis", "topology", "real-analysis"]
section_mode = "progressive"
+++

A function \(u:X\to[-\infty,\infty\)) on a [[topology/topological-space|topological space]] is
**upper-semicontinuous** if
\[
\limsup_{y\to x}u(y)\le u(x)
\]
for every \(x\in X\). Equivalently, every strict sublevel set
\(\{x:u(x)<a\}\) is open.

## Sequential form

On a [[topology/metric-space|metric space]], upper semicontinuity is equivalent to
\(\limsup_{n\to\infty}u(x_n)\le u(x)\) whenever \(x_n\to x\).

## Role in potential theory

The upper-semicontinuity condition prevents upward jumps from being hidden by
averaging. Together with a sub-mean inequality, it is part of the definition
of [[complex-analysis/subharmonic-function|subharmonic]] and
[[complex-analysis/plurisubharmonic-function|plurisubharmonic]] functions.

## References

1. Thomas Ransford, *Potential Theory in the Complex Plane*, Cambridge University Press, 1995. [DOI record](https://doi.org/10.1017/CBO9780511623776).
