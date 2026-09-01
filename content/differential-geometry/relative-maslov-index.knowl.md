+++
id = "differential-geometry/relative-maslov-index"
title = "Relative Maslov index"
kind = "definition"
summary = "The Maslov index of a pair of moving Lagrangian subspaces, including a crossing-form definition for nontransverse endpoints."
aliases = ["Maslov index of a pair", "Robbin–Salamon index"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/lagrangian-subspace", "differential-geometry/symplectic-vector-space", "differential-geometry/maslov-index"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(\Lambda_0,\Lambda_1:[a,b]\to\Lambda(V)\) be continuous paths of [[differential-geometry/lagrangian-subspace|Lagrangian subspaces]] in a finite-dimensional real [[differential-geometry/symplectic-vector-space|symplectic vector space]]. Their **relative Maslov index** is the [[differential-geometry/maslov-index|Maslov index]]
\[
\mu(\Lambda_0,\Lambda_1)
=\mu\bigl(\Delta,\Lambda_0\times\Lambda_1\bigr)
\]
in \((V\oplus V,-\omega\oplus\omega)\), where \(\Delta=\{(v,v):v\in V\}\) is the diagonal Lagrangian. This convention orders the two paths and fixes the sign. For smooth pairs with only regular crossings, where \(\Lambda_0(t)\cap\Lambda_1(t)\neq0\), the index is the sum of signatures of the relative crossing forms, with one-half of the endpoint signatures. Continuous pairs are defined by regular perturbation or homotopy.

## Relative crossing form

At a crossing \(t\), each moving plane determines a quadratic form on the common subspace. The relative crossing form is their difference
\[
\Gamma(\Lambda_0,\Lambda_1,t)
=\Gamma(\Lambda_0,\Lambda_1(t),t)
-\Gamma(\Lambda_1,\Lambda_0(t),t).
\]
When it is nondegenerate, the crossing is regular. The signature formula is
\[
\mu(\Lambda_0,\Lambda_1)
=\tfrac12\operatorname{sign}\Gamma(a)
+\sum_{a<t<b}\operatorname{sign}\Gamma(t)
+\tfrac12\operatorname{sign}\Gamma(b).
\]
This agrees with the diagonal construction.

## Properties

The relative index is natural under a common path of symplectic transformations, additive under concatenation and direct sum, and antisymmetric:
\[
\mu(\Lambda_1,\Lambda_0)=-\mu(\Lambda_0,\Lambda_1).
\]
If \(\Lambda_1(t)\equiv L_0\) is constant, it reduces to the path index relative to \(L_0\). When both endpoint pairs are transverse, it is integer-valued and invariant under homotopies that preserve endpoint transversality.

## Example and near-miss

In \(\mathbb R^2\), keep \(\Lambda_1=\mathbb R\) fixed and rotate \(\Lambda_0\) counterclockwise through one transverse crossing in the interior. The relative index is \(+1\). If a crossing occurs at an endpoint instead, the Robbin–Salamon value may be \(+\tfrac12\), so it is incorrect to assert integer-valuedness without transverse endpoints or another endpoint convention.

## Relation to spectral flow

For suitable paths of self-adjoint first-order operators with Lagrangian boundary data, [[noncommutative-geometry/spectral-flow|spectral flow]] is expressed by a relative Maslov index. Several equivalent definitions make this relation precise. Analytic applications may reverse the order of the two boundary-data paths, which reverses the sign.

## References

1. Joel Robbin and Dietmar Salamon, “The Maslov index for paths,” *Topology* 32 (1993), 827–844. [DOI record](https://doi.org/10.1016/0040-9383%2893%2990052-W). Relevant: §3, especially Theorem 3.2 and Corollary 3.3.
2. Sylvain E. Cappell, Ronnie Lee, and Edward Y. Miller, “On the Maslov index,” *Communications on Pure and Applied Mathematics* 47 (1994), 121–186. [DOI record](https://doi.org/10.1002/cpa.3160470202). Relevant: equivalent definitions and the relation to spectral flow.
