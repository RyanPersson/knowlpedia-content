+++
id = "proofs/grh/upper-objects/inserting-a-block-satisfies-the-block-rule"
title = "Inserting a block into a parameter satisfies the block rule"
kind = "theorem"
summary = "In a separated centre system, the parameters lambda_B and lambda_{B+c} satisfy the block rule of the theta correspondence for a down centre c, and their negatives do for an up centre."
aliases = ["insertion of a block"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CentreSystem.IsParam.isBlockRule_insert_of_down", "New.CentreSystem.IsParam.isBlockRule_neg_insert_of_up", "New.CentreSystem.IsParam.image_eq_union_and_sign_ne_iff", "New.CentreSystem.IsSeparated.lowering_eq_rank_emod_two", "New.CentreSystem.sign_eq_ite_sign_insert"]
lean_files = ["src/New/UpperBound/Objects/InsertBlock.lean"]
proof_status = "outline"
+++

Let \(X\) be a [[proofs/grh/upper-objects/centre-system|centre system]] separated with bound \(h\), \(B\subseteq C\), \(c\in C\setminus B\) and \(B'=B\cup\{c\}\). Let \(\lambda\) be the parameter \(\lambda_B\) on a space of rank \(n\) with signs \(s\), and \(\lambda'\) the parameter \(\lambda_{B'}\) on a space of rank \(n'\) with signs \(s'\), both with the same common sign \(\sigma\). Assume \(h\ge500(n+n')^3\).

**Theorem.**

1. If \(c\) is **down**, then \((\lambda,\lambda')\) satisfy the [[?lean:New.IsBlockRule|block rule]] with \(\gamma=c+\lfloor n/2\rfloor\) and \(\gamma'=c+\lfloor n'/2\rfloor\).
2. If \(c\) is **up**, then \((-\lambda,-\lambda')\) satisfy the block rule with \(\gamma=-c+\lceil n/2\rceil\) and \(\gamma'=-c+\lceil n'/2\rceil\).

Here the block rule for \((\gamma,\gamma',\lambda,\lambda')\) says: both parameters have gap \(500(n+n')^3\); after shifting \(\lambda\) by \(n'/2-\gamma'\) and \(\lambda'\) by \(n/2-\gamma\), the entries of the longer one are those of the shorter one together with the block \([\lvert n'-n\rvert]\) centred at \(0\); and two coordinates carrying a common shifted entry have equal signs if the entry is positive and opposite signs if it is negative.

## Proof

*Key computation.* We have \(n\le n'=n+l_c\). We claim:

(a) \(\{\lambda'_r+\tfrac12(n\bmod2)\}=\{\lambda_x+\tfrac12(n'\bmod2)\}\cup(c+[n'-n])\);

(b) if \(\lambda_x+\tfrac12(n'\bmod 2)=\lambda'_r+\tfrac12(n\bmod2)=:y\), then \(s_x\ne s'_r\) if and only if \(c\) counts for \(y\).

Indeed, from \(n_B\equiv\lvert S\rvert-2\delta_B\) (see the [[proofs/grh/upper-objects/centre-system-parameter-has-gap|gap lemma]]), from \(l_c\equiv\lvert S\rvert\) and from the definition of the lowering one checks \(2\delta_B=n'\bmod2\) and \(2\delta_{B'}=n\bmod2\). So the two sets in (a) are \(\lambda^+_{B'}\) and \(\lambda^+_B\), and \(\lambda^+_{B'}=\lambda^+_B\cup(c+[l_c])\). For (b): \(C\setminus B=(C\setminus B')\cup\{c\}\), so \(\operatorname{sgn}_B(y)=-\operatorname{sgn}_{B'}(y)\) if \(c\) counts for \(y\) and \(\operatorname{sgn}_B(y)=\operatorname{sgn}_{B'}(y)\) otherwise; multiply by the common sign \(\sigma\).

*1.* By the gap lemma, \(\lambda\) and \(\lambda'\) have gap \(h\ge500(n+n')^3\). For a down centre, \(c\) counts for \(y\) iff \(y<c\). By the Lean theorem `New.isBlockRule_iff_of_character` (another area; an unwinding of the definition of the block rule for \(n\le n'\), \(\gamma=e+\lfloor n/2\rfloor\), \(\gamma'=e+\lfloor n'/2\rfloor\)), the block rule is equivalent to: both gaps, (a) with \(e=c\), and "\(s_x\ne s'_r\) iff the common entry is below \(e\)". This step is cited, not reproved here.

*2.* Negating a parameter preserves the gap. Negating (a) gives \(\{-\lambda'_r-\tfrac12(n\bmod2)\}=\{-\lambda_x-\tfrac12(n'\bmod2)\}\cup(-c+[n'-n])\), and for an up centre \(c\) counts for \(y\) iff \(y>c\) iff \(-y<-c\). By the Lean theorem `New.isBlockRule_iff_of_character_conj` (the analogous unwinding for \(\gamma=e+\lceil n/2\rceil\), \(\gamma'=e+\lceil n'/2\rceil\), with \(e=-c\)) this is the block rule for \((-\lambda,-\lambda')\). \(\square\)

## Remarks

The two cases correspond to the two characters used in a theta lift (weights \(e\) minus, resp. plus, the fractional part of half the rank). Only the equivalences `isBlockRule_iff_of_character(_conj)` are taken from the Lean library without proof here; everything else is complete.

## References

1. Lean: `New.CentreSystem.IsParam.isBlockRule_insert_of_down`, `New.CentreSystem.IsParam.isBlockRule_neg_insert_of_up` in `src/New/UpperBound/Objects/InsertBlock.lean`; `New.IsBlockRule`, `New.isBlockRule_iff_of_character` in `src/Lib/DiscreteSeries/Theta/BlockRule.lean`.
