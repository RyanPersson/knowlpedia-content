+++
id = "proofs/grh/onelift-values/hyperplane-sums-annihilate"
title = "Forms annihilated by the hyperplane sums"
kind = "definition"
summary = "A form on V of a descent pair is annihilated by the hyperplane sums if every tensor product over the chosen places of hyperplane sums of rows, not all zero, kills it."
aliases = ["hyperplane sums annihilate"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.HyperplaneSumsAnnihilate", "New.DescentPair.sum_formAction_mulSingle_eq_zero", "New.DescentPair.sum_blockAction_eq_zero"]
lean_files = ["src/New/OneLift/FalseLifts/BottomOfTower.lean"]
+++

Let \(O\) be a [[?lean:New.DescentPair|descent pair]] with chosen places \(w\), residue characters
\(\chi_w\) and space \(\mathcal{F}_V\) of [[?lean:New.DescentPair.FormV|forms on \(V\)]], on which
\(G_M=\prod_{w\ \mathrm{chosen}}\mathrm{GL}_r(k_w)\) acts by the
[[?lean:New.DescentPair.formAction|form action]]. For a row \(\lambda_w\in k_w^{r}\) let
\[
\sigma_w(\lambda_w)=\sum_{s\in H_{\lambda_w}}\chi_w(\det s)^{-1}\,s\ \in\ \mathbb{C}[\mathrm{GL}_r(k_w)]
\]
be the [[?lean:New.hyperplaneSum|hyperplane sum]] over the
[[proofs/grh/onelift-values/hyperplane-group-character-sum|hyperplane group]] \(H_{\lambda_w}\).

The **hyperplane sums annihilate** a form \(y\in\mathcal{F}_V\) if for every family of rows
\((\lambda_w)_{w\ \mathrm{chosen}}\) that is not identically zero,
\[
\Bigl(\bigotimes_{w\ \mathrm{chosen}}\sigma_w(\lambda_w)\Bigr)\cdot y=0 ,
\]
the tensor product being an element of \(\mathbb{C}[G_M]=\bigotimes_w\mathbb{C}[\mathrm{GL}_r(k_w)]\).

## Properties

Suppose the hyperplane sums annihilate \(y\).

1. For a single chosen place \(w\) and a row \(l\ne0\) over \(k_w\),
   \(\sum_{s\in H_l}\chi_w(\det s)^{-1}\,(s\text{ at }w)\cdot y=0\). Indeed, take the row \(l\) at \(w\) and
   the zero row elsewhere; the hyperplane sum of the zero row is \(1\).
2. Suppose moreover \(\chi_w\ne1\) for every twist place \(w\in Q\). Then for every place \(w\in S_O\) and
   every row \(l\ne 0\) over \(k_w\), the [[proofs/grh/onelift-values/triangular-level-action|block action]]
   satisfies \(\sum_{s\in H_l}(s\text{ at }w)\star y=0\). At a chosen place this is (1). At \(w\in Q\) the
   block action is \(\chi_w(\det s)^{-1}y\), and
   [[proofs/grh/onelift-values/hyperplane-group-character-sum|the character sum over \(H_l\) vanishes]].

## Remarks

Good forms satisfy this condition: for \(W\) of rank one it holds for forms in the image of the mean over
\(G_M\) when the \(\chi_w\) are nontrivial at the chosen places
([[proofs/grh/onelift-values/false-lifts-from-a-line|false lifts from a line]]).

## References

1. Lean: `New.DescentPair.HyperplaneSumsAnnihilate`, `New.DescentPair.sum_blockAction_eq_zero` in `src/New/OneLift/FalseLifts/BottomOfTower.lean`.
