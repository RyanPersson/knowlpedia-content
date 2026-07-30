+++
id = "formal-groups/tangent-lie-algebra"
title = "Tangent Lie algebra of a formal group"
kind = "construction"
summary = "The tangent space at the identity of a formal group, with bracket induced by invariant formal vector fields."
aliases = ["Lie algebra of a formal group", "formal-group tangent algebra", "Lie functor for formal groups"]
domains = ["formal-groups", "lie-groups"]
section_mode = "progressive"
+++

Let \(\mathcal G\) be a finite-dimensional
[[formal-groups/formal-group|formal group]] over a field \(k\), with identity
\(e\). Its **tangent Lie algebra** is
\[
\operatorname{Lie}(\mathcal G):=T_e\mathcal G
\]
with the bracket obtained by extending tangent vectors uniquely to
left-invariant formal vector fields and taking their commutator.

## Invariant derivations

In affine coordinates, formal vector fields are continuous derivations of the
complete coordinate ring. Multiplication on \(\mathcal G\) defines the
left-translation condition. Evaluation at \(e\) identifies left-invariant
derivations with \(T_e\mathcal G\), and the commutator of derivations preserves
left invariance. Transporting that commutator back to the tangent space gives
the bilinear alternating bracket satisfying the Jacobi identity.

## Formula from a formal group law

Choose coordinates and write the corresponding
[[formal-groups/formal-group-law|formal group law]] as
\[
F(X,Y)=X+Y+B(X,Y)+O(3),
\]
where \(B\) is the homogeneous bilinear part. Then
\[
[u,v]=B(u,v)-B(v,u).
\]
The antisymmetric part of the quadratic multiplication therefore contains the
first nonabelian information. In BCH coordinates,
\(B(u,v)=\tfrac12[u,v]\), recovering the original bracket.

## Functoriality

For a formal group homomorphism
\(\phi:\mathcal G\to\mathcal H\), the differential at the identity
\[
d\phi_e:T_e\mathcal G\longrightarrow T_e\mathcal H
\]
preserves brackets. Hence
\[
\operatorname{Lie}:\mathbf{FGrp}^{\mathrm{fd}}_k
\longrightarrow\mathbf{LieAlg}^{\mathrm{fd}}_k
\]
is a functor.

In characteristic zero this functor is an
[[formal-groups/lie-algebra-formal-group-equivalence|equivalence]] on the
formal-disc category. In positive characteristic it remains useful but is not
a complete invariant.

## References

1. A. Fröhlich, *Formal Groups*, Lecture Notes in Mathematics 74, Springer, 1968. [Publisher record](https://link.springer.com/book/10.1007/BFb0074373). Relevant: Chapter 2, Lie theory.
2. Jean-Pierre Serre, *Lie Algebras and Lie Groups*, second edition, Springer, 1992. [Publisher record](https://link.springer.com/book/10.1007/978-3-540-70634-2). Relevant: Lie functors and invariant vector fields.
