+++
id = "algebra-rings/formal-inverse-function-theorem"
title = "Formal inverse function theorem"
kind = "theorem"
summary = "A pointed tuple of formal series is compositionally invertible exactly when its linear coefficient matrix is invertible."
aliases = ["inverse function theorem for formal power series", "formal inverse mapping theorem"]
domains = ["algebra-rings", "formal-groups"]
section_mode = "progressive"
prerequisites = ["algebra-rings/commutative-ring", "algebra-rings/substitution-of-formal-power-series", "linear-algebra/matrix"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(R\) be a [[algebra-rings/commutative-ring|commutative ring]] and let
\[
f=(f_1,\ldots,f_n)\in(X_1,\ldots,X_n)R[[X_1,\ldots,X_n]]^n.
\]
Write \(J_f(0)\in M_n(R)\) for the matrix of linear coefficients of \(f\).
The **formal inverse function theorem** says that the following are equivalent:

1. \(J_f(0)\) is invertible over \(R\);
2. there is a unique tuple \(g\in(X)R[[X]]^n\) satisfying
   \(f(g(X))=X=g(f(X))\);
3. [[algebra-rings/substitution-of-formal-power-series|substitution]] by \(f\)
   is a continuous \(R\)-algebra automorphism of \(R[[X]]\).

## Recursive construction

Decompose \(f=f^{(1)}+f^{(2)}+\cdots\) into homogeneous terms. The degree-one
equation forces \(g^{(1)}=(f^{(1)})^{-1}\). Once
\(g^{(1)},\ldots,g^{(d-1)}\) are known, the degree-\(d\) part of
\(f(g)=X\) is a linear equation for \(g^{(d)}\) with coefficient matrix
\(J_f(0)\). Inverting that matrix determines \(g^{(d)}\) uniquely.
Completeness of \(R[[X]]\) assembles the degreewise solution.

## Consequences

A pointed formal map is a coordinate change exactly when its tangent map is an
isomorphism. In particular, a
[[formal-groups/formal-group-law-morphism|morphism of formal group laws]] whose
linear coefficient is invertible is automatically an isomorphism.

## Formal, not analytic

This theorem is coefficientwise and valid over any commutative base ring. It
does not claim that the series defines a convergent function on an open subset
of \(\mathbb R^n\) or \(\mathbb C^n\); no norm or analytic convergence is
part of the statement.

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, AMS Chelsea Publishing, 2012. [AMS book record](https://bookstore.ams.org/chel-375-h). Relevant: Appendix A, “Homomorphisms and isomorphisms; formal inverse function theorem.”
2. Nicolas Bourbaki, *Algebra II: Chapters 4–7*, Springer, 1990. Relevant: Chapter 4, formal series and substitution.
