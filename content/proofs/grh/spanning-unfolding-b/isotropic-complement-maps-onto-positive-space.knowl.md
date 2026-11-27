+++
id = "proofs/grh/spanning-unfolding-b/isotropic-complement-maps-onto-positive-space"
title = "The isotropic complement modulo the common isotropic space is the positive space"
kind = "theorem"
summary = "The map sending a vector orthogonal to A and its image to its X0-part plus the z-coordinate of its preimage is surjective onto the positive space with kernel the common isotropic space."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.ker_perpToPositive_and_surjective", "New.Filling.perpToPositive", "New.Filling.perpToPositive_apply", "New.Filling.commonIsotropic_le_isotropicPerp", "New.Filling.ker_perpToPositive", "New.Filling.perpToPositive_surjective"]
lean_files = ["src/New/Spanning/Unfolding/Link.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\), \(\gamma\in G(E)\), \(A=\langle e_0,\dots,e_{\varrho-1}\rangle\), and \(I_\gamma=A\cap\gamma A\), \((A+\gamma A)^\perp\) the [[proofs/grh/spanning-unfolding-b/positive-space-and-link-maps|isotropic spaces of \(\gamma\)]]. Consider the linear map
\[
\Pi_\gamma\colon(A+\gamma A)^\perp\to P=X_0\perp Ez^+,\qquad y\mapsto y_{X_0}+(\gamma^{-1}y)_z\,z^+ .
\]
Then \(I_\gamma\subset(A+\gamma A)^\perp\), \(\ker\Pi_\gamma=I_\gamma\), and \(\Pi_\gamma\) is surjective. So \(\Pi_\gamma\) induces an isomorphism \((A+\gamma A)^\perp/(A\cap\gamma A)\cong P\).

## Proof

\(\Pi_\gamma(y)=\operatorname{src}(p_y)\) for the pair \(p_y=(y_{\mathrm{mid}},(\gamma^{-1}y)_{\mathrm{mid}})\) of the link. A vector \(y\) lies in \(I_\gamma\) if and only if \(y\) and \(\gamma^{-1}y\) lie in \(A\), i.e. their middle and \(e^*\)-blocks vanish; equivalently \(y\in(A+\gamma A)^\perp\) (vanishing \(e^*\)-blocks, by [[proofs/grh/spanning-unfolding-b/link-in-coordinates|the link in coordinates]]) and \(p_y=0\). This gives the inclusion. By [[proofs/grh/spanning-unfolding-b/rank-of-the-link|the lemma on the link]], \(\operatorname{src}(p_y)=0\) if and only if \(p_y=0\); so \(\ker\Pi_\gamma=I_\gamma\). Surjectivity: \(\operatorname{src}\) maps the link onto \(P\), and every element of the link is \(p_y\) for some \(y\in(A+\gamma A)^\perp\).

## References

1. Lean: `New.Filling.ker_perpToPositive_and_surjective`, `New.Filling.perpToPositive` in `src/New/Spanning/Unfolding/Link.lean`.
