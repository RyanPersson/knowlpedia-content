+++
id = "operator-algebras/gns-construction"
title = "GNS construction"
kind = "definition"
summary = "The canonical construction of a cyclic Hilbert-space representation from a positive functional on a C*-algebra."
aliases = ["Gelfand–Naimark–Segal construction", "cyclic representation from a positive functional"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/positive-linear-functional", "linear-algebra/hilbert-space", "operator-algebras/cyclic-cstar-representation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] and let
\(\varphi\) be a
[[operator-algebras/positive-linear-functional|positive linear functional]] on
\(A\). The **GNS construction** associates a
[[linear-algebra/hilbert-space|Hilbert space]] \(H_\varphi\), a
\(*\)-representation \(\pi_\varphi:A\to B(H_\varphi)\), and a vector
\(\xi_\varphi\) such that
\[
\varphi(a)=\langle\pi_\varphi(a)\xi_\varphi,\xi_\varphi\rangle
\quad(a\in A)
\]
and \(\pi_\varphi(A)\xi_\varphi\) is dense in \(H_\varphi\). Thus
\((\pi_\varphi,H_\varphi,\xi_\varphi)\) is a
[[operator-algebras/cyclic-cstar-representation|cyclic representation]]. The
functional is bounded automatically; neither unitality of \(A\) nor
faithfulness of \(\varphi\) is assumed.

## Quotient construction

Set \(N_\varphi=\{a\in A:\varphi(a^*a)=0\}\). The formula
\[
\langle[a],[b]\rangle_\varphi=\varphi(b^*a)
\]
defines an [[linear-algebra/inner-product|inner product]], linear in the first
variable, on \(A/N_\varphi\). Completing gives \(H_\varphi\), and left
multiplication gives \(\pi_\varphi(a)[b]=[ab]\). If \(A\) is unital, then
\(\xi_\varphi=[1]\). In the nonunital case, the bounded extension of
\(\varphi\) to the [[operator-algebras/unitization|unitization]], or
equivalently an
[[operator-algebras/approximate-identity|approximate identity]], produces the
canonical [[operator-algebras/cyclic-vector|cyclic vector]].

## Uniqueness and faithfulness

If \((\pi,H,\xi)\) is another cyclic realization of \(\varphi\), the rule
\(\pi_\varphi(a)\xi_\varphi\mapsto\pi(a)\xi\) extends to a unitary
intertwining the two representations and carrying \(\xi_\varphi\) to
\(\xi\). Hence the pointed cyclic representation is unique up to a unique
unitary of this form. The representation \(\pi_\varphi\) need not be faithful:
its kernel consists of those elements acting trivially on the quotient, a
stronger condition than merely belonging to \(N_\varphi\).

## States and von Neumann algebras

When \(A\) is unital, \(\|\xi_\varphi\|^2=\varphi(1)=\|\varphi\|\); in
particular a state gives a unit cyclic vector. If \(A=M\) is a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] and \(\varphi\)
is normal, then \(\pi_\varphi\) is a
[[operator-algebras/normal-representation|normal representation]]. GNS also
extends to suitable densely defined weights, but the construction then starts
from the left ideal of square-integrable elements rather than all of \(M\);
that extension is not part of the bounded-functional definition above.

## References

1. Gerard J. Murphy, \(C^*\)-Algebras and Operator Theory, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §3.3 on the GNS construction and cyclic representations.
2. Gert K. Pedersen, \(C^*\)-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §3.3 on positive functionals and representations.
