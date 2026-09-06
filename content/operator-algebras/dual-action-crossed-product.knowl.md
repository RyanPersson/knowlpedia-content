+++
id = "operator-algebras/dual-action-crossed-product"
title = "Dual action on a crossed product"
kind = "definition"
summary = "The canonical action of the Pontryagin dual on a crossed product by a locally compact abelian group."
aliases = ["dual action of the Pontryagin dual"]
domains = ["operator-algebras", "harmonic-analysis", "dynamical-systems"]
prerequisites = ["operator-algebras/cstar-dynamical-system", "operator-algebras/full-crossed-product", "shared-foundations/complex-conjugate"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((A,G,\alpha)\) be a [[operator-algebras/cstar-dynamical-system| \(C^*\)-dynamical system]] with \(G\) locally compact abelian. The **dual
action** is the strongly continuous action
\[
\widehat\alpha:\widehat G\longrightarrow
\operatorname{Aut}(A\rtimes_\alpha G)
\]
on the [[operator-algebras/full-crossed-product|full crossed product]]
determined, for \(\chi\in\widehat G\), by
\[
\widehat\alpha_\chi(i_A(a))=i_A(a),\qquad
\widehat\alpha_\chi(i_G(s))=\overline{\chi(s)}\,i_G(s).
\]
Equivalently, on the dense convolution algebra \(C_c(G,A)\),
\[
(\widehat\alpha_\chi f)(s)=\overline{\chi(s)}f(s).
\]
It records the group variable by multiplying each Fourier mode by its
character. The action fixes the coefficient algebra pointwise and changes
only the canonical group unitaries. The [[shared-foundations/complex-conjugate|complex conjugate]] reflects the
Fourier-transform convention chosen here.

## Why the formula defines an action

Multiplying \(i_G(s)\) by the scalar \(\overline{\chi(s)}\) preserves the
covariance relation
\[
i_G(s)i_A(a)i_G(s)^*=i_A(\alpha_s(a)).
\]
The universal property of the crossed product therefore produces a unique
automorphism. Character multiplication gives
\(\widehat\alpha_{\chi\psi}=
\widehat\alpha_\chi\widehat\alpha_\psi\), and the crossed-product norm plus
density of \(C_c(G,A)\) gives strong continuity.

The same formula descends through the [[algebra-representation-theory/regular-representation|regular representation]] and defines a
dual action on the [[operator-algebras/reduced-crossed-product|reduced crossed product]].

## Standard cases and conventions

If \(A=\mathbb C\) and the action is trivial, the construction is the action
of \(\widehat G\) on \(C^*(G)\) that becomes translation after Fourier
transform. If \(G\) is discrete, elements of the algebraic core have the form
\(\sum_s a_su_s\), and
\[
\widehat\alpha_\chi\left(\sum_s a_su_s\right)
=\sum_s\overline{\chi(s)}a_su_s.
\]

Some authors omit the complex conjugate in the defining formula. That
amounts to replacing \(\chi\) by \(\chi^{-1}\); statements of duality must
use one convention consistently.

## References

1. Dana P. Williams, *Crossed Products of \(C^*\)-Algebras*, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [AMS DOI record](https://doi.org/10.1090/surv/134). Relevant: Chapter 7 on dual actions and crossed-product duality.
2. Gert K. Pedersen, *\(C^*\)-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [Publisher DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Chapter 7 on crossed products and dual actions.
