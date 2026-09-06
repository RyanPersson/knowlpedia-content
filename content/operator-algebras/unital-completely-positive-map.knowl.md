+++
id = "operator-algebras/unital-completely-positive-map"
title = "Unital completely positive map"
kind = "definition"
summary = "A unital completely positive map preserves the identity and is positive at every matrix level."
aliases = ["UCP map"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/unital-cstar-algebra", "operator-algebras/completely-positive-map", "linear-algebra/linear-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\) and \(B\) be
[[operator-algebras/unital-cstar-algebra|unital \(C^*\)-algebras]]. A
**unital completely positive map**, or **UCP map**, is a
[[operator-algebras/completely-positive-map|completely positive]] [[linear-algebra/linear-map|linear map]]
\(\Phi:A\to B\) satisfying
\[
\Phi(1_A)=1_B.
\]
Thus every matrix amplification
\(\Phi^{(n)}:M_n(A)\to M_n(B)\) is positive, and \(\Phi\) preserves the
distinguished unit. Multiplicativity, injectivity, surjectivity, and
normality are not part of the definition. UCP maps are the morphisms commonly
used for operator systems and for Heisenberg-picture quantum operations.

## Contractivity and the Schwarz inequality

Every UCP map has norm one and is contractive. It also satisfies the
[[operator-algebras/kadison-schwarz-inequality|Kadison–Schwarz inequality]]
\[
\Phi(a)^*\Phi(a)\leq\Phi(a^*a)\qquad(a\in A).
\]
Complete positivity is stronger than needed for this inequality—unital
\(2\)-positivity suffices—but it supplies stable matrix-level control.
Compositions and [[convex-analysis/convex-combination|convex combinations]] of UCP maps are again UCP.

The elements \(a\) for which equality holds both for \(a^*a\) and \(aa^*\)
form the multiplicative domain of \(\Phi\). On that \(C^*\)-subalgebra,
\(\Phi\) behaves multiplicatively on both sides.

## Stinespring form

When the codomain is \(\mathcal B(H)\), Stinespring's theorem writes a UCP map
as
\[
\Phi(a)=V^*\pi(a)V,
\]
where \(\pi:A\to\mathcal B(K)\) is a unital
[[operator-algebras/cstar-representation|representation]] and \(V:H\to K\)
is an isometry. Conversely, every such compression is UCP.
Unitality is exactly what changes the general Stinespring operator \(V\) into
an isometry, since \(\Phi(1_A)=V^*V\).

## Examples and distinctions

Every unital [[operator-algebras/star-homomorphism|\(*\)-homomorphism]] is
UCP. A [[operator-algebras/state-cstar-algebra|state]] on a unital
\(C^*\)-algebra is precisely a UCP map \(A\to\mathbb C\). More generally, a
[[operator-algebras/conditional-expectation|conditional expectation]] between
unital \(C^*\)-algebras with a common unit is UCP.

The normalized trace map
\[
M_n(\mathbb C)\longrightarrow\mathbb C,\qquad
a\longmapsto \frac{1}{n}\operatorname{Tr}(a),
\]
is UCP but is not multiplicative for \(n>1\). This shows why UCP maps should
not be confused with \(*\)-homomorphisms.

## Conventions and scope

Unitality presupposes specified units in both domain and codomain. A
completely positive map between nonunital \(C^*\)-algebras may instead be
contractive, nondegenerate, or extend unitally to suitable unitizations, but
it is not literally UCP under the core definition. For
[[operator-algebras/von-neumann-algebra|von Neumann algebras]], the additional
adjective **normal** requires ultraweak continuity and gives the separate
notion of a
[[operator-algebras/normal-unital-completely-positive-map|normal UCP map]].

## References

1. Vern Paulsen, *Completely Bounded Maps and Operator Algebras*, Cambridge University Press, 2002. [DOI record](https://doi.org/10.1017/CBO9780511546631). Relevant: Chapters 2–4 on UCP maps, matrix positivity, the Schwarz inequality, and Stinespring dilation.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter IV on completely positive maps and operator-algebraic expectations.
