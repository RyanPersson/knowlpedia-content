+++
id = "proofs/grh/upper-objects/centre-system-parameter-has-gap"
title = "Parameters of a separated centre system have a gap"
kind = "lemma"
summary = "In a centre system separated with bound h, the parameter lambda_B has distinct entries of the right parity, and entries at coordinates of opposite signs are at least h apart."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CentreSystem.IsParam.hasGap", "New.CentreSystem.IsSeparated.card_entries", "New.CentreSystem.IsSeparated.disjoint_entries_block", "New.CentreSystem.IsSeparated.rank_mod_two", "New.CentreSystem.IsSeparated.odd_add_card_of_mem_entries", "New.CentreSystem.IsParam.exists_not_countsFor_iff_of_sign_ne", "New.CentreSystem.IsSeparated.add_length_le_abs_sub_two_mul_centre"]
lean_files = ["src/New/UpperBound/Objects/InsertBlock.lean"]
proof_status = "full"
+++

**Lemma.** Let \(X\) be a [[proofs/grh/upper-objects/centre-system|centre system]] separated with bound \(h\), let \(B\subseteq C\), and let \(\lambda\) be the parameter \(\lambda_B\) with common sign \(\sigma\) on a space with coordinate set \(n\) and signs \(s\). Then \(\lambda\) [[?lean:New.HCParam.HasGap|has gap \(h\)]]:

1. the entries \(\lambda_x\) are pairwise distinct;
2. \(\lambda_x\in\tfrac{\lvert n\rvert-1}2+\mathbb Z\) for all \(x\);
3. if \(s_x\ne s_{x'}\) then \(\lvert\lambda_x-\lambda_{x'}\rvert\ge h\).

## Proof

*Distance.* If \(c\in C\setminus B\) and \(y\in\lambda^+_B\), then \(\lvert y-c\rvert\ge(h+l_c)/2\): for \(y\) in the stem this is condition 3 of separation, for \(y\) in a block of \(c'\in B\) (so \(c'\ne c\)) condition 4. In particular \(y\notin c+[l_c]\), whose entries are at distance at most \((l_c-1)/2\) from \(c\).

*1.* By induction on \(B\) the stem and the blocks of \(B\) are pairwise disjoint, so \(\lvert\lambda^+_B\rvert=n_B=\lvert n\rvert\). The map \(x\mapsto\lambda_x+\delta_B\) from \(n\) onto \(\lambda^+_B\) is therefore injective.

*2.* Every entry of \(\lambda^+_B\) lies in \(\tfrac{\lvert S\rvert-1}2+\mathbb Z\): for the stem this is condition 2, and for a block \(c+[l_c]\) it follows from \(l_c\equiv\lvert S\rvert\) mod 2. By induction on \(B\), \(n_B\equiv\lvert S\rvert-2\delta_B\pmod2\). Hence \(\lambda_x=y-\delta_B\in\tfrac{n_B-1}{2}+\mathbb Z\).

*3.* If \(s_x\ne s_{x'}\), the signs \(\operatorname{sgn}_B\) of \(y=\lambda_x+\delta_B\) and \(y'=\lambda_{x'}+\delta_B\) differ, so some centre \(c\in C\setminus B\) counts for exactly one of \(y,y'\). Then \(y\) and \(y'\) lie on opposite sides of \(c\) (weakly; neither equals \(c\) when \(h+l_c>0\), and the estimate is trivial otherwise), and each is at distance at least \((h+l_c)/2\) from \(c\). So \(\lvert y-y'\rvert\ge h+l_c\ge h\). \(\square\)

## Remarks

The proof gives the stronger bound \(h+l_c\). The Lean structure `New.HCParam.HasGap` (defined in another area) is stated for the doubled entries \(2\lambda\); its head comment describes the gap condition as: entries of \(\lambda\) at coordinates of opposite signs are at least \(h\) apart.

## References

1. Lean: `New.CentreSystem.IsParam.hasGap` in `src/New/UpperBound/Objects/InsertBlock.lean`.
