+++
id = "fiber-bundles/representation-variety"
title = "Representation variety"
kind = "definition"
summary = "The affine algebraic set parameterizing homomorphisms from a finitely generated group into an affine algebraic group."
aliases = ["homomorphism variety", "G-representation variety"]
domains = ["fiber-bundles", "algebraic-geometry-foundations", "lie-groups"]
section_mode = "progressive"
+++

Let \(k\) be an [[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed field]] of characteristic zero, \(\Gamma\) a finitely generated group, and \(G\) an affine algebraic group over \(k\). The **\(G\)-representation variety** of \(\Gamma\) is
\[
\operatorname{Hom}(\Gamma,G),
\]
the set of [[algebra-groups/group-homomorphism|group homomorphisms]] \(\rho:\Gamma\to G\), equipped with its natural affine algebraic-set structure. After choosing generators \(\gamma_1,\ldots,\gamma_r\), a representation is identified with
\[
(\rho(\gamma_1),\ldots,\rho(\gamma_r))\in G^r,
\]
and the relations in \(\Gamma\) cut out \(\operatorname{Hom}(\Gamma,G)\) by polynomial equations.

## Presentation model

For a finite presentation
\[
\Gamma=\langle\gamma_1,\ldots,\gamma_r\mid R_1,\ldots,R_s\rangle,
\]
the representation variety is the common zero locus of
\[
R_j(g_1,\ldots,g_r)=e_G,\qquad 1\leq j\leq s,
\]
inside \(G^r\). Changing the finite presentation changes this embedding but not the represented affine functor. The foundational construction and its scheme-theoretic refinements are treated by [Lubotzky–Magid, chapter 1].

## Conjugation and moduli

The group \(G\) acts on \(\operatorname{Hom}(\Gamma,G)\) by
\[
(g\cdot\rho)(\gamma)=g\rho(\gamma)g^{-1}.
\]
Orbits are isomorphism classes of representations with a chosen target \(G\). The affine quotient of this action, under reductivity hypotheses, is the [[fiber-bundles/character-variety|character variety]]. The representation variety itself retains stabilizers, nonclosed orbits, and singularities that a quotient can obscure.

## Examples and scope

For the [[algebra-groups/free-group|free group]] \(F_r\), there are no relations, so \(\operatorname{Hom}(F_r,G)\cong G^r\). If \(\Gamma=\pi_1(M,x)\), its points include the [[fiber-bundles/holonomy-representation|holonomy representations]] of flat principal \(G\)-connections.

**Warning.** For a merely topological or [[fiber-bundles/lie-group|Lie group]] \(G\), \(\operatorname{Hom}(\Gamma,G)\) can be given a topology or analytic structure, but it is not automatically an algebraic variety.

## References

1. Alexander Lubotzky and Andy R. Magid, *Varieties of Representations of Finitely Generated Groups*, Memoirs of the American Mathematical Society 58, no. 336, 1985. [AMS record](https://bookstore.ams.org/memo-58-336). Relevant: chapter 1, schemes and varieties of representations.
2. Adam S. Sikora, “Character Varieties,” *Transactions of the American Mathematical Society* 364 (2012), 5173–5208. [DOI record](https://doi.org/10.1090/S0002-9947-2012-05448-1). Relevant: §§5 and 11, representation varieties and conjugation quotients.
