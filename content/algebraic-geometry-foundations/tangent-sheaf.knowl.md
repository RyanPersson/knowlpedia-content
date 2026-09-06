+++
id = "algebraic-geometry-foundations/tangent-sheaf"
title = "Tangent sheaf"
kind = "definition"
summary = "The sheaf of derivations, equivalently the dual of the sheaf of Kähler differentials."
aliases = ["algebraic tangent sheaf", "tangent sheaf"]
domains = ["algebraic-geometry-foundations", "differential-geometry"]
prerequisites = ["algebraic-geometry-foundations/relative-kahler-differentials"]
dependency_review_count = 1
section_mode = "progressive"
+++

For a morphism of schemes \(X\to S\), the **relative tangent sheaf** is
\[
\mathcal T_{X/S}
=\mathcal Hom_{\mathcal O_X}(\Omega^1_{X/S},\mathcal O_X),
\]
the \(\mathcal O_X\)-dual of the
[[algebraic-geometry-foundations/relative-kahler-differentials|sheaf of
relative Kähler differentials]]. Equivalently,
\(\mathcal T_{X/S}\) is the sheaf
\(\operatorname{Der}_S(\mathcal O_X,\mathcal O_X)\) of \(S\)-linear
derivations.

When \(S=\operatorname{Spec}k\), it is written \(\mathcal T_X\). If \(X\) is
smooth over \(S\) of relative dimension \(n\), then
\(\Omega^1_{X/S}\) and \(\mathcal T_{X/S}\) are locally free of rank \(n\).

## Lie bracket

The commutator of derivations gives \(\mathcal T_{X/S}\) a [[fiber-bundles/lie-bracket|Lie bracket]]. Along
with its action on \(\mathcal O_X\), this makes it the Lie algebroid whose
[[lie-groups/universal-enveloping-algebra|enveloping algebra]] is the sheaf \(\mathcal D_X\) of differential operators in
characteristic \(0\).

## References

1. Robin Hartshorne, *Algebraic Geometry*, Springer, 1977, Chapter II, §8.
   [DOI](https://doi.org/10.1007/978-1-4757-3849-0).
