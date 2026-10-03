+++
id = "lie-groups/norm-unitary-group"
title = "Unitary group with operator-norm topology"
kind = "construction"
summary = "The Banach–Lie structure on the unitary operators, with bounded skew-adjoint tangent operators."
aliases = ["operator-norm unitary group"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["linear-algebra/hilbert-space", "functional-analysis/unitary-operator", "linear-algebra/operator-norm", "functional-analysis/adjoint-bounded-operator", "lie-groups/banach-lie-group"]
+++

For a complex [[linear-algebra/hilbert-space|Hilbert space]] \(H\), the group
\[
U(H)=\{U\in B(H):U^*U=UU^*=I\}
\]
of [[functional-analysis/unitary-operator|unitary operators]], equipped with the [[linear-algebra/operator-norm|operator norm]], is a real [[lie-groups/banach-lie-group|Banach–Lie group]]. Its Lie algebra is
\[
\mathfrak u(H)=\{B\in B(H):B^*=-B\},
\qquad [B,C]=BC-CB,
\]
the real Banach space of **bounded** skew-adjoint operators.
Here \(B^*\) is the [[functional-analysis/adjoint-bounded-operator|bounded-operator adjoint]].

## Local charts

The operator series \(\exp B=\sum_{n\geq0}B^n/n!\) maps skew-adjoint operators to unitaries. Near \(I\), its inverse is the norm-convergent logarithm
\[
\log U=\sum_{n\geq1}\frac{(-1)^{n+1}}n(U-I)^n
\qquad(\|U-I\|<1).
\]
This logarithm is skew-adjoint. Translating the local chart around the group gives its manifold structure; multiplication and inversion are smooth in these charts.

## Why this is stronger than an orbit-map condition

For a smooth homomorphism \(\pi:G\to U(H)\) into this Banach–Lie group, differentiation produces bounded operators on all of \(H\). A [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] only makes \(g\mapsto\pi(g)v\) continuous for each \(v\). Its derivatives can be unbounded and require the common [[lie-groups/smooth-vector-unitary-representation|smooth-vector domain]]. The [[lie-groups/modulation-unitary-group|modulation group]] exhibits the distinction explicitly.

## References

1. Jesús Espinoza and Bernardo Uribe, [*Topological properties of the unitary group*](https://arxiv.org/abs/1407.1869), §1, p. 2, discussion before Theorem 1.2. The exponential and logarithm give the local construction used above.
