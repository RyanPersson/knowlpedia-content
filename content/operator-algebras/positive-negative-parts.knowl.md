+++
id = "operator-algebras/positive-negative-parts"
title = "Positive and negative parts of a self-adjoint element"
kind = "definition"
summary = "The canonical orthogonal positive elements whose difference is a given self-adjoint element."
aliases = ["positive part", "negative part", "Jordan decomposition of a self-adjoint element"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/self-adjoint-element", "operator-algebras/cstar-algebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(a\) be a [[operator-algebras/self-adjoint-element|self-adjoint element]]
of a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\), and put
\(|a|=(a^2)^{1/2}\). The **positive part** and **negative part** of \(a\) are
\[
a_+=\frac{|a|+a}{2},
\qquad
a_-=\frac{|a|-a}{2}.
\]
Both belong to the positive cone of \(A\), and they satisfy
\[
a=a_+-a_-,
\qquad |a|=a_++a_-,
\qquad a_+a_-=0.
\]
They are the unique positive elements \(b,c\in C^*(a)\) with
\(a=b-c\) and \(bc=0\). This decomposition is also called the Jordan
decomposition of \(a\).

## Functional-calculus description

Under the [[operator-algebras/continuous-functional-calculus|continuous functional calculus]] for \(a\),
\[
a_+=f_+(a),\qquad a_-=f_-(a),
\]
where \(f_+(t)=\max(t,0)\) and \(f_-(t)=\max(-t,0)\). Hence
\(a_-\) is the positive part of \(-a\), and both parts commute with every
element that commutes with \(a\). Their orthogonality follows pointwise from
\(f_+(t)f_-(t)=0\).

## Order and norm consequences

The formulas give \(a\leq a_+\), \(-a\leq a_-\), and
\[
\|a\|=\max\{\|a_+\|,\|a_-\|\}.
\]
Moreover, \(a\) is positive exactly when \(a_-=0\), and \(a\) is negative
exactly when \(a_+=0\). Applying a \(*\)-homomorphism commutes with taking
positive and negative parts because \(*\)-homomorphisms commute with
continuous functional calculus.

## Examples and cautions

For a Hermitian matrix, \(a_+\) keeps the positive eigenvalues and replaces
the negative ones by zero; \(a_-\) replaces each negative eigenvalue
\(\lambda\) by \(-\lambda\). For a real-valued function, the construction is
pointwise. The notation \(a_-\) denotes a positive element, not the
nonpositive function \(\min(a,0)\). The decomposition also should not be
confused with the Jordan decomposition of a functional or measure, which
requires a separate uniqueness theorem.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [Elsevier DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §2.2 on positive elements and continuous functional calculus.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [Elsevier DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §§1.4–1.5 on positivity, order, and functional calculus.
