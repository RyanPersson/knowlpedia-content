+++
id = "lie-groups/noncompact-finite-dimensional-unitary-example"
title = "A finite-dimensional irreducible representation of a noncompact group"
kind = "example"
summary = "The representation (t,k) ↦ e^{it}k of R × SU(2) disproves a dimension inference from noncompactness."
aliases = []
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/product-lie-group", "lie-groups/special-unitary-group", "lie-groups/irreducible-unitary-representation", "lie-groups/type-i-locally-compact-group"]
+++

The [[lie-groups/product-lie-group|product group]]
\[
G=\mathbb R\times\operatorname{SU}(2)
\]
is noncompact, nonabelian, and [[lie-groups/type-i-locally-compact-group|type I]], yet has the two-dimensional [[lie-groups/irreducible-unitary-representation|irreducible unitary representation]]
\[
\pi:G\longrightarrow U(\mathbb C^2),\qquad \pi(t,k)=e^{it}k.
\]
Here \(\operatorname{SU}(2)\) is the [[lie-groups/special-unitary-group|special unitary group]] in its defining representation.

## Verification

Scalar multiplication commutes with \(k\), so \(\pi(t,k)\pi(s,h)=\pi(t+s,kh)\). The operators are unitary and depend continuously on their parameters. Any invariant subspace must be invariant under \(\operatorname{SU}(2)\), which acts transitively on the unit sphere of \(\mathbb C^2\); a nonzero such subspace is therefore all of \(\mathbb C^2\).

The real factor makes \(G\) noncompact, and the special-unitary factor makes it nonabelian. Compact and abelian groups, and their direct product here, are type I.

## Simplest counterexample

Every topological group has its one-dimensional trivial unitary representation \(g\mapsto1\), which is irreducible. Noncompactness by itself therefore cannot force all irreducible unitary representations to be infinite-dimensional. The displayed two-dimensional example also addresses nontriviality and noncommutativity.

## References

1. Anton Deitmar and Gerrit van Dijk, [*Trace class groups*](https://arxiv.org/abs/1501.02375). Examples 1.5 (first bullet), Theorem 1.7, and Proposition 1.10(a) verify the type I claim via trace-class groups; irreducibility is checked directly above.
