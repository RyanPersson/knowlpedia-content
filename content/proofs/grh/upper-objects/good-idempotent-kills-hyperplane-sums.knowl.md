+++
id = "proofs/grh/upper-objects/good-idempotent-kills-hyperplane-sums"
title = "The good idempotent kills hyperplane sums"
kind = "lemma"
summary = "A pure tensor in the group algebra of the chosen group one of whose factors is a hyperplane sum for a character of order dividing q_2 is annihilated by e_0."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.hyperplaneSum_mul_e₀"]
lean_files = ["src/New/UpperBound/Objects/LabelsAndIndexTypes.lean"]
proof_status = "outline"
+++

**Lemma.** Let \(D\) be admissible data, \(\bar G=\prod_{w\in C}\mathrm{GL}_{\mathcal R}(\mathbb F_w)\) the [[proofs/grh/upper-objects/good-idempotent|group of the chosen places]] and \(e_0\) the good idempotent. Let \(x=(x_w)_{w\in C}\) with \(x_w\in\mathbb C[\mathrm{GL}_{\mathcal R}(\mathbb F_w)]\). Suppose that at one place \(v\in C\)
\[
x_v=\sum_{h}\chi(\det h)^{-1}\,h,
\]
the [[?lean:New.hyperplaneSum|hyperplane sum]] over the invertible matrices of the form \(h=1+u\,l^{\mathsf T}\) (\(u\in\mathbb F_v^{\mathcal R}\)), where \(l\in\mathbb F_v^{\mathcal R}\) is nonzero and \(\chi\) is a multiplicative character of \(\mathbb F_v\) with \(\chi^{q_2}=1\). Then
\[
\Big(\bigotimes_{w\in C}x_w\Big)\cdot e_0=0\quad\text{in }\mathbb C[\bar G].
\]

## Proof

By definition \(e_0=\sum_ce_c\) over the good families, and \(e_c=\bigotimes_we_{c_w}\). The product of pure tensors is the pure tensor of the products, so it suffices to show \(x_v\,e_{c_v}=0\) for every good family \(c\). Under the isomorphism between the multiplicative characters of \(\mathbb F_v\) and \(\mathbb F_v^\times\) ([[?lean:New.charName|the name of a character]]), \(\chi\) corresponds to a unit \(a\) with \(a^{q_2}=1\). Since \(c_v\) is allowed, \(c_v(a)\ne0\). The Lean lemma `New.hyperplaneSum_mul_labelIdem` (in the theory of Green's characters, another area) states that the hyperplane sum of \(\chi\) and \(l\ne0\) times the label idempotent \(e_c\) vanishes whenever the name of \(\chi\) is not a root of \(c\); this step is only cited here. \(\square\)

## References

1. Lean: `New.Data.hyperplaneSum_mul_e₀` in `src/New/UpperBound/Objects/LabelsAndIndexTypes.lean`; it uses `New.hyperplaneSum_mul_labelIdem` and `New.piTensorElem_mul_eq_zero`.
