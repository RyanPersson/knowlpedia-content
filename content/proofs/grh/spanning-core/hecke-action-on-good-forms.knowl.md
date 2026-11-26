+++
id = "proofs/grh/spanning-core/hecke-action-on-good-forms"
title = "Action of the Hecke algebra on good forms"
kind = "construction"
summary = "The spherical Hecke operators away from the level commute with the finite group at the chosen places and therefore act on the good forms."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.heckeOnGood", "New.Data.coe_heckeOnGood_apply", "New.Data.commute_heckeAlgebra_principalRep", "New.Data.principalRep_mem_eigenPart", "New.Data.liftGroupAlgebra", "New.Data.coe_principalRep_asAlgebraHom_apply", "New.Data.liftGroupAlgebra_mem_universalLevelAlgebra", "New.Data.liftResidue_apply_mem_levelSpace", "New.Data.coe_principalRep_apply"]
lean_files = ["src/New/Spanning/Multiplicities/HeckeEigensystems.lean"]
+++

Let \(D\) be admissible data, \(V\) a hermitian space of rank \(r\) over \(E\), \(\rho_V\) the [[?lean:New.Data.principalRep|action]] of the finite group \(\bar G=\) [[?lean:New.Data.chosenGL|\(\prod_w\mathrm{GL}_r(\mathbb{F}_w)\)]] on the forms of principal level on \(V\) (an element \(g\) acts through an integral lift \(\tilde g\in K_0\) supported at the chosen places and their conjugates), and \(\mathcal H\) the [[proofs/grh/spanning-core/spherical-hecke-algebra-away-from-the-level|spherical Hecke algebra away from \(M\)]].

**Fact.** For \(T\in\mathcal H\) and \(x\in\mathbb{C}[\bar G]\), \(T_V\) commutes with \(\rho_V(x)\).

Consequently each \(T_V\) preserves the [[?lean:New.Data.goodForms|good forms]] \(\rho_V(e_0)\mathcal F_V\), and the **action of \(\mathcal H\) on the good forms of \(V\)** is the multiplicative map \(T\mapsto T_V|_{\text{good forms}}\). Likewise each [[proofs/grh/spanning-core/hecke-eigensystem-part|eigensystem part]] \(\mathcal F_V[p]\) is stable under \(\mathbb{C}[\bar G]\).

Moreover, for \(x=\sum_gx_g\,g\in\mathbb{C}[\bar G]\) the **lift** \(\tilde x=\sum_gx_g\,\tilde g\in\mathbb{C}[G_f]\) acts on forms of principal level as \(\rho_V(x)\), and \(\tilde x\) maps \(J_M\)-fixed vectors to \(J_M\)-fixed vectors in every representation of \(G_f\).

## Proof

Let \(T\) be given by \(a\in\mathbb{C}[G^M]\). By linearity it suffices to treat \(x=g\in\bar G\). The lift \(\tilde g\) is supported at the chosen places and their conjugates, and such elements commute with the off-level group \(G^M\); so the translation by \(\tilde g\) commutes with the action of \(a\). If \(y=\rho_V(e_0)z\) is good then \(T_Vy=\rho_V(e_0)T_Vz\) is good. If \(T_zy=p(z)y\) for all \(z\), then \(T_z\rho_V(x)y=\rho_V(x)T_zy=p(z)\rho_V(x)y\).

For the last statement: in every representation of \(G_f\) the finite group \(\bar G\) acts on the \(J_M\)-fixed vectors through the lifts \(\tilde g\) (the library construction `New.levelRep`, which rests on \(\tilde g\) normalising \(J_M\)); in particular translation by \(\tilde g\) preserves \(J_M\)-fixed vectors. Extend linearly. \(\blacksquare\)

## References

1. Lean: `New.Data.commute_heckeAlgebra_principalRep`, `New.Data.heckeOnGood`, `New.Data.principalRep_mem_eigenPart`, `New.Data.liftGroupAlgebra`, `New.Data.liftGroupAlgebra_mem_universalLevelAlgebra` in `src/New/Spanning/Multiplicities/HeckeEigensystems.lean`.
