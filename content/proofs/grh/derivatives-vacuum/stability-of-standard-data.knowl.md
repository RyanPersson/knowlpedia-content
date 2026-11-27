+++
id = "proofs/grh/derivatives-vacuum/stability-of-standard-data"
title = "Standard data are stable under integral Heisenberg and Weil operators"
kind = "theorem"
summary = "The module of standard data of level delta at p is stable under the finite Heisenberg operators of points that delta makes integral above p and under the Weil operators of finite unitary points integral above p."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.finHeisenbergOp_mem_standardData", "New.Parameters.omega_mem_standardData", "New.Parameters.omega_finHeisenbergOp_intVacuum", "New.Parameters.mulVec_mem_integralAfter", "New.Parameters.integralAfter.stdLattice_le", "New.Parameters.smul_mem_standardData_of_norm_le_one", "New.Parameters.finHeisenbergOp_intVacuum_mem_standardData"]
lean_files = ["src/New/Derivatives/Vacuum/JetIntegrality.lean"]
proof_status = "outline"
+++

Let \(V\) be a [[?lean:New.Space|hermitian space]] over \(E\) with finite index set \(n\), \(\delta\in\mathcal{O}_K\), \(p\) a prime with a \(p\)-adic place \(\iota_p\), and \(\mathcal{D}=\mathcal{D}_p(V,\delta)\) the [[proofs/grh/derivatives-vacuum/standard-data|standard data]].

**Theorem.** Let \(f\in\mathcal{D}\).

1. If \(x\in\mathbb{A}_{E,f}^{\,n}\) is integral after \(\delta\) above \(p\), then \(h(x)f\in\mathcal{D}\).
2. Let \(g\) be an element of the standard finite adelic unitary group (matrices \(g\) over the finite adeles of \(E\) with \(g^{H}g=1\); it acts on \(\mathcal{S}(V)\) in the coordinates given by the adelic point \(a\) of \(V=(J,a)\), and corresponds to the element \(a_fga_f^{-1}\) of \(U(J)\)). If \(g\) is [[?lean:New.integralAbove|integral above \(p\)]], i.e. in these coordinates its components at all places above \(p\) are integral invertible matrices, then \(\omega(1,g)f\in\mathcal{D}\), where \(\omega\) is the [[?lean:New.Space.ω|Weil representation]].

## Proof

Both operators are \(\mathbb{C}\)-linear, so it suffices to treat a generator \(f=h(y)\theta^\circ\), \(y\) integral after \(\delta\) above \(p\).

1. \(h(x)h(y)=\psi(\cdot)\,h(x+y)\) with a value of the self-dual additive character, a root of unity, hence a \(p\)-adic unit; and \(x+y\) is again integral after \(\delta\) above \(p\).

2. Let \(L=\widehat{\mathcal{O}}_E^{\,n}\). The Lib formula for the action of the Weil operators on the untranslated vacuum (Lean `New.Space.omega_vacElem_sum`, with the scalar \(m(g)/\lvert m(g)\rvert^2\); asserted here), the covariance of the finite Heisenberg operators under \(\omega(1,g)\), and \(m(g^{-1})=\overline{m(g)}\) give (this exact identity is the Lean lemma `omega_finHeisenbergOp_intVacuum` of this file)
\[ \omega(1,g)\,h(x)\theta^\circ=m(g^{-1})^{-1}\,h(gx)\sum_{y\in L/(L\cap g^{-1}L)}h(gy)\,\theta^\circ, \]
where \(m\) is the finite part of the multiplier of the Weil operators. Now: (i) \(\lvert\iota_pm(g^{-1})\rvert_p=1\) because \(g^{-1}\) is integral above \(p\) (asserted: Lean `norm_finMultiplier_eq_one`); (ii) if \(\delta x\) is integral above \(p\) then so is \(\delta gx=g(\delta x)\), since at a place above \(p\) the matrix \(g\) is integral; (iii) every \(y\in L\) is integral after \(\delta\) (as \(\delta\) is an integer), hence so is \(gy\) by (ii). So each \(h(gy)\theta^\circ\) is a generator of \(\mathcal{D}\), their sum is in \(\mathcal{D}\), and by part 1 and (i) so is the right-hand side.

## References

1. Lean: `New.Parameters.finHeisenbergOp_mem_standardData`, `New.Parameters.omega_mem_standardData`, `New.Parameters.omega_finHeisenbergOp_intVacuum`, `New.Parameters.mulVec_mem_integralAfter`, `New.Parameters.integralAfter.stdLattice_le`, `New.Parameters.smul_mem_standardData_of_norm_le_one`, `New.Parameters.finHeisenbergOp_intVacuum_mem_standardData` in `src/New/Derivatives/Vacuum/JetIntegrality.lean`.
