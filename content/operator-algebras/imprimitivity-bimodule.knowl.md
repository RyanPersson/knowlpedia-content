+++
id = "operator-algebras/imprimitivity-bimodule"
title = "Imprimitivity bimodule"
kind = "definition"
summary = "A full Hilbert module whose compact operators are identified with a second C-star algebra by the left action."
aliases = ["equivalence bimodule", "C*-equivalence bimodule", "full Hilbert bimodule"]
domains = ["operator-algebras", "algebra-modules"]
section_mode = "progressive"
+++

Let \(A\) and \(B\) be \(C^*\)-algebras. An **\(A\)-\(B\) imprimitivity
bimodule** is a [[operator-algebras/cstar-correspondence|\(C^*\)-correspondence]]
\({}_AE_B\), hence an [[algebra-modules/bimodule|\((A,B)\)-bimodule]], such
that the closed span of \(\langle E,E\rangle_B\) is \(B\) and the left action
is a \(*\)-isomorphism
\[
A\longrightarrow
\mathcal K_B(E).
\]
The first condition is right fullness; the second makes the left action
faithful, nondegenerate, and exactly the [[operator-algebras/compact-operator-hilbert-module|generalized compact operators]].
Existence of such an \(E\) means that \(A\) and \(B\) are strongly Morita
equivalent.

## Two-inner-product formulation

For \(\xi,\eta\in E\), define the left \(A\)-valued inner product by requiring
that \({}_A\langle\xi,\eta\rangle\) act as the rank-one operator
\(\theta_{\xi,\eta}\). Then
\[
{}_A\langle\xi,\eta\rangle\zeta
=\xi\langle\eta,\zeta\rangle_B.
\]
The two inner products are full and induce the same norm. Conversely, a full
left and right Hilbert bimodule satisfying this compatibility identity gives
the compact-operator formulation above
[Raeburn–Williams, Chapter 3](https://doi.org/10.1090/surv/060).

## Standard examples

Every \(C^*\)-algebra \(A\) is an \(A\)-\(A\) imprimitivity bimodule with
\({}_A\langle x,y\rangle=xy^*\) and
\(\langle x,y\rangle_A=x^*y\). More generally, any full right Hilbert
\(B\)-module \(E\) is a
\(\mathcal K_B(E)\)-\(B\) imprimitivity bimodule. [[linear-algebra/hilbert-space|Hilbert spaces]] give the
special case \(\mathcal K(H)\sim_M\mathbb C\).

## Distinction from a correspondence

An arbitrary correspondence may have a nonfaithful left action, may fail to
be full on the right, or may act by adjointable operators outside
\(\mathcal K_B(E)\). Any of these failures prevents it from being an
imprimitivity bimodule. Thus “Hilbert \(C^*\)-bimodule” is potentially
ambiguous unless fullness and the compatibility condition are stated.

## References

1. Marc A. Rieffel, “Induced representations of C*-algebras,” *Advances in Mathematics* 13 (1974), 176–257. [DOI record](https://doi.org/10.1016/0001-8708%2874%2990068-1). Relevant: §§2–6 on rigged modules, imprimitivity, and induced representations.
2. Iain Raeburn and Dana P. Williams, *Morita Equivalence and Continuous-Trace C*-Algebras*, American Mathematical Society, 1998. [AMS DOI record](https://doi.org/10.1090/surv/060). Relevant: Chapter 3 on imprimitivity bimodules.
