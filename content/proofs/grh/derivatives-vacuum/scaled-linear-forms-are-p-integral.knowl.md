+++
id = "proofs/grh/derivatives-vacuum/scaled-linear-forms-are-p-integral"
title = "Scaled linear forms of vectors integral above p are p-integral"
kind = "lemma"
summary = "If the finite image of a vector y of E^n is integral at the places above p, then the period factor times each coefficient of the linear form of y is integral at the p-adic place."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.norm_periodFactor_mul_daggerForms_le_one", "New.norm_adeleExtension_le_one_iff"]
lean_files = ["src/New/Derivatives/Vacuum/Scale.lean"]
proof_status = "full"
+++

Let \(P\) be [[?lean:New.Parameters|parameters]], \(s\in\mathbb{N}\), \(E=K(\zeta)\), \(p\) a prime, \(\iota_p\) a \(p\)-adic place of \(\mathbb{C}\), and \(\varpi\) the [[proofs/grh/derivatives-vacuum/jet-scale|period factor]]. For \(y\in E^n\) the coefficients of the linear form \(z\mapsto y^\dagger z\), read in \(\mathbb{C}_p\), are \(y^\dagger_{(v,i)}=\iota_p\bigl(\overline{\Phi_v(y_i)}\bigr)\) for an infinite place \(v\) and a coordinate \(i\) ([[?lean:New.daggerForms|dagger forms]]).

**Lemma.** If every coordinate of \(\alpha^{-1}y\) is integral at all places of \(E\) above \(p\) (that is, \(\alpha^{-1}y\) is [[proofs/grh/derivatives-vacuum/standard-data|integral after \(1\) above \(p\)]]), then \(\lvert\iota_p(\varpi)\,y^\dagger_{(v,i)}\rvert_p\le1\) for all \((v,i)\).

## Proof

Let \(\varphi_v(x)=\iota_p(\overline{\Phi_v(x)})\) be the weight embedding of \(E\) into \(\mathbb{C}_p\); the prime of \(E\) it induces lies above \(p\). For any embedding \(\sigma\) of \(E\) into a \(p\)-adic field, \(\lvert\widehat\sigma(x)\rvert\le1\) for a finite adele \(x\) iff the component of \(x\) at the place of \(\sigma\) is integral (by definition \(\widehat\sigma\) is that component followed by the isometric extension of \(\sigma\)). So \(\lvert\widehat\varphi_v(\alpha^{-1}y_i)\rvert_p\le1\), that is \(\lvert\widehat\varphi_v(\alpha)\rvert_p^{-1}\lvert\varphi_v(y_i)\rvert_p\le1\). By [[proofs/grh/derivatives-vacuum/p-adic-size-of-period-factor|the size of the period factor]], \(\lvert\iota_p\varpi\rvert_p=\lvert\widehat\varphi_v(\alpha)\rvert_p^{-1}\), and \(y^\dagger_{(v,i)}=\varphi_v(y_i)\).

## References

1. Lean: `New.Parameters.norm_periodFactor_mul_daggerForms_le_one`, `New.norm_adeleExtension_le_one_iff` in `src/New/Derivatives/Vacuum/Scale.lean`.
