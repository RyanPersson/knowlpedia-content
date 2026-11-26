+++
id = "proofs/grh/derivatives-divisibility/critical-pair"
title = "Pairs of a character and a critical point"
kind = "definition"
summary = "A pair consists of an integer z between 1 and t and a character of U(1) of weight -c with z at most c at most 4b at every infinite place and tame part supported on the chosen places; there are finitely many pairs."
aliases = ["pair", "critical pair", "finiteness of pairs"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.CriticalPair", "New.Data.finite_criticalPair"]
lean_files = ["src/New/Derivatives/Field/ChosenPlaces.lean"]
proof_status = "full"
+++

**Definition (pair).** Let \(D\) be [[?lean:New.Data|admissible data]] with field \(E\), rank parameter \(t=5r\) and real scale \(b\). A **pair** consists of

* an [[?lean:New.AutChar|automorphic character]] \(\nu\) of \(U(1)\) of \(E\),
* a function \(c\colon\Phi\to\mathbb{N}\) on the infinite places and a family \(\psi=(\psi_w)\) of multiplicative characters of the residue fields at the finite places, such that \(\nu\) has [[?lean:New.AutChar.HasWeight|weight]] \(-c\) and tame part \(\psi\), and \(\psi_w=1\) at every place \(w\) that is not [[proofs/grh/derivatives-divisibility/chosen-places-and-characters|chosen]],
* an integer \(z\) with \(1\le z\le t\),

such that \(z\le c(v)\le4b\) for every \(v\in\Phi\).

**Theorem (finiteness).** The set of pairs is finite.

## Proof

The data \((c,z,\psi|_{\text{chosen places}})\) of a pair range over a finite set: \(c\) takes values in \([0,\lfloor4b\rfloor]\) on the finite set \(\Phi\), \(z\in[1,t]\), and there are finitely many chosen places, each with a finite residue field. These data determine \(\psi\), which is trivial elsewhere. For fixed weight and tame part there are [[?lean:New.AutChar.finite_setOf_hasWeight|finitely many characters]] \(\nu\); and a pair is determined by its data and its character. \(\blacksquare\)

## References

1. Lean: `New.Data.CriticalPair`, `New.Data.finite_criticalPair` in `src/New/Derivatives/Field/ChosenPlaces.lean`.
