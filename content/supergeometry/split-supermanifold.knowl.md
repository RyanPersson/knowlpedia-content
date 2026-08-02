+++
id = "supergeometry/split-supermanifold"
title = "Split supermanifold"
kind = "definition"
summary = "A supermanifold globally presented by the exterior algebra of the dual of a vector bundle."
aliases = ["split smooth supermanifold", "Pi E supermanifold"]
domains = ["supergeometry", "fiber-bundles"]
section_mode = "progressive"
+++

Let \(M\) be a smooth manifold and let \(E\to M\) be a real [[fiber-bundles/vector-bundle|vector bundle]] of
rank \(q\). The **split supermanifold** associated to \(E\), often denoted
\(\Pi E\), is
\[
\Pi E=\left(M,\mathcal O_{\Pi E}\right),
\qquad
\mathcal O_{\Pi E}(U)
=\Gamma\!\left(U,\Lambda E^*|_U\right)
\]
for every open set \(U\subseteq M\).
It has dimension \(\dim M|q\), and its nilpotent ideal \(\mathcal J\)
satisfies the sheaf isomorphism
\[
\mathcal J/\mathcal J^2\cong\mathcal E^*,
\]
where \(\mathcal E^*\) is the sheaf of smooth sections of \(E^*\).

The notation \(\Pi E\) indicates that fiber-linear functions have odd parity;
it does not change the underlying topological space, which remains \(M\).

## What a splitting chooses

A splitting of a [[supergeometry/supermanifold|supermanifold]] \(X\) is an
isomorphism
\[
\mathcal O_X\cong
\Lambda_{\mathcal O_{X_{\mathrm{red}}}}\!
  \left(\mathcal J_X/\mathcal J_X^2\right)
\]
compatible with reduction. It identifies all higher nilpotent terms with
exterior powers of the degree-one part. Such an isomorphism contains more
information than the underlying reduced manifold and odd vector bundle.

The [[supergeometry/batchelor-theorem|Batchelor theorem]] supplies such a
splitting in the finite-dimensional smooth real category, but supplies no
canonical or functorial choice.

## References

1. M. Batchelor, “The structure of supermanifolds,” *Transactions of the American Mathematical Society* 253, 1979, 329–338. [Article](https://doi.org/10.1090/S0002-9947-1979-0536950-X).
2. J. Monterde and O. A. Sánchez-Valenzuela, “Existence and uniqueness of solutions to superdifferential equations,” *Journal of Geometry and Physics* 10(4), 1993, 315–343. [Article](https://doi.org/10.1016/0393-0440(93)90021-T). Relevant: split smooth models and parity reversal.
