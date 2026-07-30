+++
id = "complex-analysis/projective-connection"
title = "Holomorphic projective connection"
kind = "definition"
summary = "Local holomorphic coefficients transforming by the Schwarzian cocycle on a Riemann surface."
aliases = ["projective connection", "complex projective connection"]
domains = ["complex-analysis", "differential-geometry", "projective-geometry"]
section_mode = "progressive"
+++

Let \(X\) be a Riemann surface with local coordinates \(z\). In the convention of this knowl, a **holomorphic projective connection** is a collection of holomorphic functions \(R_z\), one in each coordinate, such that under a change of coordinate \(w=w(z)\),
\[
R_z(z)=R_w(w(z))\bigl(w'(z)\bigr)^2+S(w)(z),
\]
where \(S(w)\) is the [[complex-analysis/schwarzian-derivative|Schwarzian derivative]] of the coordinate change.

## Why this transformation law

If \(f\) is a locally univalent projective coordinate, set \(R_z=S(f)(z)\). The [[complex-analysis/schwarzian-chain-rule-and-mobius-characterization|Schwarzian chain rule]] gives exactly the displayed change-of-coordinate formula. Postcomposing \(f\) with a Möbius transformation leaves \(R_z\) unchanged.

## Relation to projective structures

A complex projective structure is an atlas of charts into \(\mathbb P^1(\mathbb C)\) whose transition maps are Möbius transformations. Its charts determine a projective connection by taking their Schwarzians in ordinary holomorphic coordinates. Conversely, the local differential equation \(S(f)=R_z\) produces projective charts; global continuation can carry monodromy in \(PGL_2(\mathbb C)\).

## Affine structure

If \(R\) and \(\widetilde R\) are two projective connections, their difference obeys
\[
(R_z-\widetilde R_z)
=(R_w-\widetilde R_w)\circ w\,(w')^2.
\]
Thus the difference is a holomorphic quadratic differential. Projective connections on a fixed Riemann surface, when nonempty, form an affine space modeled on holomorphic quadratic differentials.

## Convention warning

Some sources put a factor of \(1/2\), or the opposite sign, in the Schwarzian term. The displayed transformation law fixes the normalization used here. In higher-dimensional differential geometry, “projective connection” can instead mean a projective equivalence class of affine connections; that is related but not this one-dimensional holomorphic definition.

## References

1. R. C. Gunning, *Lectures on Riemann Surfaces*, Princeton University Press, 1966. Relevant: projective structures and projective connections.
2. Otto Forster, *Lectures on Riemann Surfaces*, Springer, 1981. [Publisher record](https://doi.org/10.1007/978-1-4612-5961-9). Relevant: analytic continuation and meromorphic functions.
