+++
id = "algebra-rings/multivariable-formal-power-series-ring"
title = "Multivariable formal power series ring"
kind = "definition"
summary = "The complete augmentation-adic ring of formal series in finitely many variables."
aliases = ["formal power series in several variables", "R[[X_1,...,X_n]]", "multivariate formal power series ring"]
domains = ["algebra-rings", "formal-groups"]
prerequisites = ["algebra-rings/commutative-ring"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(R\) be a [[algebra-rings/commutative-ring|commutative ring]] and let
\(X=(X_1,\ldots,X_n)\). The **multivariable formal power series ring**
\[
R[[X_1,\ldots,X_n]]
\]
consists of all formal sums \(f=\sum_{\alpha\in\mathbb N^n}a_\alpha
X^\alpha\), where \(X^\alpha=X_1^{\alpha_1}\cdots X_n^{\alpha_n}\).
Equality and addition are coefficientwise, and multiplication is determined by
\[
[X^\gamma](fg)=\sum_{\alpha+\beta=\gamma}a_\alpha b_\beta.
\]
The sum is finite for each \(\gamma\), so no analytic convergence is involved.

## Augmentation-adic description

The constant-term map
\[
\epsilon:R[[X_1,\ldots,X_n]]\longrightarrow R,\qquad
f\longmapsto a_0
\]
has augmentation ideal \(\mathfrak m=(X_1,\ldots,X_n)\). Truncating by total
degree gives a natural isomorphism of topological rings
\[
R[[X_1,\ldots,X_n]]
\cong
\varprojlim_N R[X_1,\ldots,X_n]/\mathfrak m^N.
\]
Consequently the ring is complete and separated for its
[[algebra-commutative/i-adic-topology|\(\mathfrak m\)-adic topology]].
The one-variable case is [[algebra-rings/formal-power-series-ring|\(R[[X]]\)]].

## Universal property for pointed substitutions

For \(Y=(Y_1,\ldots,Y_m)\), a tuple
\[
g=(g_1,\ldots,g_n)\in(Y_1,\ldots,Y_m)R[[Y]]^n
\]
determines a continuous \(R\)-algebra homomorphism
\[
R[[X]]\longrightarrow R[[Y]],\qquad X_i\longmapsto g_i.
\]
This is the algebraic form of
[[algebra-rings/substitution-of-formal-power-series|substituting formal power
series with zero constant term]]. The direction reverses when the rings are
viewed as coordinate rings of [[formal-groups/formal-affine-space|formal affine spaces]].

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, AMS Chelsea Publishing, 2012. [AMS book record](https://bookstore.ams.org/chel-375-h). Relevant: Appendix A, power-series rings.
2. Nicolas Bourbaki, *Algebra II: Chapters 4–7*, Springer, 1990. Relevant: Chapter 4, formal series.
