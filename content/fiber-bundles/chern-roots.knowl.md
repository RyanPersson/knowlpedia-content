+++
id = "fiber-bundles/chern-roots"
title = "Chern roots"
kind = "definition"
summary = "Formal degree-two classes that express the Chern classes of a complex vector bundle as elementary symmetric polynomials."
aliases = ["formal Chern roots", "Chern roots under the splitting principle"]
domains = ["fiber-bundles", "topology"]
prerequisites = ["fiber-bundles/complex-vector-bundle", "fiber-bundles/splitting-principle", "fiber-bundles/line-bundle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(E\to X\) be a rank-\(r\) [[fiber-bundles/complex-vector-bundle|complex vector bundle]]. Choose a splitting space \(p:Y\to X\) supplied by the [[fiber-bundles/splitting-principle|splitting principle]], so that \(p^*\) is injective on cohomology and \(p^*E\cong L_1\oplus\cdots\oplus L_r\) for complex line bundles \(L_i\). The **Chern roots** of \(E\) are the formal degree-two classes
\[
x_i=c_1(L_i)\in H^2(Y;\mathbb Z).
\]
They satisfy
\[
p^*c(E)=\prod_{i=1}^r(1+x_i),\qquad
p^*c_k(E)=e_k(x_1,\ldots,x_r),
\]
where \(e_k\) is the \(k\)-th elementary symmetric polynomial.
The multiset packages the characteristic-class data of \(E\) in
[[fiber-bundles/line-bundle|line-bundle]]
coordinates.

## Formal-root calculus

Any symmetric polynomial in the \(x_i\) is a polynomial in the elementary symmetric functions, hence determines a unique polynomial in the [[fiber-bundles/chern-class|Chern classes]] of \(E\). Injectivity of \(p^*\) then lets an identity proved on \(Y\) descend to \(X\). This is the precise meaning of “calculating as if \(E\) were a sum of line bundles”.

For example, the roots of the dual bundle are \(-x_1,\ldots,-x_r\). If \(F\) has formal roots \(y_1,\ldots,y_s\), then \(E\otimes F\) has formal roots \(x_i+y_j\), indexed by pairs \((i,j)\). These rules follow after pulling back to a common splitting space.

## Example

For a complex line bundle \(L\), there is one root, namely \(x=c_1(L)\), and \(c(L)=1+x\). For a trivial rank-\(r\) bundle all roots may be taken to be zero.

The [[fiber-bundles/tangent-bundle|tangent bundle]] of complex [[algebraic-geometry-foundations/projective-space|projective space]] illustrates the formal nature of the language: the Euler sequence gives \(c(T\mathbb{CP}^n)=(1+h)^{n+1}\) after truncation to \(H^*(\mathbb{CP}^n)\), even though \(T\mathbb{CP}^n\) is not thereby asserted to split into \(n+1\) line bundles.

## Conventions and scope

**Warning.** Individual roots generally are not classes on \(X\), are defined only after a chosen splitting extension, and are meaningful only up to permutation. Only symmetric expressions in them canonically descend.

In algebraic geometry the same notation is used in an appropriate Chow ring extension. The splitting construction and the conclusion are analogous, but the ambient cohomology theory must be kept fixed.

## References

1. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: §14, splitting principle and formal roots.
2. William Fulton, *Intersection Theory*, 2nd ed., Springer, 1998. [DOI record](https://doi.org/10.1007/978-1-4612-1700-8). Relevant: §3.2, Chern classes and the splitting construction.
