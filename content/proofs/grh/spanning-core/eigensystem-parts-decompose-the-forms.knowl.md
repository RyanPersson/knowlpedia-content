+++
id = "proofs/grh/spanning-core/eigensystem-parts-decompose-the-forms"
title = "The eigensystem parts decompose the forms of principal level"
kind = "theorem"
summary = "The parts of the forms of principal level for the Hecke eigensystems are independent and, in finite dimension, span."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.iSupIndep_eigenPart", "New.Data.finite_setOf_inf_eigenPart_ne_bot", "New.Data.iSup_eigenPart_eq_top"]
lean_files = ["src/New/Spanning/Multiplicities/HeckeEigensystems.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(D\) be admissible data, \(V\) a hermitian space of rank \(r\) over \(E\), and \(\mathcal F_V\) the forms of principal level on \(V\), with [[proofs/grh/spanning-core/hecke-eigensystem-part|eigensystem parts]] \(\mathcal F_V[p]\).

1. The subspaces \(\mathcal F_V[p]\), for distinct eigensystems \(p\), are independent (their sum is direct).
2. If \(\mathcal F_V\) is finite-dimensional, then for every subspace \(N\) only finitely many \(p\) have \(N\cap\mathcal F_V[p]\ne0\).
3. If \(\mathcal F_V\) is finite-dimensional, then \(\sum_p\mathcal F_V[p]=\mathcal F_V\).

## Proof

(1) Let \(y_1+\dots+y_k=0\) with \(y_j\in\mathcal F_V[p_j]\), the \(p_j\) distinct; we show all \(y_j=0\) by induction on \(k\). For \(k\ge2\) choose \(x\) with \(p_1(x)\neq p_2(x)\); applying \(T_x-p_1(x)\) gives \(\sum_{j\ge2}(p_j(x)-p_1(x))y_j=0\), a relation with fewer terms, so \(y_2=0\), and then the original relation has fewer terms. (In Lean: independence of the eigenspaces of one operator, passed to intersections.)

(2) Independent nonzero subspaces of a finite-dimensional space are finite in number.

(3) *Outline.* The representation of \(G_f\) on forms is unitary for the Petersson product. The library statement `New.IsUnitary.le_span_hecke_eigenvectors` asserts: for a unitary representation and a set of split places closed under conjugation at which the given invariant finite-dimensional space of vectors is spherical and stable under the \(T_{w,i}\), that space is spanned by its joint eigenvectors of all these \(T_{w,i}\) (the spectral theorem for commuting normal operators). Its hypotheses hold for \(\mathcal F_V\) and the places split off the level by [[proofs/grh/spanning-core/hecke-operators-at-split-places|the construction of the Hecke operators]]. Each joint eigenvector lies in some \(\mathcal F_V[p]\) (Property 3 of the eigensystem parts). \(\blacksquare\)

## References

1. Lean: `New.Data.iSupIndep_eigenPart`, `New.Data.finite_setOf_inf_eigenPart_ne_bot`, `New.Data.iSup_eigenPart_eq_top` in `src/New/Spanning/Multiplicities/HeckeEigensystems.lean`.
