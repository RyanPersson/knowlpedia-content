+++
id = "algebraic-geometry-foundations/perfect-complex"
title = "Perfect complex"
kind = "definition"
summary = "A complex locally quasi-isomorphic to a bounded complex of finite-rank projective modules."
aliases = ["perfect object", "strictly perfect complex", "Perf(X)"]
domains = ["algebraic-geometry-foundations", "algebra-homological", "langlands"]
section_mode = "progressive"
+++

Let \((X,\mathcal O_X)\) be a
[[algebraic-geometry-foundations/ringed-space|ringed space]], scheme, or
[[algebraic-geometry-foundations/algebraic-stack|algebraic stack]]. A
[[algebra-homological/cochain-complex|complex]] \(E\) of
[[algebraic-geometry-foundations/sheaf-of-modules|\(\mathcal O_X\)-modules]]
is **perfect** if every point has a neighborhood \(U\) on which \(E|_U\) is
quasi-isomorphic to a bounded complex of finite-rank
[[algebraic-geometry-foundations/locally-free-sheaf|locally free]]
\(\mathcal O_U\)-modules.

For a ring \(A\), this says that \(E\in D(A)\) is quasi-isomorphic to a bounded
complex of finitely generated
[[algebra-modules/projective-module|projective \(A\)-modules]].

## Characterizations

Under standard quasi-compactness and quasi-separatedness hypotheses, perfect
complexes are precisely the compact objects of the derived category of
[[algebraic-geometry-foundations/quasi-coherent-sheaf|quasi-coherent]]
complexes. They are also the dualizable objects for the
derived tensor product.  The derived dual is

\[
E^\vee=R\mathcal Hom(E,\mathcal O_X).
\]

The perfect complexes form a stable
[[algebra-category-theory/symmetric-monoidal-category|symmetric monoidal
category]]
\(\operatorname{Perf}(X)\).

## Spectral actions

For the derived [[langlands/stack-of-l-parameters|stack of local
\(L\)-parameters]], the category
\(\operatorname{Perf}(\operatorname{LocSys}_{\widehat G})\) acts on sheaves on
[[langlands/g-bundle-on-fargues-fontaine-curve|\(\operatorname{Bun}_G\)]] in
the
[[langlands/spectral-action|Fargues–Scholze spectral action]].  Using perfect
rather than arbitrary quasi-coherent complexes provides dualizability and
finite behavior needed by the action.

## References

1. The Stacks Project Authors, “Cohomology of Sheaves,” §20.49, “Perfect
   complexes.” [Stacks Project](https://stacks.math.columbia.edu/tag/08CL).
2. R. W. Thomason and Thomas Trobaugh, “Higher algebraic K-theory of schemes
   and of derived categories,” in *The Grothendieck Festschrift III*,
   Progress in Mathematics 88, 1990, 247–435.
