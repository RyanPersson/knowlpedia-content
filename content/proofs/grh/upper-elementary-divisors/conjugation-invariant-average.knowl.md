+++
id = "proofs/grh/upper-elementary-divisors/conjugation-invariant-average"
title = "Average for a Levi subgroup on polynomials in matrix entries"
kind = "definition"
summary = "A linear form on polynomials in the entries of a matrix that is invariant under conjugation by a Levi subgroup, kills monomials of large row weight, and equals a scaled evaluation at the identity on polynomials without such monomials."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Average.conjSubst", "New.Average.evalAtOne", "New.Average.IsAverage", "New.Average.evalAtOne_conjSubst", "New.Average.conjSubst_diagGL_zpow_monomial"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean"]
+++

Let \(W,O\) be commutative rings, \(\iota\colon W\to O\) a [[algebra-rings/ring-homomorphism|ring homomorphism]], \(k\ge0\), and \(O[X]=O[X_{ij}:0\le i,j<k]\) the polynomial ring in the entries of a generic \(k\times k\) matrix \(X\). For \(a\in\mathrm{GL}_k(W)\), **conjugation** is the \(O\)-algebra endomorphism \(c_a\) of \(O[X]\) that substitutes \(\iota(a^{-1})\,X\,\iota(a)\) for \(X\):
\[
c_a(X_{ij})=\sum_{s,t}\iota\bigl((a^{-1})_{is}\bigr)\,\iota(a_{tj})\,X_{st}.
\]
For \(c\in O\), let \(\mathrm{ev}_c\colon O[X]\to O\), \(\psi\mapsto c\,\psi(1)\), be \(c\) times evaluation at the identity matrix. For \(\rho\in\mathbb{Z}^{k}\), the **row weight** of a monomial \(X^{\alpha}\) is \(\sum_{i,j}\alpha(i,j)\rho_i\) and its **column weight** is \(\sum_{i,j}\alpha(i,j)\rho_j\).

Let \(\tau\colon\{0,\dots,k-1\}\to\mathbb{N}\) be a labelling with [[?lean:New.levi|Levi subgroup]] \(L_\tau(W)=\{a\in\mathrm{GL}_k(W): a_{ij}=0\text{ if }\tau(i)\neq\tau(j)\}\), and let \(\rho\in\mathbb{Z}^{k}\), \(t\in\mathbb{Z}\), \(c\in O\), \(D\in\mathbb{N}\). An \(O\)-linear form \(I\colon O[X]\to O\) is an **average** for \((\tau,\iota,\rho,t,c,D)\) if

1. \(I(c_a\psi)=I(\psi)\) for all \(a\in L_\tau(W)\) and \(\psi\in O[X]\);
2. \(I(X^{\alpha})=0\) for every monomial of row weight \(>t\) (a **bad** monomial);
3. for every [[algebra-rings/ideal|ideal]] \(J\subseteq O\) and every \(\psi\) of total degree \(\le D\): if for all \(a\in L_\tau(W)\) the coefficients of the bad monomials of \(c_a\psi\) lie in \(J\), then \(I(\psi)-c\,\psi(1)\in J\).

## Properties

- \(\mathrm{ev}_c(c_a\psi)=\mathrm{ev}_c(\psi)\), because \(\iota(a^{-1})\cdot1\cdot\iota(a)=1\).
- If \(a=\operatorname{diag}(u^{\rho_i})\) for a unit \(u\in W^{\times}\), then \(c_a(X^{\alpha})=\iota(u)^{e}X^{\alpha}\), where \(e\) is the column weight minus the row weight of \(\alpha\) (each \(X_{ij}\) is scaled by \(\iota(u)^{\rho_j-\rho_i}\)).
- Consequently an invariant form vanishes on monomials with different row and column weights; see [[proofs/grh/upper-elementary-divisors/invariant-forms-vanish-on-unbalanced-monomials|the lemma on unbalanced monomials]].

Existence is [[proofs/grh/upper-elementary-divisors/existence-of-average|the existence theorem]].

## References

1. Lean: `New.Average.conjSubst`, `New.Average.evalAtOne`, `New.Average.IsAverage`, `New.Average.evalAtOne_conjSubst`, `New.Average.conjSubst_diagGL_zpow_monomial` in `src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean`.
