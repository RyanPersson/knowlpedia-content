+++
id = "operator-algebras/standard-hilbert-cstar-module"
title = "Standard Hilbert C*-module"
kind = "definition"
summary = "The Hilbert C*-module of square-summable sequences with entries in a C-star algebra."
aliases = ["standard module H_A", "ell2(A)"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. The
**standard Hilbert \(A\)-module**, denoted \(H_A\) or \(\ell^2(A)\), is the
space of sequences \(a=(a_n)_{n\geq1}\) in \(A\) for which the partial sums
\(\sum_{n=1}^N a_n^*a_n\) converge in norm. It is a right \(A\)-module by
componentwise multiplication, and
\[
\langle a,b\rangle_A=\sum_{n=1}^{\infty}a_n^*b_n.
\]
The series defining this inner product converges in norm. Equipped with the
induced norm, \(H_A\) is a
[[operator-algebras/hilbert-cstar-module|Hilbert \(C^*\)-module]]. It is also
the completion of the finitely supported sequences in \(A\).

## Coordinates and terminology

If \(A\) is unital, the sequences having \(1_A\) in one coordinate and zero
elsewhere form the canonical coordinate vectors. For nonunital \(A\), those
vectors need not belong to \(H_A\), although finitely supported
\(A\)-valued sequences remain dense. Accordingly, “standard” or “free”
describes the module's universal role and should not be read as asserting the
existence of a Hilbert-space orthonormal basis in every case.

## Finite and countable standard modules

The finite column module \(A^n\) embeds as the first \(n\) coordinates of
\(H_A\). Splitting the coordinates into two infinite subsets gives a unitary
Hilbert-module isomorphism
\[
H_A\oplus H_A\cong H_A.
\]
This absorption of countably many coordinates is the elementary model for
stabilization phenomena.

## Role in stabilization

Every countably generated Hilbert \(A\)-module is isomorphic to an
orthogonally complemented submodule of \(H_A\). Equivalently, adjoining one
copy of \(H_A\) absorbs such a module. This is the content of the
[[operator-algebras/kasparov-stabilization-theorem|Kasparov stabilization
theorem]] and makes \(H_A\) the standard ambient module in \(KK\)-theory.

## References

1. E. Christopher Lance, *Hilbert C*-Modules: A Toolkit for Operator Algebraists*, Cambridge University Press, 1995. [Publisher record](https://doi.org/10.1017/CBO9780511526206). Relevant: Chapter 2 on the standard module and countably generated modules.
