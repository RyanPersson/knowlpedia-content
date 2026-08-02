+++
id = "operator-algebras/primitive-ideal-space"
title = "Primitive ideal space"
kind = "definition"
summary = "The primitive ideal space is the set of primitive ideals equipped with the hull-kernel topology."
aliases = ["Prim(A)", "C*-spectrum"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

For a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\), its
**primitive ideal space** is the set of
[[operator-algebras/primitive-ideal|primitive ideals]]
\[
\operatorname{Prim}(A)=\{P\subsetneq A:P\text{ is primitive}\}
\]
equipped with the **[[operator-algebras/hull-kernel-topology|hull–kernel topology]]**. For \(S\subseteq A\), define
\[
\operatorname{hull}(S)=\{P\in\operatorname{Prim}(A):S\subseteq P\}.
\]
The closed subsets are exactly the sets \(\operatorname{hull}(I)\), where
\(I\) ranges over closed [[algebra-rings/two-sided-ideal|two-sided ideals]] of \(A\). Equivalently, for
\(Y\subseteq\operatorname{Prim}(A)\),
\[
\overline Y=\operatorname{hull}\left(\bigcap_{P\in Y}P\right).
\]
This topology is canonically determined by the ideal structure of \(A\).

## Ideals and open subsets

The hull–kernel topology turns the ideal structure of \(A\) into topology.
For a closed two-sided ideal \(I\),
\(\operatorname{hull}(I)\) is naturally homeomorphic to
\(\operatorname{Prim}(A/I)\), while
\[
\operatorname{Prim}(A)\setminus\operatorname{hull}(I)
\]
is naturally homeomorphic to \(\operatorname{Prim}(I)\). In fact, closed
two-sided ideals of \(A\) correspond order-preservingly to open subsets of
\(\operatorname{Prim}(A)\) through this construction.

## Relation to irreducible representations

Let \(\widehat A\) denote the unitary-equivalence classes of nonzero
[[operator-algebras/irreducible-cstar-representation|irreducible
representations]] of \(A\). The kernel map
\[
\widehat A\longrightarrow\operatorname{Prim}(A),\qquad
[\pi]\longmapsto\ker\pi,
\]
is always surjective, but it need not be injective. For
[[operator-algebras/type-i-cstar-algebra|type I \(C^*\)-algebras]], an
[[algebra-representation-theory/irreducible-representation|irreducible representation]] is determined up to unitary equivalence by its
kernel, so the distinction disappears at the level of sets.

## Commutative case and separation

If \(A=C_0(X)\) for a [[topology/locally-compact-space|locally compact]]
[[topology/hausdorff-space|Hausdorff space]] \(X\), evaluation at each
\(x\in X\) has kernel
\[
P_x=\{f:f(x)=0\},
\]
and \(x\mapsto P_x\) is a homeomorphism
\(X\cong\operatorname{Prim}(A)\). This explains why primitive ideals serve as
noncommutative points.

In general, \(\operatorname{Prim}(A)\) is a \(T_0\) space but need not be
Hausdorff or even \(T_1\). These failures are meaningful: specialization
relations record inclusions among primitive ideals. The phrase
**\(C^*\)-spectrum** is sometimes used for \(\operatorname{Prim}(A)\), but it
must not be confused with the spectrum \(\sigma_A(a)\) of a single element.

## References

1. Jacques Dixmier, *C*-Algebras, North-Holland Mathematical Library 15, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: §3.1 on primitive ideals and the hull–kernel topology.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Chapter 4 on primitive spectra and Chapter 6 on type I representation theory.
