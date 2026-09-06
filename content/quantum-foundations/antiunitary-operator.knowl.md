+++
id = "quantum-foundations/antiunitary-operator"
title = "Antiunitary operator"
kind = "definition"
summary = "A conjugate-linear surjective isometry of a complex Hilbert space."
aliases = ["antiunitary transformation", "anti-unitary operator"]
domains = ["quantum-foundations", "functional-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/hilbert-space", "linear-algebra/inner-product", "functional-analysis/unitary-operator", "linear-algebra/linear-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

An **antiunitary operator** between complex [[linear-algebra/hilbert-space|Hilbert spaces]]
\(\mathcal H\) and \(\mathcal K\) is a conjugate-linear bijection
\(A:\mathcal H\to\mathcal K\) such that
\[
\langle Ax,Ay\rangle_{\mathcal K}
=\overline{\langle x,y\rangle_{\mathcal H}}
\qquad(x,y\in\mathcal H),
\]
when the [[linear-algebra/inner-product|inner product]] is linear in its first argument. Equivalently, \(A\) is
a surjective conjugate-linear isometry. This differs from a
[[functional-analysis/unitary-operator|unitary operator]], which is linear.

## Basic properties

Every antiunitary operator preserves norms and orthogonality. Its inverse and
adjoint are antiunitary, while the product of two antiunitaries is unitary.
After choosing an [[linear-algebra/orthonormal-basis|orthonormal basis]], any antiunitary on one Hilbert space can
be written
\[
A=UK,
\]
where \(U\) is unitary and \(K\) is coordinatewise complex conjugation. The
factorization depends on the chosen conjugation; antiunitarity itself does
not.

Because \(A\) is conjugate-linear,
\[
A(\lambda x)=\overline{\lambda}\,Ax.
\]
It is therefore not a complex-linear element of
\(\mathcal B(\mathcal H,\mathcal K)\), even though it is continuous and
real-linear.

## Quantum symmetries

Wigner's theorem says that a bijection of rays preserving transition
probabilities is induced by either a unitary or an antiunitary operator, unique
up to a phase. The antiunitary possibility is essential for time-reversal and
related discrete symmetries. Such symmetries need not belong to the identity
component of a continuously acting gauge group.

## Convention warning

The displayed conjugation identity is valid whether the Hilbert-space inner
product is taken linear in its first or its second argument; what changes is
which slot is linear when manipulating the formula. The term **antilinear
isometry** does not by itself imply surjectivity; antiunitary does.

## References

1. Eugene P. Wigner, *Group Theory and Its Application to the Quantum
   Mechanics of Atomic Spectra*, Academic Press, 1959, Chapter 20.
2. V. S. Varadarajan, *Geometry of Quantum Theory*, 2nd ed., Springer, 1985,
   Chapter II. [Publisher record](https://doi.org/10.1007/978-0-387-49386-2).
