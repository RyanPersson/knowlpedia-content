+++
id = "langlands/local-langlands-compatibilities"
title = "Compatibility properties of local Langlands"
kind = "knowl"
summary = "The structural conditions relating representation operations, local factors, and local Langlands parameters."
aliases = ["LLC compatibilities", "properties characterizing local Langlands"]
domains = ["langlands", "harmonic-analysis"]
section_mode = "progressive"
+++

A [[langlands/local-langlands-correspondence|local Langlands
correspondence]] is expected to commute with the natural structures on its two
sides. For a representation \(\pi\) with parameter \(\varphi_\pi\), the
standard compatibilities include:

- unramified representations correspond to their
  [[langlands/satake-parameter|Satake parameters]];
- tempered and essentially square-integrable representations correspond to
  tempered and discrete parameters;
- central characters are obtained from the parameter through the center of
  the \(L\)-group and local class field theory;
- twisting \(\pi\) by a character twists \(\varphi_\pi\) by the corresponding
  one-dimensional parameter;
- contragredients correspond to the dual, or Chevalley-transformed, parameter;
- [[lie-groups/langlands-quotient|Langlands quotients]] of normalized parabolic induction correspond to the
  associated Levi parameters embedded in \({}^LG\);
- local \(L\)-, \(\varepsilon\)-, and \(\gamma\)-factors agree whenever both
  sides have an intrinsic definition.

## Theorem versus characterization

For \(\operatorname{GL}_n\), equality of Rankin–Selberg local factors,
together with elementary compatibilities, characterizes the established
correspondence. For a general [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]], not all required factors have
an intrinsic definition, and many entries in the list remain conjectural.

## Refined compatibilities

The [[langlands/refined-local-langlands-correspondence|refined
correspondence]] adds transformation laws for changing a [[langlands/whittaker-datum|Whittaker datum]] or
rigidifying cocycle, compatibility with automorphisms and homomorphisms of
groups, and endoscopic character identities. These data distinguish
parametrizations that the basic finite-to-one map cannot distinguish.

## Normalization discipline

The displayed principles do not remove normalization choices. Reciprocity
maps, geometric versus arithmetic Frobenius, normalized induction,
Whittaker data, additive characters, and [[harmonic-analysis/haar-measure|Haar measures]] must be fixed
consistently before an equality of factors or packet labels is meaningful.

## References

1. Tasho Kaletha, “Representations of reductive groups over local fields,”
   §2.3, 2022. [arXiv](https://arxiv.org/abs/2201.07741).
2. Michael Harris, “On the local Langlands correspondence,” 2003.
   [arXiv](https://arxiv.org/abs/math/0304324).
