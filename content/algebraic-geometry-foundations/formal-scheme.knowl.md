+++
id = "algebraic-geometry-foundations/formal-scheme"
title = "Formal scheme"
kind = "definition"
summary = "A locally topologically ringed space locally modeled on formal spectra of complete adic rings."
aliases = ["adic formal scheme", "EGA formal scheme"]
domains = ["algebraic-geometry-foundations", "formal-groups"]
prerequisites = ["algebraic-geometry-foundations/locally-topologically-ringed-space", "algebraic-geometry-foundations/formal-spectrum", "algebra-topological/adic-ring"]
dependency_review_count = 1
section_mode = "progressive"
+++

An **adic formal scheme** is a
[[algebraic-geometry-foundations/locally-topologically-ringed-space|locally
topologically ringed space]] locally isomorphic to a
[[algebraic-geometry-foundations/formal-spectrum|formal spectrum]]
\[
\operatorname{Spf}(A),
\]
where \(A\) is a complete and separated
[[algebra-topological/adic-ring|adic ring]]. A morphism of formal schemes is
a morphism of locally topologically ringed spaces whose maps on local
sections are continuous.

## Infinitesimal presentation

Locally, if \(A\) has an
[[algebra-topological/ideal-of-definition|ideal of definition]] \(I\), the
formal scheme packages
the compatible tower
\[
\operatorname{Spec}(A/I)
\hookrightarrow
\operatorname{Spec}(A/I^2)
\hookrightarrow\cdots .
\]
The first term is a **scheme of definition**, while the higher terms retain
progressively thicker infinitesimal neighborhoods. It is not generally the
reduction: \(\operatorname{Spec}(A/I)\) can itself be nonreduced.
Formal schemes can therefore remember an entire completed neighborhood even
when their underlying topological spaces are small.

## Ordinary schemes and formal completions

An ordinary [[algebraic-geometry-foundations/scheme|scheme]] becomes a formal
scheme by giving its [[algebraic-geometry-foundations/structure-sheaf|structure sheaf]] the discrete topology. More importantly,
completing a scheme along a closed subscheme produces a genuinely formal
scheme. For a [[algebraic-geometry-foundations/group-scheme|group scheme]], completion along the identity produces a
[[formal-groups/formal-completion-at-identity|formal group]].

## Group objects

Finite products exist in the category of formal schemes over a base. Hence one
can form [[algebra-category-theory/group-object|group objects]] in this
category. This coordinate-free definition is the natural home of
[[formal-groups/formal-group|formal groups]]; a [[formal-groups/formal-group-law|formal group law]] appears only
after choosing parameters on the underlying formal scheme.

## Convention

There are broader frameworks of formal schemes and formal algebraic spaces,
with weaker hypotheses on the topology. This knowl fixes the classical
adic/EGA setting needed for complete power-series rings. Statements using a
broader convention should say so explicitly.

## References

1. The Stacks Project Authors, “Formal schemes à la EGA.” [Section 87.2, Tag 0AHY](https://stacks.math.columbia.edu/tag/0AHY). Relevant: definitions of affine formal schemes, formal schemes, and morphisms.
2. Alexander Grothendieck and Jean Dieudonné, *Éléments de géométrie algébrique I: Le langage des schémas*, Publications Mathématiques de l’IHÉS 4 (1960). Relevant: Chapter 0, §7.
