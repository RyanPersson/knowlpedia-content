+++
id = "proofs/grh/spanning-unfolding-b/class-unipotent-discrete"
title = "Discreteness of the class unipotent groups and existence of cutoffs"
kind = "lemma"
summary = "The image at the infinite places of any subgroup of the rational unipotent group of level M at a class is discrete, and it has a measurable cutoff whose translates sum to one."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.finite_classUnipotent_inter_compact", "New.Filling.discreteTopology_map_ratToInf", "New.Filling.exists_cutoff_classUnipotent"]
lean_files = ["src/New/Spanning/Unfolding/Setup.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]], \(c\) a [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|class]], and \(\mathsf{U}_c(M)\) the group of rational unipotent elements of level \(M\) at \(c\). Let \(u\mapsto u_\infty\) be the [[proofs/grh/spanning-unfolding-b/filling-unitary-groups|map to \(G_\infty=\prod_vG_1\)]].

1. *(Finiteness.)* Let \(m\) be a finite set, \(\phi\colon m\to\{\text{basis of }V\}\) a map, and \(C\) a compact set of families \((A_v)_v\) of complex \(m\times m\) matrices. Then only finitely many points of \(C\) are of the form \(\bigl((u_\infty)_v(\phi(i),\phi(j))\bigr)_{v;\,i,j}\) with \(u\in\mathsf{U}_c(M)\).
2. *(Discreteness.)* For every subgroup \(K'\subset\mathsf{U}_c(M)\), the image \(\Gamma=\{u_\infty:u\in K'\}\) is a discrete subgroup of \(G_\infty\).
3. *(Cutoff.)* For every such \(K'\) there is a measurable function \(\beta\colon G_\infty\to[0,\infty]\) with
\[
\sum_{u\in K'}\beta(u_\infty y)=1\qquad\text{for all }y\in G_\infty ;
\]
that is, \(\beta\) is a [[?lean:New.IsCutoff|cutoff]] for \(\Gamma\) with the counting measure.

## Proof

*(1)* Let \(B\) be the lattice basis matrix and \(h_c\) the representative of \(c\). For \(u\in\mathsf{U}_c(M)\) the element \(h_c^{-1}B^{-1}uBh_c\) lies in \(K(M)\), so it is an integral invertible matrix over \(\widehat{\mathcal{O}}\). Fix \(i,j\in m\). The entry \(x=u_{\phi(i)\phi(j)}\in E\) has finite adelic component equal to the \((\phi(i),\phi(j))\) entry of \((Bh_c)\,k\,(Bh_c)^{-1}\) for an integral invertible \(k\), and infinite components \(\Phi_v(x)=(u_\infty)_v(\phi(i),\phi(j))\,\sigma_v(\phi(i))/\sigma_v(\phi(j))\). If the family of submatrices of \(u_\infty\) lies in \(C\), the adele of \(x\) therefore lies in the image of the compact set \(C\times\mathrm{GL}_r(\widehat{\mathcal{O}})\) under a continuous map (the group of integral invertible matrices over \(\widehat{\mathcal{O}}\) is compact because \(\widehat{\mathcal{O}}\) is). Since \(E\) is [[?lean:New.finite_setOf_toAdele_mem|discrete in its adeles]], a compact set of adeles contains only finitely many elements of \(E\). So each entry \(x\) takes finitely many values, hence so does the family of submatrices.

*(2)* The map sending \(\gamma\in\Gamma\) to its family of matrices \((\gamma_v)_v\) is continuous and injective. By (1) with \(\phi\) the identity, each compact set of families of matrices contains only finitely many images of elements of \(\Gamma\). An injective continuous map from a group with this property has discrete source; hence \(\Gamma\) is discrete.

*(3)* The map \(u\mapsto u_\infty\) is injective on \(G(E)\), because each \(\Phi_v\) is injective and the scales are nonzero; so \(K'\to\Gamma\) is a bijection. A discrete subgroup \(\Gamma\) of the locally compact second countable group \(G_\infty\), acting by left translation, [[?lean:New.hasCutoff_count|admits a cutoff]] for the counting measure: a measurable \(\beta\ge0\) with \(\sum_{\gamma\in\Gamma}\beta(\gamma y)=1\) for all \(y\). Transporting the sum along the bijection \(K'\to\Gamma\) gives the statement.

## References

1. Lean: `New.Filling.finite_classUnipotent_inter_compact`, `New.Filling.discreteTopology_map_ratToInf`, `New.Filling.exists_cutoff_classUnipotent` in `src/New/Spanning/Unfolding/Setup.lean`.
