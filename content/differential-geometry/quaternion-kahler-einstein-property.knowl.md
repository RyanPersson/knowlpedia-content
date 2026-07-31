+++
id = "differential-geometry/quaternion-kahler-einstein-property"
title = "Quaternion-Kähler manifolds are Einstein"
kind = "theorem"
summary = "Every quaternion-Kähler manifold of real dimension at least eight has Ricci tensor proportional to its metric."
aliases = ["Einstein property of quaternion-Kähler manifolds"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \((M^{4n},g)\) be a connected [[differential-geometry/quaternion-kahler-manifold|quaternion-Kähler manifold]] with \(n\geq2\). Then \(g\) is an [[differential-geometry/einstein-manifold|Einstein metric]]: there is a constant \(\lambda\in\mathbb R\) such that
\[
\operatorname{Ric}_g=\lambda g.
\]
Equivalently, its scalar curvature is constant and equals \(4n\lambda\). The conclusion includes the case \(\lambda=0\), which occurs when the holonomy reduces to the hyperkähler subgroup \(\operatorname{Sp}(n)\). The restriction to real dimension at least eight is essential: in dimension four the inclusion \(\operatorname{Hol}(g)\subseteq\operatorname{Sp}(1)\operatorname{Sp}(1)=\operatorname{SO}(4)\) alone is automatic and does not imply the Einstein equation.

## Geometric mechanism

The [[fiber-bundles/holonomy-representation|holonomy representation]] of \(\operatorname{Sp}(n)\operatorname{Sp}(1)\) sharply restricts the curvature tensor. The Ricci contraction of the allowed curvature components has only the metric as an invariant symmetric two-tensor, forcing proportionality to \(g\). Constancy of the proportionality factor then follows from the contracted [[fiber-bundles/bianchi-identity|Bianchi identity]]. Besse states the result as.

## Sign and examples

All three signs occur. Quaternionic projective space with its standard metric has positive Einstein constant, quaternionic hyperbolic space has negative Einstein constant, and [[differential-geometry/hyperkahler-manifold|hyperkähler manifolds]] have zero Einstein constant. Thus the theorem does not determine the sign of the scalar curvature.

Under the usual four-dimensional convention, “quaternion-Kähler” is redefined to include the Einstein condition together with self-duality. The theorem then becomes definitional in dimension four rather than a consequence of the unrestricted holonomy condition.

## References

1. Arthur L. Besse, *Einstein Manifolds*, Springer, 1987. [Springer DOI record](https://doi.org/10.1007/978-3-540-74311-8). Relevant: Chapter 14, especially Theorem 14.39.
2. Simon Salamon, “Quaternionic Kähler Manifolds,” *Inventiones Mathematicae* 67 (1982), 143–171. [DOI record](https://doi.org/10.1007/BF01393378). Relevant: the curvature and Einstein properties of quaternion-Kähler metrics.
