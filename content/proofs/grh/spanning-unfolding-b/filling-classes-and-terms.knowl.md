+++
id = "proofs/grh/spanning-unfolding-b/filling-classes-and-terms"
title = "Classes, terms over a block, and the unipotent groups of a class"
kind = "definition"
summary = "The double coset classes of U(X0), the rational terms over a block (c, s, c'), the frame products and discriminant of a term, and the groups of rational unipotent elements of level M at a class."
aliases = ["terms over a block", "termsOver", "classUnipotent", "term discriminant", "frame products"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Classes", "New.Filling.classRep", "New.Filling.translateByClassReps", "New.Filling.termsOver", "New.Filling.classUnipotent", "New.Filling.classUnipotent₀", "New.Filling.frameProducts", "New.Filling.termDisc"]
lean_files = ["src/New/Spanning/Unfolding/Setup.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] with source level \(L\), and use the [[proofs/grh/spanning-unfolding-b/filling-unitary-groups|groups and maps]] \(G(E)\), \(G_{\mathrm{fin}}\), \(\gamma\mapsto\gamma_{\mathrm{fin}}\), \(\iota_H\) and the [[proofs/grh/spanning-unfolding-b/filling-level-and-reduction|subgroups \(K\), \(K(M)\) and the reduction]] \(K\to\bar G\).

* A **class** is a [[?c:Double coset|double coset]] in \(U(X_0)(E^+)\backslash U(X_0)(\mathbb{A}_f)/L\), where \(U(X_0)(E^+)\) is the group of rational points of the unitary group of \(X_0\). The set \(\mathcal{C}\) of classes is finite and nonempty. For each class \(c\) fix a representative \(g_c\) and put \(h_c=\iota_H(g_c)\in G_{\mathrm{fin}}\).
* For classes \(c,c'\) and \(s\in\bar G\), the set of **terms over the block \((c,s,c')\)** is
\[
\mathcal{T}(c,s,c')=\bigl\{\gamma\in G(E)\ :\ h_c^{-1}\gamma_{\mathrm{fin}}h_{c'}\in K\ \text{and}\ \overline{h_c^{-1}\gamma_{\mathrm{fin}}h_{c'}}=s\bigr\}.
\]
* For \(\gamma\in G(E)\), the **frame products** are the matrix \(Z(\gamma)=\bigl(h(f_a,\gamma f_b)\bigr)_{0\le a,b\le\varrho}\) over \(E\), and the **discriminant** of \(\gamma\) is
\[
\operatorname{disc}(\gamma)=D_{\varrho+1}\overline{D_{\varrho+1}}-N^2D_\varrho\overline{D_\varrho}\in E,
\]
where \(D_l\) is the leading \(l\times l\) minor of \(Z(\gamma)\) ([[?lean:New.frameDisc|frame discriminant]]).
* Let \(\mathsf{U}\subset G(E)\) be the [[?lean:New.Shape.Form.besselU|Bessel unipotent group]] and \(\mathsf{U}^0\subset\mathsf{U}\) its [[?lean:New.Shape.Form.besselU0|subgroup fixing the frame]]. For a class \(c\),
\[
\mathsf{U}_c(M)=\{u\in\mathsf{U}\ :\ h_c^{-1}u_{\mathrm{fin}}h_c\in K(M)\},\qquad \mathsf{U}^0_c(M)=\mathsf{U}_c(M)\cap\mathsf{U}^0 .
\]

## Remarks

The representative \(g_c\) is an arbitrary fixed choice (in Lean, the chosen representative of the quotient); the finiteness of \(\mathcal{C}\) is the [[?lean:New.HasFiniteType.finite_classes|finiteness of class numbers]] for the definite unitary group \(U(X_0)\).

## References

1. Lean: `New.Filling.Classes`, `New.Filling.classRep`, `New.Filling.termsOver`, `New.Filling.classUnipotent`, `New.Filling.classUnipotent₀`, `New.Filling.frameProducts`, `New.Filling.termDisc` in `src/New/Spanning/Unfolding/Setup.lean`.
