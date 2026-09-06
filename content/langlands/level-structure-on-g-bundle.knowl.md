+++
id = "langlands/level-structure-on-g-bundle"
title = "Level structure on a G-bundle"
kind = "definition"
summary = "A reduction of the formal-frame torsor of a G-bundle at a marked point to a chosen subgroup of the positive loop group."
aliases = ["K-level structure on a G-bundle"]
domains = ["langlands", "algebraic-geometry-foundations"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/principal-g-bundle-on-scheme", "algebraic-geometry-foundations/smooth-projective-curve", "formal-groups/formal-affine-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\) be a principal \(G\)-bundle on a smooth curve \(X\), let \(x\in X\),
and choose a subgroup \(K\subseteq G(\mathcal O_x)\) of the positive loop
group. The trivializations of \(E\) on the [[formal-groups/formal-affine-space|formal disc]] at \(x\) form a
\(G(\mathcal O_x)\)-torsor. A **\(K\)-level structure on \(E\) at \(x\)** is
a reduction of this torsor to \(K\), equivalently a section of its quotient
by \(K\).

## Standard choices

- \(K=\{1\}\) gives a full formal trivialization.
- If \(K\) is the inverse image of a
  [[algebraic-geometry-foundations/borel-subgroup|Borel subgroup]] under
  \(G(\mathcal O_x)\to G\), the datum is
  [[langlands/iwahori-level-structure|Iwahori level]].
- Bruhat–Tits parahoric subgroups give
  [[langlands/parahoric-level-structure|parahoric level]].
- Congruence subgroups give successively deeper level structures.

## Automorphic moduli

Replacing \(\operatorname{Bun}_G(X)\) by the stack of bundles with a fixed
\(K\)-level structure changes the automorphic sheaf category. Which
[[langlands/ramification-of-g-local-system|spectral ramification condition]]
corresponds to it depends on \(K\), the equivariance imposed on automorphic
sheaves, and any chosen character of a deeper filtration quotient.

## References

1. Georgios Pappas and Michael Rapoport, “Twisted loop groups and their
   affine flag varieties,” *Advances in Mathematics* 219 (2008), 118–198.
   [arXiv](https://arxiv.org/abs/math/0607130).
