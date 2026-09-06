+++
id = "fiber-bundles/chern-number"
title = "Chern number"
kind = "definition"
summary = "An integer obtained by evaluating a top-degree monomial in Chern classes on an oriented fundamental class."
aliases = ["Chern characteristic number"]
domains = ["fiber-bundles", "topology"]
prerequisites = ["fiber-bundles/vector-bundle", "topology/fundamental-class", "fiber-bundles/tangent-bundle"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a closed oriented \(2n\)-manifold and let \(E\to M\) be a complex [[fiber-bundles/vector-bundle|vector bundle]]. For a partition \(\lambda=(\lambda_1,\ldots,\lambda_\ell)\) of \(n\), the associated **Chern number** is
\[
c_\lambda(E)[M]:=
\left\langle
c_{\lambda_1}(E)\smile\cdots\smile c_{\lambda_\ell}(E),
[M]\right\rangle\in\mathbb Z.
\]
Here the product lies in \(H^{2n}(M;\mathbb Z)\) and \([M]\) is the [[topology/fundamental-class|fundamental class]]. A Chern number of an almost-complex or stably almost-complex manifold means this construction for its complex [[fiber-bundles/tangent-bundle|tangent bundle]] or stable tangent bundle.

## Relation to characteristic numbers

Chern numbers are the integral [[fiber-bundles/characteristic-number|characteristic numbers]] built from [[fiber-bundles/chern-class|Chern classes]]. Only monomials of total complex degree \(n\) pair with \([M]\). Naturality of Chern classes shows that orientation-preserving bundle equivalences preserve the resulting integers.

For stably almost-complex manifolds, all Chern numbers are bordism invariants. Moreover, equality of all Chern numbers characterizes equality in complex bordism; this is a structure theorem, not part of the definition.

## Example: complex projective space

Let \(h\in H^2(\mathbb{CP}^n;\mathbb Z)\) be the positive generator with \(\langle h^n,[\mathbb{CP}^n]\rangle=1\). The Euler sequence gives
\[
c(T\mathbb{CP}^n)=(1+h)^{n+1}
\]
after truncation above degree \(2n\). Hence
\[
\left\langle c_n(T\mathbb{CP}^n),[\mathbb{CP}^n]\right\rangle=n+1,
\qquad
\left\langle c_1(T\mathbb{CP}^n)^n,[\mathbb{CP}^n]\right\rangle=(n+1)^n.
\]

## Conventions and scope

**Warning.** The partition records Chern indices, not cohomological degrees: \(c_j\) has real cohomological degree \(2j\). Reversing the orientation of \(M\) reverses every Chern number while leaving the bundle’s Chern classes unchanged.

An arbitrary complex bundle over \(M\) has Chern numbers in the displayed sense, but “the Chern numbers of \(M\)” presupposes a chosen complex or stable-complex structure on its tangent bundle.

## References

1. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: §§14 and 16, Chern classes, Chern numbers, and complex cobordism.
2. Friedrich Hirzebruch, *Topological Methods in Algebraic Geometry*, 3rd ed., Springer, 1966. [DOI record](https://doi.org/10.1007/978-3-642-62018-8). Relevant: chapter 1, characteristic numbers and genera.
