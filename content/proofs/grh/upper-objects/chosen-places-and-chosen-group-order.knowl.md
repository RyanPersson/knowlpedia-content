+++
id = "proofs/grh/upper-objects/chosen-places-and-chosen-group-order"
title = "Chosen places, the chosen level and the chosen group order"
kind = "definition"
summary = "Facts on the chosen places above p_0 and p_1 and the places above N, the level of elements reducing to 1 at the chosen places, and the order of the product of GL_{rt} over the residue fields at the chosen places, with its size bound."
aliases = ["chosen level", "chosen group order"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.chosenEquiv", "New.Data.card_chosenPlace", "New.Data.v_N_eq_exp_neg_one", "New.Data.intValuation_piN", "New.Data.intValuation_piM", "New.Data.chosenGroupOrder", "New.Data.prod_q_chosenPlace", "New.Data.card_pi_GL_chosenPlace", "New.Data.chosenLevel", "New.Data.isChosen_star_iff", "New.Data.IsChosen.not_star", "New.Data.card_GL_dvd_chosenGroupOrder", "New.Data.isConjApart_chosenPlace", "New.Data.range_chosenPlace", "New.Data.principalLevel_le_chosenLevel", "New.Data.chiMLocal_zpow_ne_one_iff_isChosen", "New.Data.log_chosenGroupOrder_le"]
lean_files = ["src/New/UpperBound/Objects/LiftChains.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] with field \(E\), \(f\) infinite places, level primes \(p_0,p_1\), \(M=p_0p_1\), level \(N=\pi_N\bar\pi_N\), the integer \(\pi_M\), ranks \(r\), \(t=5r\), and let \(C_i\) be the set of [[?lean:New.Data.ChosenPlace|chosen places above \(p_i\)]], \(C=C_0\sqcup C_1\).

**Definition.**

* For a finite index set \(n\), the **chosen level** is the subgroup of \(U(I_n)(\mathbb A_f)\) of the elements of the standard maximal compact subgroup \(K_0\) that reduce to \(1\) at every chosen place.
* The **chosen group order** is \(\Big\lvert\prod_{w\in C}\mathrm{GL}_{rt}(\mathbb F_w)\Big\rvert\).

## Properties

1. \(\lvert C_i\rvert=f\); each chosen place above \(p_i\) has norm \(p_i\); \(\prod_{w\in C}q_w=M^f\). Of a place above \(p_i\) and its conjugate exactly one is chosen; the chosen places are pairwise distinct and none is the conjugate of another.
2. \(N\) is a uniformiser at every place of \(E\) above \(N\); \(\pi_N\) is a uniformiser at each place dividing it; \(\pi_M\) is a uniformiser at each place dividing it.
3. \(\big\lvert\prod_{w\in C}\mathrm{GL}_l(\mathbb F_w)\big\rvert=\prod_{i}\lvert\mathrm{GL}_l(\mathbb F_{p_i})\rvert^{f}\); if \(\lvert n\rvert\le rt\) then \(\big\lvert\prod_{w\in C}\mathrm{GL}_n(\mathbb F_w)\big\rvert\) divides the chosen group order.
4. If \(\pi_M\mid a\) for an integer \(a\) of \(E\), the principal congruence subgroup of level \(a\) is contained in the chosen level.
5. \(\log(\text{chosen group order})\le x^{32}\).
6. For an integer \(e\ne0\) with \(\lvert e\rvert\le 8m\) and a finite place \(w\): the \(e\)-th power of the [[?lean:New.Data.chiMLocal|residue character \(\chi_{M,w}\)]] is nontrivial if and only if \(w\) is chosen.

## Proof

*1, 2.* These come from the arithmetic of primes \(\equiv1\) modulo \(q_1d\), which split completely in \(E\): \(\pi_M\bar\pi_M=p_ic\) with \(c\) prime to \(p_i\) (Lean: `New.Data.exists_piM_mul_star_eq_levelPrime_mul_coprime`), from which the Lean library lemmas `nonempty_infinitePlace_equiv_finPlace`, `star_mem_iff_notMem`, `intValuation_eq_of_mul_star`, `intValuation_natCast_eq_exp_neg_one` give the bijection of the infinite places with \(C_i\), the dichotomy for conjugates, and the uniformiser statements. These library lemmas are cited, not reproved here. Distinctness: the norm \(p_i\) of a chosen place determines \(i\).

*3.* \(\mathbb F_w\cong\mathbb F_{p_i}\) for \(w\in C_i\) and \(\lvert C_i\rvert=f\). For the divisibility, an injection \(n\hookrightarrow\{0,\dots,rt-1\}\) gives injective homomorphisms \(g\mapsto\operatorname{diag}(g,1)\), and the order of a subgroup divides the order of the group.

*4.* An element congruent to \(1\) modulo \(a\) is congruent to \(1\) at every prime dividing \(\pi_M\).

*5.* \(\lvert\mathrm{GL}_l(\mathbb F_q)\rvert\le q^{l^2}\), so the order is at most \(M^{(rt)^2f}\), and \((rt)^2f\log M\le x^{32}\) by the size relations of the data ([[?lean:New.Data.scale_inequalities|scale inequalities]]; in Lean by the automatic comparison of logarithmic bounds).

*6.* If \(w\) is not chosen the character is trivial. If \(w\) is chosen it has order \(q_2\) (Lean: `New.Data.orderOf_chiMLocal`), a multiple of \(q_1d>8m\ge\lvert e\rvert>0\), so \(q_2\nmid e\). \(\square\)

## References

1. Lean: `New.Data.chosenLevel`, `New.Data.chosenGroupOrder`, `New.Data.log_chosenGroupOrder_le`, `New.Data.chiMLocal_zpow_ne_one_iff_isChosen` in `src/New/UpperBound/Objects/LiftChains.lean`.
