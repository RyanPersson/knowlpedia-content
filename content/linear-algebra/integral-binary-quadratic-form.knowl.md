+++
id = "linear-algebra/integral-binary-quadratic-form"
title = "Integral binary quadratic form"
kind = "definition"
summary = "A homogeneous quadratic polynomial in two variables with integer coefficients, with discriminant b²−4ac."
aliases = ["binary quadratic form", "primitive binary quadratic form", "positive definite binary quadratic form"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/quadratic-form"]
dependency_heuristic = "transcript-connections-semantic-v1"
dependency_review_count = 1
+++
An **integral binary quadratic form** is a polynomial
\[
f(x,y)=ax^2+bxy+cy^2,\qquad a,b,c\in\mathbb Z.
\]
Its discriminant is \(D=b^2-4ac\). The form is **primitive** if \(\gcd(a,b,c)=1\), and **positive definite** if \(f(x,y)>0\) for every nonzero \((x,y)\in\mathbb R^2\), equivalently \(a>0\) and \(D<0\). It is a [[linear-algebra/quadratic-form|quadratic form]] on \(\mathbb Q^2\) together with its integral coordinate lattice.

## Normalization

The middle coefficient is \(b\), not \(2b\). The [[linear-algebra/symmetric-matrix|symmetric matrix]] of the form is \(\begin{pmatrix}a&b/2\\b/2&c\end{pmatrix}\), so its determinant is \(-D/4\). Confusing these two middle-coefficient conventions changes the discriminant.

For instance, \(x^2+xy+y^2\) is primitive positive definite of discriminant \(-3\). Integer changes of variables with determinant \(1\) give [[linear-algebra/proper-equivalence-binary-quadratic-forms|proper equivalence]].

## References

1. Andrew V. Sutherland, *18.785 Number Theory*, Fall 2018, [Problem Set 7](https://math.mit.edu/classes/18.785/2018fa/ProblemSet7.pdf), Problem 4, initial definitions.
