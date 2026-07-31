+++
id = "operator-algebras/primitive-ideal"
title = "Primitive ideal of a C*-algebra"
kind = "definition"
summary = "A primitive ideal is the kernel of a nonzero irreducible representation of a C*-algebra."
aliases = ["primitive C*-ideal", "kernel of an irreducible representation"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A
**primitive ideal** of \(A\) is a
[[operator-algebras/closed-two-sided-ideal|closed two-sided ideal]]
\(P\subsetneq A\) for which there is a nonzero
[[operator-algebras/irreducible-cstar-representation|irreducible
representation]]
\[
\pi:A\longrightarrow\mathcal B(H)
\]
with \(P=\ker\pi\). Equivalently, \(A/P\) has a faithful irreducible
representation. The representation \(\pi\) need not itself be faithful unless
\(P=\{0\}\), and distinct [[algebra-representation-theory/irreducible-representation|irreducible representations]] may have the same
primitive kernel. The set of all primitive ideals is denoted
\(\operatorname{Prim}(A)\).

## Quotients, pure states, and maximal ideals

If \(\omega\) is a
[[operator-algebras/pure-state-cstar-algebra|pure state]] of \(A\), its
[[operator-algebras/gns-construction|GNS representation]] is irreducible, so
its kernel is primitive. Conversely, every primitive ideal is the kernel of
an irreducible GNS representation associated with a suitable pure state after
the standard treatment of nonunital algebras.

Every maximal proper closed [[algebra-rings/two-sided-ideal|two-sided ideal]] is primitive: its simple quotient
has a faithful irreducible representation. The converse fails in general; a
primitive ideal need not be maximal. Primitive ideals therefore remember
irreducible representation theory more finely than [[algebra-rings/maximal-ideal|maximal ideals]] alone.

## Prime versus primitive

Every primitive ideal of a \(C^*\)-algebra is prime: if closed two-sided
ideals \(I,J\) satisfy \(IJ\subseteq P\), then \(I\subseteq P\) or
\(J\subseteq P\). For separable \(C^*\)-algebras, every [[algebra-rings/prime-ideal|prime ideal]] is
primitive, but without separability the converse can fail.
This is a theorem with a hypothesis, not an alternative unconditional
definition.

## Examples and interpretation

For \(A=C_0(X)\) with \(X\)
[[topology/locally-compact-space|locally compact]]
[[topology/hausdorff-space|Hausdorff]], the primitive ideals are
\[
P_x=\{f\in C_0(X):f(x)=0\},\qquad x\in X.
\]
Thus primitive ideals recover ordinary points in the commutative case. The
zero ideal of \(\mathcal K(H)\), for \(H\neq0\), is primitive because the
defining representation on \(H\) is faithful and irreducible. By contrast,
the zero ideal of a direct sum \(A_1\oplus A_2\), with both summands nonzero,
is not primitive: every irreducible representation annihilates one summand.

This point-like role motivates equipping the primitive ideals with the
[[operator-algebras/hull-kernel-topology|hull–kernel topology]] to form the
[[operator-algebras/primitive-ideal-space|primitive ideal space]].

## References

1. Jacques Dixmier, *C*-Algebras, North-Holland Mathematical Library 15, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: §§2.5 and 3.1 on irreducible representations, primitive ideals, and hull–kernel constructions.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Chapter 4 on prime and primitive ideals and their representation-theoretic structure.
