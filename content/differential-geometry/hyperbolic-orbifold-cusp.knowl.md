+++
id = "differential-geometry/hyperbolic-orbifold-cusp"
title = "Cusp of a finite-volume hyperbolic three-orbifold"
kind = "definition"
summary = "An end represented by a horoball modulo its boundary-point stabilizer."
aliases = ["hyperbolic cusp", "orbifold cusp", "cusp end"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/hyperbolic-three-orbifold", "differential-geometry/horoball", "lie-groups/parabolic-hyperbolic-isometry", "algebra-groups/stabilizer"]
+++

Let \(M=\Gamma\backslash\mathbb H^3\) be a complete orientable finite-volume [[differential-geometry/hyperbolic-three-orbifold|hyperbolic three-orbifold]]. A **cusp** is an end represented by an embedded quotient \(P\backslash B\), where:

- \(\xi\) is an ideal fixed point of a [[lie-groups/parabolic-hyperbolic-isometry|parabolic element]] of \(\Gamma\), and \(P=\operatorname{Stab}_\Gamma(\xi)\);
- \(B\) is an open [[differential-geometry/horoball|horoball]] centered at \(\xi\), preserved by \(P\), with \(\gamma B\cap B=\varnothing\) for \(\gamma\notin P\);
- the horosphere quotient \(P\backslash\partial B\) is compact.

Shrinking \(B\) toward \(\xi\) gives the same end. Boundary points in the same \(\Gamma\)-orbit specify the same cusp.

## Shape and finite volume

After moving \(\xi\) to infinity, a cusp has a compact Euclidean two-orbifold cross-section. With \(t=\log(r/r_0)\), its metric is \(dt^2+e^{-2t}g_0\). The volume beyond height \(t_0\) is proportional to \(\int_{t_0}^{\infty}e^{-2t}\,dt\), which is finite despite the unbounded length of the end.

## Torsion matters

A torsion-free orientable three-dimensional cusp has a torus cross-section. An orbifold cusp may instead have finite isotropy; do not assume every Bianchi cusp cross-section is a torus.

## References

1. F. Paulin, *Regards croisés sur les séries de Poincaré et leurs applications*, Theorem 6, p. 12. [Author’s text](https://www.imo.universite-paris-saclay.fr/~frederic.paulin/preprints/Neuchatel.pdf) See the cusp coordinates and stabilizer discussion preceding Theorem 6.
