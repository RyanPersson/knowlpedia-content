+++
id = "proofs/grh/spanning-core/rallis-series-is-a-hecke-operator"
title = "The series of Rallis' formula is a spherical Hecke operator"
kind = "theorem"
summary = "On two spaces with different signs, the Rallis operator of a tame character and a lift index is given by one spherical Hecke operator away from the level; it preserves good forms."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_hecke_eq_rallisOperator", "New.Data.exists_rallisTerm_eq_inner", "New.Data.exists_heckeAlgebra_eq_mul_inner_of_hasSum_rallisTerm", "New.Data.rallisOnGood", "New.Data.coe_rallisOnGood_apply"]
lean_files = ["src/New/Spanning/Multiplicities/EqualMultiplicities.lean"]
proof_status = "full"
+++

**Theorem.** Let \(D\) be admissible data, \(\vartheta\) a [[?lean:New.Data.TameChar|tame character]], \(j\ge0\), and \(V,V'\) hermitian spaces of rank \(r\) over \(E\), with signs \(s,s'\), such that at every infinite place the doubled parameter [[?lean:New.Data.paramW|\(2\varsigma_v\)]] [[?lean:New.HCParam.HasGap|has gap]] [[?lean:New.Data.gap|\(\Delta\)]] for \(s\) and for \(s'\). Let \(R_V=\) [[?lean:New.Data.rallisOperator|the Rallis operator]] \(\mathrm{Ral}_{j,\vartheta}\) on the forms of principal level on \(V\). Then there is \(p\) in the [[proofs/grh/spanning-core/spherical-hecke-algebra-away-from-the-level|spherical Hecke algebra away from \(M\)]] with
\[
p_V=R_V\qquad\text{and}\qquad p_{V'}=R_{V'} .
\]
In particular \(R_V\) preserves the good forms of \(V\) ([[proofs/grh/spanning-core/hecke-action-on-good-forms|Hecke action on good forms]]); its restriction to the good forms is the **Rallis operator on good forms**.

More generally: if \(a,a'\in\mathbb{C}\) and \(B\), \(B'\) are functions of pairs of forms of principal level on \(V\), \(V'\) such that \(\sum_i a\,\tau_V(z,y,i)=B(z,y)\) and \(\sum_i a'\,\tau_{V'}(z,y,i)=B'(z,y)\) for all \(z,y\), where \(\tau_W(z,y,i)\) are the [[?lean:New.Data.rallisTerm|terms of Rallis' formula]] and the sums are unconditionally convergent sums over the cosets \(i\) of \(G_f\) modulo the points integral away from the places of the modulus \(\pi_MQ\) of \(\vartheta\) and their conjugates, then one \(p\in\mathcal H\) gives \(B(z,y)=a\langle z,p_Vy\rangle\) and \(B'(z,y)=a'\langle z,p_{V'}y\rangle\).

## Proof

*Step 1: each term is a Hecke matrix coefficient.* By definition, \(\tau_W(z,y,i)=c_i\,\langle z,\gamma_i\cdot y\rangle\), where \(\gamma_i\) is the chosen representative of the coset \(i\) (`New.SiegelWeil.cosetRep`), which is supported at the places away from the modulus and its conjugate, so that its component at every place of the modulus is \(1\); and \(c_i\) is a scalar (a vacuum coefficient of the Weil representation divided by a number of matrices over the residue ring of the modulus) that depends on \(i,\vartheta,j\) but not on \(W\). The chosen places are places of the modulus (`New.Rows.places_levelModulus`), so \(\gamma_i\in G^M\). By [[proofs/grh/spanning-core/translation-as-a-hecke-operator|translations as Hecke operators]] there is \(p_i\in\mathcal H\), independent of \(W\), with \(\tau_W(z,y,i)=\langle z,(c_ip_i)_Wy\rangle\).

*Step 2: closedness.* The forms of principal level on \(V\) and on \(V'\) are finite-dimensional (the gap makes the type a cusp kernel). Consider the linear map from \(\mathcal H\) to pairs of functions
\[
p\ \longmapsto\ \bigl((z,y)\mapsto a\langle z,p_Vy\rangle,\ (z,y)\mapsto a'\langle z,p_{V'}y\rangle\bigr).
\]
It factors through the finite-dimensional space \(\operatorname{End}(\mathcal F_V)\times\operatorname{End}(\mathcal F_{V'})\), so its image \(N\) is a finite-dimensional, hence closed, subspace of the space of pairs of functions with the topology of pointwise convergence. By Step 1 every pair of terms \((a\tau_V(\cdot,\cdot,i),a'\tau_{V'}(\cdot,\cdot,i))\) lies in \(N\), hence so do all finite partial sums and their limit \((B,B')\). This proves the general statement.

*Step 3.* By [[?lean:New.Data.hasSum_inner_rallisOperator|`New.Data.hasSum_inner_rallisOperator`]], for every \(W\), \(\langle z,R_Wy\rangle=\sum_iN\,\tau_W(z,y,i)\), where \(N\ne0\) is the number of matrices by which the terms were divided. Step 2 with \(a=a'=N\) gives \(p\) with \(\langle z,R_Vy\rangle=\langle z,(Np)_Vy\rangle\) for all \(z,y\), so \(R_V=(Np)_V\); likewise for \(V'\). \(\blacksquare\)

## References

1. Lean: `New.Data.exists_rallisTerm_eq_inner`, `New.Data.exists_heckeAlgebra_eq_mul_inner_of_hasSum_rallisTerm`, `New.Data.exists_hecke_eq_rallisOperator`, `New.Data.rallisOnGood` in `src/New/Spanning/Multiplicities/EqualMultiplicities.lean`.
