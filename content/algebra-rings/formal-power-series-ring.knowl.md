+++
id = "algebra-rings/formal-power-series-ring"
title = "Formal power series ring"
kind = "definition"
summary = "The complete x-adic ring R[[x]] of coefficient sequences with Cauchy multiplication."
aliases = ["formal-power-series-ring", "Formal power series ring"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/formal-power-series-ring.md"
section_mode = "progressive"
+++

Let \(R\) be a [[algebra-rings/commutative-ring|commutative ring]] with \(1\). The **formal power series ring** \(R[[x]]\) consists of all coefficient sequences \((a_0,a_1,\ldots)\), written
\[
\sum_{i=0}^{\infty}a_i x^i,\qquad a_i\in R.
\]
Two series are equal exactly when every coefficient agrees. Addition is coefficientwise, and multiplication is the Cauchy product
\[
\left(\sum_{i\geq 0}a_i x^i\right)
\left(\sum_{j\geq 0}b_j x^j\right)
=
\sum_{n\geq 0}\left(\sum_{i+j=n}a_i b_j\right)x^n.
\]
Each coefficient on the right is a finite sum, so multiplication is algebraically defined without asking the series to converge numerically.

## Augmentation and topology

Evaluation at \(x=0\) is the augmentation
\[
\epsilon:R[[x]]\longrightarrow R,\qquad
\sum a_i x^i\longmapsto a_0,
\]
whose kernel is the principal ideal \((x)\). The powers \((x^N)\) define the \(x\)-adic topology, and truncation gives
\[
R[[x]]\cong\varprojlim_N R[x]/(x^N).
\]
Thus \(R[[x]]\) is complete and separated for its \(x\)-adic topology. This topology, rather than analytic convergence, is what makes infinite algebraic manipulations meaningful.

## Units and local structure

A series \(f=\sum a_i x^i\) is a unit precisely when \(a_0\) is a unit of \(R\). The coefficients of \(f^{-1}\) are then determined recursively from \(ff^{-1}=1\).

There is a natural inclusion of [[algebra-rings/polynomial-ring|polynomials]] into \(R[[x]]\) as the finite series. If \(R\) is a field, \(R[[x]]\) is a [[algebra-commutative/local-ring|local ring]] with unique [[algebra-rings/maximal-ideal|maximal ideal]] \((x)\). For general \(R\), maximal ideals are obtained from maximal ideals \(\mathfrak m\subset R\) as \(\mathfrak mR[[x]]+(x)\).

## Examples

- For a field \(k\), \(k[[x]]\) is a domain in which \(x\) is nonzero but topologically “small”.
- In \(\mathbb{Z}[[x]]\), the element \(1+x\) is a unit with inverse \(1-x+x^2-x^3+\cdots\).
- An expression with infinitely many negative powers of \(x\) is not in \(R[[x]]\).

## Several variables and substitution

The ring [[algebra-rings/multivariable-formal-power-series-ring|\(R[[x_1,\ldots,x_n]]\)]] is the several-variable analogue. Infinite [[algebra-rings/substitution-of-formal-power-series|substitution]] is well-defined when the substituted series have zero constant term; this is a topological condition, not an analytic one.

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, AMS Chelsea Publishing, 2012. [AMS book record](https://bookstore.ams.org/chel-375-h). Relevant: Appendix A, power-series rings.
2. Nicolas Bourbaki, *Algebra II: Chapters 4–7*, Springer, 1990. Relevant: Chapter 4, formal series and restricted substitutions.
