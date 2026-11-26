+++
id = "proofs/grh/spanning-unfolding-b/class-cutoff"
title = "Class cutoff and reduced points"
kind = "construction"
summary = "The cutoff function of a class on the product of the real groups: a cutoff for the unipotent elements fixing the frame times the indicator of the points reduced modulo M times the integers."
aliases = ["class cutoff", "reduced points", "residue domain", "reduced indicator"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.levelMultiples", "New.Filling.IsResidueDomain", "New.Filling.ratTriangle", "New.Filling.reducedPoints", "New.Filling.reducedIndicator", "New.Filling.classCutoff", "New.Filling.exists_classCutoff_eq_mul"]
lean_files = ["src/New/Spanning/Unfolding/Setup.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] and \(G_\infty=\prod_vG_1\) as in [[proofs/grh/spanning-unfolding-b/filling-unitary-groups|its groups]].

**Residue domain.** Let \(M\mathcal{O}_E\subset\prod_v\mathbb{C}\) be the additive group of the tuples \((\Phi_v(Mx))_v\), \(x\in\mathcal{O}_E\). A **residue domain** is a measurable set \(D\subset\prod_v\mathbb{C}\) such that every \(w\in D\) has \(\lvert w_v\rvert\le b^{26}\) for all \(v\), and for every \(w\in\prod_v\mathbb{C}\) there is exactly one \(l\in M\mathcal{O}_E\) with \(l+w\in D\).

**Reduced points.** For \(y\in G_\infty\) and frame indices \(0\le a,b'\le\varrho\) put
\[
t_{ab'}(y)_v=\mathrm{GS}(y_v)_{ab'}\cdot\frac{\sigma_v(f_a)}{\sigma_v(f_{b'})},
\]
where \(\mathrm{GS}(y_v)\) is the [[?lean:New.gramSchmidtMatrix|Gram–Schmidt matrix]] of \(y_v\) and \(\sigma_v\) are the scales. For a set \(D\), the **reduced points** are the \(y\in G_\infty\) with \(t_{ab'}(y)\in D\) for all \(a<b'\). The **reduced indicator** \(\mathbf{1}_{\mathrm{red}}\colon G_\infty\to\{0,1\}\) is the indicator of the reduced points for a fixed residue domain \(D\) (fixed once and for all; if no residue domain exists, \(D\) is an arbitrary set).

**Class cutoff.** For a [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|class]] \(c\), fix a measurable \(\beta^0_c\colon G_\infty\to[0,\infty]\) with \(\sum_{u\in\mathsf{U}^0_c(M)}\beta^0_c(u_\infty y)=1\) for all \(y\), which exists by [[proofs/grh/spanning-unfolding-b/class-unipotent-discrete|the existence of cutoffs]]. The **class cutoff** is
\[
\beta_c=\beta^0_c\cdot\mathbf{1}_{\mathrm{red}}\colon G_\infty\to[0,\infty].
\]

## Remarks

The function \(\beta^0_c\) is a choice; only the two stated properties (measurability and the sum over \(\mathsf{U}^0_c(M)\)) are used. That \(\beta_c\) is a cutoff for the whole group \(\mathsf{U}_c(M)\), so that integrals over \(\mathsf{U}_c(M)\backslash G_\infty\) can be written with \(\beta_c\), is proved in [[?lean:New.Filling.isCutoff_classCutoff|the cutoff property of the class cutoff]]; it uses that a residue domain exists.

## References

1. Lean: `New.Filling.IsResidueDomain`, `New.Filling.ratTriangle`, `New.Filling.reducedPoints`, `New.Filling.reducedIndicator`, `New.Filling.classCutoff`, `New.Filling.exists_classCutoff_eq_mul` in `src/New/Spanning/Unfolding/Setup.lean`.
