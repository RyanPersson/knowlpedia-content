+++
id = "langlands/ramified-geometric-langlands"
title = "Ramified geometric Langlands"
kind = "definition"
summary = "A geometric Langlands problem with fixed local singularity data on the spectral side and matching level and equivariance data on the automorphic side."
aliases = ["geometric Langlands with ramification"]
domains = ["langlands"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/pointed-algebraic-curve", "langlands/ramification-of-g-local-system", "langlands/level-structure-on-g-bundle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((X,D)\) be a
[[algebraic-geometry-foundations/pointed-algebraic-curve|pointed smooth
projective curve]] and set \(U=X\setminus D\). A **ramified geometric
Langlands problem** consists of:

1. a specified [[langlands/ramification-of-g-local-system|local condition]]
   for \(\widehat G\)-local systems at every point of \(D\);
2. a matching [[langlands/level-structure-on-g-bundle|level subgroup]] for
   \(G\)-bundles at every point of \(D\); and
3. the equivariance or character condition imposed on automorphic sheaves.

The ramified correspondence is the resulting comparison between the
spectral sheaf category on the moduli of such local systems and the
automorphic sheaf category on the moduli of bundles with those level
structures. The local data are part of the definition: “ramified geometric
Langlands” does not name a single pair of categories without them.

## Tame examples

For [[langlands/regular-singular-connection|regular-singular]] local systems,
one may prescribe monodromy [[algebra-groups/conjugacy-class|conjugacy classes]] at punctures. Borel or Iwahori
level structures are common automorphic counterparts. The precise
correspondence depends on whether monodromy is semisimple, unipotent, or
carries additional residue data.

## Wild examples

[[langlands/irregular-singular-connection|Irregular connections]] require
formal types and [[langlands/stokes-data|Stokes data]]. Their automorphic
counterparts use deeper level structures and character sheaves.

## The projective line

An ordinary complex local system on unmarked \(\mathbb P^1\) has trivial
monodromy because the analytic sphere is [[topology/simply-connected-space|simply connected]]. If
\(U=\mathbb P^1\setminus\{x_1,\ldots,x_n\}\), then
\[
\pi_1(U)=
\langle m_1,\ldots,m_n\mid m_1m_2\cdots m_n=1\rangle,
\]
so prescribed local monodromies produce nontrivial ramified spectral data. A
rank-one geometric Langlands equivalence is known for \(SL_2\) and \(PGL_2\)
on the three-punctured [[algebraic-geometry-foundations/projective-line|projective line]] with
[[langlands/tame-ramification|tame ramification]].

## References

1. David Nadler and Zhiwei Yun, “Geometric Langlands correspondence for
   \(SL(2)\), \(PGL(2)\) over the pair of pants,” *Compositio Mathematica*
   155 (2019), 324–371.
   [arXiv](https://arxiv.org/abs/1610.08398).
2. Edward Frenkel and Benedict Gross, “A rigid irregular connection on the
   projective line,” *Annals of Mathematics* 170 (2009), 1469–1512.
   [arXiv](https://arxiv.org/abs/0901.2163).
