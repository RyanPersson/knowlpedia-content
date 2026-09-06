+++
id = "complex-analysis/projective-connection"
title = "Holomorphic projective connection"
kind = "definition"
summary = "Local holomorphic coefficients transforming by the Schwarzian cocycle on a Riemann surface."
aliases = ["projective connection", "complex projective connection"]
domains = ["complex-analysis", "differential-geometry", "projective-geometry"]
prerequisites = ["differential-geometry/riemann-surface", "complex-analysis/schwarzian-derivative", "complex-analysis/schwarzian-chain-rule"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be a [[differential-geometry/riemann-surface|Riemann surface]] with local coordinates \(z\). In the convention of this knowl, a **holomorphic projective connection** is a collection of holomorphic functions \(R_z\), one in each coordinate, such that under a change of coordinate \(w=w(z)\),
\[
R_z(z)=R_w(w(z))\bigl(w'(z)\bigr)^2+S(w)(z),
\]
where \(S(w)\) is the [[complex-analysis/schwarzian-derivative|Schwarzian derivative]] of the coordinate change.

## Why this transformation law

If \(f\) is a locally univalent projective coordinate, set \(R_z=S(f)(z)\). The [[complex-analysis/schwarzian-chain-rule|Schwarzian chain rule]] gives exactly the displayed change-of-coordinate formula. Postcomposing \(f\) with a [[complex-analysis/mobius-transformation|Möbius transformation]] leaves \(R_z\) unchanged.

## Relation to projective structures

A [[complex-analysis/complex-projective-structure|complex projective structure]] determines a projective connection by taking the Schwarzians of its projective charts in ordinary holomorphic coordinates. Conversely, the local equation \(S(f)=R_z\) produces projective charts. The [[complex-analysis/projective-connections-form-an-affine-space|affine-space theorem for projective connections]] describes how any two such connections differ.

## Convention warning

Some sources put a factor of \(1/2\), or the opposite sign, in the Schwarzian term. The displayed transformation law fixes the normalization used here. In higher-dimensional differential geometry, “projective connection” can instead mean a projective equivalence class of affine connections; that is related but not this one-dimensional holomorphic definition.

## References

1. R. C. Gunning, *Lectures on Riemann Surfaces*, Princeton University Press, 1966. Relevant: projective structures and projective connections.
2. Otto Forster, *Lectures on Riemann Surfaces*, Springer, 1981. [Publisher record](https://doi.org/10.1007/978-1-4612-5961-9). Relevant: analytic continuation and meromorphic functions.
