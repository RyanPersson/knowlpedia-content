+++
id = "proofs/grh/derivatives-vacuum/integral-vacuum-values"
title = "Values of the integral vacuum are integral, bounded and not all zero"
kind = "theorem"
summary = "For a standard space of rank n the values of the integral vacuum at finite points are integral at every p-adic place, all their conjugates are at most exp(C q1^2)^n, and some value is nonzero."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.norm_intVacuum_le_one", "New.Parameters.norm_gal_intVacuum_le", "New.Parameters.norm_ringEquiv_intVacuum_le", "New.Parameters.exists_intVacuum_ne_zero", "New.Parameters.intVacuum_finVec_eq_prod", "New.Parameters.exists_algEquiv_norm_eq"]
lean_files = ["src/New/Derivatives/Vacuum/IntegralVacuum.lean"]
proof_status = "full"
+++

**Theorem.** Let \(V\) be a [[?lean:New.Space.IsStd|standard]] space over \(E\) with finite index set \(n\), and \(\theta^\circ\) its [[proofs/grh/derivatives-vacuum/integral-vacuum|integral vacuum]].

1. For every finite adelic vector \(x\), every prime \(p\) and \(p\)-adic place \(\iota_p\): \(\lvert\iota_p\theta^\circ(x_f)\rvert_p\le1\).
2. For every field automorphism \(\sigma\) of \(\mathbb{C}\) (not necessarily over \(K\)) and every \(x\): \(\lvert\sigma\,\theta^\circ(x_f)\rvert\le\exp(C_{\mathrm{vac}}q_1^2)^{\lvert n\rvert}\).
3. There is \(x\) with \(\theta^\circ(x_f)\ne0\).

## Proof

*Product formula.* For a standard space the vacuum is a product over the coordinates: \(\mathrm{vac}_V(x_f)=\prod_{i\in n}\mathrm{vac}_1((x_i)_f)\), with \(\mathrm{vac}_1\) the vacuum of rank one (Lean `New.Space.vacElem_apply_eq_prod_lineTheta`). Hence
\[ \theta^\circ(x_f)=\prod_{i\in n}c_{\mathrm{vac}}\,\mathrm{vac}_1((x_i)_f). \]

1 and 2 for \(\sigma\) over \(K\) follow factor by factor from properties (a), (b) of the vacuum scale.

2 in general: \(K\) has a single infinite place, so the restriction of \(\sigma\) to \(K\) is the inclusion or its complex conjugate. In the first case \(\sigma\) is over \(K\); in the second \(\sigma'=\overline{\phantom{x}}\circ\sigma\) is over \(K\) and \(\lvert\sigma z\rvert=\lvert\sigma'z\rvert\) for all \(z\).

3. If \(\theta^\circ\), hence \(\mathrm{vac}_V\) (as \(c_{\mathrm{vac}}\ne0\)), vanished at all finite points, [[proofs/grh/derivatives-vacuum/norm-bounded-by-values-at-finite-points|the bound of the norm by values at finite points]] with \(M=0\) would give \(\langle\mathrm{vac},\mathrm{vac}\rangle=0\); but the vacuum has norm \(1\) (Lean `New.Space.dataInner_vacElem_vacElem`).

## References

1. Lean: `New.Parameters.norm_intVacuum_le_one`, `New.Parameters.norm_gal_intVacuum_le`, `New.Parameters.norm_ringEquiv_intVacuum_le`, `New.Parameters.exists_intVacuum_ne_zero`, `New.Parameters.intVacuum_finVec_eq_prod`, `New.Parameters.exists_algEquiv_norm_eq` in `src/New/Derivatives/Vacuum/IntegralVacuum.lean`.
