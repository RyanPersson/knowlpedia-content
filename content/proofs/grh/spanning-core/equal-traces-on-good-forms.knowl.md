+++
id = "proofs/grh/spanning-core/equal-traces-on-good-forms"
title = "Equal traces of Hecke operators on good forms"
kind = "theorem"
summary = "A spherical Hecke operator away from the level has the same trace, characteristic polynomial and determinant on the good forms of two hermitian spaces that differ only in their signs at the real places."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.trace_heckeOnGood_eq", "New.Data.trace_heckeOnGood_eq_sum", "New.Data.trace_mul_tupleIdem_eq", "New.Data.charpoly_heckeOnGood_eq", "New.Data.det_heckeOnGood_eq", "New.Data.det_rallisOnGood_eq", "New.Data.exists_isPrimitivePolynomial"]
lean_files = ["src/New/Spanning/Multiplicities/EqualMultiplicities.lean"]
proof_status = "outline"
+++

**Theorem (equal traces).** Let \(D\) be [[?lean:New.Data|admissible data]] and \(V,V'\) hermitian spaces of rank \(r\) over \(E\) with signs \(s,s'\) at the infinite places, such that at every infinite place \(v\) the doubled parameter [[?lean:New.Data.paramW|\(2\varsigma_v\)]] [[?lean:New.HCParam.HasGap|has gap]] \(\Delta=\) [[?lean:New.Data.gap|`D.gap`]] both for \(s\) and for \(s'\) (its entries are distinct, have the parity of \(r-1\), and entries with different signs differ by at least \(2\Delta\)). Let \(T\) be in the [[proofs/grh/spanning-core/spherical-hecke-algebra-away-from-the-level|spherical Hecke algebra away from \(M\)]], acting on the [[?lean:New.Data.goodForms|good forms]] \(\mathcal G_V\), \(\mathcal G_{V'}\) by [[proofs/grh/spanning-core/hecke-action-on-good-forms|restriction]]. Then

1. \(\operatorname{tr}(T\mid\mathcal G_V)=\operatorname{tr}(T\mid\mathcal G_{V'})\);
2. \(T\) has the same [[linear-algebra/characteristic-polynomial|characteristic polynomial]] and the same [[linear-algebra/determinant|determinant]] on \(\mathcal G_V\) and on \(\mathcal G_{V'}\);
3. the [[proofs/grh/spanning-core/rallis-series-is-a-hecke-operator|Rallis operator on good forms]] \(\mathrm{Ral}_{j,\vartheta}\) has the same determinant on \(\mathcal G_V\) and on \(\mathcal G_{V'}\), for every tame character \(\vartheta\) and every \(j\).

## Proof

*Step 1: reduction to tuple idempotents.* The good forms are the image of the idempotent \(e=\rho_V(e_0)\), which commutes with \(T_V\); so \(T_Ve\) maps all forms of principal level into \(\mathcal G_V\) and agrees with \(T\) there, whence \(\operatorname{tr}(T\mid\mathcal G_V)=\operatorname{tr}(T_Ve\mid\mathcal F_V)\). As \(e_0=\sum_ce_c\) over the [[?lean:New.Data.goodTupleFamilies|good families]] \(c\) of labels, with \(e_c\) the [[?lean:New.tupleIdem|tuple idempotent]],
\[
\operatorname{tr}(T\mid\mathcal G_V)=\sum_c\operatorname{tr}\bigl(T_V\,\rho_V(e_c)\mid\mathcal F_V\bigr).
\]

*Step 2: each summand is the same for \(V\) and \(V'\) (outline).* Fix a good family \(c\). Let \(a\in\mathcal S\) give \(T\), and let \(f=a\cdot\tilde e_c\in\mathbb{C}[G_f]\) with \(\tilde e_c\) the [[proofs/grh/spanning-core/hecke-action-on-good-forms|lift]] of \(e_c\). Then \(f\) lies in the universal level algebra of \(J_M\) and acts on the forms of principal level of every space \(W\) as \(T_W\rho_W(e_c)\). A good family has a chosen place \(x\) at which \(c_x\) is primitive, in particular an irreducible label of degree \(r\). The library theorem [[?lean:New.isCuspidalAt_convIndicator_tupleIdem|`New.isCuspidalAt_convIndicator_tupleIdem`]] states that then the test function \(f\star1_{J_M}\) is [[?lean:New.IsCuspidalAt|cuspidal at the split place \(x\)]]. The comparison of traces [[?lean:New.trace_eq_of_isCuspidalAt|`New.trace_eq_of_isCuspidalAt`]] (library; a simple trace formula) states: if \(E\) contains the 5040-th roots of unity and has an even number of infinite places, \(r\ge2\), the parameter has gap at least \(500r^3+10r^5\) for both sign vectors, \(K\) is a level, \(f\) lies in the universal level algebra of \(K\) and \(f\star1_K\) is cuspidal at a split place, then operators acting as \(f\) on the forms of parameter \(2\varsigma\) and level \(K\) on \(V\) and on \(V'\) have the same trace. Its numerical hypotheses hold: the number \(f\) of infinite places of \(E\) is even (`New.Data.f_even`), and \(r\ge2\) and \(500r^3+10r^5\le\Delta\) are size inequalities of the data. Neither library theorem is reproved here.

*Step 3.* (1) follows from Steps 1 and 2. For (2): \(T^l\in\mathcal H\) for all \(l\), so the traces of all powers agree, and over \(\mathbb{C}\) the traces of the powers determine the characteristic polynomial (Newton's identities; `New.charpoly_eq_of_trace_pow_eq`), in particular its degree and constant coefficient, hence the determinant. For (3): by [[proofs/grh/spanning-core/rallis-series-is-a-hecke-operator|the Rallis series is a Hecke operator]] one \(p\in\mathcal H\) acts as the Rallis operator on both spaces; apply (2). \(\blacksquare\)

## Remarks

The Lean file head describes this as the analogue of the Jacquet–Langlands correspondence for a quaternion algebra ramified exactly at the real places, and names as related work Harris–Labesse (2004) and Labesse (2011).

## References

1. Lean: `New.Data.trace_heckeOnGood_eq`, `New.Data.charpoly_heckeOnGood_eq`, `New.Data.det_heckeOnGood_eq`, `New.Data.det_rallisOnGood_eq` in `src/New/Spanning/Multiplicities/EqualMultiplicities.lean`.
