+++
id = "proofs/grh/spanning-core/spherical-hecke-algebra-away-from-the-level"
title = "Spherical Hecke algebra away from the level"
kind = "definition"
summary = "The algebra of families of operators on forms of principal level of all hermitian spaces given by one element of the group algebra of the adelic points that are trivial at the chosen places."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsSplitOffLevel", "New.Data.IsSplitOffLevel.star", "New.Data.offLevelGroup", "New.Data.sphericalAlgebra", "New.Data.mem_sphericalAlgebra", "New.Data.heckeAlgebra", "New.Data.mem_heckeAlgebra", "New.Data.exists_heckeAlgebra_eq_asAlgebraHom", "New.mapDomain_mem_universalLevelAlgebra", "New.commute_asAlgebraHom_mapDomain_trivialOn", "New.Data.mem_sphericalAlgebra_of_mem_universalLevelAlgebra"]
lean_files = ["src/New/Spanning/Multiplicities/HeckeEigensystems.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]], \(E\) its CM field, \(r\) the rank, \(G_f\) the [[?lean:New.Gf|finite adelic unitary group]] of rank \(r\) over \(E\), \(K_0\) its [[?lean:New.stdLevel|standard maximal compact subgroup]], and \(J_M\subseteq K_0\) the [[?lean:New.Data.chosenLevel|principal level at the chosen places]] (the places of \(E\) dividing \(\pi_M\)). All group algebras are over \(\mathbb{C}\).

1. A finite place \(w\) of \(E\) is **split off the level** if \(w\neq\bar w\) and neither \(w\) nor \(\bar w\) is a chosen place.
2. The **off-level group** \(G^M\subseteq G_f\) is the subgroup of elements whose component at every chosen place is \(1\).
3. The **spherical algebra away from \(M\)** is the subalgebra \(\mathcal S\subseteq\mathbb{C}[G^M]\) of the elements \(a\) such that, in every [[algebra-representation-theory/group-representation|representation]] of \(G_f\) on a complex vector space, the image of \(a\) in \(\mathbb{C}[G_f]\) maps \(J_M\)-fixed vectors to \(J_M\)-fixed vectors (that is, the image lies in the [[?lean:New.universalLevelAlgebra|universal level algebra]] of \(J_M\)).
4. The **spherical Hecke algebra away from \(M\)** is the algebra \(\mathcal H\) of the families \(T=(T_V)_V\), where \(V\) runs over the hermitian spaces of rank \(r\) over \(E\) (with all sign vectors \(s\)) and \(T_V\) is an endomorphism of the [[?lean:New.Data.principalForms|forms of principal level]] on \(V\), for which there is one \(a\in\mathcal S\) with \(T_V\,y=a\cdot y\) for all \(V\) and all \(y\) (the action of \(a\) through the [[?lean:New.Space.formRep|representation of \(G_f\) on forms]]). Sums, products and scalars are taken for each \(V\).

## Properties

1. Every \(a\in\mathcal S\) defines a member of \(\mathcal H\): its action preserves the forms of principal level on each \(V\).
2. **(Criterion.)** If \(a\in\mathbb{C}[G^M]\) maps \((K_0\cap G^M)\)-fixed vectors to \((K_0\cap G^M)\)-fixed vectors in every representation of \(G^M\), then \(a\in\mathcal S\).
3. If \(w\) is split off the level, so is \(\bar w\).

## Proof

(1) By definition of \(\mathcal S\), applied to the representation on forms on \(V\).

(2) More generally let \(\Sigma\) be a set of finite places, \(H\) the subgroup of \(G_f\) of elements trivial at \(\Sigma\), and \(J\) a subgroup with \(K_0\cap H\subseteq J\subseteq K_0\); here \(\Sigma\) is the set of chosen places and \(J=J_M\) (which contains \(K_0\cap G^M\) and lies in \(K_0\)). Let \(\rho\) be a representation of \(G_f\), \(y\) a \(J\)-fixed vector and \(T=\rho(a)\). Every \(k\in J\) factors as \(k=uv\) with \(u\) supported at \(\Sigma\) and its conjugates and \(v\in H\), and since \(k\in K_0\) also \(v\in K_0\) (`New.Gf.exists_supportedOn_mul_trivialOn`); then \(v\in K_0\cap H\subseteq J\), so \(u\in J\). The vector \(y\) is fixed by \(K_0\cap H\), hence so is \(Ty\) by hypothesis (for the restriction of \(\rho\) to \(H\)); thus \(\rho(v)Ty=Ty\). Elements supported at \(\Sigma\) and its conjugates commute with \(H\), so \(\rho(u)\) commutes with \(T\), and \(\rho(u)Ty=T\rho(u)y=Ty\). Hence \(\rho(k)Ty=Ty\).

(3) Clear, as \(\bar{\bar w}=w\). \(\blacksquare\)

## Remarks

In this chapter "away from \(M\)" and "not above \(M\)" refer to the places that are neither chosen nor conjugate to a chosen place, as in the Lean source.

## References

1. Lean: `New.Data.IsSplitOffLevel`, `New.Data.offLevelGroup`, `New.Data.sphericalAlgebra`, `New.Data.heckeAlgebra`, `New.mapDomain_mem_universalLevelAlgebra` in `src/New/Spanning/Multiplicities/HeckeEigensystems.lean`.
