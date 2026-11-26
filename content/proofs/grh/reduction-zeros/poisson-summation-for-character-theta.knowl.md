+++
id = "proofs/grh/reduction-zeros/poisson-summation-for-character-theta"
title = "Poisson summation for the theta series of a character"
kind = "proposition"
summary = "For a non-principal character chi modulo q of parity j, t times |sum chi(n) w(nt)| equals |sum of the inverse Fourier transform of chi times w(n/(qt))|; hence the sum is at most 3eq exp(-t)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.gaussianTheta_poisson_summation", "New.poisson_summation_gaussianMonomial", "New.two_mul_gaussianTheta", "New.hasSum_mul_gaussianMonomial_of_classes", "New.hasSum_invDFT_mul_gaussianMonomial", "New.norm_gaussianTheta_char_le"]
lean_files = ["src/Lib/Analytic/DirichletTheta.lean"]
proof_status = "outline"
+++

**Proposition.** Let \(\chi\ne1\) be a complex Dirichlet character modulo \(q\ge1\) (primitive or not), \(j\in\{0,1\}\) with \(\chi(-1)=(-1)^{j}\), and \(t>0\). Let \(\check\chi(n)=q^{-1}\sum_{a\bmod q}\chi(a)e^{2\pi ian/q}\) be the inverse [[?c:discrete Fourier transform on a finite cyclic group|discrete Fourier transform]]. With \(\vartheta_c(u)=\sum_{n\ge1}c(n)w_j(nu)\) as in [[proofs/grh/reduction-zeros/theta-series-of-coefficients|the definition of theta series]]:

1. \(t\,\lvert\vartheta_\chi(t)\rvert=\bigl\lvert\vartheta_{\check\chi}\bigl(1/(qt)\bigr)\bigr\rvert\); more precisely \(\vartheta_{\check\chi}(1/(qt))=i^{\,j}\,t\,\vartheta_\chi(t)\).
2. \(\lvert\vartheta_\chi(t)\rvert\le3\,e\,q\,e^{-t}\).

## Proof

*Poisson summation for the weight (cited step).* For real \(a\) and \(T>0\) there is a real \(S\) with
\[
\sum_{n\in\mathbb{Z}}w_j\bigl((n+a)T\bigr)=S,\qquad\sum_{n\in\mathbb{Z}}e^{2\pi ian}\,w_j(n/T)=i^{\,j}\,T\,S .
\]
This is the [[?c:Poisson summation formula|Poisson summation formula]] for the Gaussian (\(j=0\)) and for \(ze^{-\pi z^2}\) (\(j=1\)); in the source it is read off from the functional equations of the even and odd Jacobi theta kernels in the Mathlib library (`New.poisson_summation_gaussianMonomial`). This step is not reproved here.

1. Apply this to each class \(a\bmod q\), with shift \(a/q\) and \(T=qt\), giving numbers \(S_a\); multiply by \(\chi(a)\) and add. Splitting \(\mathbb{Z}\) into classes modulo \(q\), the first sums give \(\sum_{n\in\mathbb{Z}}\chi(n)w_j(nt)=\sum_a\chi(a)S_a\), and the second, divided by \(q\), give \(\sum_{n\in\mathbb{Z}}\check\chi(n)w_j(n/(qt))=i^{\,j}t\sum_a\chi(a)S_a\). Both \(n\mapsto\chi(n)w_j(nt)\) and \(n\mapsto\check\chi(n)w_j(n/(qt))\) are even in \(n\) (as \(\chi\) and \(\check\chi\) have parity \(j\), like \(w_j\)) and vanish at \(n=0\) (\(\chi(0)=0\) since \(q\ne1\); \(\check\chi(0)=q^{-1}\sum_a\chi(a)=0\)). So each sum over \(\mathbb{Z}\) is twice the sum over \(n\ge1\), and \(\vartheta_{\check\chi}(1/(qt))=i^{\,j}t\,\vartheta_\chi(t)\).

2. If \(t\ge1\), the trivial bound gives \(\lvert\vartheta_\chi(t)\rvert\le3e^{-t}/t\le3eqe^{-t}\). If \(t\le1\): \(\lvert\check\chi(n)\rvert\le1\), so by part 1 and the trivial bound at \(1/(qt)\),
\(t\lvert\vartheta_\chi(t)\rvert\le3e^{-1/(qt)}\,qt\le3qt\le3qt\,e^{1-t}\). \(\blacksquare\)

## References

1. Lean: `New.poisson_summation_gaussianMonomial`, `New.gaussianTheta_poisson_summation`, `New.norm_gaussianTheta_char_le` in `src/Lib/Analytic/DirichletTheta.lean`.
