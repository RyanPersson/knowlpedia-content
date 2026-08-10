+++
id = "langlands-letter/knowls/global-local-fields-completions"
title = "Global and local fields; completions"
kind = "knowl"
summary = "Number and global function fields, their places, and the corresponding locally compact completions."
aliases = ["global-local-fields-completions", "Global and Local Fields; Completions"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/global-local-fields-completions.md"
section_mode = "progressive"
+++

A **global field** is either a number field, meaning a finite extension of
\(\mathbb Q\), or a global function field, meaning a finite extension of
\(\mathbb F_q(t)\), equivalently the function field of a smooth projective
geometrically connected curve over a [[algebra-fields-galois/finite-field|finite field]].

A **place** \(v\) is an [[shared-foundations/equivalence-class|equivalence class]] of nontrivial absolute values. The
completion is denoted \(F_v\).

## Number fields

A number field has:

- real and complex archimedean places, with completions \(\mathbb R\) or
  \(\mathbb C\);
- nonarchimedean places, whose completions are finite extensions of
  \(\mathbb Q_p\).

## Function fields

Every place of a global function field is nonarchimedean and corresponds to
a [[algebraic-geometry-foundations/closed-point|closed point]] of its projective curve. Its completion is a finite extension
of a Laurent-series field \(\mathbb F_q((t))\).

## Local fields

A **local field** is a nondiscrete [[topology/locally-compact-space|locally compact]] topological field.
In the Langlands program it is often useful to state separately whether the
field is archimedean, nonarchimedean of characteristic \(0\), or
nonarchimedean of positive characteristic, since representation-theoretic
and geometric constructions differ.

## Relation to the letter

The 1967 letter works with number fields. The modern function-field program
uses the parallel local–global structure together with the geometry of the
underlying curve, leading to
[[langlands/lafforgue-global-parameterization|Lafforgue's global
parameterization]].

## References

1. John W. S. Cassels and Albrecht Fröhlich, eds.,
   *Algebraic Number Theory*, Academic Press, 1967.
2. Michael Rosen, *Number Theory in Function Fields*, Springer, 2002.
