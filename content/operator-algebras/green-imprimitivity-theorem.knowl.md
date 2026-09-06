+++
id = "operator-algebras/green-imprimitivity-theorem"
title = "Green imprimitivity theorem"
kind = "theorem"
summary = "An induced dynamical system crossed by its ambient group is Morita equivalent to the original system crossed by the subgroup."
aliases = ["Green's imprimitivity theorem"]
domains = ["operator-algebras", "harmonic-analysis"]
prerequisites = ["topology/locally-compact-group", "lie-groups/left-translation", "operator-algebras/full-crossed-product", "operator-algebras/strong-morita-equivalence", "operator-algebras/imprimitivity-bimodule"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]], \(H\subseteq G\) a closed subgroup, and \((A,H,\alpha)\) a \(C^*\)-dynamical system. Form the induced algebra
\[
\operatorname{Ind}_H^G(A,\alpha)
=\{f\in C_b(G,A): f(sh)=\alpha_{h^{-1}}(f(s)),\quad
sH\mapsto\lVert f(s)\rVert\in C_0(G/H)\},
\]
with \(G\) acting by [[lie-groups/left-translation|left translation]]. The **Green imprimitivity theorem** states that the [[operator-algebras/full-crossed-product|full crossed products]]
\[
\operatorname{Ind}_H^G(A,\alpha)\rtimes G
\quad\text{and}\quad
A\rtimes_\alpha H
\]
are [[operator-algebras/strong-morita-equivalence|strongly Morita equivalent]] through a canonical [[operator-algebras/imprimitivity-bimodule|imprimitivity bimodule]] obtained by completing \(C_c(G,A)\).

## Representation-theoretic content

The Green bimodule implements [[operator-algebras/rieffel-induction|Rieffel induction]] between the [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate representation]] categories of the two
crossed products. Under the crossed-product/covariant-representation
correspondence, this recovers induction from \(H\)-covariant representations
to \(G\)-covariant representations.

## Homogeneous-space form

If \(\alpha\) is the restriction to \(H\) of an action of \(G\) on \(A\), the
induced algebra can be identified with a diagonal-action model based on
\(C_0(G/H,A)\). In particular, for \(A=\mathbb C\) with the trivial action,
the theorem says
\[
C_0(G/H)\rtimes G\ \sim_M\ C^*(H).
\]
This is the crossed-product form of [[harmonic-analysis/mackey-imprimitivity-theorem|Mackey's imprimitivity theorem]].

## Conventions and scope

The displayed theorem concerns full crossed products and an arbitrary closed
subgroup. Reduced crossed-product analogues require their own formulation and
hypotheses and should not be inferred by simply adding subscripts \(r\).
Different sources use right-coset conventions or write the covariance
condition with \(\alpha_h\) rather than \(\alpha_{h^{-1}}\); changing both the
translation and covariance conventions yields an equivalent induced system.

## References

1. Philip Green, “The Local Structure of Twisted Covariance Algebras,” *Acta Mathematica* 140 (1978), 191–250. [DOI record](https://doi.org/10.1007/BF02392308). Relevant: the imprimitivity theorem for induced covariance algebras.
2. Dana P. Williams, *Crossed Products of \(C^*\)-Algebras*, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: Chapter 4 on induced algebras and Green's imprimitivity theorem.
