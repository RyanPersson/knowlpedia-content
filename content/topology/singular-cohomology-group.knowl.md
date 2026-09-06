+++
id = "topology/singular-cohomology-group"
title = "Singular cohomology group"
kind = "definition"
summary = "The cohomology of the cochain complex dual to the singular chain complex of a topological space."
aliases = ["ordinary cohomology", "integral cohomology", "H^k(X,R)"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/topological-space", "algebra-groups/abelian-group", "topology/continuous-map", "algebra-homological/cohomology-module", "algebra-homological/cochain-complex"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a [[topology/topological-space|topological space]] and \(A\) an [[algebra-groups/abelian-group|abelian group]]. The singular \(k\)-chains \(C_k(X;\mathbb Z)\) form the free abelian group on [[topology/continuous-map|continuous maps]] \(\Delta^k\to X\), with the alternating face boundary \(\partial\). The singular cochains with coefficients in \(A\) are
\[
C^k(X;A)
:=
\operatorname{Hom}\!\bigl(C_k(X;\mathbb Z),A\bigr),
\]
with coboundary \(\delta\varphi=\varphi\circ\partial\). The **\(k\)th singular cohomology group** is
\[
H^k(X;A)
:=
\ker(\delta:C^k\to C^{k+1})
/
\operatorname{im}(\delta:C^{k-1}\to C^k).
\]
Thus it is the [[algebra-homological/cohomology-module|cohomology]] of the resulting [[algebra-homological/cochain-complex|cochain complex]].

## Functoriality and invariance

A continuous map \(f:X\to Y\) induces a pullback
\[
f^*:H^k(Y;A)\to H^k(X;A),
\]
so singular cohomology is contravariant in the space. Homotopic maps induce the same pullback. Consequently, [[topology/homotopy-equivalence|homotopy-equivalent spaces]] have isomorphic singular cohomology groups.

For a fixed \(X\), a homomorphism of coefficient groups \(A\to B\) induces \(H^k(X;A)\to H^k(X;B)\). When \(A=R\) is a [[algebra-rings/commutative-ring|commutative ring]], [[topology/cup-product-and-cohomology-ring|cup products]] make
\[
H^*(X;R)=\bigoplus_{k\ge0}H^k(X;R)
\]
into a graded-commutative ring.

## Examples

- For a one-point space and any coefficient group \(A\), \(H^0(\mathrm{pt};A)\cong A\) and \(H^k(\mathrm{pt};A)=0\) for \(k>0\).
- Every nonempty contractible space has the same cohomology as a point.
- With integer coefficients,
\[
H^k(S^n;\mathbb Z)
\cong
\begin{cases}
\mathbb Z,&k=0,n,\\
0,&\text{otherwise},
\end{cases}
\]
for \(n>0\).

## Coefficients and variants

The notation \(H^k(X)\) often means \(H^k(X;\mathbb Z)\), but coefficients should be stated when ambiguity matters. Integral, rational, real, and finite-field coefficients can reveal different information. Reduced cohomology modifies degree zero so that a point has zero cohomology in every degree. Relative cohomology \(H^k(X,B;A)\) records the topology of a pair \(B\subseteq X\) and participates in a long exact sequence.

For a [[fiber-bundles/smooth-manifold|smooth manifold]], [[differential-geometry/integration-of-differential-forms|integration of differential forms]] gives the de Rham comparison isomorphism
\[
H^k_{\mathrm{dR}}(M)\cong H^k(M;\mathbb R).
\]
This identifies real singular cohomology with [[fiber-bundles/de-rham-cohomology-group|de Rham cohomology]], but not with integral cohomology: torsion classes disappear after passing to real coefficients.

## References

1. Allen Hatcher, *Algebraic Topology*, Cambridge University Press, 2002. [Author-hosted chapter record](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html). Relevant: Chapter 3, singular cohomology and cup products.
2. Edwin H. Spanier, *Algebraic Topology*, Springer, 1966. [DOI record](https://doi.org/10.1007/978-1-4684-9322-1). Relevant: Chapter 5, cohomology theory.
