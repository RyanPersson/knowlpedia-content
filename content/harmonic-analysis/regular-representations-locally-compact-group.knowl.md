+++
id = "harmonic-analysis/regular-representations-locally-compact-group"
title = "Left and right regular representations of a locally compact group"
kind = "definition"
summary = "The regular representations act unitarily on square-integrable functions by left and modularly corrected right translation."
aliases = ["left regular representation on L2(G)", "right regular representation on L2(G)", "regular Hilbert representation", "left regular unitary representation of a locally compact group"]
domains = ["harmonic-analysis", "lie-groups", "functional-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]] with
left [[harmonic-analysis/haar-measure|Haar measure]] \(\mu\) and
[[harmonic-analysis/modular-function|modular function]] \(\Delta\), normalized
by \(\int_G h(xg)\,d\mu(x)=\Delta(g)^{-1}\int_G h(x)\,d\mu(x)\). On the
[[measure-theory/lp-space|\(L^2\)-space]] \(L^2(G,\mu)\), the **left and right
regular representations** are
\[
(\lambda(g)\xi)(x)=\xi(g^{-1}x),\qquad
(\rho(g)\xi)(x)=\Delta(g)^{1/2}\xi(xg).
\]
Both maps are
[[lie-groups/strongly-continuous-unitary-representation|strongly
continuous unitary representations]],
and their images commute:
\(\lambda(g)\rho(h)=\rho(h)\lambda(g)\).
The modular factor is precisely what makes [[lie-groups/right-translation|right translation]] unitary for a
left Haar measure; it equals \(1\) when \(G\) is unimodular. With the displayed
conventions, both \(g\mapsto\lambda(g)\) and \(g\mapsto\rho(g)\) are group
homomorphisms.

## Unitarity and continuity

Left invariance of \(\mu\) gives
\(\lVert\lambda(g)\xi\rVert_2=\lVert\xi\rVert_2\). Right translation changes
the squared \(L^2\)-norm by \(\Delta(g)^{-1}\), so the factor
\(\Delta(g)^{1/2}\) makes \(\rho(g)\) unitary. Strong continuity follows
first for compactly supported
continuous functions and then for all of \(L^2(G)\) by density, as in
[Folland, §§2.4 and 3.1].

## Relation to convolution

For suitable \(f\), the [[harmonic-analysis/integrated-operator-continuous-representation|integrated operator]]
\(\lambda(f)=\int_G f(g)\lambda(g)\,d\mu(g)\) acts by left
[[harmonic-analysis/convolution-on-locally-compact-group|convolution]]. Its
adjoint is \(\lambda(f^*)\), where \(f^*\) is the
[[harmonic-analysis/convolution-involution|convolution involution]]. This is
the analytic regular representation used to define
[[operator-algebras/reduced-group-cstar-algebra|reduced group \(C^*\)-algebras]].

## Conventions and scope

**Warning.** One may instead write the right regular representation using
\(xg^{-1}\); then the modular factor and the order convention change. The
displayed choice makes \(g\mapsto\rho(g)\) a representation and makes
\(\lambda(G)\) commute with \(\rho(G)\). It is distinct from the
[[algebra-representation-theory/regular-representation|algebraic regular representation]]
on a finite-dimensional
[[algebra-representation-theory/group-algebra|group algebra]].

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §§2.4 and 3.1 on Haar translation and regular unitary representations.
