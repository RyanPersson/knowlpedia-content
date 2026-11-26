+++
id = "proofs/grh/upper-elementary-divisors/density-of-points-over-local-ring"
title = "Density of unit points for forms over a local ring"
kind = "lemma"
summary = "Over a local ring whose residue field has at least n+e elements, the vectors of values of the monomials of degree n at the points where a form of degree e is a unit span everything."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Average.eq_top_of_eval_monomial", "New.Average.eq_top_of_forall_linearMap_residueField_eq_zero"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean"]
proof_status = "full"
+++

**Lemma.** Let \(W\) be a [[algebra-commutative/local-ring|local ring]] with [[algebra-commutative/residue-field|residue field]] \(\kappa\), \(\iota\colon W\to O\) a ring homomorphism to a commutative ring, \(\sigma\) a finite set of variables, and \(n,e\ge0\). Let \(g\in W[x_i:i\in\sigma]\) be homogeneous of degree \(e\) and suppose \(g(b_0)\in W^{\times}\) for some point \(b_0\in W^{\sigma}\). Assume \(n+e\le\lvert\kappa\rvert\) (in the formal statement \(\lvert\kappa\rvert\) is read as \(0\) when \(\kappa\) is infinite, so \(\kappa\) is finite unless \(n=e=0\)). Let \(\mathcal{M}_n\) be the set of exponents of degree \(n\). If an \(O\)-submodule \(V\subseteq O^{\mathcal{M}_n}\) contains the vector \(\bigl(\iota(b^{\gamma})\bigr)_{\gamma\in\mathcal{M}_n}\) for every \(b\in W^{\sigma}\) with \(g(b)\in W^{\times}\), then \(V=O^{\mathcal{M}_n}\).

## Proof

Let \(V'\subseteq W^{\mathcal{M}_n}\) be the preimage of \(V\) under entrywise \(\iota\); it is a \(W\)-submodule. If \(V'=W^{\mathcal{M}_n}\) then \(V\) contains the images of the standard basis vectors, hence \(V=O^{\mathcal{M}_n}\). By [[algebra-commutative/nakayama-lemma|Nakayama's lemma]] (the finitely generated module \(W^{\mathcal{M}_n}/V'\) is zero if its reduction modulo the maximal ideal is, i.e. if it has no nonzero \(W\)-linear map to \(\kappa\)), it suffices to show that every \(W\)-linear \(l\colon W^{\mathcal{M}_n}/V'\to\kappa\) vanishes.

Put \(F=\sum_{\gamma}l(e_\gamma)\,x^{\gamma}\in\kappa[x]\), a form of degree \(n\); we must show \(F=0\). Let \(\bar g\in\kappa[x]\) be the reduction of \(g\); \(\bar g\ne0\) since \(\bar g(\bar b_0)\ne0\). For \(z\in\kappa^{\sigma}\) choose a lift \(b\in W^{\sigma}\). Then \(F(z)=l\bigl((b^{\gamma})_\gamma\bigr)\). If \(g(b)\) is a unit, \((b^{\gamma})_\gamma\in V'\) and \(F(z)=0\); otherwise \(\bar g(z)=0\). So \(F\bar g\), homogeneous of degree \(n+e\le\lvert\kappa\rvert\), vanishes at every point of \(\kappa^{\sigma}\). A homogeneous polynomial of degree \(d\le\lvert\kappa\rvert\) vanishing on \(\kappa^{\sigma}\) is zero ([[?c:Vanishing of homogeneous polynomials on a finite field|vanishing criterion]]: modulo \(x_i^{\lvert\kappa\rvert}-x_i\) only monomials with some exponent \(\ge\lvert\kappa\rvert\) are changed, which for a form of degree \(\le\lvert\kappa\rvert\) are the pure powers \(x_i^{\lvert\kappa\rvert}\), and these are controlled by homogeneity). Hence \(F\bar g=0\) and, \(\kappa[x]\) being a domain, \(F=0\). \(\square\)

## References

1. Lean: `New.Average.eq_top_of_eval_monomial`, `New.Average.eq_top_of_forall_linearMap_residueField_eq_zero` in `src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean`.
2. Mathlib: `MvPolynomial.IsHomogeneous.eq_zero_of_forall_eval_eq_zero_of_le_card` (the vanishing criterion used in the proof).
