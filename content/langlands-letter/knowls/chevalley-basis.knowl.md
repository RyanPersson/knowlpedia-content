+++
id = "langlands-letter/knowls/chevalley-basis"
title = "Chevalley Basis"
kind = "definition"
summary = "A root-adapted basis of a split semisimple Lie algebra with normalized integral bracket constants."
aliases = ["chevalley-basis", "Chevalley Basis"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/chevalley-basis.md"
+++

Let \(\mathfrak g\) be a split semisimple [[lie-groups/lie-algebra|Lie algebra]] over a characteristic-zero field, with split Cartan subalgebra \(\mathfrak t\), root system \(\Phi\), and simple roots \(\Delta=\{\alpha_1,\ldots,\alpha_\ell\}\). A **Chevalley basis** is a basis
\[
\{h_1,\ldots,h_\ell\}\cup\{e_\alpha\}_{\alpha\in\Phi},
\]
where \(h_i=h_{\alpha_i}\) represents the simple coroot and \(e_\alpha\) spans the root space \(\mathfrak g_\alpha\), normalized so that
\[
[h_i,h_j]=0,\qquad
[h_i,e_\alpha]=\langle\alpha,\alpha_i^\vee\rangle e_\alpha,
\qquad
[e_\alpha,e_{-\alpha}]=h_\alpha.
\]
If \(\alpha+\beta\in\Phi\), then
\[
[e_\alpha,e_\beta]=N_{\alpha,\beta}e_{\alpha+\beta}
\quad\text{with }N_{\alpha,\beta}\in\mathbb Z;
\]
if \(\alpha+\beta\notin\Phi\) and \(\beta\ne-\alpha\), the bracket is zero.

## Root-string normalization

The signs of the root vectors may be chosen so that
\[
N_{\alpha,\beta}=\pm(p+1),
\]
where \(p\) is the largest nonnegative integer for which \(\beta-p\alpha\) is a root. These choices are not unique, but every Chevalley basis has integral structure constants.

## Integral form

The \(\mathbb Z\)-span
\[
\mathfrak g_{\mathbb Z}
=
\bigoplus_{i=1}^{\ell}\mathbb Zh_i
\oplus
\bigoplus_{\alpha\in\Phi}\mathbb Ze_\alpha
\]
is closed under the Lie bracket and is called the **Chevalley integral form**. Base change recovers \(\mathfrak g\) over the original field.

## Role in the letter

Choosing root vectors satisfying the Chevalley normalization rigidifies pinning-preserving automorphisms and supplies the integral structures used in reduction at finite places.
