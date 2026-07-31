+++
id = "operator-algebras/completely-positive-map"
title = "Completely positive map"
kind = "definition"
summary = "A linear map between C*-algebras whose every matrix amplification is positive."
aliases = ["CP map", "completely positive linear map"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) and \(B\) be [[operator-algebras/cstar-algebra|\(C^*\)-algebras]]. A
bounded [[linear-algebra/linear-map|linear map]] \(\Phi:A\to B\) is **completely positive** if it is
[[operator-algebras/n-positive-map|\(n\)-positive]] for every integer
\(n\geq1\). Explicitly, for each \(n\), the entrywise amplification
\[
\Phi^{(n)}:M_n(A)\longrightarrow M_n(B),\qquad
[a_{ij}]\longmapsto[\Phi(a_{ij})],
\]
must carry positive elements to positive elements. Complete positivity
therefore controls positivity simultaneously at every matrix level, not only
on \(A\) itself. The definition does not require \(\Phi\) to preserve the
identity, be multiplicative, or be normal when the algebras are von Neumann
algebras.

## Stinespring characterization

When \(B=B(H)\), Stinespring's theorem characterizes complete positivity by a
factorization
\[
\Phi(a)=V^*\pi(a)V,
\]
where \(\pi\) is a
[[operator-algebras/cstar-representation|\(*\)-representation]] of \(A\) on a
[[linear-algebra/hilbert-space|Hilbert space]] \(K\) and \(V:H\to K\) is
bounded. With the usual minimality condition the factorization is unique up to
unitary equivalence
[Paulsen, Chapter 4].

## Closure properties and examples

Every [[operator-algebras/star-homomorphism|\(*\)-homomorphism]] is completely
positive. Compositions and nonnegative [[convex-analysis/linear-combination|linear combinations]] of completely
positive maps are completely positive, as are maps
\(a\mapsto V^*\pi(a)V\). A
[[operator-algebras/positive-linear-functional|positive linear functional]]
\(A\to\mathbb C\) is automatically completely positive. These facts make CP
maps stable under the constructions used for representations and quantum
operations.

## Positivity is not enough

**Warning.** A [[operator-algebras/positive-linear-map|positive map]] need not
be completely positive. Matrix transposition on \(M_n(\mathbb C)\) is positive
but, for \(n\geq2\), is not \(2\)-positive. Conversely, complete positivity
does not include unitality: the extra condition \(\Phi(1_A)=1_B\) defines a
[[operator-algebras/unital-completely-positive-map|unital completely positive
map]] when both algebras are unital.

## References

1. Vern Paulsen, *Completely Bounded Maps and Operator Algebras*, Cambridge University Press, 2002. [DOI record](https://doi.org/10.1017/CBO9780511546631). Relevant: Chapters 2–4 on matrix positivity, completely positive maps, and Stinespring dilation.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter IV on completely positive maps.
