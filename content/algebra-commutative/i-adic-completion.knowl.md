+++
id = "algebra-commutative/i-adic-completion"
title = "\\(I\\)-adic completion"
kind = "construction"
summary = "The inverse limit A-hat = lim A/I^n that completes a ring along the powers of an ideal."
aliases = ["adic completion", "I-adic completion", "completion along an ideal"]
domains = ["algebra-commutative", "algebra-rings", "algebraic-geometry-foundations"]
prerequisites = ["algebra-rings/commutative-ring"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a [[algebra-rings/commutative-ring|commutative ring]] and
\(I\subseteq A\) an ideal. Its **\(I\)-adic completion** is the inverse limit
\[
\widehat A^{\,I}:=\varprojlim_{n\geq1}A/I^n
\]
with respect to the quotient maps \(A/I^{n+1}\to A/I^n\). The canonical map
\[
A\longrightarrow\widehat A^{\,I},\qquad
a\longmapsto(a\bmod I^n)_n
\]
has kernel \(\bigcap_n I^n\).

## What an element records

An element of \(\widehat A^{\,I}\) is a compatible system
\((a_n)_{n\geq1}\) with \(a_n\in A/I^n\). It records an element to every
finite \(I\)-adic order, whether or not one compatible representative already
lies in \(A\). The completion carries the inverse-limit topology with kernels
\[
\ker(\widehat A^{\,I}\to A/I^n)
\]
as a neighborhood basis of zero; it is complete and separated for this
topology.

## Important general-ring caution

In well-behaved settings, such as a [[algebra-commutative/noetherian-ring|Noetherian ring]] with any ideal \(I\), the
inverse-limit topology agrees with the \(I\widehat A\)-adic topology and the
completion operation is idempotent. For arbitrary non-Noetherian rings and
non-finitely generated ideals, these assertions can fail. Thus
“\(\widehat A\) is complete” should specify the inverse-limit topology unless
hypotheses identifying it with the
[[algebra-commutative/i-adic-topology|\(I\)-adic topology]] are available.

## Examples

- Completing \(R[x]\) along \((x)\) gives
  [[algebra-rings/formal-power-series-ring|\(R[[x]]\)]].
- Completing \(R[X_1,\ldots,X_n]\) along
  \((X_1,\ldots,X_n)\) gives
  [[algebra-rings/multivariable-formal-power-series-ring|\(R[[X_1,\ldots,X_n]]\)]].
- Completing \(\mathbb Z\) along \((p)\) gives \(\mathbb Z_p\).

## Geometric role

Completion along an ideal keeps all infinitesimal neighborhoods of the closed
subscheme cut out by \(I\). Its formal-geometric avatar is the
[[algebraic-geometry-foundations/formal-spectrum|formal spectrum]]
\(\operatorname{Spf}(\widehat A^{\,I})\).

## References

1. The Stacks Project Authors, “Topological rings and modules.” [Section 15.37, Tag 07E7](https://stacks.math.columbia.edu/tag/07E7). Relevant: completion and the distinction between limit and adic topologies.
2. Hideyuki Matsumura, *Commutative Ring Theory*, Cambridge University Press, 1986. Relevant: Section 8, completions and the Noetherian case.
