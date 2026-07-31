+++
id = "operator-algebras/double-centralizer"
title = "Double centralizer of a C*-algebra"
kind = "definition"
summary = "A compatible pair of left and right multiplier maps on a C*-algebra."
aliases = ["double multiplier", "double centralizer pair"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A
**double centralizer** of \(A\) is a pair \((L,R)\) of bounded
[[linear-algebra/linear-map|linear maps]] \(A\to A\) satisfying
\[
L(ab)=L(a)b,\qquad R(ab)=aR(b),\qquad
aL(b)=R(a)b
\]
for all \(a,b\in A\). Thus \(L\) is a left multiplier, \(R\) is a right
multiplier, and the last identity couples them. For \(x\in A\), multiplication
gives the double centralizer \(L_x(a)=xa\), \(R_x(a)=ax\), but nonunital
algebras generally have double centralizers not arising from elements of
\(A\).

## \(C^*\)-algebra operations

Double centralizers form a unital \(C^*\)-algebra. Products reverse the order
on the right:
\[
(L_1,R_1)(L_2,R_2)
=(L_1\mathbin{\circ}L_2,R_2\mathbin{\circ}R_1).
\]
The adjoint is
\[
(L,R)^*=(L^\sharp,R^\sharp),\qquad
L^\sharp(a)=R(a^*)^*,\quad R^\sharp(a)=L(a^*)^*,
\]
and \(\lVert(L,R)\rVert=\lVert L\rVert=\lVert R\rVert\). The identity pair is
\((\operatorname{id}_A,\operatorname{id}_A)\). These formulas are forced by
viewing a pair as left and right multiplication by one generalized element.

## Intrinsic multiplier algebra

The algebra of all double centralizers is canonically the
[[operator-algebras/multiplier-algebra|multiplier algebra]] \(M(A)\). The map
\[
A\longrightarrow M(A),\qquad x\longmapsto(L_x,R_x),
\]
is an injective \(*\)-homomorphism whose image is an essential ideal. If \(A\)
is unital, every double centralizer is multiplication by the single element
\(L(1)=R(1)\), so \(M(A)=A\). For nonunital \(A\), this construction adjoins
multipliers without choosing a representation on a Hilbert space.

## Concrete model and distinction

For a nondegenerate concrete representation \(A\subseteq B(\mathcal H)\) on a
[[linear-algebra/hilbert-space|Hilbert space]], \(M(A)\) can be realized as the
operators \(T\in B(\mathcal H)\) satisfying \(TA\subseteq A\) and
\(AT\subseteq A\). In particular, \(M(K(\mathcal H))=B(\mathcal H)\). A left
multiplier alone is not a double centralizer until a compatible right
multiplier is supplied; nor is an arbitrary bounded endomorphism of the
[[linear-algebra/banach-space|Banach space]] \(A\) a multiplier. Busby's
construction makes this distinction precise.

## References

1. Robert C. Busby, “Double Centralizers and Extensions of \(C^*\)-Algebras,” *Transactions of the American Mathematical Society* 132 (1968), 79–99. [AMS DOI record](https://doi.org/10.1090/S0002-9947-1968-0225175-5). Relevant: the double-centralizer construction and its \(C^*\)-algebra structure.
2. Gert K. Pedersen, *\(C^*\)-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §3.12 on multiplier algebras and double centralizers.
