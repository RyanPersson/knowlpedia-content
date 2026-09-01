+++
id = "differential-geometry/hodge-star-operator"
title = "Hodge star operator"
kind = "definition"
summary = "The Hodge star is the degree-complementing operator on differential forms determined by a metric and an orientation."
aliases = ["Hodge star", "star operator", "Hodge dual", "star operator on differential forms"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/riemannian-manifold", "differential-geometry/orientation-of-a-smooth-manifold", "linear-algebra/inner-product", "fiber-bundles/wedge-product-of-differential-forms"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M,g)\) be an oriented \(n\)-dimensional [[differential-geometry/riemannian-manifold|Riemannian manifold]]. The metric and [[differential-geometry/orientation-of-a-smooth-manifold|orientation]] determine an [[linear-algebra/inner-product|inner product]] on \(k\)-forms and a volume form \(\operatorname{vol}_g\). The **Hodge star operator** is the unique linear isomorphism
\[
*:\Omega^k(M)\longrightarrow\Omega^{n-k}(M)
\]
such that, for all real \(k\)-forms \(\alpha,\beta\),
\[
\alpha\wedge *\beta=\langle\alpha,\beta\rangle_g\,\operatorname{vol}_g.
\]
It is defined pointwise and varies smoothly with \(g\). Thus the star combines the [[fiber-bundles/wedge-product-of-differential-forms|wedge product]], the metric, and orientation into an operator complementary in degree.

## Characterizing identities

On real \(k\)-forms in the Riemannian convention,
\[
*(*\alpha)=(-1)^{k(n-k)}\alpha.
\]
The star is a pointwise isometry, and \(*1=\operatorname{vol}_g\), while \(*\operatorname{vol}_g=1\). These identities follow directly in an oriented orthonormal coframe and characterize the signs used here.

The star also converts the [[fiber-bundles/exterior-derivative|exterior derivative]] into its [[differential-geometry/formal-adjoint-differential-operator|formal adjoint]], up to a degree- and dimension-dependent sign. This is the basic mechanism behind the [[differential-geometry/hodge-laplacian|Hodge Laplacian]] and harmonic-form theory.

## Computation in an orthonormal coframe

If \(e^1,\ldots,e^n\) is a positively oriented orthonormal coframe and \(I=(i_1<\cdots<i_k)\), then \(*e^I\) is the uniquely signed complementary wedge \(e^{I^c}\) for which
\[
e^I\wedge *e^I=e^1\wedge\cdots\wedge e^n.
\]
For the standard orientation of \(\mathbb R^3\), for example, \(*dx=dy\wedge dz\), \(*dy=dz\wedge dx\), and \(*dz=dx\wedge dy\).

## Conventions and scope

**Warning.** Reversing orientation multiplies the Hodge star by \(-1\). On a pseudo-Riemannian manifold, the square of the star contains an additional signature sign. For complex-valued forms, authors choose either a complex-linear star with a Hermitian pairing written using conjugation separately, or a conjugate-linear star. This knowl defines the real, positive-definite, complex-linearly extended convention.

## References

1. Shigeyuki Morita, *Geometry of Differential Forms*, Translations of Mathematical Monographs 201, American Mathematical Society, 2001. [Publisher record](https://doi.org/10.1090/mmono/201). Relevant: “Laplacian and harmonic forms.”
2. Raymond O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Graduate Texts in Mathematics 65, Springer, 2008. [Publisher record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: Chapter III, “Differential Geometry,” Hermitian exterior algebra and the Hodge star.
