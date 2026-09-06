+++
id = "lie-groups/spherical-principal-series"
title = "Spherical principal series representation"
kind = "definition"
summary = "The spherical principal series is the normalized minimal-parabolic induction of a character of the split factor with trivial compact and nilpotent data."
aliases = ["class-one principal series", "unramified real principal series"]
domains = ["lie-groups", "harmonic-analysis"]
prerequisites = ["lie-groups/real-reductive-lie-group", "lie-groups/maximal-compact-subgroup-real-reductive-group", "lie-groups/minimal-parabolic-subgroup", "lie-groups/normalized-parabolic-induction", "lie-groups/principal-series-representation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a [[lie-groups/real-reductive-lie-group|real reductive group]],
\(K\) a
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]], and
\(P=MAN\) a [[lie-groups/minimal-parabolic-subgroup|minimal parabolic]] in
Langlands form. For \(\lambda\in\mathfrak a_{\mathbb C}^{*}\), the
**spherical principal series** is the
[[lie-groups/normalized-parabolic-induction|normalized induction]]
\[
I(\lambda)=\operatorname{Ind}_{P}^{G}
   \bigl(1_M\otimes e^\lambda\otimes 1_N\bigr).
\]
Its restriction to \(K\) contains the trivial \(K\)-type with multiplicity one;
a nonzero vector on this line is called spherical. Thus this is precisely the
[[lie-groups/principal-series-representation|principal-series family]] induced
from trivial \(M\)-data, rather than an arbitrary principal series that happens
to have a special parameter.

## Spherical vector and functions

In the compact picture the spherical vector is represented by the constant
function on \(K/M\). Its normalized matrix coefficient is an elementary
spherical function on \(G/K\), so the family connects principal-series
representation theory with harmonic analysis on the Riemannian symmetric
space.

## Example and near-miss

For \(G=\mathrm{SL}(2,\mathbb R)\), normalized induction from a character of
the positive diagonal subgroup, trivial on the compact factor of the minimal
parabolic, gives the spherical principal series and an even \(K\)-type
spectrum. Induction using the nontrivial character of the finite group \(M\)
gives a nonspherical principal series: it has no \(K\)-fixed vector and is not
part of this family.

## Conventions and scope

**Warning.** In the real-group setting, “unramified” is an analogy with
nonarchimedean representation theory; “spherical” or “class one” is more
standard. Parameter formulas change when the modular half-density is absorbed
into \(\lambda\). Reducible parameters can produce several constituents, and
the induced module itself should not be silently identified with a chosen
irreducible spherical constituent.

## References

1. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton Mathematical Series 36, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter VII on nonunitary and spherical principal series.
2. Anthony W. Knapp and Peter E. Trapa, *Representations of Semisimple Lie Groups*, Park City Mathematics Institute lecture notes, 2000. [Author PDF](https://www.math.stonybrook.edu/~aknapp/pdf-files/parkcity.pdf). Relevant: Lecture 3, pp. 42–43 on normalized induction and the compact picture of principal series.
