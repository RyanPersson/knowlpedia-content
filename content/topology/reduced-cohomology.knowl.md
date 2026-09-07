+++
id = "topology/reduced-cohomology"
title = "Reduced cohomology"
kind = "definition"
summary = "The cohomology theory whose degree-zero constant contribution is removed from ordinary singular cohomology."
aliases = ["reduced singular cohomology", "reduced cohomology group"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/singular-cohomology-group", "topology/topological-space", "algebra-groups/abelian-group", "algebra-groups/quotient-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a nonempty [[topology/topological-space|topological space]], \(A\) an [[algebra-groups/abelian-group|abelian group]], and \(H^k(X;A)\) its [[topology/singular-cohomology-group|singular cohomology]]. For \(k\geq0\), the **reduced cohomology group** is
\[
\widetilde H^k(X;A)=
\begin{cases}
H^0(X;A)/A,&k=0,\\
H^k(X;A),&k>0,
\end{cases}
\]
where the [[algebra-groups/quotient-group|quotient]] is by the subgroup of constant \(0\)-cocycles.

## Augmented cochain description

Equivalently, dualize the augmented singular chain complex with coefficients in \(A\) and take cohomology. The added coboundary sends \(a\in A\) to the constant \(0\)-cochain with value \(a\). This gives the natural reduction map \(H^k(X;A)\to\widetilde H^k(X;A)\), which is the quotient in degree zero and the identity in positive degrees.

For any chosen point \(x_0\in X\), the long exact sequence of the pair identifies these groups with relative cohomology \(H^k(X,\{x_0\};A)\). No path-connectedness assumption is needed. The quotient definition itself requires no choice of basepoint.

## Basic examples

For a one-point space, \(\widetilde H^k(\{x_0\};A)=0\) for all \(k\geq0\). For \(n>0\),
\[
\widetilde H^k(S^n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=n,\\
0,&k\ne n.
\end{cases}
\]

## Degree zero

Ordinary \(H^0(X;A)\) is the group of functions from the set of path components of \(X\) to \(A\). Reduced cohomology quotients this product by the diagonal subgroup of constant functions. In particular, it vanishes for a nonempty path-connected space.

## Reference

Allen Hatcher, *Algebraic Topology*, Cambridge University Press, 2002, §3.1, pp. 199–200, “Reduced Groups” and “Relative Groups.” [Author-hosted chapter](https://pi.math.cornell.edu/~hatcher/AT/ATch3.pdf).
