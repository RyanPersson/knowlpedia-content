+++
id = "differential-geometry/biholomorphism"
title = "Biholomorphism"
kind = "definition"
summary = "A bijective holomorphic map whose inverse is holomorphic."
aliases = ["biholomorphic map", "holomorphic isomorphism"]
domains = ["differential-geometry", "complex-analysis"]
section_mode = "progressive"
+++

Let \(X\) and \(Y\) be [[differential-geometry/complex-manifold|complex manifolds]]. A **biholomorphism** from \(X\) to \(Y\) is a bijective [[differential-geometry/holomorphic-map|holomorphic map]]
\[
f:X\to Y
\]
whose set-theoretic inverse \(f^{-1}:Y\to X\) is also holomorphic. Two complex manifolds are **biholomorphic** if a biholomorphism exists between them. Biholomorphisms are precisely the isomorphisms in the category of complex manifolds and holomorphic maps; they preserve complex dimension, holomorphic functions, and the holomorphic-coordinate structure.

## Local criterion

A holomorphic map is locally biholomorphic near a point exactly when its complex differential there is invertible, by the holomorphic inverse-function theorem. A globally bijective local biholomorphism is a biholomorphism. Bijectivity alone should not be substituted for the local differential condition without a theorem guaranteeing holomorphicity of the inverse.

## Examples and invariants

Every invertible complex-affine map \(z\mapsto Az+b\) on \(\mathbb C^n\) is a biholomorphism. The [[fiber-bundles/exponential-map|exponential map]] \(\exp:\mathbb C\to\mathbb C^\times\) is locally biholomorphic but not globally biholomorphic because it is not injective. Biholomorphic manifolds have isomorphic algebras of global holomorphic functions, though the converse need not hold without additional hypotheses.

## Conventions and contrasts

A biholomorphism is stronger than a [[fiber-bundles/diffeomorphism|diffeomorphism]] of the underlying [[fiber-bundles/smooth-manifold|smooth manifolds]] because its differential must be complex linear in holomorphic coordinates. An antiholomorphic diffeomorphism is not a biholomorphism under this convention.

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: local holomorphic maps, complex manifolds, and the holomorphic inverse-function theorem.
