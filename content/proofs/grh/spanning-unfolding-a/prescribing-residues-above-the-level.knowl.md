+++
id = "proofs/grh/spanning-unfolding-a/prescribing-residues-above-the-level"
title = "Prescribing residues at the places above M"
kind = "lemma"
summary = "Residues may be prescribed simultaneously at the chosen places and at their conjugates by one integral finite adele."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.exists_reduceAboveM_eq", "New.Filling.exists_reduceAt_eq_and_reduceAt_star_eq", "New.Filling.exists_lift_reduceAboveM_eq", "New.Filling.reduceAboveM_star"]
lean_files = ["src/New/Spanning/Unfolding/Climbing.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be [[?lean:New.Filling|filling data]] over a [[?c:CM field|CM field]] \(E\). The *places above \(M\)* are the pairs \(p=(w,\varepsilon)\) of a [[?lean:New.Filling.chosenPlaces|chosen place]] \(w\) (above \(p_0\) or \(p_1\)) and a sign \(\varepsilon\in\{\text{false},\text{true}\}\), standing for \(w\) itself or for its complex conjugate \(\bar w\); the [[?lean:New.Filling.reduceAboveM|reduction at \(p\)]] is the ring homomorphism \(\operatorname{red}_p:\widehat{\mathcal O}\to k_w\) to the [[algebra-commutative/residue-field|residue field]] at \(w\) given by \(y\mapsto y\bmod w\) if \(\varepsilon\) is false and \(y\mapsto\bar y\bmod w\) if \(\varepsilon\) is true. Then:

1. for every family \((t_p)_p\) with \(t_p\in k_w\) there is \(y\in\widehat{\mathcal O}\) with \(\operatorname{red}_p(y)=t_p\) for all places \(p\) above \(M\);
2. \(\operatorname{red}_{(w,\varepsilon)}(\bar y)=\operatorname{red}_{(w,\neg\varepsilon)}(y)\);
3. for every place \(p=(w,\varepsilon)\) above \(M\) there is a map \(\ell:k_w\to\widehat{\mathcal O}\) with \(\ell(0)=0\), \(\operatorname{red}_p(\ell(t))=t\), and \(\operatorname{red}_{p'}(\ell(t))=0\) for every place \(p'\ne p\) above \(M\).

## Proof

1. It suffices to find, for residues \((u_w)\) at the chosen places, an \(a\in\widehat{\mathcal O}\) with \(a\equiv u_w\) and \(\bar a\equiv0\) modulo every chosen \(w\); then \(y=a+\bar b\), with \(a\) for the residues \(t_{(w,\mathrm{false})}\) and \(b\) for \(t_{(w,\mathrm{true})}\), works. Let \(e_w\in\widehat{\mathcal O}\) be the [[?c:Idempotent element|idempotent]] that is \(1\) at \(w\) and \(0\) at all other finite places, and \(\tilde u_w\in\mathcal O_E\) a lift of \(u_w\). Put \(a=\sum_w\tilde u_we_w\). The chosen places are distinct, so \(a\equiv u_w\) at \(w\). The conjugate \(\bar e_w\) is the idempotent of \(\bar w\), and the conjugate of a chosen place is never chosen (part of the data), so \(\bar a\equiv0\) at every chosen place.

2. Immediate from the definition.

3. With \(y(\cdot)\) a choice as in 1, put \(\ell(t)=y(t\ \text{at }p,\ 0\ \text{elsewhere})-y(0)\).

## References

1. Lean: `New.Filling.exists_reduceAboveM_eq` in `src/New/Spanning/Unfolding/Climbing.lean`.
2. Lean: `New.Filling.exists_reduceAt_eq_and_reduceAt_star_eq` in `src/New/Spanning/Unfolding/Climbing.lean`.
3. Lean: `New.Filling.exists_lift_reduceAboveM_eq` in `src/New/Spanning/Unfolding/Climbing.lean`.
4. Lean: `New.Filling.reduceAboveM_star` in `src/New/Spanning/Unfolding/Climbing.lean`.
