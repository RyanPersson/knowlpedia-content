+++
id = "fiber-bundles/character-variety"
title = "Character variety"
kind = "definition"
summary = "The affine geometric-invariant-theory quotient of a representation variety by conjugation."
aliases = ["G-character variety", "affine character variety"]
domains = ["fiber-bundles", "algebraic-geometry-foundations", "lie-groups"]
section_mode = "progressive"
+++

Let \(k\) be an [[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed field]] of characteristic zero, let \(\Gamma\) be a finitely generated group, and let \(G\) be a reductive affine algebraic group over \(k\). The **\(G\)-character variety** of \(\Gamma\) is the affine categorical quotient
\[
X_G(\Gamma)
=
\operatorname{Hom}(\Gamma,G)\mathbin{/\mkern-6mu/}G:=
\operatorname{Spec}\!\left(
k[\operatorname{Hom}(\Gamma,G)]^G
\right),
\]
where \(G\) acts on the [[fiber-bundles/representation-variety|representation variety]] by conjugation. Its regular functions are exactly the conjugation-invariant regular functions on \(\operatorname{Hom}(\Gamma,G)\).

## Closed-orbit interpretation

The quotient map is constant on conjugacy orbits, but it need not distinguish all of them. Each [[algebraic-geometry-foundations/closed-point|closed point]] of \(X_G(\Gamma)\) corresponds to a unique closed orbit contained in an orbit closure. For \(G=\operatorname{GL}_n\), the closed orbits are the [[algebra-representation-theory/completely-reducible-representation|completely reducible representations]].

## Relation to flat connections

When \(\Gamma=\pi_1(M,x)\), conjugation records the change of a framing in the fiber over \(x\) for a [[fiber-bundles/holonomy-representation|holonomy representation]]. Thus character varieties provide algebraic models for moduli of flat connections. Their smooth loci can carry additional geometry; for surface groups and suitable \(G\), the good-representation locus has Goldman's symplectic structure.

## Examples and scope

For \(\Gamma=\mathbb Z\), the [[fiber-bundles/representation-variety|representation variety]] is \(G\), and the character variety is the affine quotient \(G\mathbin{/\mkern-6mu/}G\) by conjugation. For \(G=\operatorname{GL}_n\), [[fiber-bundles/invariant-function|invariant functions]] include traces of words in the images of generators.

**Warning.** The character variety is not generally the set-theoretic [[fiber-bundles/quotient-space-of-an-action|orbit space]] \(\operatorname{Hom}(\Gamma,G)/G\). In compact-group topology that [[lie-groups/orbit-space|orbit space]] may be the intended moduli space, but it is a different construction unless an explicit comparison theorem applies.

## References

1. Adam S. Sikora, “Character Varieties,” *Transactions of the American Mathematical Society* 364 (2012), 5173–5208. [DOI record](https://doi.org/10.1090/S0002-9947-2012-05448-1). Relevant: §§5, 7, and 11, representation varieties, closed orbits, and the categorical quotient.
2. William M. Goldman, “The Symplectic Nature of Fundamental Groups of Surfaces,” *Advances in Mathematics* 54 (1984), 200–225. [DOI record](https://doi.org/10.1016/0001-8708%2884%2990040-9). Relevant: the symplectic structure on surface-group representation moduli.
