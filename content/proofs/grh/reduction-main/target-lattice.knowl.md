+++
id = "proofs/grh/reduction-main/target-lattice"
title = "The target forms as a twisted lattice"
kind = "construction"
summary = "The twisted lattice on the target forms: twists are the m-fold twists, the lift at a twist is the chain of m theta lifts, a twist is allowed at l if the norm of its modulus is prime to l, and integral means integral values."
aliases = ["targetLattice", "target lattice"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.targetLattice", "New.Data.levelOf_lastResidueLevel_le_chosenLevel", "New.Data.classAut_lastResidueLevel_eq_bot", "New.Data.mem_integralVectors_targetLattice", "New.Data.normSqAt_targetLattice", "New.Data.volume_targetLattice", "New.Data.injective_lift_targetLattice"]
lean_files = ["src/New/Reduction/IntegralTargetForms.lean"]
proof_status = "outline"
+++

Let \(D\) be [[proofs/grh/reduction-main/data|data]]. Let \(\mathcal T\) be the space of [[?lean:New.Data.targetForms|target forms]] (the good forms on the hermitian space \(Y_0\)), a finite-dimensional complex inner product space of dimension \(d_T\) ([[?lean:New.Data.targetDim|target dimension]]). The **target lattice** is the [[proofs/grh/reduction-main/twisted-lattice|twisted lattice]] \(L_D\) on \(\mathcal T\) with:

- twists: the [[proofs/grh/reduction-main/m-fold-twist|\(m\)-fold twists]] \(\vartheta\), with trivial twist \(1\);
- \(S_\vartheta\): the space of algebraic modular forms on \(\mathrm U(Y_m)\) with the weight, level and level character attached to \(\vartheta\) (level trivial at the chosen places and block upper triangular at the places of the modulus \(Q(\vartheta)\)), with its Petersson-type inner product;
- \(\Theta_\vartheta:\mathcal T\to S_\vartheta\): the [[?lean:New.Data.Θ|chain of \(m\) theta lifts for \(\vartheta\)]] restricted to the target forms;
- \(\vartheta\) is allowed at \(\ell\) iff \(\gcd(\ell,\mathrm{Nm}\,Q(\vartheta))=1\), where \(\mathrm{Nm}\,Q(\vartheta)\) is the product of the norms of the places of the modulus;
- \(\Lambda_{\vartheta,\iota}\): the [[?lean:New.LevelPlaces.LevelForm.integralForms|forms integral at \(\iota\)]] (all values in the unit ball of the \(\ell\)-adic gauge);
- coordinates for \(\vartheta=1\): the coordinates, in the standard basis of the Weyl module, of the values of a form at representatives \(g_c\) of the classes \(c\in\Gamma\backslash G_f/K\); \(G\) is the block sum of the rational Gram matrices of the Weyl module.

**Proposition.** This is a twisted lattice, and:

1. \(y\in\mathcal T\) is an integral vector at \(\iota\mid\ell\) iff \(\Theta_\vartheta y\) is integral at \(\iota\) for every \(m\)-fold twist \(\vartheta\) with \(\gcd(\ell,\mathrm{Nm}\,Q(\vartheta))=1\);
2. \(\lVert\Theta_1y\rVert_\sigma^2\) in the sense of the twisted lattice equals the squared norm at \(\sigma\) of the algebraic form \(\Theta_1y\);
3. the [[proofs/grh/reduction-main/twisted-lattice-volume|volume]] is \(Z(\vartheta)=\det(\Theta_\vartheta^*\Theta_\vartheta)\), the [[?lean:New.Data.chainDeterminant|chain determinant]];
4. every \(\Theta_\vartheta\) is injective.

## Proof

Outline. The level \(K_\vartheta\) of \(S_\vartheta\) is contained in the group of integral elements reducing to \(1\) at every chosen place (the reductions are trivial there by definition of the residue level). Such a level is sufficiently small: \(\Gamma\cap gK_\vartheta g^{-1}=1\) for all \(g\) (asserted by `New.Data.classAut_eq_bot_of_le_chosenLevel`, using that the rank of \(Y_m\) is at most \(2n_m\)). With trivial stabilisers, the inner product of two forms is the plain sum over classes of the Weyl-module pairings of their values; this gives the rational-form axiom (`inner_eq_valueCoord`), statement (2) (`normSqAt_eq_re_valueCoord`), and the integrality axiom: the pairing of a form integral at \(\bar\iota\) with a form integral at \(\iota\) is integral at \(\iota\) (`norm_nsmul_inner_le_one`, with the factor \(\#\)stabiliser \(=1\)). (1) is the definition of integral vectors, (3) holds by definition, and (4) is the injectivity of the chain of lifts on the forms of principal level, [[?lean:New.Data.lowerChainAtLevel_injective|injectivity of the lower chain]]. The steps quoted from other files are asserted here, not reproved.

## References

1. Lean: `New.Data.targetLattice` and the lemmas in the front matter, in `src/New/Reduction/IntegralTargetForms.lean`.
