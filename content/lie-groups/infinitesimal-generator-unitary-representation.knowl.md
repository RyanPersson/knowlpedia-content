+++
id = "lie-groups/infinitesimal-generator-unitary-representation"
title = "Infinitesimal generator of a unitary representation"
kind = "definition"
summary = "The self-adjoint Stone generator associated with a one-parameter subgroup of a unitary Lie-group representation."
aliases = ["Stone generator", "generator dπ(X)"]
domains = ["lie-groups", "functional-analysis"]
section_mode = "progressive"
+++

Let \(\pi\) be a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] of a Lie group
\(G\) on \(\mathcal H\), and let \(X\) lie in the [[lie-groups/lie-algebra|Lie algebra]] of \(G\). The
**infinitesimal generator in the direction \(X\)** is the unique self-adjoint
operator \(A_X\) supplied by
[[lie-groups/stone-theorem-one-parameter-unitary-groups|Stone's theorem]] such
that
\[
\pi(\exp(tX))=e^{itA_X}\qquad(t\in\mathbb R).
\]
Its domain consists exactly of vectors \(v\) for which the strong limit
\[
\lim_{t\to0}\frac{\pi(\exp(tX))v-v}{t}
\]
exists; on that domain the limit equals \(iA_Xv\). The generator is generally
unbounded and therefore includes its domain as part of its data.

## Relation with the derived representation

Every [[lie-groups/smooth-vector-unitary-representation|smooth vector]] lies
in \(\operatorname{Dom}(A_X)\). The
[[lie-groups/derived-representation-on-smooth-vectors|derived representation
operator]] satisfies, on \(\mathcal H^\infty\),
\[
d\pi(X)=iA_X,
\qquad A_X=-i\,d\pi(X).
\]
The first equality denotes equality of the two actions on the smooth-vector
domain, not equality of maximal operators. The derived operator is
essentially skew-adjoint there, and its closure is \(iA_X\)
[Warner, §4.4](https://doi.org/10.1007/978-3-642-50275-0).

## Covariance and common domains

Unitary conjugation transports generators according to
\[
A_{\operatorname{Ad}(g)X}=\pi(g)A_X\pi(g)^{-1}.
\]
On the common domain \(\mathcal H^\infty\), the assignment
\(X\mapsto d\pi(X)\) is linear and preserves Lie brackets. Statements such as
\(A_{X+Y}=A_X+A_Y\) require care at the level of unbounded operators: the
algebraic equality holds on smooth vectors, while the domains and closures of
the maximal operators must still be controlled.

## Sign conventions

**Warning.** Some authors call the skew-adjoint operator
\(\overline{d\pi(X)}\) the infinitesimal generator. Others write the subgroup
as \(e^{-itH_X}\), in which case \(H_X=-A_X\) under the convention above.
Stating both the exponential formula and the derivative formula removes this
sign ambiguity.

## References

1. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1972. [DOI record](https://doi.org/10.1016/B978-0-12-585001-8.X5001-6). Relevant: §VIII.4 on one-parameter unitary groups.
2. Garth Warner, *Harmonic Analysis on Semi-Simple Lie Groups I*, Grundlehren der mathematischen Wissenschaften 188, Springer, 1972. [DOI record](https://doi.org/10.1007/978-3-642-50275-0). Relevant: §4.4 on derived representations and their generators.
