+++
id = "operator-algebras/reduced-crossed-product"
title = "Reduced crossed product"
kind = "definition"
summary = "The C*-completion of a dynamical system obtained from a faithful regular covariant representation."
aliases = ["reduced C*-crossed product"]
domains = ["operator-algebras", "dynamical-systems"]
section_mode = "progressive"
+++

Let \((A,G,\alpha)\) be a [[operator-algebras/cstar-dynamical-system|\(C^*\)-dynamical system]], choose a faithful [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate representation]] \(\pi:A\to\mathcal B(H)\), and form its [[operator-algebras/regular-covariant-representation|regular covariant representation]] \((\widetilde\pi,\lambda)\) on \(L^2(G,H)\). The **reduced crossed product** is
\[
A\rtimes_{\alpha,r}G
=\overline{(\widetilde\pi\rtimes\lambda)(C_c(G,A))}^{\,\|\cdot\|}.
\]
Equivalently, it is the completion of the crossed-product convolution algebra in the norm \(\|f\|_r=\|(\widetilde\pi\rtimes\lambda)(f)\|\). Different faithful nondegenerate choices of \(\pi\) give canonically isomorphic \(C^*\)-algebras. The construction therefore depends only on the action, up to this canonical identification, and not on the faithful concrete realization of \(A\). Its dense image encodes the coefficient action and the group translations through integrated compactly supported functions.

## Relation to the full crossed product

Because the [[operator-algebras/covariant-representation-cstar-dynamical-system|regular covariant pair]] is among all covariant representations, \(\|f\|_r\leq\|f\|_{\mathrm u}\). Hence the identity on \(C_c(G,A)\) extends to a canonical quotient from the [[operator-algebras/full-crossed-product|full crossed product]]:
\[
A\rtimes_\alpha G\longrightarrow A\rtimes_{\alpha,r}G.
\]
This quotient measures what is lost by retaining only regular covariant representations. It is an isomorphism for every action of an [[harmonic-analysis/amenable-locally-compact-group|amenable locally compact group]] [Williams, §7.2, Theorem 7.13].

## Standard cases

For \(A=\mathbb C\) with the trivial action, the reduced crossed product is the [[operator-algebras/reduced-group-cstar-algebra|reduced group \(C^*\)-algebra]] \(C_r^*(G)\). For the trivial action on a general \(A\), it is canonically the [[operator-algebras/minimal-cstar-tensor-product|minimal \(C^*\)-tensor product]] \(A\otimes_{\min}C_r^*(G)\). When \(G\) is discrete, the dense core consists of finite sums indexed by \(G\), represented on \(\ell^2(G,H)\).

## Conventions and scope

The adjective “reduced” refers to the norm coming from regular induction, not to a quotient of the coefficient algebra \(A\). Faithfulness of the initial representation is necessary for the standard independence statement. Amenability of \(G\) is sufficient for full and reduced crossed products to agree, but more general equality phenomena are action-dependent and require separate notions of amenable action.

## References

1. Dana P. Williams, Crossed Products of \(C^*\)-Algebras, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: §7.2, especially Definition 7.7 and Theorem 7.13 on the reduced norm and amenable groups.
2. Nathanial P. Brown and Narutaka Ozawa, \(C^*\)-Algebras and Finite-Dimensional Approximations, Graduate Studies in Mathematics 88, American Mathematical Society, 2008. [DOI record](https://doi.org/10.1090/gsm/088). Relevant: Chapter 4 on crossed products and approximation properties.
