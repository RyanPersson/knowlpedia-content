+++
id = "proofs/grh/derivatives-vacuum/jets-along-homogeneous-polynomials"
title = "Jets of the jet series along homogeneous polynomials"
kind = "lemma"
summary = "The jet of the jet series at scale a along a homogeneous polynomial Q of degree l is a^l times the theta value of the Fock vector of Q tensored with the vector."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Space.jet_jetSeries_of_isHomogeneous", "New.jet_rescale"]
lean_files = ["src/New/Derivatives/Vacuum/Scale.lean"]
proof_status = "full"
+++

For a commutative ring \(R\), a polynomial \(Q\) and a power series \(F\) in variables \(X_x\), \(x\in X\), the [[?lean:New.jet|jet]] of \(F\) along \(Q\) is \((Q(\partial)F)(0)\in R\).

**Lemma.**

1. If \(Q\) is homogeneous of degree \(l\) and \(a\in R\), then the jet along \(Q\) of \(F(aX)\) (all variables rescaled by \(a\)) is \(a^l\) times the jet of \(F\).
2. Let \(E\) be a CM field with CM type and [[?lean:New.WeilData|Weil data]], \(V\) a [[?lean:New.Space|hermitian space]] over \(E\) with index set \(n\) and signs \(\varepsilon\), \(f\in\mathcal{S}(V)\), \(a\in\mathbb{C}\), and \(Q\in\mathbb{C}[X_p:p\in\Sigma\times n]\) homogeneous of degree \(l\). Then the jet along \(Q\) of the [[?lean:New.Space.jetSeries|jet series]] \(J_a(f)\) is
\[ a^{\,l}\;\theta\bigl(v_Q\otimes f\bigr), \]
where \(\Sigma\) is the set of infinite places of \(E\), the pair \((v,i)\in\Sigma\times n\) carries the sign \(\varepsilon_i\), \(v_Q\) is the Fock vector of \(Q\) for these signs, and \(v\otimes f\) is the [[?lean:New.Space.integrated|integrated action]] of the real Heisenberg group on \(f\) against \(v\).

## Proof

1. The jet along a monomial \(X^\alpha\) is \(\alpha!\) times the coefficient of \(X^\alpha\); rescaling multiplies this coefficient by \(a^{\lvert\alpha\rvert}=a^l\) for every monomial of \(Q\).

2. By definition of the coefficients, \(J_a(f)\) is \(J_1(f)\) rescaled by \(a\) (Lean `New.Space.jetSeries_mul_eq_rescale`), and the jet of \(J_1(f)\) along \(Q\) is \(\theta(v_Q\otimes f)\) (Lean `New.Space.jet_jetSeries_eq_theta`; for a monomial this is the definition of the coefficient, and both sides are linear in \(Q\)). Apply 1.

## References

1. Lean: `New.Space.jet_jetSeries_of_isHomogeneous`, `New.jet_rescale` in `src/New/Derivatives/Vacuum/Scale.lean`.
