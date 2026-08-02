+++
id = "lie-groups/complex-lie-group"
title = "Complex Lie group"
kind = "definition"
summary = "A complex manifold whose multiplication and inversion maps are holomorphic."
aliases = ["complex analytic Lie group"]
domains = ["lie-groups", "differential-geometry"]
section_mode = "progressive"
+++

A **complex Lie group** is a [[differential-geometry/complex-manifold|complex manifold]] \(G\) with a group structure for which
\[
m:G\times G\longrightarrow G,\qquad (g,h)\longmapsto gh,
\]
and \(\iota:G\to G,\ g\mapsto g^{-1}\), are [[differential-geometry/holomorphic-map|holomorphic maps]]. A morphism of complex Lie groups is a holomorphic [[algebra-groups/group-homomorphism|group homomorphism]].

## Tangent Lie algebra

The complex [[differential-geometry/tangent-space|tangent space]] \(T_eG\) carries a complex-bilinear Lie bracket obtained from left-invariant holomorphic vector fields. Thus the [[lie-groups/lie-algebra|Lie algebra]] \(\operatorname{Lie}_{\mathbb C}(G)\) is a complex Lie algebra of complex dimension \(\dim_{\mathbb C}G\). Forgetting the complex structure gives the [[lie-groups/underlying-real-lie-group|underlying real Lie group]] and doubles the manifold dimension; it does not produce a second complex Lie group.

## Examples

The groups \(GL_n(\mathbb C)\), \(SL_n(\mathbb C)\), and every [[differential-geometry/complex-torus|complex torus]] are complex Lie groups. A real Lie group need not admit a compatible complex structure, and a complex manifold with a merely smooth group operation is not, on that account, a complex Lie group.

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005, §1.3. [Publisher record](https://doi.org/10.1007/b137952).
2. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002, Chapter I. [Publisher record](https://doi.org/10.1007/978-1-4757-2453-0).
