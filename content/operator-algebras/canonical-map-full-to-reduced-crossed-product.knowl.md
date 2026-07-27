+++
id = "operator-algebras/canonical-map-full-to-reduced-crossed-product"
title = "Canonical map from full to reduced crossed product"
kind = "definition"
summary = "The surjective star-homomorphism obtained by completing the identity on the dense crossed-product convolution algebra in the reduced norm."
aliases = ["regular quotient of a crossed product", "canonical regular quotient"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

For a [[operator-algebras/cstar-dynamical-system|\(C^*\)-dynamical system]]
\((A,G,\alpha)\), the **canonical map from the full to the reduced crossed
product** is the surjective [[operator-algebras/star-homomorphism|
\(*\)-homomorphism]]
\[
\Lambda_A:A\rtimes_\alpha G\longrightarrow A\rtimes_{\alpha,r}G
\]
induced by the identity on the common dense convolution algebra
\(C_c(G,A)\). It exists because the reduced norm is [[real-analysis/bounded-above|bounded above]] by the
universal crossed-product norm. Equivalently, \(\Lambda_A\) is the quotient
associated with a faithful
[[operator-algebras/regular-covariant-representation|regular covariant
representation]] of \(A\); its kernel consists precisely of elements
annihilated by that [[algebra-representation-theory/regular-representation|regular representation]].

## Equality of the two completions

The map \(\Lambda_A\) is injective exactly when the full and reduced norms
agree on \(C_c(G,A)\); in that case it is an isomorphism. Amenability of the
action is a standard sufficient condition for this equality. For the trivial
action on \(A=\mathbb C\), \(\Lambda_{\mathbb C}\) becomes the regular quotient
\[
C^*(G)\longrightarrow C_r^*(G),
\]
and it is injective exactly when \(G\) is amenable
[Williams, discussion of regular representations and amenability](https://doi.org/10.1090/surv/134).

## Functorial role

The quotient compares two universal procedures applied to the same algebraic
data. Every [[operator-algebras/regular-covariant-representation|regular covariant representation]] factors through
\(A\rtimes_{\alpha,r}G\), whereas every covariant representation factors
through the [[operator-algebras/full-crossed-product|full crossed product]].
Consequently, any property that passes to quotients passes from the full
crossed product to the reduced one, but the converse generally requires
additional hypotheses.

On the coefficient algebra, the canonical embeddings are compatible with
\(\Lambda_A\). For non-discrete \(G\), those embeddings may land naturally in
[[operator-algebras/multiplier-algebra|multiplier algebras]], so compatibility
should not be mistaken for the assertion that \(A\) is literally a subalgebra
of both crossed products.

## Conventions and scope

**Warning.** The notation \(\Lambda\) is also used for the left regular
representation of a group. Here it denotes the integrated quotient between
crossed products. The map is always surjective by construction, but it is not
automatically faithful. Suppressing this quotient amounts to assuming an
amenability or full-equals-reduced hypothesis that must be stated.

## References

1. Dana P. Williams, *Crossed Products of C*-Algebras*, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: Chapter 2 on full and reduced crossed products and Chapter 7 on amenability.
