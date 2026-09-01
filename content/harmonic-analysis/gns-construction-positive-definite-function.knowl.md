+++
id = "harmonic-analysis/gns-construction-positive-definite-function"
title = "GNS construction for a positive-definite function"
kind = "construction"
summary = "The canonical cyclic unitary representation whose distinguished coefficient is a continuous positive-definite function."
aliases = ["cyclic representation from a positive-definite function", "Gelfand-Naimark-Segal construction for groups", "cyclic representation from a positive-type function", "GNS representation of a positive-definite function"]
domains = ["harmonic-analysis", "lie-groups", "operator-algebras"]
prerequisites = ["topology/topological-group", "harmonic-analysis/positive-definite-function", "linear-algebra/hilbert-space", "lie-groups/strongly-continuous-unitary-representation", "lie-groups/cyclic-vector-and-cyclic-representation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a [[topology/topological-group|topological group]] and let
\(\varphi:G\to\mathbb C\) be a continuous
[[harmonic-analysis/positive-definite-function|positive-definite function]].
The **GNS construction for \(\varphi\)** produces a
[[linear-algebra/hilbert-space|Hilbert space]] \(\mathcal H_\varphi\), a
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] \(\pi_\varphi\), and a
[[lie-groups/cyclic-vector-and-cyclic-representation|cyclic vector]]
\(\xi_\varphi\) such that
\[
\varphi(g)=\langle\pi_\varphi(g)\xi_\varphi,\xi_\varphi\rangle.
\]
This pointed cyclic representation is unique up to a unique unitary
intertwiner carrying \(\xi_\varphi\) to the other distinguished vector.
Moreover, \(\lVert\xi_\varphi\rVert^2=\varphi(e)\), so the vector is a unit
vector exactly when \(\varphi\) is normalized.

## Construction

Let \(V_0\) be the [[linear-algebra/vector-space|vector space]] spanned by formal symbols
\(\{\delta_x:x\in G\}\). With the [[linear-algebra/inner-product|inner product]] linear in the first variable,
set
\[
\left\langle\sum_i c_i\delta_{x_i},\sum_jd_j\delta_{y_j}\right\rangle_\varphi
=\sum_{i,j}c_i\overline{d_j}\,\varphi(y_j^{-1}x_i).
\]
Positive definiteness makes this form positive semidefinite. Quotient \(V_0\)
by its null space and complete. [[lie-groups/left-translation|Left translation]]
\(\pi_\varphi(g)\delta_x=\delta_{gx}\) preserves the form, and
\(\xi_\varphi=[\delta_e]\). Continuity of \(\varphi\), followed by density of
the symbol span, gives strong continuity.

## Cyclicity and uniqueness

The orbit of \(\xi_\varphi\) contains every symbol class, so its linear span is
dense. If \((\pi,\mathcal H,\xi)\) is another cyclic realization of
\(\varphi\), the rule
\[
\sum_i c_i\pi_\varphi(x_i)\xi_\varphi\longmapsto
\sum_i c_i\pi(x_i)\xi
\]
preserves inner products. It therefore extends to the unique unitary
intertwiner required above. This is the group form of the Gelfand–Naimark–Segal
construction.

## Degenerate and normalized cases

If \(\varphi(e)=0\), positive definiteness forces \(\varphi=0\), and the
construction yields the zero Hilbert space. Otherwise one may normalize by
\(\varphi(e)\). The GNS representation is irreducible precisely when the
normalized function is an extreme point of the [[convex-analysis/convex-set|convex set]] of normalized
continuous positive-definite functions; cyclicity alone does not imply
irreducibility.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Theorem 3.20 and the discussion of cyclic representations.
2. Jacques Dixmier, \(C^*\)-Algebras, North-Holland Mathematical Library 15, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: Chapter 2 on positive forms and representations.
