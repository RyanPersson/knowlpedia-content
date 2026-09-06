+++
id = "differential-geometry/de-rham-complex"
title = "de Rham complex"
kind = "definition"
summary = "The cochain complex of smooth differential forms with the exterior derivative."
aliases = ["complex of differential forms", "de Rham cochain complex"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-manifold", "algebra-homological/cochain-complex", "linear-algebra/vector-space", "fiber-bundles/differential-k-form", "fiber-bundles/exterior-derivative", "fiber-bundles/wedge-product-of-differential-forms"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For a [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\), the **de Rham complex** is the [[algebra-homological/cochain-complex|cochain complex]]
\[
0\longrightarrow\Omega^0(M)\xrightarrow{d}\Omega^1(M)\xrightarrow{d}\Omega^2(M)
\xrightarrow{d}\cdots,
\]
where \(\Omega^k(M)\) is the [[linear-algebra/vector-space|vector space]] of smooth [[fiber-bundles/differential-k-form|differential \(k\)-forms]] and each differential is the [[fiber-bundles/exterior-derivative|exterior derivative]]. The identity \(d\circ d=0\) makes this a cochain complex. Its degree-\(k\) cocycles are closed forms, its coboundaries are exact forms, and its cohomology is the de Rham cohomology of \(M\).

## Differential graded algebra structure

The [[fiber-bundles/wedge-product-of-differential-forms|wedge product]] makes \(\Omega^\bullet(M)\) a graded-commutative algebra, while the exterior derivative obeys
\[
d(\alpha\wedge\beta)=d\alpha\wedge\beta+(-1)^{\deg\alpha}\alpha\wedge d\beta.
\]
Thus the de Rham complex is more specifically a commutative differential graded algebra, not merely a sequence of vector spaces and [[linear-algebra/linear-map|linear maps]].

## Cohomology and topology

The quotient
\[
H_{\mathrm{dR}}^k(M)=\ker(d:\Omega^k\to\Omega^{k+1})/
\operatorname{im}(d:\Omega^{k-1}\to\Omega^k)
\]
is the [[fiber-bundles/de-rham-cohomology-group|de Rham cohomology group]]. De Rham's theorem identifies it with singular cohomology with real coefficients, so a complex built from smooth forms recovers a topological invariant.

## Functoriality

A [[fiber-bundles/smooth-map|smooth map]] \(f:M\to N\) induces [[fiber-bundles/pullback-of-differential-forms|pullback maps]] \(f^*:\Omega^k(N)\to\Omega^k(M)\). Since \(f^*d=df^*\) and pullback preserves wedge products, \(f^*\) is a morphism of differential graded algebras and induces the contravariant map on de Rham cohomology.

## References

1. R. Bott and L. W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982. [Springer DOI record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: Chapter I.
2. L. W. Tu, *An Introduction to Manifolds*, 2nd ed., Springer, 2011. [Springer DOI record](https://doi.org/10.1007/978-1-4419-7400-6). Relevant: chapters on differential forms and de Rham cohomology.
