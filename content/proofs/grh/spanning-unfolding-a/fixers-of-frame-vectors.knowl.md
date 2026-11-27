+++
id = "proofs/grh/spanning-unfolding-a/fixers-of-frame-vectors"
title = "Fixers of frame vectors in the residue group"
kind = "definition"
summary = "The subgroup of the residue group fixing prescribed nonzero vectors of the span of the frame modulo chosen places or their conjugates; it contains the reduction of U(X_0)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.vectorFixer", "New.Filling.fixer", "New.Filling.FrameVector", "New.Filling.mem_vectorFixer", "New.Filling.mem_vectorFixer_false", "New.Filling.mem_vectorFixer_true", "New.Filling.reducedImage_besselH_le_vectorFixer", "New.Filling.reducedImage_besselH_le_fixer", "New.Filling.mem_fixer", "New.Filling.mem_fixer_insert", "New.Filling.meetsAt_of_mem_vectorFixer"]
lean_files = ["src/New/Spanning/Unfolding/Climbing.lean"]
+++

Let \(S\) be [[?lean:New.Filling|filling data]] over a [[?c:CM field|CM field]] \(E\), \(w\) a chosen place with [[algebra-commutative/residue-field|residue field]] \(k_w\), and \(f\) the frame. A **frame vector at \(w\)** is a pair \(d=(\varepsilon,v)\) of a sign \(\varepsilon\) and a nonzero \(v\in k_w^{\varrho+1}\); it stands for the vector \(f\cdot v=\sum_av_af_a\) modulo \(w\) (if \(\varepsilon\) is false) or modulo \(\bar w\) (if true). Its **vector fixer** is the subgroup of the [[?lean:New.Filling.ResidueGL|residue group]]
\[
\operatorname{Fix}_w(d)=\{s:\ s[(w,\varepsilon)]\,(f\cdot v)=f\cdot v\},
\]
where \(s[p]\) is the [[proofs/grh/spanning-unfolding-a/meeting-places-and-meet-norm|action of \(s\) at \(p\)]]. For a finite set \(P\) of chosen places above the first level prime \(p_0\) and a choice of frame vectors \(d_w\), the **fixer** is \(\operatorname{Fix}(P,d)=\bigcap_{w\in P}\operatorname{Fix}_w(d_w)\).

## Properties

1. For \(\varepsilon\) true, \(s\in\operatorname{Fix}_w(d)\) if and only if the inverse transpose of \(s_w\) fixes the linear form \(J\,(f\cdot v)\), \(J\) the [[?c:Gram matrix|Gram matrix]] in the lattice basis modulo \(w\). (The inverse adjoint is the conjugate of the inverse transpose by \(J^{-1}\).)
2. The image in the residue group of the integral points of \(H=U(X_0)\) ([[?lean:New.Filling.reducedImage|reduced image]] of [[?lean:New.Shape.Form.besselH|\(H\)]]) is contained in every \(\operatorname{Fix}_w(d)\), hence in every \(\operatorname{Fix}(P,d)\): an element of \(H\) fixes the frame vectors, its columns at the frame are those of the identity, and this passes to the residue fields.
3. If \(s\in\operatorname{Fix}_w(d)\) then \(s\) meets at \((w,\varepsilon)\) (take \(x=y=v\)).
4. For \(w\notin P\): \(s\in\operatorname{Fix}(P\cup\{w\},d')\iff s\in\operatorname{Fix}(P,d)\) and \(s\in\operatorname{Fix}_w(d'_w)\), where \(d'\) agrees with \(d\) on \(P\).

## References

1. Lean: `New.Filling.FrameVector`, `New.Filling.vectorFixer`, `New.Filling.fixer`, `New.Filling.mem_vectorFixer`, `New.Filling.mem_vectorFixer_true`, `New.Filling.reducedImage_besselH_le_fixer`, `New.Filling.mem_fixer_insert`, `New.Filling.meetsAt_of_mem_vectorFixer` in `src/New/Spanning/Unfolding/Climbing.lean`.
