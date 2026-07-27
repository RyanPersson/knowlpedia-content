+++
id = "harmonic-analysis/tensor-product-unitary-representations"
title = "Tensor product of unitary representations"
kind = "definition"
summary = "The unitary representation acting diagonally on the completed Hilbert tensor product of two representation spaces."
aliases = ["Hilbert tensor product representation"]
domains = ["harmonic-analysis", "lie-groups", "functional-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/topological-group|topological group]], and let \(\pi:G\to\mathcal U(\mathcal H)\) and \(\sigma:G\to\mathcal U(\mathcal K)\) be [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representations]] on complex [[linear-algebra/hilbert-space|Hilbert spaces]]. Their **tensor product representation** is the homomorphism
\[
\pi\otimes\sigma:G\longrightarrow
\mathcal U(\mathcal H\widehat\otimes_2\mathcal K)
\]
specified on elementary tensors by
\[
(\pi\otimes\sigma)(g)(\xi\otimes\eta)
=\pi(g)\xi\otimes\sigma(g)\eta.
\]
Here \(\mathcal H\widehat\otimes_2\mathcal K\) is the completed Hilbert tensor product. The formula preserves [[linear-algebra/inner-product|inner products]], extends uniquely to a [[functional-analysis/unitary-operator|unitary operator]] for each \(g\), and defines a strongly continuous representation.

## Continuity and coefficients

Strong continuity is immediate on finite sums of elementary tensors and extends to the completion because all operators have norm one. [[harmonic-analysis/coefficient-function|Matrix coefficients]] multiply:
\[
\langle(\pi\otimes\sigma)(g)(\xi\otimes\eta),
\xi'\otimes\eta'\rangle
=\langle\pi(g)\xi,\xi'\rangle
\langle\sigma(g)\eta,\eta'\rangle.
\]
This identity makes tensor products fundamental in studying positive-definite functions, [[harmonic-analysis/weak-containment-unitary-representations|weak containment]], and representations possessing invariant vectors.

## Exterior tensor products

If \(\pi\) represents \(G\) and \(\sigma\) represents another group \(H\), their exterior tensor product is the representation of \(G\times H\) defined by
\[
(\pi\boxtimes\sigma)(g,h)=\pi(g)\otimes\sigma(h).
\]
Restricting this exterior product along the diagonal map \(G\to G\times G\) recovers the tensor product in the core. Thus the two constructions are related but are not synonyms.

## Conventions and scope

The completion is essential: the algebraic tensor product is dense but usually not complete. The construction here is for unitary Hilbert-space representations, not projective tensor products of Banach representations. In particular, “tensor product representation” does not mean a direct sum or a direct integral.

## References

1. Bachir Bekka, Pierre de la Harpe, and Alain Valette, *Kazhdan's Property (T)*, Cambridge University Press, 2008. [Appendix A DOI record](https://doi.org/10.1017/CBO9780511542749.009). Relevant: Appendix A on tensor products of unitary representations.
2. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Chapter 3 on unitary representations.
