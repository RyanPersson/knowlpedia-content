+++
id = "algebraic-geometry-foundations/harder-narasimhan-filtration"
title = "Harder–Narasimhan filtration"
kind = "theorem"
summary = "The canonical filtration of a bundle by semistable pieces of strictly decreasing slope."
aliases = ["Harder-Narasimhan filtration", "Harder–Narasimhan polygon", "HN filtration", "Harder–Narasimhan truncation"]
domains = ["algebraic-geometry-foundations", "langlands"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/locally-free-sheaf", "algebraic-geometry-foundations/smooth-projective-curve"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\) be a
[[algebraic-geometry-foundations/locally-free-sheaf|vector bundle]] on a
[[algebraic-geometry-foundations/smooth-projective-curve|smooth projective
geometrically connected curve]]. Its slope is
\(\mu(E)=\deg(E)/\operatorname{rk}(E)\).  The **Harder–Narasimhan filtration**
is the unique filtration by subbundles

\[
0=E_0\subset E_1\subset\cdots\subset E_r=E
\]

such that every quotient \(E_i/E_{i-1}\) is semistable and

\[
\mu(E_1/E_0)>\mu(E_2/E_1)>\cdots>
\mu(E_r/E_{r-1}).
\]

Its slopes and ranks determine the **Harder–Narasimhan polygon**.  The bundle
is semistable precisely when the filtration has one nonzero quotient.

## Principal G-bundles

For an [[algebraic-geometry-foundations/principal-g-bundle-on-scheme|algebraic
principal bundle]] under a
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]
\(G\), the analogue is a
canonical reduction to a
[[algebraic-geometry-foundations/parabolic-subgroup|parabolic subgroup]] whose
degree data define a
[[langlands/dominant-coweight|dominant rational cocharacter]], the HN type.
For
\(G=\operatorname{GL}_n\) this recovers the filtration above.

## Truncation of moduli

Bounding the HN polygon or HN type defines open substacks of the
[[algebraic-geometry-foundations/moduli-stack-of-g-bundles-on-a-curve|moduli
stack of bundles]] that are of finite type. This **Harder–Narasimhan
truncation** is used to control non-quasi-compact stacks of \(G\)-bundles and
[[langlands/shtuka|shtukas]]. It is a
geometric boundedness operation, distinct from
[[langlands/arthur-truncation|Arthur's analytic truncation]], although the two
reflect parallel parabolic asymptotics.

## References

1. G. Harder and M. S. Narasimhan, “On the cohomology groups of moduli spaces
   of vector bundles on curves,” *Mathematische Annalen* 212 (1975), 215–248.
2. Sudarshan Gurjar and Nitin Nitsure, “Harder–Narasimhan stacks for principal
   bundles in higher dimensions and arbitrary characteristics,” 2016.
   [arXiv](https://arxiv.org/abs/1605.08997).
