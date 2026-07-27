+++
id = "operator-algebras/stinespring-dilation-theorem"
title = "Stinespring dilation theorem"
kind = "theorem"
summary = "Every completely positive map into bounded operators is a compression of a star-representation."
aliases = ["Stinespring representation theorem", "Stinespring theorem"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a unital \(C^*\)-algebra, \(H\) a [[linear-algebra/hilbert-space|Hilbert space]], and \(\Phi:A\to B(H)\) a [[operator-algebras/completely-positive-map|completely positive map]]. The **Stinespring dilation theorem** provides a Hilbert space \(K\), a unital [[operator-algebras/cstar-representation|\(*\)-representation]] \(\pi:A\to B(K)\), and a bounded operator \(V:H\to K\) such that
\[
\Phi(a)=V^*\pi(a)V\qquad(a\in A).
\]
One may require minimality, \(K=\overline{\pi(A)VH}\); then the triple \((K,\pi,V)\) is unique up to a unique intertwining unitary. Conversely, every map of the displayed form is completely positive.

## Construction

On the algebraic tensor product \(A\odot H\), define
\[
\left\langle\sum_i a_i\otimes\xi_i,\sum_j b_j\otimes\eta_j\right\rangle
=\sum_{i,j}\langle\xi_i,\Phi(a_i^*b_j)\eta_j\rangle.
\]
Complete positivity makes this form nonnegative. Quotienting its null space
and completing gives \(K\); left multiplication gives \(\pi\), and
\(V\xi\) is represented by \(1_A\otimes\xi\). This is Stinespring's original
construction [Stinespring, Theorem 1](https://doi.org/10.1090/S0002-9939-1955-0069403-4).

## Norm and unitality consequences

The construction yields
\[
\lVert\Phi\rVert=\lVert\Phi(1_A)\rVert=\lVert V\rVert^2.
\]
If \(\Phi\) is [[operator-algebras/unital-completely-positive-map|unital completely positive]], then \(V^*V=1_H\), so \(V\) is an isometry and
\(\Phi\) is a compression of \(\pi\). A \(*\)-homomorphism is the special
case in which the compression is unnecessary.

## Conventions and scope

For a nonunital \(A\), an analogous theorem uses a nondegenerate
representation after passing through an [[operator-algebras/approximate-identity|approximate identity]] or a suitable
unitization. For completely positive maps \(A\to B\) with abstract
\(C^*\)-algebra codomain, representing \(B\) faithfully on a Hilbert space
produces the operator-valued form above; Hilbert-module versions require a
separate module formulation.

## References

1. W. Forrest Stinespring, “Positive Functions on \(C^*\)-Algebras,” *Proceedings of the American Mathematical Society* 6 (1955), 211–216. [DOI record](https://doi.org/10.1090/S0002-9939-1955-0069403-4). Relevant: Theorem 1 and the representation construction.
2. Vern Paulsen, *Completely Bounded Maps and Operator Algebras*, Cambridge University Press, 2002. [DOI record](https://doi.org/10.1017/CBO9780511546631). Relevant: Chapter 4 on Stinespring dilation, minimality, uniqueness, and norm consequences.
