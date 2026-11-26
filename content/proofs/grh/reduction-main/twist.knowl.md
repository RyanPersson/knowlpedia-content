+++
id = "proofs/grh/reduction-main/twist"
title = "Tame characters and twists"
kind = "definition"
summary = "An automorphic character of U(1) of weight 0 whose tame part is supported on a finite set Q of places prime to MN and disjoint from its conjugate; a twist if the tame part is nontrivial at every place of Q."
aliases = ["TameChar", "Twist", "tame character", "modulus of a twist", "normQ"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.TameChar", "New.Data.TameChar.normQ", "New.Data.Twist", "New.Data.TameChar.one", "New.Data.TameChar.pow", "New.Data.Twist.toAutChar_one", "New.Data.Twist.Q_one"]
lean_files = ["src/New/Reduction/Data/LevelAndTwists.lean", "src/New/Determinant/Twist/FitTwists.lean"]
+++

Let \(D\) be [[proofs/grh/reduction-main/data|data]] with CM field \(E\), principal level \(M=p_0p_1\) and level \(N\). Recall that an [[?lean:New.AutChar|automorphic character \(\mu\) of \(\mathrm U(1)(\mathbb A)\)]] (for \(E\) over its maximal real subfield) *has weight \(e\) and tame part \(\psi\)* ([[?lean:New.AutChar.HasWeight|weight and tame part]]), for integers \(e(v)\) at the infinite places \(v\) and characters \(\psi_w\) of the residue fields \(k_w^\times\) at the finite places \(w\) of \(E\), if almost all \(\psi_w\) are trivial and \(\mu(u)=\prod_vu_v^{e(v)}\prod_w\psi_w(u\bmod w)\) whenever \(u\) has integral finite part.

A **tame character** \(\vartheta\) (for \(D\)) consists of

1. an automorphic character of \(\mathrm U(1)(\mathbb A)\), also written \(\vartheta\);
2. a finite set \(Q=Q(\vartheta)\) of finite places of \(E\), its **modulus**;
3. a family \(\psi=(\psi_w)_w\) of characters of the residue fields, its **tame part**;

such that \(\vartheta\) has weight \(0\) and tame part \(\psi\); \(\psi_w=1\) for \(w\notin Q\); \(\bar w\notin Q\) for every \(w\in Q\) (\(Q\) is disjoint from its complex conjugate); and \(\gcd\bigl(MN,\mathrm{Nm}\,Q\bigr)=1\), where \(\mathrm{Nm}\,Q:=\prod_{w\in Q}\#k_w\).

A **twist** is a tame character with \(\psi_w\ne1\) for every \(w\in Q\). The **trivial twist** \(1\) has trivial character, \(Q=\emptyset\) and trivial tame part. For \(n\ge0\) the **power** \(\vartheta^n\) of a tame character has character \(\vartheta^n\), the same \(Q\), and tame part \(\psi^n\); it is again a tame character.

## References

1. Lean: `New.Data.TameChar`, `New.Data.TameChar.normQ`, `New.Data.Twist`, `New.Data.TameChar.pow` in `src/New/Reduction/Data/LevelAndTwists.lean`; `New.Data.Twist.toAutChar_one`, `New.Data.Twist.Q_one` in `src/New/Determinant/Twist/FitTwists.lean`.
