+++
id = "proofs/grh/spanning-unfolding-b/class-basis"
title = "Basis of the lattice of a class"
kind = "definition"
summary = "The finite adelic matrix whose columns are a basis of the translate of the standard lattice by the representative of a class."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.classBasis", "New.Filling.classBasis_eq_latticeBasis_mul_classRep", "New.Filling.coe_translateByClassReps"]
lean_files = ["src/New/Spanning/Unfolding/BesselLevelStructure.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]], \(B\) its [[proofs/grh/spanning-unfolding-b/filling-unitary-groups|lattice basis matrix]], and \(c\) a [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|class]] with representative \(g_c\in U(X_0)(\mathbb{A}_f)\). Let \(\tilde g_c\in G(\mathbb{A}_f)\) be the element that acts as \(g_c\) on \(X_0\) and trivially on \(z\), \(e_a\), \(e_a^*\) ([[?lean:New.toBesselH|extension by the identity]]). The **class basis** of \(c\) is the invertible matrix over the finite adeles
\[
B_c=\tilde g_c\,B .
\]
Its columns are a basis of \(\tilde g_c\Lambda_0\), where \(\Lambda_0\) is the \(\widehat{\mathcal{O}}\)-lattice spanned by the columns of \(B\).

## Properties

With \(h_c=B^{-1}\tilde g_cB\in G_{\mathrm{fin}}\) the representative in the lattice basis, \(B_c=B\,h_c\). Consequently, for classes \(c,c'\) and \(\gamma\in G(E)\), the matrix of \(h_c^{-1}\gamma_{\mathrm{fin}}h_{c'}\) is
\[
h_c^{-1}B^{-1}\gamma Bh_{c'}=B_c^{-1}\,\gamma\,B_{c'} ,
\]
so \(\gamma\) is a term over a block \((c,s,c')\) exactly when \(B_c^{-1}\gamma B_{c'}\) is integral with integral inverse and has reduction \(s\).

## References

1. Lean: `New.Filling.classBasis`, `New.Filling.classBasis_eq_latticeBasis_mul_classRep`, `New.Filling.coe_translateByClassReps` in `src/New/Spanning/Unfolding/BesselLevelStructure.lean`.
