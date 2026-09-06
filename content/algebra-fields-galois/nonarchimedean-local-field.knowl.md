+++
id = "algebra-fields-galois/nonarchimedean-local-field"
title = "Nonarchimedean local field"
kind = "definition"
summary = "A complete discretely valued field with finite residue field."
aliases = ["non-archimedean local field", "nonarchimedean local fields", "non-archimedean local fields"]
domains = ["algebra-fields-galois", "topology", "langlands"]
prerequisites = ["algebra-fields-galois/valuation-on-a-field", "algebra-commutative/residue-field", "algebra-fields-galois/non-archimedean-absolute-value"]
dependency_review_count = 1
section_mode = "progressive"
+++

A **nonarchimedean local field** is a field \(F\) complete with respect to a
nontrivial discrete
[[algebra-fields-galois/valuation-on-a-field|valuation]] whose
[[algebra-commutative/residue-field|residue field]] is finite.

Equivalently, it is a nondiscrete locally compact field whose topology is
defined by a
[[algebra-fields-galois/non-archimedean-absolute-value|nonarchimedean absolute
value]].

## Classification by characteristic

In characteristic \(0\), \(F\) is a finite extension of \(\mathbb Q_p\) for a
unique prime \(p\), hence a
[[langlands-letter/knowls/p-adic-field|\(p\)-adic field]]. In positive
characteristic, \(F\) is isomorphic to a finite extension of
\(\mathbb F_q((t))\).

## Basic local data

The valuation determines a
[[algebra-fields-galois/valuation-ring|valuation ring]] \(\mathcal O_F\), its
maximal ideal \(\mathfrak p_F\), a finite residue field
\(k_F=\mathcal O_F/\mathfrak p_F\), and a uniformizer. The ring
\(\mathcal O_F\) is compact and open, so the additive and multiplicative
groups of \(F\) are locally profinite.

## References

1. Jean-Pierre Serre, *Local Fields*, Springer, 1979, Chapter I.
2. André Weil, *Basic Number Theory*, third edition, Springer, 1974,
   Chapter I.
