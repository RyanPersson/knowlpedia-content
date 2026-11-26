+++
id = "proofs/grh/upper-objects/descent-pair"
title = "Descent pair"
kind = "definition"
summary = "The data of one theta lift from U(W), W of rank r, to a definite group U(V) of larger rank n, and of its descent: level places M and Q, signs and a numbering on W, column numbers, and a character of U(1) with weight and tame part; with its level group, level character and forms on V."
aliases = ["descent pair", "auxiliary pair", "level of a descent pair", "forms on V of a descent pair"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair", "New.LevelPlaces.ChosenGL", "New.firstBlockHom", "New.descentResidueLevel", "New.mem_descentResidueLevel_iff", "New.firstBlockHom_conj_mem_descentResidueLevel", "New.DescentPair.levelGroup", "New.DescentPair.residueLevelChar", "New.DescentPair.levelChar", "New.DescentPair.columnCount", "New.DescentPair.detExp", "New.DescentPair.FormV", "New.DescentPair.chosenGLRep", "New.DescentPair.formAction", "New.DescentPair.rankDiff", "New.DescentPair.charW", "New.DescentPair.charV", "New.DescentPair.pairThetaKernel"]
lean_files = ["src/New/UpperBound/Objects/AuxiliaryPair.lean"]
+++

Let \(E\) be a [[?c:CM field|CM field]] with [[?lean:New.WeilData|Weil data]] (in particular with the character \(\upsilon\) of the Weil data), and let \(r,n\) be finite index sets.

**Definition.** A **descent pair** \(O\) (for \(E,r,n\)) consists of

1. [[?lean:New.LevelPlaces|level places]]: two finite families of split finite places of \(E\), the *chosen places* \(M\) and the *places of the twist* \(Q\) (with residue fields \(k_w\));
2. signs \(s\colon r\to\{\pm1\}\) and a hermitian space \(W\) of rank \(\lvert r\rvert\) with these signs at the infinite places (a [[?lean:New.Space|space]] in the sense of the proof);
3. an injection \(u\colon r\hookrightarrow n\) of index sets and a map \(\nu\colon r\to\mathbb N\), the *numbering*;
4. column numbers \(k^+,k^-\colon\{\text{infinite places of }E\}\times\mathbb N\to\mathbb N\);
5. a [[?lean:New.AutChar|character \(\mu\) of \(U(1)(\mathbb A)\) trivial on rational points]], with a weight \(\tau\mapsto\operatorname{wt}_\tau\in\mathbb Z\) and a tame part \((\psi_w)_w\), \(\psi_w\) a multiplicative character of \(k_w\), such that \(\mu\) [[?lean:New.AutChar.HasWeight|has this weight and tame part]];

subject to: \(\psi_w=1\) for every finite place \(w\) not among the places of \(M\) and \(Q\); and \(\lvert r\rvert<\lvert n\rvert\).

The space \(V\) is the [[?lean:New.stdSpace|standard definite hermitian space]] \(I_n\) of rank \(\lvert n\rvert\). Block \(0\) of \(n\) is the image of \(u\), block \(1\) the rest. Attached to \(O\) are:

* the **residue level** \(\bar K_O\subseteq\prod_{w\in M\sqcup Q}\mathrm{GL}_n(k_w)\): the families \(g\) with \(g_w\,\iota_u=\iota_u\) for \(w\in M\) (\(\iota_u\) the \(n\times r\) inclusion matrix of \(u\); i.e. \(g_w\) fixes the basis vectors indexed by \(u\)) and \(g_w\) in the [[?lean:New.rangeParabolic|parabolic preserving the span of the basis vectors of block 1]] for \(w\in Q\);
* the **level group** \(K_O\): the elements of the standard maximal compact \(K_0\subset U(V)(\mathbb A_f)\) whose reductions at the places of \(M\) and \(Q\) lie in \(\bar K_O\);
* the **level character** \(K_O\to\mathbb C^\times\), \(g\mapsto\prod_{w\in Q}\psi_w^{-1}(\det\bar g_{w,00})\), where \(\bar g_{w,00}\) is the block of the reduction on the indices \(u(r)\) (multiplicative because these reductions are block triangular);
* the weight of forms on \(V\): column numbers \((\tau,i)\mapsto k^+(\tau,i)+k^-(\tau,\lvert n\rvert-i)\) and determinant exponent \(-\sum_{1\le i<\lvert n\rvert}k^-(\tau,i)\);
* the space \(\mathcal F_V(O)\) of **forms on \(V\)**: [[?lean:New.LevelPlaces.LevelForm|algebraic modular forms]] on \(U(V)\) of this weight on which \(K_O\) acts by the level character;
* the **action of \(\prod_{w\in M}\mathrm{GL}_r(k_w)\)** on \(\mathcal F_V(O)\): \(g\) acts by \(\prod_{w\in M}\psi_w(\det g_w)\) times right translation by a lift to \(K_0\) of the family equal to \(\operatorname{diag}(g_w,1)\) at \(M\) and to \(1\) at \(Q\);
* the characters \(\nu_W=\upsilon_{U(1)}^{\,r_-}\) (with \(r_-\) the number of minus signs of \(W\)) and \(\nu_V=\mu\cdot\upsilon^{\lfloor n/2\rfloor}\) (the [[?lean:New.rankTwist|rank twist]] of \(\mu\)), and the [[?lean:New.pairThetaKer|theta kernel]] of the pair \((W,V)\) with these characters;
* the rank difference \(t=\lvert n\rvert-\lvert r\rvert\).

## Properties

Conjugation by \(\operatorname{diag}(s_w,1)_{w\in M}\) (and \(1\) at \(Q\)) maps \(\bar K_O\) into itself and preserves the residue level character; this makes the action of \(\prod_M\mathrm{GL}_r(k_w)\) well defined. *Proof.* With \(d=\operatorname{diag}(t,1)\), \(d\,\iota_u=\iota_u\,t\); so if \(x\iota_u=\iota_u\) then \(d^{-1}xd\,\iota_u=d^{-1}x\iota_ut=d^{-1}\iota_ut=\iota_u\). At \(Q\) nothing changes, and the character reads only the components at \(Q\). \(\square\)

## Remarks

Other files call a descent pair an *auxiliary pair*. The structure itself asserts nothing about the relation between \(k^\pm\), the numbering and the signs; that is the condition [[proofs/grh/upper-objects/descent-pair-fitting-parameters|fitting parameters]].

## References

1. Lean: `New.DescentPair`, `New.descentResidueLevel`, `New.DescentPair.FormV`, `New.DescentPair.formAction` in `src/New/UpperBound/Objects/AuxiliaryPair.lean`.
