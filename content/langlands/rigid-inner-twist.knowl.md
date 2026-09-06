+++
id = "langlands/rigid-inner-twist"
title = "Rigid inner twist"
kind = "definition"
summary = "An inner twist equipped with a cohomological rigidification used to normalize refined local Langlands packets and transfer factors."
aliases = ["rigid inner form", "rigidifying cocycle", "rigid inner twist of a reductive group"]
domains = ["langlands", "algebraic-geometry-foundations"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/local-field", "algebraic-geometry-foundations/quasi-split-reductive-group", "algebra-groups/center-of-group", "langlands-letter/knowls/galois-extension-and-group", "langlands-letter/knowls/galois-descent-forms"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(F\) be a
[[algebra-fields-galois/local-field|local field]], let
\(G^*\) be a
[[algebraic-geometry-foundations/quasi-split-reductive-group|quasi-split
connected reductive group]], and choose a finite
[[algebra-groups/center-of-group|central subgroup]]
\(Z\subset G^*\).  A **rigid inner twist** is an inner twist

\[
\psi:G^*_{\overline F}\xrightarrow{\sim}G_{\overline F}
\]

together with a cocycle \(z\) in Kaletha's rigid cohomology set
\(Z^1(u\to W,Z\to G^*)\), whose image in
\(Z^1(\Gamma_F,G^*_{\mathrm{ad}})\), where \(\Gamma_F\) is the
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]],
is the cocycle
\(\sigma\mapsto\psi^{-1}\sigma(\psi)\) defining the underlying
[[langlands-letter/knowls/galois-descent-forms|inner twist]].

The extra cocycle is the **rigidification**.  Forgetting it retains the inner
form but loses information needed for canonical packet pairings.

## Why the rigidification is used

For quasi-split groups a [[langlands/whittaker-datum|Whittaker datum]]
normalizes [[langlands/transfer-factor|transfer factors]] and the internal
parametrization of an
[[langlands/l-packet|L-packet]].  For arbitrary inner forms, a rigid inner
twist supplies the additional cohomological datum needed to extend those
normalizations and to pair representations with the appropriate
[[langlands/component-group-of-l-parameter|component group]].

Different rigidifications of the same underlying inner twist need not give
identical labels.  Statements of the
[[langlands/refined-local-langlands-correspondence|refined local Langlands
correspondence]] must therefore include the rigidifying data, not merely the
isomorphism class of \(G\).

## Framework warning

Pure inner twists, rigid inner twists, and extended pure inner twists are
related but not interchangeable frameworks.  The notation for the gerbe
\(u\to W\) and the allowed central subgroup \(Z\) also varies with the source.

## References

1. Tasho Kaletha, “Rigid inner forms of real and \(p\)-adic groups,”
   *Annals of Mathematics* 184 (2016), 559–632.
   [arXiv](https://arxiv.org/abs/1304.3292).
2. Tasho Kaletha, “Representations of reductive groups over local fields,”
   2022, §2.3. [arXiv](https://arxiv.org/abs/2201.07741).
