+++
id = "noncommutative-geometry/odd-index-pairing"
title = "Odd K-theory/K-homology index pairing"
kind = "definition"
summary = "The Fredholm index of a unitary compressed by the positive projection of an odd Fredholm module."
aliases = ["odd index pairing", "K1 index pairing", "compressed-unitary pairing"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a unital complex \(C^*\)-algebra, let \((H,\pi,F)\) be a normalized [[noncommutative-geometry/odd-fredholm-module|odd Fredholm module]], and set \(P=(I+F)/2\). For a [[operator-algebras/unitary-element|unitary]] \(u\in M_n(A)\) representing a [[operator-algebras/k1-cstar-algebra|\(K_1(A)\)-class]], the compression
\[
P_n\pi_n(u)P_n:P_nH^n\longrightarrow P_nH^n
\]
is [[functional-analysis/fredholm-operator|Fredholm]]. The **odd index pairing**, with the Fredholm-index sign convention used here, is
\[
\langle[u],[H,\pi,F]\rangle
=\operatorname{ind}(P_n\pi_n(u)P_n).
\]
It depends only on the classes in \(K_1(A)\) and \(K^1(A)\), and extends bilinearly to a pairing \(K_1(A)\times K^1(A)\to\mathbb Z\).

## Why the compression is Fredholm

The compact commutator \([P,\pi(a)]\) implies that
\[
P_n\pi_n(u^{-1})P_n
\]
is a two-sided inverse to \(P_n\pi_n(u)P_n\) modulo [[linear-algebra/compact-operator|compact operators]]. Atkinson's characterization therefore makes the compression Fredholm. Homotopy of \(u\), stabilization, compact perturbation of \(F\), and stable homotopy of the cycle preserve its index. Hence the formula descends to [[operator-algebras/k1-cstar-algebra|\(K_1(A)\)]] and odd [[noncommutative-geometry/analytic-k-homology|analytic K-homology]].

The same construction works with an invertible representative. For a \(C^*\)-algebra, polar decomposition lets one use unitary representatives without changing the \(K_1\)-class.

## Circle and Toeplitz example

Take \(A=C(S^1)\), \(H=L^2(S^1)\), and let \(P\) be the Hardy projection. With \(F=2P-I\), multiplication by the coordinate function \(u(z)=z\) has compact commutator with \(P\). Its compression is the Toeplitz operator \(T_z\), the unilateral shift on the Hardy space, so
\[
\langle[u],[H,\pi,F]\rangle=\operatorname{ind}(T_z)=-1.
\]
This sign uses the convention \(\operatorname{ind}T=\dim\ker T-\dim\ker T^*\). Replacing \(u\) by \(u^{-1}\) gives \(+1\).

## Conventions and scope

For nonunital \(A\), use a unitary in a matrix algebra over the [[operator-algebras/unitization|unitization]] whose scalar image is the identity. The resulting class lies in \(K_1(A)\).

Some authors define the odd pairing with an overall minus sign, often to align a chosen orientation or boundary-map convention. A stated sign convention is therefore part of a numerical computation. The formula in the core agrees with Connes's Proposition 2(b).

## References

1. [Alain Connes, *Noncommutative Geometry*, Chapter IV, Section 1, Proposition 2(b), Academic Press, 1994](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).
2. [Nigel Higson and John Roe, *Analytic K-Homology*, Chapters 8–10, Oxford University Press, 2000](https://doi.org/10.1093/oso/9780198511762.001.0001).
