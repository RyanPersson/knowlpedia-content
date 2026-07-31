+++
id = "lie-groups/furstenberg-boundary"
title = "Furstenberg boundary of a semisimple Lie group"
kind = "definition"
summary = "The compact homogeneous space obtained by quotienting a semisimple Lie group by a minimal parabolic subgroup."
aliases = ["minimal flag manifold", "G/P boundary"]
domains = ["lie-groups", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a connected noncompact real semisimple
[[fiber-bundles/lie-group|Lie group]] with finite center, and let \(P\) be a
[[lie-groups/minimal-parabolic-subgroup|minimal parabolic subgroup]]. The
**Furstenberg boundary** is the compact
[[lie-groups/homogeneous-space|homogeneous space]]
\[
\partial_F G=G/P.
\]
Different minimal parabolics are conjugate, so the resulting \(G\)-space is
well defined up to \(G\)-equivariant diffeomorphism. If \(P=MAN\) is its
[[lie-groups/langlands-decomposition-of-a-parabolic|Langlands decomposition]]
and \(K\) is the corresponding
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]],
the
[[lie-groups/iwasawa-decomposition|Iwasawa decomposition]] induces a
\(K\)-equivariant identification \(G/P\cong K/M\).

## Geometric interpretation

The space \(G/P\) is also called the minimal real flag manifold. For
\(G=\operatorname{SL}(n,\mathbb R)\), it is the space of complete flags in
\(\mathbb R^n\). For \(G=\operatorname{SL}(2,\mathbb R)\), it is
\(\mathbb{RP}^1\), which is a circle. Compactness follows from
\(G=KP\), while transitivity is built into the quotient construction
[Helgason, Chapter I].

## Role in representation theory

Functions or sections of equivariant bundles over \(G/P\) provide compact
models of spherical and more general principal-series representations.
Boundary values of eigenfunctions on the symmetric space \(G/K\) likewise
live naturally on \(G/P\). The identification \(G/P\cong K/M\) makes the
compact-group action available without discarding the full \(G\)-action.

## Terminology and scope

**Warning.** The word “boundary” here does not mean the topological boundary
of \(G\) inside a fixed compactification. It denotes a canonical compact
\(G\)-space with strong dynamical properties. This knowl uses the
Lie-theoretic quotient \(G/P\) for the semisimple class in the core and does
not define the broader dynamical boundary notion for [[topology/locally-compact-group|locally compact groups]].

## References

1. Sigurdur Helgason, *Groups and Geometric Analysis: Integral Geometry, Invariant Differential Operators, and Spherical Functions*, Mathematical Surveys and Monographs 83, American Mathematical Society, 2000. [AMS record](https://bookstore.ams.org/SURV/83). Relevant: Chapter I on \(G/K\), Iwasawa decomposition, and the boundary \(K/M\).
2. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton Mathematical Series 36, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter VII on principal-series representations and their compact picture.
