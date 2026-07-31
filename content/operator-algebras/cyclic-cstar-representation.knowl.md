+++
id = "operator-algebras/cyclic-cstar-representation"
title = "Cyclic representation of a C*-algebra"
kind = "definition"
summary = "A representation of a C*-algebra is cyclic when the orbit of one vector has dense linear span in its Hilbert space."
aliases = ["cyclic *-representation", "cyclic vector representation"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(\pi:A\to B(H)\) be a [[operator-algebras/cstar-representation|representation of a \(C^*\)-algebra]]. A vector \(\xi\in H\) is **cyclic** for \(\pi\) when
\[
\overline{\operatorname{span}}\{\pi(a)\xi:a\in A\}=H.
\]
The representation is **cyclic** if it has at least one [[operator-algebras/cyclic-vector|cyclic vector]]. For a nonunital algebra the closure in this formula is essential. The existence of a cyclic vector forces \(\pi\) to be nondegenerate: the closed span of \(\pi(A)H\) is then all of \(H\). Cyclicity is a property of the represented action together with its [[linear-algebra/hilbert-space|Hilbert space]], not merely of \(A\).

## Equivalent viewpoint

A vector is cyclic for \(\pi(A)\) if and only if it is separating for the [[operator-algebras/commutant|commutant]] \(\pi(A)'\): an operator \(T\in\pi(A)'\) satisfying \(T\xi=0\) must be zero. This converts density of one orbit into uniqueness detected by the commuting operators.

## Sources of cyclic representations

The [[operator-algebras/gns-construction|GNS construction]] associated with a [[operator-algebras/positive-linear-functional|positive linear functional]] produces a cyclic representation whose distinguished cyclic vector recovers the functional as a vector functional. Conversely, every cyclic representation with a chosen unit cyclic vector yields a state \(a\mapsto\langle\pi(a)\xi,\xi\rangle\). This correspondence is treated in [Murphy, section 3.3].

## Examples and limits

The identity representation of \(C(X)\) on \(L^2(X,\mu)\) is cyclic when the constant function \(1\) belongs to the space and bounded continuous functions are dense there. A direct sum of cyclic representations need not be cyclic: one vector must simultaneously generate every summand with enough independence.

## References

1. Gerald J. Murphy, \(C^*\)-*Algebras and Operator Theory*, Academic Press, 1990. [Publisher record](https://shop.elsevier.com/books/c-algebras-and-operator-theory/murphy/978-0-08-092496-0). Relevant: section 3.3 on cyclic representations and the GNS construction.
