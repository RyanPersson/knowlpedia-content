+++
id = "differential-geometry/quaternionic-manifold"
title = "Quaternionic manifold"
kind = "definition"
summary = "An almost-quaternionic manifold whose rank-three quaternionic structure is preserved by a torsion-free connection."
aliases = ["integrable quaternionic manifold"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) have real dimension \(4n\) with \(n\geq2\). A **quaternionic manifold** is an [[differential-geometry/almost-quaternionic-manifold|almost-quaternionic manifold]] \((M,Q)\) for which there exists a torsion-free [[fiber-bundles/connection-on-a-vector-bundle|connection]] \(\nabla\) on \(TM\) that preserves \(Q\):
\[
\nabla_XA\in\Gamma(Q)
\]
for every [[fiber-bundles/vector-field|vector field]] \(X\) and every local section \(A\in\Gamma(Q)\). Such a \(\nabla\) is called a quaternionic connection. Preservation of \(Q\) does not require a chosen local admissible triple \((I,J,K)\) to be individually parallel; the connection may rotate that triple within \(Q\). The existence of \(\nabla\), not its choice, is part of the definition.

## Integrability and intrinsic torsion

The almost-quaternionic reduction has an [[fiber-bundles/intrinsic-torsion-of-a-g-structure|intrinsic torsion]]. In dimensions at least eight, its vanishing is equivalent to the existence of a torsion-free connection preserving \(Q\), which explains the synonym “integrable quaternionic manifold.” Unlike the hypercomplex case, a compatible torsion-free connection is generally not unique. The definition and its twistor interpretation originate in [Salamon, “Quaternionic Manifolds”].

## Relationship to nearby structures

A hypercomplex triple \((I,J,K)\) determines \(Q=\operatorname{span}\{I,J,K\}\), and its [[differential-geometry/obata-connection|Obata connection]] makes \(Q\) quaternionic. This construction forgets the distinguished global frame of \(Q\).

A [[differential-geometry/quaternion-kahler-manifold|quaternion-Kähler manifold]] of dimension at least eight is quaternionic because its [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]] is torsion-free and preserves \(Q\). Conversely, a quaternionic manifold has no preferred metric and need not admit a quaternion-Kähler metric. Thus “quaternionic” is an integrability condition on the \(GL(n,\mathbb H)Sp(1)\)-structure, whereas “quaternion-Kähler” is a Riemannian holonomy condition.

## Examples and non-examples

Quaternionic projective space \(\mathbb H P^n\) with its standard \(Q\) is quaternionic; its standard metric is in fact quaternion-Kähler. Every [[differential-geometry/hypercomplex-manifold|hypercomplex manifold]] is another example after forgetting its global triple.

An arbitrary almost-quaternionic manifold is a near miss: when its intrinsic torsion is nonzero, no torsion-free preserving connection exists. A connection preserving \(Q\) but having torsion also fails the defining condition.

## Four-dimensional convention

**Warning.** The restriction \(n\geq2\) is essential to the core convention. In real dimension four, an almost-quaternionic structure is equivalent to an oriented conformal structure, and the torsion-free-connection formulation no longer isolates the intended integrability condition. Authors commonly define a four-dimensional quaternionic manifold instead by a self-duality condition, with “self-dual” versus “anti-self-dual” depending on the orientation convention.

## References

1. Simon Salamon, “Quaternionic Manifolds,” *Symposia Mathematica* 26, 1982, 139–151. [Stable repository record](https://hdl.handle.net/11583/1405679). Relevant: the torsion-free definition, twistor construction, and dimension-four convention.
2. Arthur L. Besse, *Einstein Manifolds*, Springer, 1987. [Springer DOI record](https://doi.org/10.1007/978-3-540-74311-8). Relevant: Chapter 14, quaternionic and quaternion-Kähler manifolds.
