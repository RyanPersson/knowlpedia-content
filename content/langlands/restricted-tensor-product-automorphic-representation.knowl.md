+++
id = "langlands/restricted-tensor-product-automorphic-representation"
title = "Restricted tensor-product factorization of an automorphic representation"
kind = "knowl"
summary = "The factorization of an irreducible admissible adelic representation into local components."
aliases = ["Flath tensor product theorem", "restricted tensor product of local representations", "automorphic tensor product decomposition"]
domains = ["langlands", "number-theory", "representation-theory"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "langlands-letter/knowls/global-local-fields-completions", "langlands/automorphic-representation", "algebra-fields-galois/completion-at-place", "harmonic-analysis/unramified-representation-p-adic-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over a
[[langlands-letter/knowls/global-local-fields-completions|global field]]
\(F\). An
irreducible admissible [[langlands/automorphic-representation|automorphic
representation]] has a factorization

\[
\pi \simeq \bigotimes_v' \pi_v
\]

into irreducible admissible representations \(\pi_v\) of the groups over the
[[algebra-fields-galois/completion-at-place|completions]]
\(F_v\). The restricted tensor product is taken with respect to distinguished
[[harmonic-analysis/unramified-representation-p-adic-group|spherical vectors]]
at almost all finite places.

## Construction

Choose [[topology/locally-profinite-group|compact open subgroups]]
\(K_v\subset G(F_v)\) such that, outside a
finite set \(S\), the space \(\pi_v^{K_v}\) is one-dimensional. Choose a
nonzero vector \(e_v\in\pi_v^{K_v}\). Algebraically,

\[
\bigotimes_v'(\pi_v,e_v)
=
\varinjlim_{S'}
\left(
\bigotimes_{v\in S'}\pi_v
\otimes
\bigotimes_{v\notin S'} \mathbb C e_v
\right),
\]

where \(S'\) ranges over finite sets containing \(S\). Rescaling finitely many
\(e_v\) does not change the isomorphism class.

At archimedean places one uses the appropriate completed topological tensor
product or, more commonly in algebraic statements, the tensor product of
[[lie-groups/harish-chandra-module|Harish–Chandra modules]] together with the
finite-adelic restricted product.

## The theorem and its converse

Flath's tensor-product theorem gives the factorization for irreducible
admissible representations of the adelic group under the standard
hypotheses. Conversely, a suitable restricted tensor product of irreducible
admissible local representations is an irreducible admissible representation
of \(G(\mathbb A_F)\); being automorphic is an additional global condition.

## Arithmetic role

The factorization makes local-to-global constructions possible. For almost
all \(v\), the
[[harmonic-analysis/unramified-representation-p-adic-group|unramified]]
\(\pi_v\) has a
[[langlands/satake-parameter|Satake parameter]]. Applying a representation of
the [[langlands/l-group|\(L\)-group]] gives the
[[langlands-letter/knowls/euler-product-and-local-factor|local Euler factor]].
The
resulting Euler product depends on the global representation, not merely on
an arbitrary collection of local factors.

## References

1. D. Flath, “Decomposition of representations into tensor products,” in
   *Automorphic Forms, Representations and \(L\)-Functions*, Proc. Sympos.
   Pure Math. 33, part 1, 1979, pp. 179–183.
2. A. Borel and H. Jacquet, “Automorphic forms and automorphic
   representations,” ibid., pp. 189–207.
