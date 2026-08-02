+++
id = "lie-groups/compact-symplectic-group"
title = "Compact symplectic group"
kind = "definition"
summary = "The compact Lie group of quaternionic linear transformations preserving the standard quaternionic Hermitian form."
aliases = ["quaternionic unitary group", "USp(2n)"]
domains = ["lie-groups", "linear-algebra"]
section_mode = "progressive"
+++

For \(n\geq 1\), regard \(\mathbb H^n\) as a right [[linear-algebra/vector-space|vector space]] over the
[[linear-algebra/quaternion-division-algebra|quaternion division algebra]]
with Hermitian form
\[
\langle v,w\rangle=\sum_{r=1}^n\overline{v_r}w_r.
\]
The **compact symplectic group** is
\[
\operatorname{Sp}(n)
=\{A\in\operatorname{GL}(n,\mathbb H):A^*A=I\}.
\]
Thus \(\operatorname{Sp}(n)\) consists precisely of the right
\(\mathbb H\)-linear isometries of \(\mathbb H^n\), with group operation
given by composition. As a closed, bounded real matrix group, it is a compact
[[fiber-bundles/lie-group|Lie group]].

## Complex matrix realization

Writing each quaternionic matrix as a complex matrix of twice the size
identifies
\[
\operatorname{Sp}(n)
\cong \operatorname{Sp}(n,\mathbb C)\cap\operatorname{U}(2n).
\]
Here [[lie-groups/unitary-group|\(\operatorname{U}(2n)\)]] preserves the
standard Hermitian form, while the complex symplectic factor preserves the
standard nondegenerate alternating complex [[linear-algebra/bilinear-form|bilinear form]].

## Structure and low-rank example

The group \(\operatorname{Sp}(n)\) is connected and simply connected. Its real
[[lie-groups/lie-algebra|Lie algebra]] consists of quaternionic matrices \(X\) satisfying
\(X^*+X=0\), and has dimension \(n(2n+1)\).
For \(n=1\), it is the group of unit quaternions; hence
\(\operatorname{Sp}(1)\) is isomorphic to
[[lie-groups/special-unitary-group|\(\operatorname{SU}(2)\)]], with
underlying manifold \(S^3\).

## Conventions and scope

**Warning.** The notation \(\operatorname{Sp}(n)\) here denotes the compact
quaternionic unitary group, also written \(\operatorname{USp}(2n)\). It is
not the noncompact [[lie-groups/symplectic-group|real symplectic group]]
\(\operatorname{Sp}(2n,\mathbb R)\). The two groups preserve different
ambient structures and have different real dimensions.

## References

1. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Progress in Mathematics 140, Birkhäuser, 2002. [Author-hosted text](https://www.math.stonybrook.edu/~aknapp/download/Beyond2.pdf). Relevant: §I.17, especially (1.135), Proposition 1.136, and Proposition 1.139.
