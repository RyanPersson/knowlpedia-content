+++
id = "differential-geometry/kronecker-foliation"
title = "Kronecker foliation of the two-torus"
kind = "example"
summary = "The foliation by orbits of a constant-slope linear flow, with an irrational rotation as return map."
aliases = []
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/foliation", "ergodic-theory/measure-preserving-flow", "ergodic-theory/first-return-map", "topology/flat-torus"]
+++

For irrational \(\theta\), the **Kronecker foliation** of \(\mathbb T^2\) has leaves given by the [[fiber-bundles/orbit-of-a-group-action|orbits]] of
\[
\Phi^t(x,y)=(x+t,y+\theta t)\bmod\mathbb Z^2.
\]
Locally these are parallel straight lines; each leaf is dense. The flow preserves Haar probability.

## Rotation on a transversal

The circle \(\{0\}\times\mathbb T\) meets each leaf. Its first-return map at time one is \(y\mapsto y+\theta\). Two points on this transversal belong to the same leaf exactly when they belong to the same irrational-rotation orbit.

The rotation crossed product is therefore a concrete algebra associated with the transversal dynamics of the leaf space. The full foliation operator algebra and the transversal algebra are related by Morita equivalence; they should not be identified merely by writing the same orbit relation.

## References

1. Alain Connes, [*Noncommutative Geometry*](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf), 1994, Introduction, Kronecker foliation and its transverse rotation.
