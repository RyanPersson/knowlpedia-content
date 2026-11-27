+++
id = "proofs/grh/spanning-unfolding-a/meeting-places-and-meet-norm"
title = "Meeting places and the meet norm of a residue element"
kind = "definition"
summary = "An element s of the residue group meets at a place above M if the span of the frame and its image under s share a nonzero vector modulo that place; the meet norm is the product of the norms of these places."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.MeetsAt", "New.Filling.meetNorm", "New.Filling.actionAt", "New.Filling.prod_le_meetNorm", "New.Filling.one_le_meetNorm", "New.Filling.actionAt_reduction", "New.Filling.actionAt_mul", "New.Filling.eq_of_forall_actionAt_eq"]
lean_files = ["src/New/Spanning/Unfolding/Climbing.lean"]
+++

Let \(S\) be [[?lean:New.Filling|filling data]] over a [[?c:CM field|CM field]] \(E\), and \(s=(s_w)_w\) an element of the [[?lean:New.Filling.ResidueGL|residue group]] \(\prod_w GL_r(k_w)\), the product over the chosen places \(w\) above \(p_0,p_1\). For a place \(p=(w,\varepsilon)\) above \(M\) (the chosen place \(w\), or its conjugate if \(\varepsilon\) is true), the **action of \(s\) at \(p\)** is the matrix
\[
s[p]=\begin{cases}s_w&\varepsilon\ \text{false},\\ J^{-1}\,(s_w^{-1})^{\top}J&\varepsilon\ \text{true},\end{cases}
\]
over \(k_w\), where \(J\) is the [[?c:Gram matrix|Gram matrix]] of the form in the lattice basis, reduced modulo \(w\) ([[?lean:New.Filling.idOrInvAdjoint|identity or inverse adjoint]]). The element \(s\) **meets at \(p\)** if there are coefficient vectors \(x\ne0\) and \(y\) in \(k_w^{\varrho+1}\) with
\[
\sum_ax_a\,f_a=\sum_ay_a\,s[p]f_a ,
\]
where \(f=(f_0,\dots,f_\varrho)=(e_1,\dots,e_\varrho,z)\) is the frame; that is, the span of the frame and its image under \(s[p]\) share a nonzero vector. The **meet norm** of \(s\) is
\[
\operatorname{mn}(s)=\prod_{p=(w,\varepsilon)\,:\ s\ \text{meets at}\ p}\mathbf N(w),
\]
where \(\mathbf N(w)\in\{p_0,p_1\}\) is the norm of \(w\).

## Properties

1. \(\operatorname{mn}(s)\ge1\), and if \(s\) meets at every place of a set \(A\), then \(\prod_{p\in A}\mathbf N(p)\le\operatorname{mn}(s)\).
2. If \(k\) lies in the integral subgroup \(K\) ([[?lean:New.Filling.latticeStabilizer|lattice stabiliser]]) with reduction \(\bar k\), then \(\bar k[p]\) is the matrix of \(k\) reduced entrywise by the [[?lean:New.Filling.reduceAboveM|reduction at \(p\)]] (for the conjugate place this uses \(k^{-1}=J^{-1}k^{*}J\)); see [[?lean:New.Filling.intGL_map_reduceAboveM|reduction above \(M\) of integral matrices]].
3. \((st)[p]=s[p]\,t[p]\); and for a fixed sign \(\varepsilon\), \(s\) is determined by the matrices \(s[(w,\varepsilon)]\), \(w\) chosen.

## References

1. Lean: `New.Filling.actionAt`, `New.Filling.MeetsAt`, `New.Filling.meetNorm`, `New.Filling.prod_le_meetNorm`, `New.Filling.one_le_meetNorm`, `New.Filling.actionAt_reduction`, `New.Filling.actionAt_mul`, `New.Filling.eq_of_forall_actionAt_eq` in `src/New/Spanning/Unfolding/Climbing.lean`.
