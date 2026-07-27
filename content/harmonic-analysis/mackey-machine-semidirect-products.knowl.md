+++
id = "harmonic-analysis/mackey-machine-semidirect-products"
title = "Mackey machine for semidirect products"
kind = "theorem"
summary = "A classification of irreducible unitary representations of regular semidirect products with an abelian normal factor."
aliases = ["little-group method"]
domains = ["harmonic-analysis", "representation-theory"]
section_mode = "progressive"
+++

Let \(A\) and \(K\) be [[topology/locally-compact-group|second-countable locally compact Hausdorff groups]], with \(A\) abelian, and let \(G=A\rtimes K\) be their [[algebra-groups/semidirect-product|semidirect product]]. Suppose the \(K\)-action on the [[harmonic-analysis/pontryagin-dual|Pontryagin dual]] \(\widehat A\) is regular. For \(\chi\in\widehat A\), let \(K_\chi\) be its [[algebra-groups/stabilizer|stabilizer]]. The **Mackey machine** states that every [[lie-groups/irreducible-unitary-representation|irreducible unitary representation]] of \(G\) is
\[
\operatorname{Ind}_{A\rtimes K_\chi}^{G}(\widetilde\chi\otimes\sigma),
\]
where \(\widetilde\chi(a,k)=\chi(a)\) and \(\sigma\) is an irreducible unitary representation of \(K_\chi\). Two such representations are equivalent exactly when their characters lie in the same \(K\)-orbit and their little-group representations correspond under conjugation.

## Why the classification works

Restricting a representation of \(G\) to the abelian [[algebra-groups/normal-subgroup|normal subgroup]] \(A\) produces spectral data on \(\widehat A\). Under the regularity hypothesis, irreducibility concentrates that data on one \(K\)-orbit. The resulting transitive [[harmonic-analysis/system-of-imprimitivity|system of imprimitivity]] is classified by the [[harmonic-analysis/mackey-imprimitivity-theorem|Mackey imprimitivity theorem]], which recovers a representation of \(K_\chi\); [[harmonic-analysis/unitary-induced-representation|unitary induction]] then reconstructs the original representation [Folland, §6.6, Theorem 6.43](https://doi.org/10.1201/B19172).

## Example: Euclidean motion groups

For \(G=\mathbb R^n\rtimes SO(n)\), the dual of the translation subgroup is \(\widehat{\mathbb R^n}\cong\mathbb R^n\). Nonzero orbits are spheres. The stabilizer of a nonzero covector is isomorphic to \(SO(n-1)\), so a radius together with an irreducible representation of \(SO(n-1)\) determines an induced irreducible representation. The zero orbit has little group \(SO(n)\) and gives representations trivial on translations.

## Hypotheses and scope

Regularity may be expressed by the existence of a Borel cross-section for the [[lie-groups/orbit-space|orbit space]]; it prevents pathologies in which orbit data do not provide a usable measurable parametrization. The theorem above exploits both the abelianness of \(A\) and the splitting \(G=A\rtimes K\). For a general normal subgroup, one replaces characters by irreducible representations and may encounter projective representations and a Mackey obstruction. “Mackey machine” is also used for that broader analysis [Mackey, group-extension analysis](https://doi.org/10.1007/BF02392428).

## References

1. George W. Mackey, “Unitary Representations of Group Extensions I,” *Acta Mathematica* 99 (1958), 265–311. [Springer DOI record](https://doi.org/10.1007/BF02392428). Relevant: the orbit, stabilizer, and multiplier analysis for group extensions.
2. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §6.6, especially Theorem 6.43 on semidirect products with an abelian normal subgroup.
