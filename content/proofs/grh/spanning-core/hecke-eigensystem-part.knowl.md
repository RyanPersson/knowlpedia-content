+++
id = "proofs/grh/spanning-core/hecke-eigensystem-part"
title = "Part of the forms with a given Hecke eigensystem"
kind = "definition"
summary = "The forms of principal level on which each Hecke operator T_{w,i} acts by a prescribed scalar."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.eigenPart", "New.Data.mem_eigenPart", "New.Data.hasHeckePolynomial_of_mem_eigenPart", "New.Data.exists_mem_eigenPart_of_heckeSplit_eq_smul"]
lean_files = ["src/New/Spanning/Multiplicities/HeckeEigensystems.lean"]
+++

Let \(D\) be admissible data and \(V\) a hermitian space of rank \(r\) over \(E\). An **eigensystem** is a function \(p\) assigning a complex number \(p(w,i)\) to every pair of a finite place \(w\) of \(E\) and a natural number \(i\). The **\(p\)-part** of the [[?lean:New.Data.principalForms|forms of principal level]] on \(V\) is the subspace
\[
\mathcal F_V[p]=\{\,y\ :\ T_x\,y=p(x)\,y\ \text{ for all }x=(w,i)\,\},
\]
the intersection of the [[linear-algebra/eigenspace|eigenspaces]] of the [[proofs/grh/spanning-core/hecke-operators-at-split-places|Hecke operators]] \(T_x\).

## Properties

1. Since \(T_{(w,i)}=0\) when \(w\) is not split off the level, a nonzero \(p\)-part can occur only if \(p(w,i)=0\) for all such \(w\) and all \(i\).
2. If \(y\in\mathcal F_V[p]\) and \(w\) is split off the level with residue cardinality \(q\), then \(y\) is spherical at \(w\) and for each complex \(X\) the operator \(\sum_{i\le r}(-X)^iq^{i(i-1)/2}T_{w,i}\) multiplies \(y\) by \(\sum_{i\le r}(-X)^iq^{i(i-1)/2}p(w,i)\) (the Hecke polynomial; in Lean [[?lean:New.HasHeckePolynomial|`HasHeckePolynomial`]]).
3. A form \(y\) of principal level that is an eigenvector of \(T_{w,i}\) for every \(i\) and every \(w\) split off the level lies in \(\mathcal F_V[p]\) for some \(p\) (take \(p=0\) at the other places).

## References

1. Lean: `New.Data.eigenPart`, `New.Data.hasHeckePolynomial_of_mem_eigenPart`, `New.Data.exists_mem_eigenPart_of_heckeSplit_eq_smul` in `src/New/Spanning/Multiplicities/HeckeEigensystems.lean`.
