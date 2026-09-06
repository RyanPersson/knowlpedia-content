+++
id = "langlands/shtuka"
title = "Shtuka"
kind = "knowl"
summary = "A vector bundle on a curve equipped with a Frobenius isomorphism away from finitely many moving legs."
aliases = ["chtouca", "Drinfeld shtuka", "multiple-leg shtuka"]
domains = ["langlands", "algebraic-geometry-foundations", "number-theory"]
prerequisites = ["algebraic-geometry-foundations/smooth-projective-curve", "algebra-fields-galois/finite-field", "algebraic-geometry-foundations/locally-free-sheaf", "algebra-fields-galois/frobenius-endomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be a [[algebraic-geometry-foundations/smooth-projective-curve|smooth projective curve]] over the
[[algebra-fields-galois/finite-field|finite field]] \(\mathbb F_q\), let
\(S\) be an \(\mathbb F_q\)-scheme, and let \(x_i:S\to X\) be finitely many
**legs**. In
the multiple-leg form, a rank-\(n\) **shtuka** consists of an
[[algebraic-geometry-foundations/locally-free-sheaf|algebraic vector bundle]]
\(\mathcal E\) on \(X\times S\) and an isomorphism

\[
\varphi:
\mathcal E\big|_{(X\times S)\setminus\bigcup_i\Gamma_{x_i}}
\xrightarrow{\ \sim\ }
({\rm id}_X\times{\rm Frob}_S)^*\mathcal E
\big|_{(X\times S)\setminus\bigcup_i\Gamma_{x_i}},
\]

with prescribed bounds on the relative positions at the graphs
\(\Gamma_{x_i}\). Here \({\rm Frob}_S\) denotes the
[[algebra-fields-galois/frobenius-endomorphism|absolute Frobenius
endomorphism]] of \(S\).

## Frobenius bundle with controlled singularities

Without legs, \(\varphi\) is a global Frobenius descent datum. The legs allow
\(\varphi\) to have controlled zeros or poles, expressed invariantly as
[[langlands/hecke-modification|modifications]] of vector bundles. Classical
Drinfeld shtukas often have two
distinguished legs, customarily called a zero and a pole.

The rank-\(n\) definition is the
\(\operatorname{GL}_n\)-case of a [[langlands/g-shtuka|\(G\)-shtuka]].

## Moduli interpretation

Allowing the legs and bundle to vary gives an [[algebraic-geometry-foundations/algebraic-stack|algebraic stack]] over \(X^I\).
Bounds by [[langlands/dominant-coweight|dominant coweights]] produce
finite-type truncations after imposing level and
[[algebraic-geometry-foundations/harder-narasimhan-filtration|Harder–Narasimhan]]
conditions. The fibers carry actions of Hecke
correspondences and [[langlands/partial-frobenius-on-shtukas|partial Frobenius morphisms]].

## Arithmetic role

Drinfeld used shtukas to prove the [[langlands/global-langlands-reciprocity|global Langlands correspondence]] for
\(\operatorname{GL}_2\) over
[[algebra-fields-galois/global-function-field|function fields]];
Laurent Lafforgue extended
this to \(\operatorname{GL}_n\). Vincent Lafforgue's construction for
general [[algebraic-geometry-foundations/reductive-algebraic-group|reductive groups]] uses multiple-leg \(G\)-shtukas, the
[[langlands/geometric-satake-equivalence|geometric Satake equivalence]], and
[[langlands/excursion-operator|excursion operators]].

## Not the same as a local shtuka

A [[langlands/local-shtuka|local shtuka]] in the Fargues–Fontaine setting is
a local modification object over a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]]. It is inspired
by the same Frobenius-and-modification pattern but lives in a different
geometry.

## References

1. V. G. Drinfeld, “Moduli varieties of \(F\)-sheaves,” *Functional
   Analysis and Its Applications* 21 (1987), 107–122.
   [DOI](https://doi.org/10.1007/BF01078026).
2. Vincent Lafforgue, “Chtoucas pour les groupes réductifs et
   paramétrisation de Langlands globale,” 2018.
   [arXiv](https://arxiv.org/abs/1209.5352).
