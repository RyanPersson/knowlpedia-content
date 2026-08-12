+++
id = "langlands-letter/knowls/chevalley-basis"
title = "Chevalley basis"
kind = "definition"
summary = "A root-adapted basis of a split semisimple Lie algebra with normalized integral bracket constants."
aliases = ["chevalley-basis", "Chevalley Basis"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/chevalley-basis.md"
section_mode = "progressive"
+++

Let \(\mathfrak g\) be a split [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]] over a
characteristic-zero field, with split [[lie-groups/cartan-subalgebra|Cartan subalgebra]] \(\mathfrak t\),
[[lie-groups/root-system|root system]] \(\Phi\), and [[lie-groups/simple-root|simple roots]]
\(\Delta=\{\alpha_1,\ldots,\alpha_\ell\}\). A **Chevalley basis** is

\[
\{h_1,\ldots,h_\ell\}\cup\{e_\alpha\}_{\alpha\in\Phi},
\]

where \(h_i\) represents the
[[langlands-letter/knowls/coroots-and-pairing|simple coroot]] and
\(e_\alpha\) spans
\(\mathfrak g_\alpha\), normalized so that

\[
[h_i,e_\alpha]
=
\langle\alpha,\alpha_i^\vee\rangle e_\alpha,
\qquad
[e_\alpha,e_{-\alpha}]=h_\alpha,
\]

and

\[
[e_\alpha,e_\beta]
=
N_{\alpha,\beta}e_{\alpha+\beta}
\]

when \(\alpha+\beta\) is a root, with
\(N_{\alpha,\beta}\in\mathbb Z\).

## Root-string normalization

The root-vector signs can be chosen so that

\[
N_{\alpha,\beta}=\pm(p+1),
\]

where \(p\) is the largest nonnegative integer such that
\(\beta-p\alpha\in\Phi\). The sign choices are not canonical, but the
existence of integral structure constants is.

## Integral Lie form

The \(\mathbb Z\)-span

\[
\mathfrak g_{\mathbb Z}
=
\bigoplus_i\mathbb Zh_i
\oplus
\bigoplus_{\alpha\in\Phi}\mathbb Ze_\alpha
\]

is closed under the bracket. It is the Chevalley Lie form. Constructing
integral representations and a [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] scheme additionally uses
divided powers and the full root datum; see the
[[langlands-letter/knowls/chevalley-lattice-integral-model|integral-model
page]].

## Role in the letter

Root-vector normalization rigidifies the
[[langlands-letter/knowls/pinned-automorphisms|pinning]] and gives integral
structures from which almost-all local integral models and
[[harmonic-analysis/hecke-algebra-locally-compact-group-pair|spherical Hecke
algebras]] can be obtained.

## References

1. Claude Chevalley, “Sur certains groupes simples,” *Tohoku Mathematical
   Journal* 7 (1955), 14–66.
2. Robert Steinberg, *Lectures on Chevalley Groups*, AMS, 2016.
