+++
id = "proofs/grh/onelift-values/hyperplane-group-character-sum"
title = "The hyperplane group of a row and its character sum"
kind = "lemma"
summary = "Over a finite field, the invertible matrices 1 + v l for a fixed nonzero row l form a group on which a nontrivial character of the determinant sums to zero."
aliases = ["hyperplane group"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.hyperplaneGroup", "New.sum_inv_det_hyperplaneGroup_eq_zero", "New.hyperplaneSum_zero", "New.asAlgebraHom_hyperplaneSum", "New.coeff_hyperplaneSum_eq_ite"]
lean_files = ["src/New/OneLift/FalseLifts/BottomOfTower.lean"]
proof_status = "full"
+++

Let \(k\) be a finite field, \(R\) a finite index set and \(l\in k^{R}\) a row vector. The **hyperplane
group** of \(l\) is
\[
H_l=\{\,s\in\mathrm{GL}_R(k) : s=1+v\,l \text{ for some column } v\in k^{R}\,\}.
\]
It is a subgroup of \(\mathrm{GL}_R(k)\): \((1+vl)(1+v'l)=1+(v+sv')l\) with \(s=1+vl\), and
\(s^{-1}=1-(s^{-1}v)l\).

**Lemma.** Let \(\chi\colon k^\times\to\mathbb{C}^\times\) be a nontrivial
[[?c:multiplicative character of a finite field|multiplicative character]] (extended by \(\chi(0)=0\)) and
\(l\ne0\). Then
\[
\sum_{s\in H_l}\chi(\det s)^{-1}=0 .
\]
Consequently the [[?lean:New.hyperplaneSum|hyperplane sum]]
\(\sum_{s\in H_l}\chi(\det s)^{-1}\,s\) in the [[algebra-representation-theory/group-algebra|group algebra]]
\(\mathbb{C}[\mathrm{GL}_R(k)]\) acts in any representation \(\sigma\) by
\(y\mapsto\sum_{s\in H_l}\chi(\det s)^{-1}\sigma(s)y\); for \(l=0\) the group \(H_0\) is trivial and the
hyperplane sum is \(1\).

## Proof

The map \(f\colon H_l\to\mathbb{C}^\times\), \(s\mapsto\chi^{-1}(\det s)\), is a group homomorphism, and the
sum of a nontrivial homomorphism from a finite group to \(\mathbb{C}^\times\) is zero. So it suffices to
show \(f\ne1\). Since \(\chi\ne1\) there is \(\tau\in k^\times\) with \(\chi^{-1}(\tau)\ne1\). Pick \(b\)
with \(l_b\ne0\) and let \(v\) be the column with entry \((\tau-1)/l_b\) at \(b\) and zero elsewhere. By the
matrix determinant lemma \(\det(1+vl)=1+l\,v=\tau\ne0\), so \(s=1+vl\in H_l\) and \(f(s)=\chi^{-1}(\tau)\ne1\).

The two remaining statements are the definition of the hyperplane sum (whose coefficient at \(s\) is
\(\chi(\det s)^{-1}\) for \(s\in H_l\) and \(0\) otherwise) read in a representation, and the fact that
\(1+v\cdot 0=1\). \(\blacksquare\)

## References

1. Lean: `New.hyperplaneGroup`, `New.sum_inv_det_hyperplaneGroup_eq_zero` in `src/New/OneLift/FalseLifts/BottomOfTower.lean`; the hyperplane sum is `New.hyperplaneSum` in `src/Lib/LocalGL/Green/TauFunctions.lean`.
