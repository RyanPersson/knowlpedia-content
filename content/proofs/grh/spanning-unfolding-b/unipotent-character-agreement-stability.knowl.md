+++
id = "proofs/grh/spanning-unfolding-b/unipotent-character-agreement-stability"
title = "Unipotent character, agreeing residues, stable sets and terms of a link"
kind = "definition"
summary = "The character of the finite adelic unipotent group built from the entries above the diagonal of the frame block, the residues that respect it, stable sets of terms, and the terms of nonzero discriminant with a given link."
aliases = ["unipotent character", "Agrees", "stable set of terms", "terms of a link", "self-dual character"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.selfDualChar", "New.Filling.ideleM", "New.Filling.unipotentChar", "New.Filling.Agrees", "New.Filling.IsStable", "New.Filling.termsOfLink"]
lean_files = ["src/New/Spanning/Unfolding/Setup.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]], with [[proofs/grh/spanning-unfolding-b/filling-unitary-groups|groups]] \(G(E)\), \(G_{\mathrm{fin}}\), [[proofs/grh/spanning-unfolding-b/filling-level-and-reduction|lattice stabiliser \(K\), residue group \(\bar G\) and reduction]] \(u\mapsto\bar u\), and let \(\mathsf{U}\) denote the [[?lean:New.Shape.Form.besselU|Bessel unipotent group]] in each of these groups. Let \(\psi_f\) be the [[?lean:New.ψf|standard additive character of the finite adeles]] of \(E\) (trivial on \(\widehat{\mathcal{O}}\), equal to \(e^{2\pi i\operatorname{Tr}_{E/\mathbb{Q}}a}\) on \(a\in E\)).

* The **self-dual character** is \(\psi_S(x)=\psi_f(-x/\varpi)\), an [[?c:additive character|additive character]] of \(\mathbb{A}_f\) with values in \(\mathbb{C}\).
* For \(u\in G_{\mathrm{fin}}\), let \(\sigma(u)=\sum_{a=0}^{\varrho-1}u_{f_a,f_{a+1}}\) be the [[?lean:New.simpleRootSum|sum of the entries just above the diagonal]] of the frame block of \(u\). The **unipotent character** is
\[
\psi_{\mathsf U}(u)=\psi_S\bigl(\sigma(u)/M\bigr)=\psi_f\bigl(-\sigma(u)/(M\varpi)\bigr).
\]
* An element \(s\in\bar G\) **agrees** if for all \(u,u'\in K\cap\mathsf{U}\) with \(\bar u\,s=s\,\bar u'\) one has \(\psi_{\mathsf U}(u)=\psi_{\mathsf U}(u')\).
* A set \(T\subset G(E)\) is **stable** if for all \(u,u'\in\mathsf{U}(E)\) and \(\gamma\in G(E)\): \(u^{-1}\gamma u'\in T\) if and only if \(\gamma\in T\).
* For an \(E\)-subspace \(\Lambda\) of \((E^{\kappa\sqcup\{z\}})^2\), the **terms of link \(\Lambda\)** are the \(\gamma\in G(E)\) with [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|discriminant]] \(\operatorname{disc}(\gamma)\ne0\) whose [[?lean:New.link|link]] is \(\Lambda\).

## Remarks

Because \(\varpi\) generates the different, \(\widehat{\mathcal{O}}\) is its own dual for \(\psi_S\). The function \(\psi_{\mathsf U}\) is defined on all of \(G_{\mathrm{fin}}\) but is multiplicative only on the Bessel subgroup, where \(\sigma\) is additive ([[?lean:New.simpleRootSum_mul|additivity of the simple root sum]]).

## References

1. Lean: `New.Filling.selfDualChar`, `New.Filling.unipotentChar`, `New.Filling.Agrees`, `New.Filling.IsStable`, `New.Filling.termsOfLink` in `src/New/Spanning/Unfolding/Setup.lean`.
