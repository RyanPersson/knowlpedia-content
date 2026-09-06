+++
id = "langlands-letter/knowls/langlands-dual-group"
title = "Langlands dual group"
kind = "knowl"
summary = "The pinned connected complex reductive group whose based root datum is dual to that of a reductive group."
aliases = ["langlands-dual-group", "Langlands Dual Group"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/langlands-dual-group.md"
section_mode = "progressive"
prerequisites = ["langlands-letter/knowls/split-reductive-group", "algebraic-geometry-foundations/reductive-algebraic-group", "langlands-letter/knowls/maximal-torus-weight-lattice", "langlands-letter/knowls/roots-weights-weyl", "langlands-letter/knowls/pinned-automorphisms"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[langlands-letter/knowls/split-reductive-group|split]]
connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] with split
[[langlands-letter/knowls/maximal-torus-weight-lattice|maximal torus]]
\(T\) and [[langlands-letter/knowls/roots-weights-weyl|based root datum]]

\[
\Psi(G)=
\bigl(
X^*(T),\Delta,
X_*(T),\Delta^\vee
\bigr).
\]

The **Langlands dual group** \(\widehat G\) is the connected complex
reductive group with dual based root datum

\[
\Psi(\widehat G)=
\bigl(
X_*(T),\Delta^\vee,
X^*(T),\Delta
\bigr).
\]

A [[langlands-letter/knowls/pinned-automorphisms|pinning]] makes
\(\widehat G\) and automorphisms of its based root datum
usable coherently, although the unpinned group is intrinsically determined
only up to inner isomorphism.

## Nonsplit groups

For a nonsplit \(G/F\), the
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]]
or [[langlands/weil-group|Weil group]] acts on the based
root datum and hence by pinned automorphisms on \(\widehat G\). The
[[langlands/l-group|\(L\)-group]] combines these data as an extension or
[[algebra-groups/semidirect-product|semidirect product]]. The dual group alone does not record the \(F\)-form.

## Examples

- \(\widehat{\operatorname{GL}_n}=\operatorname{GL}_n(\mathbb C)\).
- \(\widehat{\operatorname{SL}_n}=\operatorname{PGL}_n(\mathbb C)\).
- \(\widehat{\operatorname{PGL}_n}=\operatorname{SL}_n(\mathbb C)\).
- \(\widehat{\operatorname{Sp}_{2n}}=\operatorname{SO}_{2n+1}(\mathbb C)\).

Duality exchanges
[[langlands-letter/knowls/simply-connected-semisimple-group|simply
connected]] and
[[langlands-letter/knowls/root-vs-weight-lattice-isogeny|adjoint
semisimple isogeny forms]].

## Relation to the letter

The letter writes \(\widehat G\) as \(cG\) and uses \(cL\) for the dual
lattice, now represented by the
[[langlands-letter/knowls/dual-lattice|dual-lattice construction]]. Its
construction is the root-datum origin of the modern dual
group; the later \(L\)-group adds the Galois action needed for nonsplit
groups and local parameters.

## Rank-one scope warning

Over \(\mathbb C\), \(\operatorname{PGL}_2\) is also the [[algebra-groups/automorphism-group|automorphism group]]
of the
[[algebraic-geometry-foundations/projective-line|projective line]]. That
action does not define Langlands duality:
\(\widehat{\operatorname{SL}_2}=\operatorname{PGL}_2\) because roots and
coroots, with their character and cocharacter lattices, are exchanged.

## References

1. A. Borel, “Automorphic \(L\)-functions,” Proc. Sympos. Pure Math. 33,
   part 2, 1979.
2. Robert P. Langlands, “Problems in the theory of automorphic forms,” 1970.
   [DOI](https://doi.org/10.1007/BFb0079065).
