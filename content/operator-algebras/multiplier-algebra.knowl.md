+++
id = "operator-algebras/multiplier-algebra"
title = "Multiplier algebra"
kind = "definition"
summary = "The canonical unital C*-algebra in which a C*-algebra sits as an essential ideal."
aliases = ["M(A)", "multiplier C*-algebra"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. Its
**multiplier algebra** \(M(A)\) is the unital \(C^*\)-algebra of
[[operator-algebras/double-centralizer|double centralizers]] of \(A\). An
element is a compatible pair \((L,R)\) of bounded [[linear-algebra/linear-map|linear maps]] \(A\to A\)
satisfying
\[
aL(b)=R(a)b\qquad(a,b\in A).
\]
Every \(a\in A\) defines a multiplier by left and right multiplication,
giving a canonical injective \(*\)-homomorphism
\[
A\longrightarrow M(A),\qquad a\longmapsto(L_a,R_a).
\]
Under this embedding, \(A\) is an
[[operator-algebras/essential-ideal|essential ideal]] of \(M(A)\).

## Universal role

If a \(C^*\)-algebra \(B\) contains \(A\) as an essential closed two-sided
ideal, multiplication of elements of \(B\) on \(A\) gives a canonical
injective \(*\)-homomorphism \(B\to M(A)\) that restricts to the standard
embedding of \(A\). This is the precise sense in which \(M(A)\) is the largest
unital \(C^*\)-algebra containing \(A\) essentially. The qualifier
“essential” matters: without it, one could adjoin unrelated direct summands.

## Fundamental examples

If \(A\) is unital, then every multiplier comes from an element of \(A\), so
\(M(A)=A\). For a [[topology/locally-compact-space|locally compact]]
[[topology/hausdorff-space|Hausdorff space]] \(X\),
\[
M(C_0(X))\cong C_b(X),
\]
the bounded continuous functions, whereas the unitization generally gives
only functions on the one-point compactification. If \(H\) is a Hilbert
space and [[operator-algebras/compact-operator-cstar-algebra|\(\mathcal K(H)\)]]
is its compact-operator \(C^*\)-algebra, then
\[
M(\mathcal K(H))\cong\mathcal B(H),
\]
so [[operator-algebras/bounded-operator-cstar-algebra|bounded operators]] are
precisely its multipliers.

## Nondegenerate morphisms

A [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate
\(*\)-homomorphism]] \(\varphi:A\to M(B)\) extends uniquely to a unital
\(*\)-homomorphism
\[
\overline{\varphi}:M(A)\to M(B)
\]
that is continuous for the
[[operator-algebras/strict-topology|strict topologies]]. This extension
principle is why multiplier-valued morphisms, rather than only maps
\(A\to B\), are natural in crossed products, Hilbert \(C^*\)-modules, and
nonunital noncommutative geometry.

## Strict versus norm approximation

An [[operator-algebras/approximate-identity|approximate identity]]
\((e_i)\) of \(A\) converges to \(1_{M(A)}\) in the strict topology, meaning
\(e_ia\to a\) and \(ae_i\to a\) in norm for every \(a\in A\). It usually
does not converge in the norm of \(M(A)\). Thus \(M(A)\) is not generally the
norm completion of \(A\); it adds multipliers visible through their left and
right actions.

## References

1. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §3.12 on double centralizers and multiplier algebras.
2. E. Christopher Lance, *Hilbert C*-Modules: A Toolkit for Operator Algebraists*, Cambridge University Press, 1995. [DOI record](https://doi.org/10.1017/CBO9780511526206). Relevant: Chapter 2 on multiplier algebras and nondegenerate homomorphisms.
3. Robert C. Busby, “Double Centralizers and Extensions of C*-Algebras,” *Transactions of the American Mathematical Society* 132 (1968), 79–99. [DOI record](https://doi.org/10.1090/S0002-9947-1968-0225175-5).
