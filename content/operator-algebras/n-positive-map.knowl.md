+++
id = "operator-algebras/n-positive-map"
title = "n-positive map"
kind = "definition"
summary = "A linear map between C*-algebras whose entrywise amplification to n-by-n matrices preserves positivity."
aliases = ["matrix-positive map", "2-positive map"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) and \(B\) be [[operator-algebras/cstar-algebra|\(C^*\)-algebras]]
and let \(n\geq1\) be an integer. A bounded [[linear-algebra/linear-map|linear map]] \(\Phi:A\to B\) is
**\(n\)-positive** if its amplification
\[
\Phi^{(n)}=\operatorname{id}_{M_n}\otimes\Phi:
M_n(A)\longrightarrow M_n(B),\qquad
[a_{ij}]\longmapsto[\Phi(a_{ij})],
\]
is a [[operator-algebras/positive-linear-map|positive linear map]] between the
corresponding [[operator-algebras/matrix-cstar-algebra|matrix
\(C^*\)-algebras]]. No unitality is assumed. The case \(n=1\) is ordinary
positivity; \(2\)-positivity is the first condition that tests interactions
between two matrix entries.
[[operator-algebras/completely-positive-map|Complete positivity]] means
\(n\)-positivity for every positive integer \(n\), not merely for one fixed
matrix size.

## The positivity hierarchy

If \(\Phi\) is \(n\)-positive, then it is \(m\)-positive for every
\(1\leq m\leq n\), by embedding \(M_m(A)\) as a corner of \(M_n(A)\).
The converses fail in general. For maps out of \(M_k(\mathbb C)\),
\(k\)-positivity already implies complete positivity, but this
finite-dimensional cutoff depends on the size of the domain
[Paulsen, Chapter 2](https://doi.org/10.1017/CBO9780511546631).

## Schwarz inequality

If \(\Phi\) is unital and \(2\)-positive, positivity of a suitable
\(2\times2\) operator matrix gives the [[operator-algebras/kadison-schwarz-inequality|Kadison–Schwarz inequality]]
\[
\Phi(a)^*\Phi(a)\leq\Phi(a^*a)\qquad(a\in A).
\]
Unitality is essential to this normalization; for nonunital or merely
contractive maps the statement requires a modified hypothesis. Ordinary
positivity alone yields Kadison's inequality for self-adjoint inputs under
unitality, but not the full displayed inequality for arbitrary \(a\).

## Examples and non-examples

Every [[operator-algebras/star-homomorphism|\(*\)-homomorphism]] is completely
positive because each amplification is again a \(*\)-homomorphism.
[[operator-algebras/positive-linear-functional|Positive linear functionals]]
are completely positive when viewed as maps into \(\mathbb C\). Matrix
transposition on \(M_k(\mathbb C)\) is positive but, for \(k\geq2\), is not
\(2\)-positive; its failure on an entangled
[[quantum-foundations/rank-one-projector|rank-one projection]] shows why
entrywise positivity is stronger than positivity of the original map.

## References

1. Vern Paulsen, *Completely Bounded Maps and Operator Algebras*, Cambridge University Press, 2002. [DOI record](https://doi.org/10.1017/CBO9780511546631). Relevant: Chapter 2 on \(n\)-positive maps, complete positivity, and matrix-order tests.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter IV on positive and completely positive maps.
