+++
id = "operator-algebras/cstar-representation"
title = "Representation of a C*-algebra"
kind = "definition"
summary = "A *-homomorphism from a C*-algebra to the bounded operators on a Hilbert space."
aliases = ["*-representation", "C*-representation"]
domains = ["operator-algebras", "algebra-representation-theory"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] and \(H\)
a [[linear-algebra/hilbert-space|Hilbert space]]. A **representation of
\(A\) on \(H\)** is a
[[operator-algebras/star-homomorphism|\(*\)-homomorphism]]
to [[operator-algebras/bounded-operator-cstar-algebra|\(\mathcal B(H)\)]],
written
\[
\pi:A\longrightarrow\mathcal B(H).
\]
It is **faithful** if \(\pi\) is injective, and **nondegenerate** if
\(\overline{\pi(A)H}=H\). No unitality is required in the definition. When
\(A\) is unital, nondegeneracy is equivalent to
\(\pi(1_A)=I_H\); a representation that sends \(1_A\) to a proper projection
is degenerate rather than unital.

## Automatic boundedness

Every \(*\)-homomorphism between \(C^*\)-algebras is contractive, so no
separate continuity hypothesis is necessary. A faithful representation is
isometric:
\[
\|\pi(a)\|=\|a\|\qquad(a\in A).
\]
The [[operator-algebras/gelfand-naimark-theorem|Gelfand–Naimark theorem]] says
that every \(C^*\)-algebra admits a faithful
[[operator-algebras/nondegenerate-star-homomorphism|nondegenerate
representation]] on some Hilbert space. Abstract \(C^*\)-algebras can
therefore always be realized concretely as operator-norm-closed
\(*\)-algebras of bounded operators.

## Degenerate and essential subspaces

For an arbitrary representation, the closed subspace
\[
H_{\mathrm{ess}}=\overline{\pi(A)H}
\]
reduces \(\pi\). The restriction to \(H_{\mathrm{ess}}\) is nondegenerate,
and \(\pi\) is zero on \(H_{\mathrm{ess}}^\perp\). Consequently, degeneracy
adds only a zero summand. For a nonunital algebra, nondegeneracy is also
equivalent to strong convergence \(\pi(e_i)\to I_H\) for any approximate
identity \((e_i)\) of \(A\).

## Cyclic and irreducible representations

A representation is
**[[operator-algebras/cyclic-cstar-representation|cyclic]]** if some
\(\xi\in H\) has
\(\overline{\pi(A)\xi}=H\). It is **irreducible** if its only closed invariant
subspaces are \(0\) and \(H\), equivalently if its
[[operator-algebras/commutant|commutant]] consists only of scalar operators.
Every [[operator-algebras/irreducible-cstar-representation|irreducible
nonzero representation]] is nondegenerate. The
[[operator-algebras/gns-construction|GNS construction]] produces cyclic
representations from
[[operator-algebras/positive-linear-functional|positive linear functionals]]
and states.

## Distinction from a group representation

A \(C^*\)-representation acts linearly on algebra elements and preserves
products, sums, scalar multiplication, and involution. A unitary group
representation instead assigns a [[functional-analysis/unitary-operator|unitary operator]] to each group element.
For a [[topology/locally-compact-group|locally compact group]] the two
settings are connected by the
[[harmonic-analysis/integrated-form-unitary-representation|integrated form]],
but they are not the same definition.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: Chapter 3 on representations and the Gelfand–Naimark theorem.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Chapter 3 on representations.
