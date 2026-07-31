+++
id = "differential-geometry/d-c-operator"
title = "The d-c operator"
kind = "definition"
summary = "A real differential operator on a complex manifold obtained from the difference of the two Dolbeault operators."
aliases = ["conjugate differential", "d^c operator", "d superscript c"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(X\) be a [[differential-geometry/complex-manifold|complex manifold]], and write \(d=\partial+\bar\partial\) for its [[differential-geometry/dolbeault-operators|Dolbeault decomposition]]. In this knowl the **\(d^c\)-operator** is the real first-order differential operator
\[
d^c=i(\bar\partial-\partial).
\]
It raises total form degree by one and satisfies
\[
dd^c=2i\,\partial\bar\partial,\qquad d^cd=-dd^c,\qquad (d^c)^2=0.
\]
On a real-valued smooth function \(f\), one has \(d^cf=-df\circ J\), where \(J\) is the complex structure on the real [[fiber-bundles/tangent-bundle|tangent bundle]]. The displayed normalization is part of the definition.

## Structure and consequences

Complex conjugation interchanges \(\partial\) and \(\bar\partial\), while also replacing \(i\) by \(-i\); hence \(d^c\) preserves real forms. The identity \(dd^c=2i\partial\bar\partial\) follows from \(\partial^2=\bar\partial^2=0\) and \(\partial\bar\partial=-\bar\partial\partial\). Thus a real function determines a real \((1,1)\)-form \(dd^cf\).

In a holomorphic coordinate \(z=x+iy\),
\[
d^cf=\frac{\partial f}{\partial x}\,dy-\frac{\partial f}{\partial y}\,dx.
\]
This local formula makes the relation \(d^cf=-df\circ J\) explicit.

## Conventions and scope

**Warning.** Normalizations vary. Demailly uses
\[
d^c_{\mathrm{Dem}}=\frac{1}{2\pi i}(\partial-\bar\partial)
=\frac{1}{2\pi}d^c,
\qquad
dd^c_{\mathrm{Dem}}=\frac{i}{\pi}\partial\bar\partial
\]
in [Chapter III, §3]. Other texts insert a factor \(1/2\) or reverse the sign. Formulas involving \(d^c\), \(dd^c\), curvature, or [[differential-geometry/local-kahler-potential|Kähler potentials]] must therefore be interpreted with their stated convention.

## References

1. Jean-Pierre Demailly, *Complex Analytic and Differential Geometry*, 2012. [Author-hosted text](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf). Relevant: Chapter III, §3, “Definition of Monge–Ampère Operators,” for an explicitly normalized \(d^c\)-operator and the resulting \(dd^c\) formula.
2. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [Publisher record](https://doi.org/10.1007/b137952). Relevant: §3.1 for \(\partial\bar\partial\)-formulas in Kähler geometry.
