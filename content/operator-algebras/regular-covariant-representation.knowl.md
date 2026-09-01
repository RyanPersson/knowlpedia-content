+++
id = "operator-algebras/regular-covariant-representation"
title = "Regular covariant representation"
kind = "definition"
summary = "The canonical covariant pair on L2(G,H) induced from a representation of the coefficient C*-algebra."
aliases = ["induced regular covariant representation"]
domains = ["operator-algebras", "representation-theory", "harmonic-analysis"]
prerequisites = ["operator-algebras/cstar-dynamical-system", "operator-algebras/nondegenerate-star-homomorphism", "harmonic-analysis/haar-measure", "harmonic-analysis/regular-representations-locally-compact-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((A,G,\alpha)\) be a [[operator-algebras/cstar-dynamical-system|\(C^*\)-dynamical system]] and let \(\pi:A\to\mathcal B(H)\) be a [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate representation]]. The **regular covariant representation induced by \(\pi\)** acts on \(L^2(G,H)\) by
\[
(\widetilde\pi(a)\xi)(s)=\pi(\alpha_{s^{-1}}(a))\xi(s),
\qquad
(\lambda_t\xi)(s)=\xi(t^{-1}s).
\]
Here \(L^2(G,H)\) uses a left [[harmonic-analysis/haar-measure|Haar measure]], and \(\lambda\) is the [[harmonic-analysis/regular-representations-locally-compact-group|left regular representation]]. The pair \((\widetilde\pi,\lambda)\) is covariant because
\[
\widetilde\pi(\alpha_t(a))=\lambda_t\widetilde\pi(a)\lambda_t^*.
\]
Both representations are nondegenerate, and \(\lambda\) is strongly
continuous. Their integrated form is consequently a nondegenerate
representation of the crossed-product convolution algebra; when \(\pi\) is
faithful, its operator norm defines the reduced crossed-product norm.

## Integrated regular representation

Its [[operator-algebras/integrated-form-covariant-representation|integrated form]] is
\[
((\widetilde\pi\rtimes\lambda)(f)\xi)(s)
=\int_G\pi(\alpha_{s^{-1}}(f(t)))\xi(t^{-1}s)\,dt.
\]
The [[linear-algebra/operator-norm|operator norm]] of this representation supplies the reduced crossed-product norm. Thus “regular” refers to the use of translation on the group variable, not to a regularity condition on vectors or coefficients.

## Dependence on the coefficient representation

If \(\pi\) is faithful and nondegenerate, the resulting reduced norm and [[operator-algebras/reduced-crossed-product|reduced crossed product]] are independent of \(\pi\) up to canonical isomorphism. Faithfulness matters: starting from a representation with nonzero kernel can discard coefficient-algebra information and produce a smaller image.

The construction can also be viewed as inducing \(\pi\) from the identity subgroup. This perspective explains the common notation \(\operatorname{Ind}\pi\) for the integrated [[algebra-representation-theory/regular-representation|regular representation]].

## Standard cases

When \(A=\mathbb C\) with the trivial action and \(\pi\) is the scalar representation, \(\widetilde\pi\) acts by scalars and the integrated form is the usual regular representation of \(C_c(G)\). For a discrete \(G\), \(L^2(G,H)=\ell^2(G,H)\), and the formulas become pointwise coefficient action together with shifts of the \(G\)-coordinate.

## References

1. Dana P. Williams, Crossed Products of \(C^*\)-Algebras, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: §2.2, Example 2.14 on regular covariant representations, and §7.2 on reduced crossed products.
