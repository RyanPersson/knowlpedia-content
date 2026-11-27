+++
id = "proofs/grh/spanning-unfolding-b/bessel-translate"
title = "The twisted translation operators of the reduced Bessel group"
kind = "definition"
summary = "The operator on the source space whose blocks are the conjugates of the amplitude sums of the terms in the Bessel subgroup divided by the unipotent covolume."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.besselTranslate"]
lean_files = ["src/New/Spanning/Unfolding/Moments.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] and consider the *source* \(\mathcal{X}=\mathbb{C}^{\mathcal{C}\times I}\), the Euclidean space with orthonormal basis \(e_{(c,i)}\) indexed by a [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|class]] \(c\) and a Bessel coordinate \(i\); its dimension is the [[proofs/grh/spanning-unfolding-b/filling-constants|source dimension]] \(\dim_S\). For \(s\in\bar G\) the operator \(r_\psi(s)\colon\mathcal{X}\to\mathcal{X}\) is the linear map with matrix
\[
r_\psi(s)_{(c,i),(c',j)}=\overline{A_{\mathsf{S}}(c,s,c')_{(i,j)}}\big/\nu ,
\]
where \(A_{\mathsf{S}}\) is the [[proofs/grh/spanning-unfolding-b/filling-amplitude|amplitude sum]], for the full Bessel function, of the rational elements of the [[?lean:New.Shape.Form.besselS|Bessel subgroup]] \(\mathsf{S}\), and \(\nu\) is the unipotent covolume.

## Remarks

By [[proofs/grh/spanning-unfolding-b/bessel-translate-is-a-unitary-representation|the theorem on these operators]], \(r_\psi\) vanishes off the reduced Bessel group \(\bar R_0\) and is a unitary representation of \(\bar R_0\): translation by \(s\), twisted by the unipotent character and the representations of the Bessel systems.

## References

1. Lean: `New.Filling.besselTranslate` in `src/New/Spanning/Unfolding/Moments.lean`.
