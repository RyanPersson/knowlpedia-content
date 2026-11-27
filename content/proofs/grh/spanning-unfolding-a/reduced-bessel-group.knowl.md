+++
id = "proofs/grh/spanning-unfolding-a/reduced-bessel-group"
title = "The structure of the reduced Bessel group"
kind = "theorem"
summary = "The reduction of the Bessel subgroup is the product of the reductions of U and of U(X_0), which meet trivially; it normalises the reduced unipotent group, and its order is |H-bar| times the unipotent order."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.card_reducedImage_besselS", "New.Filling.mem_reducedImage_besselS", "New.Filling.disjoint_reducedImage_besselU_besselH", "New.Filling.reducedImage_besselS_le_normalizer"]
lean_files = ["src/New/Spanning/Unfolding/ReducedGroups.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be [[?lean:New.Filling|filling data]] over a [[?c:CM field|CM field]] \(E\), and let \(\bar{\mathsf U},\bar H,\bar{\mathsf S}\) be the [[?lean:New.Filling.reducedImage|reduced images]] of the Bessel unipotent group \(\mathsf U\), of \(H=U(X_0)\) and of the [[?lean:New.Shape.Form.besselS|Bessel subgroup]] \(\mathsf S=\mathsf UH\) (the head of the source writes \(\bar R\) for \(\bar{\mathsf S}\)). Then:

1. \(\bar{\mathsf S}=\bar{\mathsf U}\,\bar H\): an element \(s\) lies in \(\bar{\mathsf S}\) iff \(s=uh\) with \(u\in\bar{\mathsf U}\), \(h\in\bar H\);
2. \(\bar{\mathsf U}\cap\bar H=\{1\}\);
3. \(\bar{\mathsf S}\) normalises \(\bar{\mathsf U}\);
4. \(\lvert\bar{\mathsf S}\rvert=\lvert\bar H\rvert\cdot M^{f\varrho(2k+2\varrho+1)}\).

## Proof

The key fact, from another area, is: if \(u\in\mathsf U\), \(h\in H\) and \(uh\) is integral and congruent to \(1\) modulo an integral level, then so is \(h\) ([[?lean:New.mem_unitaryLevel_of_besselU_mul|the Levi factor of an element of a unitary level]]).

1. Let \(x\in K\cap\mathsf S\), \(x=uh\) with \(u\in\mathsf U\), \(h\in H\). By the key fact with level \(1\), \(h\) is integral, hence so is \(u=xh^{-1}\), and the reduction of \(x\) is the product of the reductions. The converse is clear.

2. Let \(s\) be the reduction of \(u\in K\cap\mathsf U\) and of \(h\in K\cap H\). Then \(u^{-1}h\) has reduction \(1\), i.e. lies in \(K(M)\), the unitary level \(M\) ([[?lean:New.Filling.principalLevel_eq_unitaryLevel|description of the principal level]]). By the key fact \(h\in K(M)\), so \(s=1\).

3. \(\mathsf S\) normalises \(\mathsf U\) ([[?lean:New.besselS_le_normalizer_besselU|the Bessel subgroup normalises the unipotent group]]), and conjugation of integral elements by integral elements commutes with reduction.

4. By 1 and 2, multiplication \(\bar{\mathsf U}\times\bar H\to\bar{\mathsf S}\) is a bijection, and \(\lvert\bar{\mathsf U}\rvert\) is given by the theorem on the [[proofs/grh/spanning-unfolding-a/reduced-unipotent-group|reduced unipotent group]].

## References

1. Lean: `New.Filling.card_reducedImage_besselS` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
2. Lean: `New.Filling.mem_reducedImage_besselS` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
3. Lean: `New.Filling.disjoint_reducedImage_besselU_besselH` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
4. Lean: `New.Filling.reducedImage_besselS_le_normalizer` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
