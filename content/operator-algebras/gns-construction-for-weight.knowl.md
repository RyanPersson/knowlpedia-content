+++
id = "operator-algebras/gns-construction-for-weight"
title = "GNS construction for a weight"
kind = "definition"
summary = "The Hilbert-space representation obtained by completing the finite left ideal of a weight."
aliases = ["GNS representation of a weight"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(\varphi\) be a weight on a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] \(M\), and let
\(\mathfrak n_\varphi\) be its
[[operator-algebras/left-ideal-of-weight|finite left ideal]]. On
\(\mathfrak n_\varphi\) set
\[
\langle x,y\rangle_\varphi=\varphi(y^*x),\qquad
\mathcal N_\varphi=\{x:\varphi(x^*x)=0\}.
\]
Here \(\varphi(y^*x)\) denotes the canonical polarized linear extension of
\(\varphi\) to
\(\mathfrak m_\varphi=\operatorname{span}(\mathfrak n_\varphi^*
\mathfrak n_\varphi)\).
The **GNS construction for \(\varphi\)** is the Hilbert-space completion
\(H_\varphi\) of
\(\mathfrak n_\varphi/\mathcal N_\varphi\), with quotient map
\(\Lambda_\varphi\), together with the representation
\[
\pi_\varphi(a)\Lambda_\varphi(x)=\Lambda_\varphi(ax).
\]
The inequality
\(\varphi(x^*a^*ax)\leq\|a\|^2\varphi(x^*x)\) makes
\(\pi_\varphi(a)\) bounded and the formula well defined.

## Regularity of the representation

If \(\varphi\) is
[[operator-algebras/normal-semifinite-faithful-weight|normal, semifinite, and faithful]], then \(\pi_\varphi\) is a faithful
[[operator-algebras/normal-representation|normal representation]].
Semifiniteness ensures that the finite domain is sufficiently large,
faithfulness removes nonzero positive elements from the kernel, and
normality supplies ultraweak continuity.
Without these hypotheses the construction still exists, but the
representation may be degenerate or nonfaithful.

## Relation to the ordinary GNS construction

When \(\varphi\) is a state, \(\mathfrak n_\varphi=M\), and the construction
reduces to the usual [[operator-algebras/gns-construction|GNS construction]].
For the canonical trace on \(\mathcal B(H)\), the resulting [[linear-algebra/hilbert-space|Hilbert space]] is
the Hilbert–Schmidt class and \(\pi_\varphi\) acts by left multiplication.
The weight construction therefore retains the familiar state case while
allowing genuinely unbounded noncommutative integrals.

## Modular role

For a normal semifinite faithful weight, the dense vectors represented by
finite products support the [[operator-algebras/tomita-operator|Tomita operator]]. Its
[[shale-paper/polar-decomposition|polar decomposition]] yields the
[[operator-algebras/modular-conjugation|modular conjugation]] and
[[operator-algebras/modular-operator|modular operator]], from which the
[[operator-algebras/modular-automorphism-group|modular automorphism group]] of
\(\varphi\) is obtained. The weight GNS construction is therefore the
Hilbert-space entry point to
[[operator-algebras/tomita-takesaki-theorem|Tomita–Takesaki theory]].

## References

1. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: Chapter VII, §1 on weights and semi-cyclic representations, and §2 on their associated left Hilbert algebras.
