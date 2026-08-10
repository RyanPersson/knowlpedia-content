+++
id = "langlands/algebraic-automorphic-representation"
title = "Algebraic automorphic representation"
kind = "knowl"
summary = "An automorphic representation with integral archimedean infinitesimal data, with the normalization stated explicitly."
aliases = ["algebraic automorphic representations", "automorphic representation of algebraic type"]
domains = ["langlands", "number-theory", "representation-theory"]
section_mode = "progressive"
+++

An **algebraic automorphic representation** is an
[[langlands/automorphic-representation|automorphic representation]] over a
number field whose archimedean [[langlands/local-l-parameter|Langlands parameters]] have integral
infinitesimal data. This phrase is incomplete unless its normalization is
specified.

In the Buzzard–Gee terminology the two standard normalizations are
[[langlands/c-algebraic-automorphic-representation|\(C\)-algebraic]] and
[[langlands/l-algebraic-automorphic-representation|\(L\)-algebraic]]. They
differ by the half-sum of the [[lie-groups/positive-root|positive roots]].

## Classical convention for general linear groups

For an isobaric automorphic representation of
\(\operatorname{GL}_n(\mathbb A_F)\), Clozel's “algebraic” condition agrees
with the modern \(C\)-algebraic condition: its [[lie-groups/infinitesimal-character|infinitesimal character]] at
each archimedean place is that of a finite-dimensional algebraic
representation. Authors often say simply “algebraic” in this setting.

A twist by a suitable half-integral power of the norm converts the
\(C\)-normalization to the \(L\)-normalization when that twist exists. For a
general [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]], such a twist need not exist on the group itself.

## Cohomology and Galois representations

A [[langlands/cohomological-automorphic-representation|cohomological
automorphic representation]] is \(C\)-algebraic. By contrast,
\(L\)-algebraicity is the normalization naturally used when conjecturing a
Galois representation valued directly in the usual \(L\)-group. A
\(C\)-algebraic representation is expected to give a representation valued
in the associated \(C\)-group.

## Usage rule

Statements such as “algebraic automorphic representations have Galois
representations” must specify:

1. \(C\)- or \(L\)-normalization;
2. the reductive group and coefficient field;
3. regularity, cuspidality, polarization, or other hypotheses;
4. whether the claim is a theorem or a conjecture;
5. the target \(L\)-group or \(C\)-group.

## References

1. Laurent Clozel, “Motifs et formes automorphes: applications du principe
   de fonctorialité,” in *Automorphic Forms, Shimura Varieties, and
   \(L\)-Functions*, vol. I, 1990, pp. 77–159.
2. Kevin Buzzard and Toby Gee, “The conjectural connections between
   automorphic representations and Galois representations,” *Automorphic
   Forms and Galois Representations*, vol. 1, 2014.
   [arXiv](https://arxiv.org/abs/1009.0785).
