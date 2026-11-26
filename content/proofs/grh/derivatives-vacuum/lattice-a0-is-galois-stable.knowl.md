+++
id = "proofs/grh/derivatives-vacuum/lattice-a0-is-galois-stable"
title = "The lattice a0 is Galois stable and its vectors have integral norms"
kind = "lemma"
summary = "The lattice a0 of E = K(zeta) is described place by place, is stable under Gal(E/K), and the sum of the squared absolute values of a vector over the CM type is a natural number."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.finiteImage_mem_iff", "New.Parameters.valuation_galOfPlace", "New.Parameters.finiteImage_galOfPlace_mem", "New.Parameters.exists_natCast_eq_sum_norm_sq", "New.QuadField.exists_algebraMap_eq_of_star_eq", "New.exists_eq_intCast_of_mem_quadInt_of_conj_eq", "New.Parameters.phi_betaKInE"]
lean_files = ["src/New/Derivatives/Vacuum/ShortVectors.lean"]
proof_status = "full"
+++

Let \(P\) be [[?lean:New.Parameters|parameters]], \(s\in\mathbb{N}\), \(E=K(\zeta)\), \(g=P'(\zeta)\) the [[?lean:New.Parameters.relDifferentGen|generator of the different]] of \(E/K\), \(\beta=(1+\sqrt{-d})/2\), and \(\mathfrak{a}_0=E\cap\alpha\widehat{\mathcal{O}}_E\) for the [[?lean:New.Parameters.α|idele \(\alpha\)]].

**Lemma.**

1. \(y\in E\) lies in \(\mathfrak{a}_0\) if and only if for every finite place \(w\) of \(E\): \(\lvert gy\rvert_w\le1\) if \(\beta\in w\), and \(\lvert y\rvert_w\le1\) otherwise.
2. \(\mathfrak{a}_0\) is stable under \(\operatorname{Gal}(E/K)\).
3. For \(y\in\mathfrak{a}_0\), \(\sum_\tau\lvert\Phi_\tau(y)\rvert^2\) is a natural number.

## Proof

1. The component of \(\alpha\) at \(w\) is \(g^{-1}\) if \(\beta\in w\) and \(1\) otherwise; \(\alpha^{-1}y\) is integral iff it is so at every \(w\).

2. Let \(\rho\in\operatorname{Gal}(E/K)\). The valuation of \(\rho(y)\) at \(w\) is that of \(y\) at \(\rho^{-1}w\) (the preimage of \(w\)). Since \(\rho\) fixes \(\beta\in K\), \(\beta\in w\iff\beta\in\rho^{-1}w\); and \(g\) has the same valuation at \(w\) and at \(\rho^{-1}w\), the different being Galois stable ([[?lean:New.Parameters.valuation_map_relDifferentGen|conjugates of \(g\) have equal valuations]]). So the criterion 1 for \(\rho(y)\) at \(w\) is the criterion for \(y\) at \(\rho^{-1}w\).

3. By [[proofs/grh/derivatives-vacuum/hermitian-product-of-lattice-vectors-is-integral|integrality of hermitian products]], \(z=\langle y,y\rangle\in\mathcal{O}_K\), and \(z\) is real. A real element of \(K\) is fixed by the nontrivial automorphism of \(K/\mathbb{Q}\), hence rational; a rational algebraic integer is an integer. Finally \(z\ge0\).

## References

1. Lean: `New.Parameters.finiteImage_mem_iff`, `New.Parameters.valuation_galOfPlace`, `New.Parameters.finiteImage_galOfPlace_mem`, `New.Parameters.exists_natCast_eq_sum_norm_sq`, `New.QuadField.exists_algebraMap_eq_of_star_eq`, `New.exists_eq_intCast_of_mem_quadInt_of_conj_eq`, `New.Parameters.phi_betaKInE` in `src/New/Derivatives/Vacuum/ShortVectors.lean`.
