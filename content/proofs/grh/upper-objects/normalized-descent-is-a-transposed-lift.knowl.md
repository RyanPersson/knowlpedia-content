+++
id = "proofs/grh/upper-objects/normalized-descent-is-a-transposed-lift"
title = "The normalized descent is a multiple of the conjugate transposed lift"
kind = "theorem"
summary = "The normalized descent of a form on V equals the dimension of the Weyl module times the index of the level, times the conjugate of the theta lift from V to W of the conjugate scalar form, with the datum of the highest vector."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.normalizedDescent_eq_smul_star_lift_swap", "New.DescentPair.omega_fockDatum_star", "New.DescentPair.conjKernel_equivariant", "New.LevelPlaces.ker_reductionGL_eq", "New.LevelPlaces.card_levelModulus_residueRing", "New.LevelPlaces.card_GL_levelModulus"]
lean_files = ["src/New/UpperBound/Objects/AuxiliaryPair.lean"]
proof_status = "outline"
+++

Let \(O\) be a [[proofs/grh/upper-objects/descent-pair|descent pair]], \(\mathcal V\) its Weyl module with \(d=\dim\mathcal V\), \(v^+\in\mathcal V\) the highest vector for the [[proofs/grh/upper-objects/descent-pair-fitting-parameters|parameter \(l'\) of \(V\)]], \(K_O\subseteq K_0\) the level group and \(\chi_O\) its character. For a form \(\Xi\in\mathcal F_V(O)\) let \(\Xi^\natural(g)=\langle v^+,\rho(g_\infty^{-1})\Xi(g_f)\rangle\) be the associated scalar function on \(U(V)(\mathbb A)\) ([[?lean:New.ofAlgForm|scalar form of an algebraic form]]).

**Theorem.** For every \(\Xi\in\mathcal F_V(O)\), the [[proofs/grh/upper-objects/normalized-descent|normalized descent]] satisfies
\[
\theta\Xi=d\cdot[K_0:K_O]\cdot\overline{\operatorname{Lift}_{V\to W}\big(v_{P_{v^+}}\otimes\Psi_{\mathrm{bl}}\otimes\mathrm{vac};\ \overline{\Xi^\natural}\big)},
\]
where \(\operatorname{Lift}_{V\to W}(\varphi;F)(y)=\int\theta(\omega(y,x)\varphi)\,F(x)\,dx\) is the [[?lean:New.Space.lift|theta lift]] for the swapped theta kernel of \(O\), integrated over \(U(V)(E^+)\backslash U(V)(\mathbb A)\) with the quotient measure of the Lean development, and \([K_0:K_O]\) is the [[?lean:New.stdLevelIndex|level index]].

Auxiliary statements:

1. For \(x\in U(V)(\mathbb R)\), \(k\in K_O\), \(\xi\in\mathcal V\): \(\omega(1,(x,k))\,(v_{P_{\bar\xi}}\otimes\Psi_{\mathrm{bl}}\otimes\mathrm{vac})=\chi_O(k)\cdot v_{P_{\overline{\rho(x)\xi}}}\otimes\Psi_{\mathrm{bl}}\otimes\mathrm{vac}\).
2. For rational \(\gamma\in U(V)\), \(k\in K_O\), \(v\in\mathcal V\), \(g\in U(W)(\mathbb A)\), \(x\in U(V)(\mathbb A_f)\): the conjugate kernel at \((g,\gamma_fxk)\) applied to \(\chi_O(k)\rho(\gamma)v\) equals the conjugate kernel at \((g,x)\) applied to \(v\).
3. For level places \(X\) with modulus \(MQ\) and residue ring \(R\) of the modulus \(M^eQ\): \(\lvert R\rvert=(\prod_{w\in M}q_w)^e\prod_{w\in Q}q_w\); an element of \(K_0\) reduces to \(1\) modulo \(MQ\) iff it does at every place of \(X\); and \(\lvert\mathrm{GL}_N(R_{MQ})\rvert\) is the index in \(K_0\) of the principal level at the places of \(X\).

## Proof

*1.* The real point acts on the Fock vector by part 4 of [[proofs/grh/upper-objects/highest-vector-polynomial-is-an-edge|the theorem on the highest vector]], and the finite point \(k\) multiplies the block datum by \(\chi_O(k)\) by part 4 of the [[proofs/grh/upper-objects/block-datum-laws|laws of the block datum]] (with trivial component in \(U(W)\)). The Weil representation of an adelic point factors as the real action on the Fock vector and the finite action on the finite datum (Lean: `New.pairWeil_integrated_all`, cited).

*2.* Since \(\chi_O\) has finite order, \(\chi_O(k^{-1})=\overline{\chi_O(k)}\). By 1, the datum of \(\overline{\chi_O(k)\rho(\gamma)v}\) is \(\omega(1,(\gamma_\infty,k^{-1}))\) applied to the datum of \(\bar v\); as \((g,(1,\gamma_fxk))\cdot(1,(\gamma_\infty,k^{-1}))=(g,\gamma\cdot(1,x))\) and the theta functional is invariant under rational points, the two kernels agree.

*Theorem.* Fix \(y\). By definition of the lift and since \(\bar v^+\) corresponds to \(v^+\) under conjugation of the highest vector, the right-hand lift at \(y\), conjugated, is \(\int\Phi(x)\,\Xi^\natural(x)\,dx\) with \(\Phi(x)=\overline{\theta(\omega(y,x)(v_{P_{\bar v^+}}\otimes\Psi_{\mathrm{bl}}\otimes\mathrm{vac}))}\). \(\Phi\) is automorphic on \(U(V)\). By 1 with \(k=1\), \(\Phi(x_\infty,g)\) is the conjugate kernel at \((y,g)\) applied to \(\rho(x_\infty)v^+\). The Lean lemma `New.integral_mul_eq_classIntegral` (cited) states: if \(\Phi\) is automorphic and \(\Phi(x_\infty,g)=L_g(\rho(x_\infty)v^+)\) with linear forms \(L_g\), then \(\int\Phi\cdot\Xi^\natural=(d\,[K_0:K])^{-1}\) times the *class integral* at any level \(K\) of \(g\mapsto L_g(\Xi(g))\), i.e. its integral over \(\Gamma\backslash U(V)(\mathbb A_f)\) for the measure with \(\operatorname{vol}(K)=1\) (the factor \(1/d\) comes from Schur orthogonality on the compact group \(U(V)(\mathbb R)\)). By 2 the function \(g\mapsto(\text{conjugate kernel at }(y,g))(\Xi(g))\) is right invariant under \(K_O\), and for a right \(K\)-invariant function the class integral at \(K\) is the class sum \(\sum_cf(g_c)/\lvert\Gamma\cap g_cKg_c^{-1}\rvert\) (Lean: `New.classIntegral_eq_classSum`, by definition of the class integral). Multiplying by \(d[K_0:K_O]\) gives the formula.

*3.* The cardinality is the absolute norm of the ideal \(M^eQ\), which is multiplicative; the kernel statement is the Chinese remainder theorem for matrices; and the level is the preimage of the trivial subgroup under reduction, whose index is \(\lvert\mathrm{GL}_N(R)\rvert\) (Lean: `New.Modulus.stdLevelIndex_levelOfSubgroup`, cited). \(\square\)

## References

1. Lean: `New.DescentPair.normalizedDescent_eq_smul_star_lift_swap`, `New.DescentPair.conjKernel_equivariant`, `New.DescentPair.omega_fockDatum_star`, `New.LevelPlaces.card_GL_levelModulus` in `src/New/UpperBound/Objects/AuxiliaryPair.lean`.
