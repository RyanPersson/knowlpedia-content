+++
id = "differential-geometry/orbifold"
title = "Smooth effective orbifold"
kind = "definition"
summary = "A space with compatible smooth local charts that are quotients by finite effective group actions."
aliases = ["orbifold", "effective orbifold", "smooth orbifold"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["topology/hausdorff-space", "topology/second-countable-space", "algebra-groups/faithful-action", "fiber-bundles/smooth-map"]
+++

A **smooth effective orbifold** of dimension \(n\) is a Hausdorff, second-countable space \(X\) equipped with an equivalence class of compatible local quotient atlases. A chart consists of a connected open set \(\widetilde U\subseteq\mathbb R^n\), a finite group \(G\) acting smoothly and [[algebra-groups/faithful-action|effectively]] on it, and a continuous map \(\phi:\widetilde U\to X\) inducing a homeomorphism \(\widetilde U/G\cong U\) onto an open subset of \(X\).

The chart images cover \(X\). At each point of two overlapping images there must be a third chart mapping into both: a chart embedding consists of an injective group homomorphism and an equivariant smooth open embedding of the chart domains that commutes with the maps to \(X\). Atlases are equivalent when they admit a common refinement. These compatibility conditions, together with the local finite-quotient charts, are the orbifold structure.

## What the underlying space forgets

In \(\mathbb R^2/C_m\), let \(C_m\) act by rotation through \(2\pi/m\). The underlying quotient is homeomorphic to a plane, but the origin has an isotropy group of order \(m\). The orbifold remembers this group.

## Convention

We use effective actions and allow general finite chart actions. Ineffective orbifolds retain additional stabilizer information and require a broader convention.

## References

1. A. Adem and M. Klaus, *Lectures on orbifolds and group cohomology*, §2, Definitions 2.1–2.2. [Author-hosted notes](https://www.math.ubc.ca/~adem/hangzhou.pdf)
