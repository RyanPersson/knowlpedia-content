+++
id = "operator-algebras/graded-operator"
title = "Even and odd operators on a graded Hilbert space"
kind = "definition"
summary = "A homogeneous bounded operator on a graded Hilbert space is even when it preserves parity and odd when it reverses parity."
aliases = ["homogeneous operator", "graded operator", "operator parity"]
domains = ["operator-algebras", "functional-analysis"]
prerequisites = ["functional-analysis/z2-graded-hilbert-space", "functional-analysis/bounded-linear-operator"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(H=H^0\oplus H^1\) be a [[functional-analysis/z2-graded-hilbert-space|graded Hilbert space]], with grading operator \(\Gamma\). A [[functional-analysis/bounded-linear-operator|bounded operator]] \(T\in B(H)\) is **even** (of degree \(0\)) if \(T(H^j)\subseteq H^j\), equivalently \(T\Gamma=\Gamma T\). It is **odd** (of degree \(1\)) if \(T(H^j)\subseteq H^{j+1\!\!\pmod 2}\), equivalently \(T\Gamma=-\Gamma T\). An operator is **homogeneous** if it is even or odd, and its degree is written \(|T|\in\mathbb Z/2\). A general bounded operator need not be homogeneous, but decomposes uniquely as the sum of its even and odd parts.

## Block-matrix form

Relative to \(H^0\oplus H^1\), the grading and the two homogeneous forms are
\[
\Gamma=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix},
\qquad
T_{\mathrm{ev}}=
\begin{pmatrix}
T_{00}&0\\
0&T_{11}
\end{pmatrix},
\qquad
T_{\mathrm{odd}}=
\begin{pmatrix}
0&T_{01}\\
T_{10}&0
\end{pmatrix}.
\]
For arbitrary \(T\in B(H)\), the projections onto these parts are
\[
T_{\mathrm{ev}}=\frac12(T+\Gamma T\Gamma),
\qquad
T_{\mathrm{odd}}=\frac12(T-\Gamma T\Gamma).
\]

## Graded products and commutators

If \(S\) and \(T\) are homogeneous, then \(ST\) has degree \(|S|+|T|\) modulo \(2\). The **graded commutator** is
\[
[S,T]_{\mathrm{gr}}
=ST-(-1)^{|S||T|}TS.
\]
Thus it is the ordinary commutator unless both operators are odd, in which case it is the anticommutator \(ST+TS\). This sign rule is the one used for graded representations, [[noncommutative-geometry/fredholm-module|Fredholm modules]], and Kasparov cycles.

## Unbounded operators

Parity for an unbounded operator requires a domain condition. A [[functional-analysis/densely-defined-operator|densely defined operator]] \(D\) is even or odd only when \(\Gamma\operatorname{Dom}(D)=\operatorname{Dom}(D)\) and
\[
D\Gamma=\Gamma D
\quad\text{or}\quad
D\Gamma=-\Gamma D
\]
on \(\operatorname{Dom}(D)\), respectively. Bounded-operator formulas should not be applied to an unbounded \(D\) without checking this invariant-domain hypothesis.

## Convention

Some authors use **graded operator** for every operator on a graded space and **homogeneous operator** only for a pure degree. Here “even” and “odd” always assert homogeneity; no parity is assigned to a sum having both components.

## References

- [Nigel Higson and John Roe, *Analytic K-Homology*, Chapter 8 (Oxford University Press, 2000)](https://doi.org/10.1093/oso/9780198511762.001.0001)
- [Bruce Blackadar, *K-Theory for Operator Algebras*, Section 17 (2nd ed., Cambridge University Press, 1998)](https://bruceblackadar.com/Mathematics/book6.pdf)
