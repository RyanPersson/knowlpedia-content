+++
id = "proofs/grh/spanning-core/hecke-operators-at-split-places"
title = "Hecke operators at split places off the level"
kind = "construction"
summary = "The operators T_{w,i} at split places off the level, as members of the spherical Hecke algebra away from the level."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.principalHeckeSplit", "New.Data.heckeOperator", "New.Data.coe_heckeOperator_apply", "New.Data.principalHeckeSplit_mem_heckeAlgebra", "New.Data.exists_asAlgebraHom_eq_heckeSplit", "New.Data.heckeSplit_mem_principalForms", "New.Data.principalForms_le_sphericalAt", "New.Data.IsSplitOffLevel.ofSplitPlace_mem"]
lean_files = ["src/New/Spanning/Multiplicities/HeckeEigensystems.lean"]
+++

Let \(D\) be admissible data and \(w\) a finite place of \(E\) that is [[proofs/grh/spanning-core/spherical-hecke-algebra-away-from-the-level|split off the level]]. For \(i\ge0\) let \(T_{w,i}\) be the [[?lean:New.heckeSplit|Hecke operator at the split place \(w\)]] of the double coset of \(\operatorname{diag}(\varpi 1_i,1_{r-i})\) in \(\mathrm{GL}_r(E_w)\), acting in any representation of \(G_f\) through the embedding of \(\mathrm{GL}_r(E_w)\) at the places \(w,\bar w\).

For every hermitian space \(V\) of rank \(r\), \(T_{w,i}\) maps the [[?lean:New.Data.principalForms|forms of principal level]] on \(V\) to themselves. The **Hecke operator** \(T_x\in\mathcal H\), for a pair \(x=(w,i)\) of a finite place and a natural number, is the member of the [[proofs/grh/spanning-core/spherical-hecke-algebra-away-from-the-level|spherical Hecke algebra away from \(M\)]] given by the family of restrictions of \(T_{w,i}\) if \(w\) is split off the level, and \(T_x=0\) otherwise.

## Proof

*That the family is well defined and lies in \(\mathcal H\).* The embedding of \(\mathrm{GL}_r(E_w)\) has image in the off-level group \(G^M\), because its components at places other than \(w,\bar w\) are \(1\) and \(w,\bar w\) are not chosen. The operator \(T_{w,i}\) is a finite sum of translations by representatives of the cosets \(gK_w\) in the double coset; let \(a\in\mathbb{C}[G^M]\) be the corresponding sum of group elements (in Lean: the operator of the regular representation of \(G^M\) applied to \(1\)). Then \(a\) acts as \(T_{w,i}\) in every representation of \(G_f\). It lies in the spherical algebra: a \(J_M\)-fixed vector \(y\) is fixed by the part of \(K_0\) supported at \(w,\bar w\) (which lies in \(J_M\), as \(w\) is off the level), i.e. it is spherical at \(w\); and \(T_{w,i}\) maps vectors that are spherical at \(w\) and fixed by a subgroup \(J\subseteq K_0\) to \(J\)-fixed vectors (`New.heckeSplit_mem_levelSpace`, a Lean statement of the library, used as stated). \(\blacksquare\)

## References

1. Lean: `New.Data.heckeOperator`, `New.Data.principalHeckeSplit`, `New.Data.principalHeckeSplit_mem_heckeAlgebra` in `src/New/Spanning/Multiplicities/HeckeEigensystems.lean`.
