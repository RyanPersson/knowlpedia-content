+++
id = "algebraic-geometry-foundations/tilt-and-untilt"
title = "Tilt and untilt of a perfectoid field"
kind = "definition"
summary = "The passage between perfectoid fields of mixed and positive characteristic via inverse-limit Frobenius."
aliases = ["tilting equivalence", "perfectoid tilt", "untilt", "K-flat"]
domains = ["algebraic-geometry-foundations", "number-theory", "langlands"]
prerequisites = ["algebraic-geometry-foundations/perfectoid-field", "algebraic-geometry-foundations/perfectoid-space", "topology/topological-space", "langlands-letter/knowls/galois-extension-and-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(K\) be a [[algebraic-geometry-foundations/perfectoid-field|perfectoid
field]] of residue characteristic \(p\).  Its **tilt** is the
characteristic-\(p\) field whose ring of integers has multiplicative
presentation

\[
\mathcal O_{K^\flat}
=\varprojlim_{x\mapsto x^p}\mathcal O_K/p.
\]

Addition is reconstructed from the inverse-limit multiplication.  The map
\(x\mapsto x^\sharp\) sends a compatible sequence to its multiplicative limit
in \(K\); it is multiplicative but generally not additive.

An **untilt** of a perfectoid field \(L\) of characteristic \(p\) is a
perfectoid field \(K\), often of characteristic \(0\), equipped with an
identification \(K^\flat\simeq L\).  A field can have many nonisomorphic
untilts.

## Tilting equivalence

Tilting induces equivalences between finite étale extensions of \(K\) and
\(K^\flat\), hence an isomorphism of their
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois groups]].
It also induces an equivalence between
[[algebraic-geometry-foundations/perfectoid-space|perfectoid spaces]] over the
two fields and
identifies their underlying [[topology/topological-space|topological spaces]]
and étale sites.

## Untilts and the Fargues–Fontaine curve

Primitive ideals in [[langlands/fontaine-period-rings|period rings]], or
equivalently suitable points of the
[[langlands/fargues-fontaine-curve|Fargues–Fontaine curve]], encode untilts of
a fixed characteristic-\(p\) perfectoid field.  This turns the curve into a
parameter space for characteristic-zero realizations.

## References

1. Peter Scholze, “Perfectoid spaces,” *Publications Mathématiques de l'IHÉS*
   116 (2012), 245–313. [arXiv](https://arxiv.org/abs/1111.4914).
2. Laurent Fargues and Jean-Marc Fontaine, *Courbes et fibrés vectoriels en
   théorie de Hodge \(p\)-adique*, Astérisque 406, 2018.
