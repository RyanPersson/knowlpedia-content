+++
id = "fiber-bundles/pontryagin-number"
title = "Pontryagin number"
kind = "definition"
summary = "An integer obtained by evaluating a top-degree monomial in Pontryagin classes on an oriented fundamental class."
aliases = ["Pontryagin characteristic number"]
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
+++

Let \(M\) be a closed oriented \(4k\)-manifold and let \(E\to M\) be a real [[fiber-bundles/vector-bundle|vector bundle]]. For a partition \(\lambda=(\lambda_1,\ldots,\lambda_\ell)\) of \(k\), the associated **Pontryagin number** is
\[
p_\lambda(E)[M]:=
\left\langle
p_{\lambda_1}(E)\smile\cdots\smile p_{\lambda_\ell}(E),
[M]\right\rangle\in\mathbb Z.
\]
The monomial has degree \(4k\), since \(p_j(E)\in H^{4j}(M;\mathbb Z)\). A Pontryagin number of an oriented [[fiber-bundles/smooth-manifold|smooth manifold]] conventionally means the number obtained from its [[fiber-bundles/tangent-bundle|tangent bundle]] \(E=TM\).
The evaluation uses the ordinary integral
[[topology/cup-product-and-cohomology-ring|cup product]] and the chosen
orientation of \(M\).

## Bordism and the signature

Tangent-bundle Pontryagin numbers are [[fiber-bundles/characteristic-number|characteristic numbers]] and are invariant under [[differential-geometry/oriented-cobordism|oriented bordism]]. Together with Stiefel–Whitney numbers they detect oriented bordism classes. Rationally, the Pontryagin numbers alone detect the oriented bordism class modulo torsion.

The Hirzebruch signature theorem expresses the signature of a closed oriented \(4k\)-manifold as evaluation of the \(L\)-polynomial in its [[fiber-bundles/pontryagin-class|Pontryagin classes]]. In dimension four this reads
\[
\operatorname{sign}(M)=\frac{1}{3}\left\langle p_1(TM),[M]\right\rangle.
\]

## Example: the complex projective plane

For \(\mathbb{CP}^2\), regarded as an oriented real four-manifold, the relation between the underlying real tangent bundle and its complex tangent bundle gives
\[
p_1(T\mathbb{CP}^2)
=c_1(T\mathbb{CP}^2)^2-2c_2(T\mathbb{CP}^2)
=3h^2.
\]
Therefore \(\langle p_1,[\mathbb{CP}^2]\rangle=3\), in agreement with \(\operatorname{sign}(\mathbb{CP}^2)=1\).

## Conventions and scope

**Warning.** A Pontryagin class is defined without orienting \(M\), but its evaluation as a signed integer uses an orientation; reversing that orientation negates every Pontryagin number.

Only top-degree monomials produce numbers. On a manifold whose dimension is not divisible by four there are no tangent-bundle Pontryagin numbers, although lower-degree Pontryagin classes may be nonzero.

## References

1. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: §§15–17, Pontryagin classes, characteristic numbers, and cobordism.
2. Friedrich Hirzebruch, *Topological Methods in Algebraic Geometry*, 3rd ed., Springer, 1966. [DOI record](https://doi.org/10.1007/978-3-642-62018-8). Relevant: chapter 1, the signature theorem and Pontryagin numbers.
