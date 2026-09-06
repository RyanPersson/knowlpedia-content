+++
id = "langlands/strong-multiplicity-one-theorem"
title = "Strong multiplicity one theorem"
kind = "theorem"
summary = "Cuspidal automorphic representations of GL_n are determined by their local components outside any finite set of places."
aliases = ["strong multiplicity one", "multiplicity one for GL_n", "strong multiplicity one for automorphic representations"]
domains = ["langlands", "number-theory"]
section_mode = "progressive"
prerequisites = ["langlands-letter/knowls/global-local-fields-completions", "langlands/cuspidal-automorphic-representation", "langlands-letter/knowls/adeles-restricted-product", "langlands/satake-parameter"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(F\) be a
[[langlands-letter/knowls/global-local-fields-completions|global field]], and
let \(\pi\) and \(\pi'\) be
[[langlands/cuspidal-automorphic-representation|cuspidal automorphic
representations]] of
\(\operatorname{GL}_n(\mathbb A_F)\), where \(\mathbb A_F\) is the
[[langlands-letter/knowls/adeles-restricted-product|adele ring]]. If

\[
\pi_v\simeq\pi'_v
\]

for all but finitely many places \(v\) of \(F\), then
\(\pi\simeq\pi'\).  This is the **strong multiplicity one theorem**.

Thus a cuspidal representation of \(\operatorname{GL}_n\) is determined by
its almost-everywhere unramified
[[langlands/satake-parameter|Satake parameters]].

## Strength and scope

Ordinary multiplicity one says that a fixed cuspidal representation occurs
with multiplicity one in the
[[langlands/cuspidal-automorphic-representation|cuspidal spectrum]]. Strong
multiplicity one is a
separate uniqueness statement comparing two representations from their local
components.

The theorem extends to [[langlands/isobaric-automorphic-representation|isobaric
automorphic representations]] after comparing their cuspidal constituents.
For general
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
groups]], nearly equivalent
[[langlands/automorphic-representation|automorphic representations]]
can be distinct, so the statement is not valid without modification.

## Use in reciprocity

If an automorphic construction matches
[[langlands-letter/knowls/frobenius-unramified|Frobenius]] or Satake data
outside a
finite set of places, strong multiplicity one identifies the resulting
general-linear-group representation globally.  On the Galois side,
[[algebra-fields-galois/chebotarev-density-theorem|Chebotarev density]] plays
the analogous uniqueness role.

## References

1. Hervé Jacquet and Joseph A. Shalika, “On Euler products and the
   classification of automorphic representations I,” *American Journal of
   Mathematics* 103 (1981), 499–558.
   [JSTOR](https://doi.org/10.2307/2374103).
2. I. I. Piatetski-Shapiro, “Multiplicity one theorems,” in *Automorphic
   Forms, Representations and L-Functions*, Proceedings of Symposia in Pure
   Mathematics 33, part 1, 1979, 209–212.
