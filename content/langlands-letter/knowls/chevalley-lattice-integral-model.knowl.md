+++
id = "langlands-letter/knowls/chevalley-lattice-integral-model"
title = "Chevalley lattice and integral model"
kind = "knowl"
summary = "Integral Lie and representation lattices and the reductive Chevalley group scheme determined by a root datum."
aliases = ["chevalley-lattice-integral-model", "Chevalley Lattice and Integral Model"]
domains = ["langlands-letter"]
prerequisites = ["langlands-letter/knowls/chevalley-basis", "lie-groups/semisimple-lie-algebra", "lie-groups/universal-enveloping-algebra", "algebraic-geometry-foundations/group-scheme", "langlands-letter/knowls/roots-weights-weyl"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "langlands-letter/knowls/chevalley-lattice-integral-model.md"
section_mode = "progressive"
+++

A [[langlands-letter/knowls/chevalley-basis|Chevalley basis]] of a split
[[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]] defines a Lie lattice
\(\mathfrak g_{\mathbb Z}\) with integral structure constants. To integrate
this to representations and groups, one uses the Kostant integral form of
the universal [[lie-groups/universal-enveloping-algebra|enveloping algebra]], including divided powers, and the
Chevalley–Demazure [[algebraic-geometry-foundations/group-scheme|group
scheme]] attached to the full
[[langlands-letter/knowls/roots-weights-weyl|root datum]].

## Representation lattice

For a rational representation \(V\), a **Chevalley or admissible lattice**
is a full \(\mathbb Z\)-lattice \(V_{\mathbb Z}\subset V\) stable under the
appropriate Kostant \(\mathbb Z\)-form, equivalently under the resulting
integral
[[algebraic-geometry-foundations/group-scheme|group-scheme]] action when that
action has been constructed.

Stability merely under the Lie lattice
\(\mathfrak g_{\mathbb Z}\) is not, by itself, equivalent in every
representation to stability under the integral group scheme; divided-power
integrality is the stronger condition.

## Integral group model

A split reductive root datum determines a smooth [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] scheme
\(\mathcal G/\mathbb Z\). [[algebraic-geometry-foundations/base-change|Base change]] gives
\(\mathcal G_{\mathbb Z_p}\), and

\[
\mathcal G(\mathbb Z_p)
\subset
\mathcal G(\mathbb Q_p)
\]

is [[langlands-letter/knowls/maximal-compact-hyperspecial|hyperspecial]]. For
a reductive group originally defined over a
[[algebra-fields-galois/number-field|number field]],
such a reductive integral model exists outside a finite set of bad
places rather than canonically at every place.

## Relation to the letter

The letter uses lattices to define integral points and hence the
[[algebraic-geometry-foundations/unramified-reductive-group|unramified]]
[[harmonic-analysis/hecke-algebra-locally-compact-group-pair|spherical Hecke
algebra]] at almost all primes. Modern language separates the
Lie-algebra integral form, an integral representation lattice, and the
reductive group scheme.

## References

1. Claude Chevalley, “Sur certains groupes simples,” *Tohoku Mathematical
   Journal* 7 (1955), 14–66.
2. Michel Demazure and Alexander Grothendieck, eds., *Schémas en groupes
   (SGA 3)*, Exposés XXII–XXV.
