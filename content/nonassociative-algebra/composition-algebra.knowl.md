+++
id = "nonassociative-algebra/composition-algebra"
title = "Composition algebra"
kind = "definition"
summary = "A unital algebra with a nondegenerate quadratic norm that composes under multiplication."
aliases = ["Hurwitz algebra", "unital composition algebra"]
domains = ["nonassociative-algebra"]
prerequisites = ["nonassociative-algebra/nonassociative-algebra", "linear-algebra/quadratic-form"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(k\) be a field of characteristic different from \(2\). A **composition algebra** over \(k\) is a finite-dimensional unital [[nonassociative-algebra/nonassociative-algebra|algebra]] \(A\) with a nondegenerate [[linear-algebra/quadratic-form|quadratic form]] \(N:A\to k\) such that
\[
 N(xy)=N(x)N(y)
\]
for all \(x,y\in A\). Here “composition algebra” means *unital* composition algebra, also called a **Hurwitz algebra**.

## Trace and conjugation

Polarizing \(N\) gives the symmetric [[linear-algebra/bilinear-form|bilinear form]]
\[
 \langle x,y\rangle=N(x+y)-N(x)-N(y).
\]
After the normalization \(N(1)=1\), define the trace \(t(x)=\langle x,1\rangle\) and the standard conjugation
\[
 x^*=t(x)1-x.
\]
Every element satisfies
\[
 x^*x=xx^*=N(x)1,
 \qquad
 x^2-t(x)x+N(x)1=0.
\]
If \(N(x)\ne0\), then \(x^{-1}=x^*/N(x)\).

## Structure

Every composition algebra is [[nonassociative-algebra/alternative-algebra|alternative]], and its dimension is \(1\), \(2\), \(4\), or \(8\). Over a general field the norm may be isotropic, producing zero divisors; thus a composition algebra need not be a division algebra. Over \(\mathbb R\), positive-definite norm gives \(\mathbb R\), \(\mathbb C\), \(\mathbb H\), or \(\mathbb O\), while indefinite forms give split composition algebras.

## Convention warning

Some authors allow a composition algebra without a multiplicative identity. This broader class includes symmetric composition algebras such as Okubo algebras. The unital convention used here is the one relevant to [[nonassociative-algebra/hurwitz-theorem|Hurwitz's theorem]] and the classical [[nonassociative-algebra/real-normed-division-algebra|real normed division algebras]].

## References

1. Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer, 2000. [DOI record](https://doi.org/10.1007/978-3-662-12622-6). Relevant: Chapter 1.
2. Richard D. Schafer, *An Introduction to Nonassociative Algebras*, Academic Press, 1966. [Project Gutenberg edition](https://www.gutenberg.org/ebooks/25156). Relevant: Chapter III, §4.
