+++
id = "algebraic-geometry-foundations/quasi-split-reductive-group"
title = "Quasi-split reductive group"
kind = "definition"
summary = "A connected reductive group having a Borel subgroup defined over the base field."
aliases = ["quasisplit reductive group", "quasi-split group", "quasisplit group"]
domains = ["algebraic-geometry-foundations", "langlands", "algebra-groups"]
section_mode = "progressive"
+++

Let \(k\) be a field and let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(k\)-group]]. The
group \(G\) is **quasi-split over \(k\)** if it contains a
[[algebraic-geometry-foundations/borel-subgroup|Borel subgroup]] defined over
\(k\).

Every [[langlands-letter/knowls/split-reductive-group|split reductive group]]
is quasi-split, but the converse can fail: a quasi-split group need not have
a split
[[langlands-letter/knowls/maximal-torus-weight-lattice|maximal torus]]. After
a finite [[algebra-fields-galois/separable-extension|separable extension]]
every connected reductive group becomes split and hence quasi-split.

## Role among inner forms

An [[langlands-letter/knowls/galois-descent-forms|inner class]] over a
[[langlands-letter/knowls/global-local-fields-completions|local or global
field]] has a quasi-split representative, unique up to isomorphism. The
[[langlands/l-group|\(L\)-group]] and the basic
[[langlands/local-l-parameter|local Langlands parameter space]] are normally
attached
to this representative.  Describing packets on the other inner forms requires
additional data, such as a [[langlands/rigid-inner-twist|rigid inner twist]].

## Borel data and Galois action

For a quasi-split group one may choose a Borel pair \((B,T)\) over \(k\).  The
resulting
[[langlands-letter/knowls/galois-extension-and-group|Galois action]] on the
[[langlands-letter/knowls/roots-weights-weyl|based root datum]] defines the
[[langlands-letter/knowls/pinned-automorphisms|pinned action]] used
in the [[langlands/l-group|L-group]].  Different rational Borel pairs are
conjugate by \(G(k)\) under the usual hypotheses, so the resulting outer action
is canonical.

## References

1. Armand Borel and Jacques Tits, “Groupes réductifs,” *Publications
   Mathématiques de l'IHÉS* 27 (1965), 55–150.
   [Numdam](https://www.numdam.org/item/PMIHES_1965__27__55_0/).
2. Brian Conrad, *Reductive Group Schemes*, §§5.2–5.3.
   [Author notes](https://math.stanford.edu/~conrad/papers/luminysga3.pdf).
