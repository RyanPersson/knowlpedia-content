+++
id = "harmonic-analysis/group-fourier-transform-nonabelian"
title = "Nonabelian group Fourier transform"
kind = "definition"
summary = "The operator-valued transform obtained by integrating a function against each irreducible unitary representation of a locally compact group."
aliases = ["operator-valued Fourier transform", "Fourier transform on a type I group"]
domains = ["harmonic-analysis", "lie-groups", "functional-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]] with a
left [[harmonic-analysis/haar-measure|Haar measure]], and let
\(\widehat G\) be its [[harmonic-analysis/unitary-dual|unitary dual]]. For
\(f\in L^1(G)\), the **nonabelian group Fourier transform** is the
operator-valued field determined weakly by
\[
\langle\widehat f(\pi)\xi,\eta\rangle
=\int_G f(g)\langle\pi(g)\xi,\eta\rangle\,dg,
\qquad \xi,\eta\in\mathcal H_\pi.
\]
Equivalently, one writes
\(\widehat f(\pi)=\int_Gf(g)\pi(g)\,dg\) for this
[[harmonic-analysis/integrated-form-unitary-representation|integrated
operator]]. It
satisfies the [[linear-algebra/operator-norm|operator-norm]] estimate
\(\lVert\widehat f(\pi)\rVert\leq\lVert f\rVert_1\). Replacing \(\pi\) by a
unitarily equivalent representative conjugates \(\widehat f(\pi)\), so the
field is intrinsically defined only up to fiberwise unitary equivalence. For
[[lie-groups/type-i-locally-compact-group|type I groups]], the fibers can be
organized as a measurable operator field.

## Convolution and involution

The transform is the
[[harmonic-analysis/integrated-form-unitary-representation|integrated form]]
evaluated at every [[algebra-representation-theory/irreducible-representation|irreducible representation]]. Consequently,
\[
\widehat{f*h}(\pi)=\widehat f(\pi)\widehat h(\pi).
\]
With the standard [[harmonic-analysis/convolution-involution|group-algebra involution]], it also satisfies
\(\widehat{f^*}(\pi)=\widehat f(\pi)^*\). These identities replace scalar
diagonalization by simultaneous operator-valued representation of the
convolution algebra.

## Plancherel realization

For a second-countable unimodular type I group, restricting the transform to
\(L^1(G)\cap L^2(G)\) gives
[[functional-analysis/hilbert-schmidt-operator|Hilbert–Schmidt operators]] for almost every
\([\pi]\) and extends to an \(L^2\) unitary isomorphism with respect to
[[harmonic-analysis/plancherel-measure-nonabelian|Plancherel measure]]. The
resulting field simultaneously realizes the
[[harmonic-analysis/direct-integral-unitary-representations|direct-integral decomposition]] of the
[[harmonic-analysis/regular-representations-locally-compact-group|regular representation]].

## Conventions and the abelian case

Some authors put \(\pi(g^{-1})\) in the integral. That convention matches the
usual conjugated-character formula directly but reverses the displayed
convolution product unless other conventions are changed. When \(G\) is
abelian, every fiber is one-dimensional, and after reindexing characters the
operator-valued transform becomes the
[[harmonic-analysis/fourier-transform-lca|Fourier transform on a locally compact abelian group]].

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §§4.1 and 7.4 on group Fourier transforms, integrated representations, and Plancherel theory.
2. Jacques Dixmier, *\(C^*\)-Algebras*, North-Holland Mathematical Library 15, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: Chapters 13 and 18 on group \(C^*\)-algebras and the dual of a locally compact group.
