+++
id = "formal-groups/formal-completion-at-identity"
title = "Formal completion of a group at the identity"
kind = "construction"
summary = "The formal group obtained by retaining every infinitesimal neighborhood of the identity in a group scheme."
aliases = ["completion of a group scheme at the identity", "identity formal completion", "formal neighborhood of the identity"]
domains = ["formal-groups", "algebraic-geometry-foundations", "lie-groups"]
section_mode = "progressive"
+++

Let \(G\) be a group scheme separated over a field \(k\), with identity section
\(e:\operatorname{Spec}k\to G\). Because \(G\to\operatorname{Spec}k\) is
separated, \(e\) is a closed immersion. The **formal completion of \(G\) at
the identity**, denoted \(\widehat G_e\), is the formal scheme obtained by
completing \(G\) along the closed subscheme \(e(\operatorname{Spec}k)\).
More generally, the same construction applies whenever the identity section
is a closed immersion.
The multiplication, identity, and inverse maps of \(G\) restrict continuously
to its infinitesimal neighborhoods, making \(\widehat G_e\) a
[[formal-groups/formal-group|formal group]].

## Local coordinates

If \(G\) is affine and \(e\) corresponds to a maximal ideal
\(\mathfrak m_e\) of its coordinate ring near the identity, then locally
\[
\widehat G_e
=
\operatorname{Spf}\widehat{\mathcal O}_{G,e},
\qquad
\widehat{\mathcal O}_{G,e}
=
\varprojlim_n\mathcal O_{G,e}/\mathfrak m_e^n.
\]
If \(G\) is smooth of dimension \(n\), this completed local ring is
noncanonically isomorphic to \(k[[X_1,\ldots,X_n]]\), so \(\widehat G_e\) is
a formal \(n\)-disc with a formal group structure.

## Tangent algebra

Completion does not change first-order directions:
\[
\operatorname{Lie}(\widehat G_e)\cong\operatorname{Lie}(G).
\]
Over a characteristic-zero field, the
[[formal-groups/lie-algebra-formal-group-equivalence|formal Lie
correspondence]] then says that the completed group is determined by this Lie
algebra.

## Information that completion forgets

Formal completion sees only arbitrarily high infinitesimal data at the
identity. It forgets disconnected components, fundamental groups, compactness,
lattices, and the behavior of multiplication far from \(e\). For example, in
characteristic zero the additive and multiplicative groups have isomorphic
formal completions via \(\log(1+X)\), although the global algebraic groups are
not isomorphic.

Likewise, a local isogeny can induce an isomorphism on identity completions
while the global groups have different centers or topology. Thus formal
completion is a bridge from algebraic or Lie groups to formal groups, not a
reconstruction of the global object.

## References

1. The Stacks Project Authors, “Formal schemes à la EGA.” [Section 87.2, Tag 0AHY](https://stacks.math.columbia.edu/tag/0AHY). Relevant: formal spectra and completed neighborhoods.
2. Michel Demazure and Pierre Gabriel, *Groupes algébriques, Tome I*, Masson, 1970. Relevant: formal completion and Lie algebras of group schemes.
3. A. Fröhlich, *Formal Groups*, Lecture Notes in Mathematics 74, Springer, 1968. [Publisher record](https://link.springer.com/book/10.1007/BFb0074373). Relevant: Lie theory.
