+++
id = "harmonic-analysis/haar-measure"
title = "Haar measure"
kind = "definition"
summary = "A nonzero regular Borel measure on a locally compact group that is invariant under translation on one chosen side."
aliases = ["left Haar measure", "right Haar measure", "Haar measure on a locally compact group"]
domains = ["harmonic-analysis", "topology", "measure-theory"]
section_mode = "progressive"
prerequisites = ["topology/locally-compact-group", "measure-theory/measure", "topology/compact-set"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact Hausdorff group]]. A **left Haar measure** on \(G\) is a nonzero [[measure-theory/measure|Borel measure]] \(\mu\) that is finite on [[topology/compact-set|compact sets]], inner regular on open sets, outer regular on Borel sets, and left invariant:
\[
\mu(gE)=\mu(E)
\]
for every \(g\in G\) and Borel set \(E\). A **right Haar measure** instead satisfies \(\mu(Eg)=\mu(E)\). Haar’s theorem states that left and right Haar measures exist on every locally compact Hausdorff group and that any two on the same side differ by multiplication by a positive constant.

## Existence and uniqueness

Existence and uniqueness up to scale are the substantive content of Haar’s theorem, not formal consequences of invariance. The regularity and local finiteness conditions exclude pathological invariant set functions and make integration compatible with the topology. A left Haar measure has full support: every nonempty open set has positive measure.

## Left, right, and the modular function

If \(\mu\) is left Haar, then \(E\mapsto\mu(E^{-1})\) is right Haar. [[lie-groups/right-translation|Right translation]] of \(\mu\) is measured by the continuous homomorphism [[harmonic-analysis/modular-function|\(\Delta:G\to\mathbb R_{>0}\)]]. With the convention used here,
\[
\mu(Eg)=\Delta(g)\mu(E),
\qquad
\int_G f(xg)\,d\mu(x)=\Delta(g)^{-1}\int_G f(x)\,d\mu(x).
\]
The group is unimodular exactly when \(\Delta=1\), in which case a left Haar measure is also right invariant. Abelian, discrete, and compact groups are unimodular.

## Normalizations and analytic use

On a discrete group, counting measure is Haar measure. On \((\mathbb R^n,+)\), [[measure-theory/lebesgue-measure|Lebesgue measure]] is Haar measure. A compact group has a unique Haar [[probability/probability-measure|probability measure]] after imposing \(\mu(G)=1\). Haar integration defines convolution by
\[
(f*h)(x)=\int_G f(y)h(y^{-1}x)\,d\mu(y),
\]
and underlies [[algebra-representation-theory/regular-representation|regular representations]], harmonic analysis, and group operator algebras.

**Warning.** “The Haar measure” is canonical only after a normalization has been chosen. On a nonunimodular group, left and right Haar measures are not the same measure up to a single shared invariance convention.

## References

1. G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §§2.2–2.3, Haar measure and the modular function.
