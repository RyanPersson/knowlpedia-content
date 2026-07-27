+++
id = "fiber-bundles/splitting-principle"
title = "Splitting principle"
kind = "theorem"
summary = "A complex vector bundle pulls back to a sum of line bundles on a flag bundle without losing cohomological information."
aliases = ["splitting principle for characteristic classes", "flag-bundle splitting"]
domains = ["fiber-bundles"]
section_mode = "progressive"
+++

Let \(E\to X\) be a rank-\(n\) [[fiber-bundles/complex-vector-bundle|complex vector bundle]] over a [[fiber-bundles/smooth-manifold|smooth manifold]]. There is a complete flag bundle \(p:\operatorname{Fl}(E)\to X\) such that the [[fiber-bundles/pullback-bundle|pullback bundle]] \(p^*E\) has a filtration with [[fiber-bundles/line-bundle|line-bundle]] quotients \(L_1,\ldots,L_n\); after choosing a [[fiber-bundles/hermitian-metric|Hermitian metric]], \(p^*E\cong L_1\oplus\cdots\oplus L_n\). Moreover,
\[
p^*:H^*(X;\mathbb Z)\longrightarrow H^*(\operatorname{Fl}(E);\mathbb Z)
\]
is injective. Consequently, identities among [[fiber-bundles/characteristic-class|characteristic classes]] may be checked after pullback, where the bundle behaves as a sum of line bundles. This is the **splitting principle**.

## Construction and justification

One constructs \(\operatorname{Fl}(E)\) by iteratively projectivizing the remaining quotient bundle. The resulting tautological filtration has line-bundle subquotients. Hermitian [[linear-algebra/orthogonal-complement|orthogonal complements]] split the filtration in the smooth category.

The projective bundle theorem, applied at each stage, makes cohomology of the new base a [[algebra-modules/free-module|free module]] over the preceding cohomology ring with a basis containing \(1\). The pullback at each stage is therefore injective, and so is their composite [Milnor and Stasheff, chapter 14](https://doi.org/10.1515/9781400881826).

## Use with Chern classes

Writing \(x_i=c_1(L_i)\), naturality and the [[fiber-bundles/whitney-sum-formula|Whitney product formula]] give
\[
p^*c(E)=\prod_{i=1}^{n}(1+x_i).
\]
The classes \(x_i\) are called [[fiber-bundles/chern-roots|formal Chern roots]]. A symmetric polynomial identity in the \(x_i\) descends uniquely to an identity in the [[fiber-bundles/chern-class|Chern classes]] of \(E\), because \(p^*\) is injective. This turns many calculations with characteristic classes into calculations with elementary symmetric polynomials.

The same method applies to identities involving duals, tensor products, exterior powers, and Pontryagin classes after complexification.

## Conventions and scope

One may formulate the principle using a full flag bundle, a tower of projective bundles, or an unspecified auxiliary space over which the bundle splits and cohomology pullback is injective. Conventions that projectivize lines versus hyperplanes change the signs used for tautological first Chern classes.

**Warning.** The theorem does not say that \(E\) splits over \(X\). Nor does it say that \(p\) is injective as a map of spaces or is a [[topology/homotopy-equivalence|homotopy equivalence]]; injectivity refers to the stated map on cohomology.

## References

1. J. W. Milnor and J. D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: chapter 14, the splitting principle and formal roots.
2. D. Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-4008-0). Relevant: chapter 17, splitting constructions and characteristic classes.
