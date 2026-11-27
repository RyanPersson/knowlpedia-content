+++
id = "proofs/grh/spanning-unfolding-b/real-gram-discriminant-of-a-term"
title = "The real Gram discriminant of a rational term"
kind = "lemma"
summary = "At an infinite place, the Gram discriminant of the rescaled image of a rational isometry is the absolute value of its discriminant times the square of the product of the squared frame scales."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.gramDiscReal_realFrameGram_ratToInf"]
lean_files = ["src/New/Spanning/Unfolding/Terms.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]], \(\gamma\in G(E)\) and \(v\) an infinite place. Let \(Z_1\) be the matrix of frame products of \((\gamma_\infty)_v\in G_1\), with leading minor \(D^{(1)}_\varrho\) of order \(\varrho\), and let \(\operatorname{disc}_{\mathbb{R}}(Z_1)=\lvert\det Z_1\rvert^2-\lvert D^{(1)}_\varrho\rvert^2\) be its [[?lean:New.RealPlace.gramDiscReal|real Gram discriminant]]. Then, with the [[proofs/grh/spanning-unfolding-b/filling-constants|squared frame scales]] \(\lambda_{v,a}=\kappa_v^{2(\varrho-a)}/N\),
\[
\operatorname{disc}_{\mathbb{R}}(Z_1)=\Bigl(\prod_{a=0}^{\varrho}\lambda_{v,a}\Bigr)^{2}\,\bigl\lvert\Phi_v(\operatorname{disc}(\gamma))\bigr\rvert .
\]

## Proof

By [[proofs/grh/spanning-unfolding-b/frame-products-at-infinity|the formula for minors at infinity]], \(\det Z_1=\bigl(\prod_{a\le\varrho}\lambda_{v,a}\bigr)\Phi_v(D_{\varrho+1})\) and \(D^{(1)}_\varrho=\bigl(\prod_{a<\varrho}\lambda_{v,a}\bigr)\Phi_v(D_\varrho)\). Since \(\lambda_{v,\varrho}=1/N\), the second product is \(N\prod_{a\le\varrho}\lambda_{v,a}\). Hence
\[
\lvert\det Z_1\rvert^2-\lvert D^{(1)}_\varrho\rvert^2=\Bigl(\prod_{a\le\varrho}\lambda_{v,a}\Bigr)^2\Bigl(\lvert\Phi_v(D_{\varrho+1})\rvert^2-N^2\lvert\Phi_v(D_\varrho)\rvert^2\Bigr)=\Bigl(\prod_{a\le\varrho}\lambda_{v,a}\Bigr)^2\Phi_v(\operatorname{disc}(\gamma)),
\]
and \(\Phi_v(\operatorname{disc}(\gamma))=\lvert\Phi_v(\operatorname{disc}(\gamma))\rvert\) by [[proofs/grh/spanning-unfolding-b/term-discriminant-is-totally-positive-or-zero|the positivity of the discriminant]].

## References

1. Lean: `New.Filling.gramDiscReal_realFrameGram_ratToInf` in `src/New/Spanning/Unfolding/Terms.lean`.
