+++
id = "lie-groups/compatible-cartan-subalgebras"
title = "Compatible Cartan subalgebras"
kind = "definition"
summary = "Cartan subalgebras chosen along an inclusion so that the smaller one is obtained by intersection with the larger."
aliases = ["compatible Cartans", "compatible choice of Cartan subalgebras"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/cartan-subalgebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

For an inclusion \(\mathfrak k\subseteq\mathfrak g\) of finite-dimensional Lie
algebras, [[lie-groups/cartan-subalgebra|Cartan subalgebras]] \(\mathfrak t\subseteq\mathfrak k\) and
\(\mathfrak h\subseteq\mathfrak g\) are **compatible with the inclusion** if
\[
\mathfrak t=\mathfrak k\cap\mathfrak h.
\]
In the common maximal-rank case, one can take
\(\mathfrak t=\mathfrak h\subseteq\mathfrak k\), so the two algebras use the
same Cartan subalgebra.

## What compatibility supplies

Compatible Cartans let the [[lie-groups/root-space-decomposition|root-space
decomposition]] of the subalgebra be compared directly with that of the
ambient algebra. If \(\mathfrak k\) is a
[[lie-groups/regular-lie-subalgebra|regular subalgebra]] reductive in
\(\mathfrak g\) and normalized by \(\mathfrak h\), then \(\mathfrak k\) is assembled from a subspace of
\(\mathfrak h\) and selected \(\mathfrak g\)-root spaces. Its roots can
therefore be recorded as a [[lie-groups/root-subsystem|root subsystem]] of the
ambient [[lie-groups/root-system|root system]], subject to the relevant span and closure conditions.

For inclusions that are not of maximal rank, roots of \(\mathfrak g\) restrict
from \(\mathfrak h^*\) to \(\mathfrak t^*\). Several ambient roots may have the
same nonzero restriction, and some may restrict to zero. Compatibility alone
does not make the smaller root system a literal subset of the larger one.

## Scope and terminology

“Compatible” describes a choice made for a particular inclusion; it is not an
additional intrinsic structure on either algebra. Authors sometimes use the
term more loosely for nested Cartans \(\mathfrak t\subseteq\mathfrak h\).
Stating the intersection equation removes that ambiguity. Existence and
conjugacy statements depend on hypotheses such as reductivity, regularity, and
the ground field, and should not be inferred from the definition alone.

## References

1. Eugene B. Dynkin, “Semisimple subalgebras of semisimple Lie algebras,”
   *American Mathematical Society Translations*, Series 2, vol. 6, 1957,
   pp. 111–244.
2. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed.,
   Birkhäuser, 2002, Chapters IV–VI. [Publisher
   record](https://doi.org/10.1007/978-1-4757-2453-0).
