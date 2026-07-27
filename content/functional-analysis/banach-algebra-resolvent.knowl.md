+++
id = "functional-analysis/banach-algebra-resolvent"
title = "Resolvent of an element in a Banach algebra"
kind = "definition"
summary = "The inverse of the scalar shift of a Banach-algebra element, defined on its resolvent set."
aliases = ["resolvent set", "resolvent function"]
domains = ["functional-analysis", "operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a complex unital [[functional-analysis/banach-algebra|Banach algebra]] with identity \(1\), and let \(a\in A\). The **resolvent set** of \(a\) is
\[
\rho_A(a)=\{\lambda\in\mathbb C:\lambda1-a\text{ is invertible in }A\}
=\mathbb C\setminus \sigma_A(a).
\]
For \(\lambda\in\rho_A(a)\), the **resolvent of \(a\) at \(\lambda\)** is the [[functional-analysis/banach-algebra-invertible-element|inverse]]
\[
R(\lambda,a)=(\lambda1-a)^{-1}.
\]
Thus “resolvent” may denote either the \(A\)-valued function \(R(\,\cdot\,,a)\) or one of its values. For a nonunital Banach algebra, both [[functional-analysis/banach-algebra-spectrum|spectrum]] and resolvent are defined using its [[operator-algebras/unitization|unitization]].

## Analytic structure

The set \(\rho_A(a)\) is open, and \(R(\lambda,a)\) is holomorphic there. For \(\lambda,\mu\in\rho_A(a)\), the [[functional-analysis/resolvent-identity|resolvent identity]] is
\[
R(\lambda,a)-R(\mu,a)
=(\mu-\lambda)R(\lambda,a)R(\mu,a).
\]
In particular, \(R'(\lambda,a)=-R(\lambda,a)^2\). If \(|\lambda|>\lVert a\rVert\), the Neumann series
\[
R(\lambda,a)=\sum_{n=0}^{\infty}\lambda^{-n-1}a^n
\]
converges in norm. These facts are established in [Murphy, §1.2](https://doi.org/10.1016/C2009-0-22289-6).

## Estimates and example

The resolvent detects approach to the spectrum through
\[
\lVert R(\lambda,a)\rVert\geq
\frac{1}{\operatorname{dist}(\lambda,\sigma_A(a))}.
\]
For a complex matrix \(A\), \(\rho(A)\) is the complement of its eigenvalues and \(R(\lambda,A)=(\lambda I-A)^{-1}\). Near a nonnormal matrix’s spectrum, the norm of this inverse can be much larger than the reciprocal-distance lower bound; the resolvent therefore records more than the spectral set alone.

## Conventions and scope

Some operator-theory texts define the resolvent as \((a-\lambda1)^{-1}\), which differs by a minus sign from the convention used here. The identity and derivative formulas change signs accordingly. The ambient algebra matters: an element can become invertible in a larger algebra, changing both its spectrum and resolvent.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: Chapter 1, §1.2 on spectra and resolvents.
2. F. F. Bonsall and J. Duncan, *Complete Normed Algebras*, Springer, 1973. [DOI record](https://doi.org/10.1007/978-3-642-65669-9). Relevant: Chapters 1–2 on inverses, spectra, and resolvent functions.
