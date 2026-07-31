+++
id = "operator-algebras/compact-operator-cstar-algebra"
title = "C*-algebra of compact operators"
kind = "definition"
summary = "The norm-closed C*-algebra of compact operators on a Hilbert space."
aliases = ["K(H)", "compact operator algebra"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
+++

Let \(\mathcal H\) be a complex
[[linear-algebra/hilbert-space|Hilbert space]]. The **\(C^*\)-algebra of
compact operators** on \(\mathcal H\), denoted \(K(\mathcal H)\), consists of
all [[linear-algebra/compact-operator|compact operators]] on \(\mathcal H\).
Equivalently,
\[
K(\mathcal H)=\overline{\{T\in B(\mathcal H):
\operatorname{rank}T<\infty\}}^{\lVert\cdot\rVert}.
\]
It is a [[operator-algebras/closed-two-sided-ideal|norm-closed,
adjoint-closed two-sided ideal]] in the
[[operator-algebras/bounded-operator-cstar-algebra|bounded-operator algebra]]
\(B(\mathcal H)\), and therefore a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]].
It is unital exactly when \(\mathcal H\) is finite-dimensional.

## Rank-one generators and approximate units

For \(\xi,\eta\in\mathcal H\), the rank-one operator
\(\theta_{\xi,\eta}\) is given by
\(\theta_{\xi,\eta}\zeta=\xi\langle\eta,\zeta\rangle\). Finite linear
combinations of these operators are the [[functional-analysis/finite-rank-operator|finite-rank operators]] and are norm
dense in \(K(\mathcal H)\). If \((P_\lambda)\) is the net of orthogonal
projections onto finite-dimensional subspaces, directed by inclusion, then
\((P_\lambda)\) is a positive contractive
[[operator-algebras/approximate-identity|approximate identity]] for
\(K(\mathcal H)\).

## Ideal and representation structure

When \(\mathcal H\neq 0\), \(K(\mathcal H)\) is simple: it has no nonzero
proper [[operator-algebras/closed-two-sided-ideal|closed two-sided ideals]].
Every nonzero
[[operator-algebras/irreducible-cstar-representation|irreducible
representation]] is unitarily equivalent to its defining action on
\(\mathcal H\), and every
[[operator-algebras/nondegenerate-star-homomorphism|nondegenerate
representation]] is an amplification of that action. These facts make
compact-operator algebras the elementary pieces in the representation theory
of type I \(C^*\)-algebras.

## Multiplier algebra and examples

For nonzero \(\mathcal H\), the
[[operator-algebras/multiplier-algebra|multiplier algebra]] of
\(K(\mathcal H)\) is \(B(\mathcal H)\). If
\(\mathcal H=\ell^2(\mathbb N)\), diagonal compact operators correspond to
sequences converging to zero, while the identity operator is not compact. In
finite dimension,
\(K(\mathbb C^n)=B(\mathbb C^n)=M_n(\mathbb C)\), so the distinction between
compact and bounded operators disappears.

## References

1. Gerard J. Murphy, *\(C^*\)-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §4.1 on compact operators and their representations.
2. Kenneth R. Davidson, *\(C^*\)-Algebras by Example*, Fields Institute Monographs 6, American Mathematical Society, 1996. [AMS publisher record](https://bookstore.ams.org/fim-6). Relevant: §I.4 on compact-operator algebras.
