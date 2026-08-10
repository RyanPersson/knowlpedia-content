+++
id = "harmonic-analysis/test-function-space-local-group"
title = "Test-function space on a local group"
kind = "definition"
summary = "The compactly supported smooth functions on an archimedean Lie group or locally constant compactly supported functions on a locally profinite group."
aliases = ["test functions on a local group", "C_c infinity of a local group", "local-group test-function space"]
domains = ["harmonic-analysis", "langlands", "functional-analysis"]
section_mode = "progressive"
+++

Let \(F\) be a [[langlands-letter/knowls/global-local-fields-completions|local
field]] and let \(G(F)\) be a local group. Its **test-function space** is
denoted

\[
\mathcal D(G(F))=C_c^\infty(G(F)).
\]

The superscript has two different, category-dependent meanings:

- if \(F\) is archimedean and \(G(F)\) is a
  [[fiber-bundles/lie-group|Lie group]], it consists of smooth complex
  functions with compact support;
- if \(F\) is nonarchimedean and \(G(F)\) is
  [[topology/locally-profinite-group|locally profinite]], it consists of
  locally constant complex functions with compact support.

In both cases \(\mathcal D(G(F))\) carries its standard locally convex
inductive-limit topology. This topology, not only the underlying vector
space, determines what it means for a
[[harmonic-analysis/distribution-local-group|distribution]] to be continuous.

## Nonarchimedean description

A nonarchimedean test function is fixed by translation by some compact open
subgroup on each chosen side. Spaces with fixed compact support and fixed
open invariance are finite-dimensional, and their directed union gives
\(C_c^\infty(G(F))\). The notation “smooth” therefore means locally constant;
it does not refer to derivatives.

For a compact open subgroup \(K\), the bi-\(K\)-invariant test functions form
the [[harmonic-analysis/hecke-algebra-locally-compact-group-pair|Hecke
algebra]] \(\mathcal H(G(F),K)\). Allowing \(K\) to shrink recovers the full
test-function space.

## Convolution and measures

After choosing a [[harmonic-analysis/haar-measure|Haar measure]], test
functions can be convolved. Changing the Haar measure rescales formulas that
identify functions with measures, so trace formulas,
[[langlands/orbital-integral|orbital integrals]], and character distributions
must state compatible measure normalizations.

## Adelic form

For an [[algebraic-geometry-foundations/algebraic-group|algebraic group]] over
a global field, the adelic test-function space is a restricted tensor product
of the local spaces. At almost every finite place
where the group is unramified, one fixes a hyperspecial subgroup \(K_v\) and
uses the distinguished function \(1_{K_v}\). This is the group analogue of the
[[harmonic-analysis/restricted-tensor-product-test-functions|restricted tensor
product of local Schwartz–Bruhat spaces]].

## Scope warning

The [[functional-analysis/test-function-space|Euclidean test-function space]]
\(\mathcal D(\Omega)\) is the archimedean open-set model, not a definition of
locally constant \(p\)-adic test functions. An arbitrary
[[topology/locally-compact-group|locally compact group]] that is neither a Lie
group nor locally profinite has no canonical \(C_c^\infty\) until an
additional [[fiber-bundles/smooth-structure|smooth structure]] or
test-function category is specified.

## References

1. François Bruhat, “Distributions sur un groupe localement compact et
   applications à l'étude des représentations des groupes \(p\)-adiques,”
   *Bulletin de la Société Mathématique de France* 89 (1961), 43–75.
   [Numdam](https://www.numdam.org/item/BSMF_1961__89__43_0/).
2. James Arthur, “An introduction to the trace formula,” in *Harmonic
   Analysis, the Trace Formula, and Shimura Varieties*, Clay Mathematics
   Proceedings 4, 2005, §§1–3.
   [Clay](https://www.claymath.org/library/cw/arthur/pdf/61.pdf).
