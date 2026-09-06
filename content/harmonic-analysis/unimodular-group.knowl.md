+++
id = "harmonic-analysis/unimodular-group"
title = "Unimodular locally compact group"
kind = "definition"
summary = "A unimodular locally compact group has trivial modular function, so its left Haar measures are also right invariant."
aliases = ["unimodular group", "unimodularity"]
domains = ["harmonic-analysis", "topology", "algebra-groups"]
section_mode = "progressive"
prerequisites = ["topology/locally-compact-group", "harmonic-analysis/modular-function", "harmonic-analysis/haar-measure", "lie-groups/right-translation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]]. It is
**unimodular** if its [[harmonic-analysis/modular-function|modular function]]
is identically one:
\[
\Delta(g)=1\qquad\text{for every }g\in G.
\]
Equivalently, any left [[harmonic-analysis/haar-measure|Haar measure]] on
\(G\) is also right invariant. The property is independent of the scaling of
the Haar measure. Thus, for a unimodular group, left and [[lie-groups/right-translation|right translation]]
have the same measure-theoretic behavior, and group inversion preserves Haar
measure. Unimodularity is a property of the [[topology/topological-group|topological group]], not an extra
choice of measure.

## Equivalent characterizations

For a fixed left Haar measure \(\mu\), unimodularity is equivalent to each of
the identities
\[
\mu(Eg)=\mu(E),\qquad
\int_G f(x^{-1})\,d\mu(x)=\int_G f(x)\,d\mu(x)
\]
whenever the expressions are defined. These equivalences follow from the
change-of-variables formulas for Haar measure.

## Examples and non-examples

Every abelian, compact, or discrete locally compact group is unimodular.
Connected semisimple [[fiber-bundles/lie-group|Lie groups]] are also unimodular. The affine group of the
real line, consisting of transformations \(x\mapsto ax+b\) with \(a>0\), is a
standard nonunimodular example.

## Consequences for harmonic analysis

On a unimodular group, the
[[harmonic-analysis/convolution-involution|convolution involution]] simplifies
to \(f^*(x)=\overline{f(x^{-1})}\), and the
[[harmonic-analysis/regular-representations-locally-compact-group|right regular representation]]
needs no modular correction. These simplifications do not imply that the
group is abelian or compact.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: chapter 2 on Haar measure and the modular function.
