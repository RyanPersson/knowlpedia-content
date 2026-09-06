+++
id = "functional-analysis/bounded-commutator"
title = "Bounded commutator"
kind = "definition"
summary = "A commutator on a dense domain that extends uniquely to a bounded operator on the ambient Hilbert space."
aliases = ["bounded extension of a commutator", "bounded [D,a]"]
domains = ["functional-analysis"]
prerequisites = ["linear-algebra/hilbert-space", "functional-analysis/operator-commutator", "functional-analysis/bounded-linear-operator"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(E\) be a dense subspace of a [[linear-algebra/hilbert-space|Hilbert space]] \(H\), and suppose the
[[functional-analysis/operator-commutator|operator commutator]] \([A,B]\) is
defined on \(E\). It is a **bounded commutator** if there is a constant
\(C\geq 0\) such that
\[
\|[A,B]\xi\|\leq C\|\xi\|\qquad(\xi\in E).
\]
The commutator then extends uniquely by continuity to a
[[functional-analysis/bounded-linear-operator|bounded operator]] on \(H\).
This extension, rather than the generally unbounded products \(AB\) and \(BA\),
is also denoted \([A,B]\). Density of \(E\) is essential for uniqueness; an
estimate on a nondense common domain does not determine an operator on all of
\(H\).

## Extension criterion

The defining estimate makes \([A,B]:E\to H\) continuous for the norm inherited
from \(H\). Completing \(E\) therefore produces the unique bounded extension,
whose norm is
\[
\|[A,B]\|=\sup_{\xi\in E,\ \xi\neq0}
\frac{\|[A,B]\xi\|}{\|\xi\|}.
\]
No separate assumption that the initial commutator is closed is needed. Its
graph closure is precisely the graph of the bounded extension restricted to
the closure of \(E\).

## Spectral-triple convention

In a [[noncommutative-geometry/spectral-triple|spectral triple]]
\((\mathcal A,H,D)\), the standard axiom means that every represented element
\(\pi(a)\) preserves \(\operatorname{Dom}(D)\) and that the commutator
\([D,\pi(a)]\), initially on \(\operatorname{Dom}(D)\), satisfies the bounded
estimate above. The same symbol is then used for its unique extension to
\(H\). Requiring only a bounded form commutator, or defining the expression on
a smaller core, gives a variant of the axiom and should not be silently
identified with this convention.

## Examples and scope

For bounded operators \(A\) and \(B\), the commutator is automatically bounded
and satisfies \(\|[A,B]\|\leq2\|A\|\|B\|\). More geometrically, for
\(D=-i\,d/dx\) and multiplication \(M_f\) on the circle, the identity
\([D,M_f]=-iM_{f'}\) shows that the commutator is bounded when \(f'\) is
essentially bounded. The axiom controls one derivative of \(f\); it does not
assert that either product \(DM_f\) or \(M_fD\) is bounded.

## References

1. Alain Connes and Henri Moscovici, “The Local Index Formula in Noncommutative Geometry,” *Geometric and Functional Analysis* 5 (1995), 174–243. [DOI record](https://doi.org/10.1007/BF01895667). Relevant: the spectral-triple hypotheses at the beginning of the article.
2. José M. Gracia-Bondía, Joseph C. Várilly, and Héctor Figueroa, *Elements of Noncommutative Geometry*, Birkhäuser, 2001. [DOI record](https://doi.org/10.1007/978-1-4612-0005-5). Relevant: §10.1 on the domain and bounded-extension convention.
