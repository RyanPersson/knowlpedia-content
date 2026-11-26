+++
id = "proofs/grh/derivatives-vacuum/product-of-translated-thetas-as-theta-power"
title = "Products of theta functions translated by division points"
kind = "lemma"
summary = "A product of translates of theta by delta-division points, evaluated at conj(delta) times linear forms, is the N-th power of the product of theta at these forms times an integral series in the parameters, N the norm of delta."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.exists_prod_twistedTranslate_eq_thetaProd_mul"]
lean_files = ["src/New/Derivatives/Vacuum/StandardDataProducts.lean"]
proof_status = "outline"
+++

Notation as in [[proofs/grh/derivatives-vacuum/jet-ring|the definition of the jet ring]]: \(d\) a prime \(\equiv7\bmod8\), \(C\) a CM lattice for \(d\), \(\iota_p\) a \(p\)-adic place, \(\mu_i\) (\(i\in I\)) linear forms in variables \(z_x\) with coefficients in \(\mathbb{C}_p\). For an entire function \(G\) write \(T_p(G)\in\mathbb{C}_p[\![T]\!]\) for its Taylor series at \(0\) with \(\iota_p\) applied to the coefficients.

**Lemma.** Let \(\delta\in\mathcal{O}_K\subset\mathbb{C}\), \(\delta\ne0\), \(N=\delta\bar\delta\), and \(y_i\in\mathbb{C}\) with \(\delta y_i\in\Lambda_C\) for all \(i\). Then there is \(H\in\mathcal{O}[\![y(\mu z)]\!]\) with
\[ \prod_{i\in I}T_p\bigl(\tau^{(1)}_{y_i}\theta_C\bigr)\bigl(\iota_p(\bar\delta)\,\mu_i(z)\bigr)=\Bigl(\prod_{i\in I}\theta(\mu_iz)\Bigr)^{N}H . \]

## Proof

Multiplication by \(\bar\delta\) is an isogeny of \(C\) to itself of degree \(N\). The one-variable statement is a Lib result on isogenies ([[?lean:New.CMLattice.exists_rescale_twistedTranslate_eq_theta_pow_mul|integrality principle on one curve]]; asserted here): for each \(i\) there is \(u_i\in\mathcal{O}[\![y]\!]\) with \(T_p(\tau^{(1)}_{y_i}\theta_C)(\iota_p(\bar\delta)T)=\theta(T)^N\,u_i(T)\). Substitute \(T=\mu_i(z)\) and multiply over \(i\); \(H=\prod_iu_i(\mu_iz)\) lies in \(\mathcal{O}[\![y(\mu z)]\!]\), a ring containing each substituted series.

## References

1. Lean: `New.CMLattice.exists_prod_twistedTranslate_eq_thetaProd_mul` in `src/New/Derivatives/Vacuum/StandardDataProducts.lean`.
