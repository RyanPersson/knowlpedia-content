+++
id = "differential-geometry/algebra-of-smooth-functions"
title = "Algebra of smooth functions"
kind = "definition"
summary = "The unital commutative algebra of scalar-valued smooth functions on a smooth manifold under pointwise operations."
aliases = ["C-infinity algebra", "smooth function algebra"]
domains = ["differential-geometry", "algebra-rings"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/smooth-manifold"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]]. The **algebra of smooth functions on \(M\)** is
\[
C^\infty(M)=\{f:M\to\mathbb R\mid f\text{ is smooth}\}.
\]
Addition, multiplication, and scalar multiplication are defined pointwise:
\[
(f+g)(p)=f(p)+g(p),\qquad (fg)(p)=f(p)g(p),\qquad
(af)(p)=a f(p).
\]
With these operations, \(C^\infty(M)\) is a commutative unital \(\mathbb R\)-algebra whose multiplicative identity is the constant function \(1\). For complex-valued functions the same construction gives the commutative unital \(\mathbb C\)-algebra \(C^\infty(M,\mathbb C)\).

## Canonical smooth functional calculus

The real algebra \(C^\infty(M)\) carries more than its polynomial
operations. Every smooth map \(g:\mathbb R^n\to\mathbb R\) defines
\[
\Phi_g(f_1,\ldots,f_n)(p)
=g(f_1(p),\ldots,f_n(p)).
\]
These operations make \(C^\infty(M)\) a canonical
[[differential-geometry/c-infinity-ring|\(C^\infty\)-ring]]. In particular,
one may apply \(\sin\), \(\exp\), and arbitrary multivariable smooth
functions to elements. Forgetting these operations leaves the underlying
commutative \(\mathbb R\)-algebra.

## Geometric information in the algebra

Evaluation at \(p\in M\), \(f\mapsto f(p)\), is a unital [[algebra-modules/algebra-homomorphism|algebra homomorphism]] \(C^\infty(M)\to\mathbb R\). Smooth functions separate distinct points and supply local coordinates and [[differential-geometry/bump-function|bump functions]]. Under the usual Hausdorff and second-countability hypotheses, this algebra therefore retains substantial information about the manifold.

## Pullback and modules

A [[fiber-bundles/smooth-map|smooth map]] \(F:M\to N\) induces a unital algebra homomorphism
\[
F^*:C^\infty(N)\to C^\infty(M),\qquad F^*h=h\circ F.
\]
It preserves every operation \(\Phi_g\), so it is a \(C^\infty\)-ring
morphism. Thus smooth manifolds map contravariantly to their smooth-function
algebras. For finite-dimensional Hausdorff second-countable manifolds,
[[differential-geometry/smooth-maps-from-smooth-function-algebras|every
\(C^\infty\)-ring morphism in the opposite direction arises uniquely this
way]]. Spaces of smooth sections of
[[fiber-bundles/vector-bundle|vector bundles]] over \(M\) are naturally
\(C^\infty(M)\)-modules, with multiplication defined pointwise.

## Conventions and examples

The notation \(C^\infty(M)\) normally means real-valued functions unless the scalar field is stated. It includes all smooth functions, not only compactly supported ones. For \(M=\mathbb R^n\), it is the familiar algebra of functions with continuous derivatives of every order. For the empty manifold it is the zero ring, so some authors exclude that case when requiring a unital algebra with \(0\ne1\).

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: chapters on smooth manifolds and smooth maps.
2. Jet Nestruev, *Smooth Manifolds and Observables*, Springer, 2003. [DOI record](https://doi.org/10.1007/b98871). Relevant: “Algebras and Points,” “Smooth Manifolds,” and “Smooth Maps.”
3. Ieke Moerdijk and Gonzalo E. Reyes, *Models for Smooth Infinitesimal Analysis*, Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4757-4148-6). Relevant: Chapter I, \(C^\infty\)-rings.
