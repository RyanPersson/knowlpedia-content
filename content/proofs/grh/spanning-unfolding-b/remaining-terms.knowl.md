+++
id = "proofs/grh/spanning-unfolding-b/remaining-terms"
title = "Remaining terms"
kind = "definition"
summary = "The rational isometries with nonzero discriminant, together with those of discriminant zero at which the characters agree and which do not preserve the isotropic span A."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.remainingTerms", "New.Filling.mem_remainingTerms_iff"]
lean_files = ["src/New/Spanning/Unfolding/TermStructure.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\) and \(A=\langle e_0,\dots,e_{\varrho-1}\rangle\). The set of **remaining terms** is
\[
\Gamma^*=\bigl\{\gamma\in G(E)\ :\ \operatorname{disc}(\gamma)\ne0,\ \text{or}\ \bigl(\text{the characters agree at }\gamma,\ \operatorname{disc}(\gamma)=0\ \text{and}\ A\ne\gamma A\bigr)\bigr\},
\]
where \(\operatorname{disc}\) is the [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|discriminant]] and agreement of characters is [[proofs/grh/spanning-unfolding-b/characters-agree|this condition]].

## Remarks

These are the terms left for the estimate of the second moment, after the terms at which the characters do not agree (which contribute zero, see [[?lean:New.Filling.amplitudeSum_eq_zero_of_not_charsAgree|vanishing of disagreeing terms]]) and the terms with \(A=\gamma A\) have been treated separately.

## References

1. Lean: `New.Filling.remainingTerms` in `src/New/Spanning/Unfolding/TermStructure.lean`.
