+++
id = "operator-algebras/self-adjoint-element"
title = "Self-adjoint element of a C*-algebra"
kind = "definition"
summary = "An element of a C-star algebra that equals its involution."
aliases = ["hermitian element", "self-adjoint C*-element"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. An element
\(a\in A\) is **self-adjoint** if
\[
a^*=a.
\]
The self-adjoint elements form a closed real vector subspace \(A_{\mathrm{sa}}\)
of \(A\), not generally a complex subalgebra. Every \(x\in A\) has the unique
decomposition
\[
x=\frac{x+x^*}{2}+i\,\frac{x-x^*}{2i},
\]
whose two summands before and after the factor \(i\) are self-adjoint. In a
concrete \(C^*\)-algebra of operators on a [[linear-algebra/hilbert-space|Hilbert space]], this definition is
exactly the usual condition that an operator equal its Hilbert-space adjoint.

## Spectral characterizations

An element of a \(C^*\)-algebra is self-adjoint exactly when its spectrum is
contained in \(\mathbb R\). Equivalently, \(\|\exp(ita)\|=1\) for every real
\(t\), with the exponential computed in the unitization when the algebra is
nonunital. These equivalences use the \(C^*\)-identity and functional
calculus; they fail as stated in a general involutive [[functional-analysis/banach-algebra|Banach algebra]]
[Murphy, §2.2].

## Order and functional calculus

A self-adjoint element is **positive** when its spectrum lies in
\([0,\infty)\); self-adjointness alone does not imply positivity. The order on
\(A_{\mathrm{sa}}\) is defined by \(a\leq b\) when \(b-a\) is positive.
Continuous real-valued functions on the spectrum of \(a\) produce
self-adjoint elements by functional calculus, while nonnegative functions
produce positive elements. In particular, the positive and [[operator-algebras/positive-negative-parts|negative parts]]
recover \(a=a_+-a_-\) with \(a_+a_-=0\).

## Examples and boundary cases

Hermitian matrices are the self-adjoint elements of \(M_n(\mathbb C)\).
Multiplication by an essentially bounded real-valued function is self-adjoint
in the commutative operator algebra on \(L^2\). A unitary element need not be
self-adjoint; it is self-adjoint precisely when its square is the identity.
For unbounded operators, the equation \(T=T^*\) includes equality of domains
and belongs to a different theory than self-adjoint elements of a
\(C^*\)-algebra, whose elements are bounded.

## References

1. Gerard J. Murphy, \(C^*\)-Algebras and Operator Theory, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §2.2 on self-adjoint elements, positivity, and continuous functional calculus.
2. Gert K. Pedersen, \(C^*\)-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §1.2 on self-adjoint and positive elements.
