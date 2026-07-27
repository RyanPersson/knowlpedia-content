+++
id = "functional-analysis/hilbert-schmidt-operator"
title = "Hilbert–Schmidt operator"
kind = "definition"
summary = "A Hilbert-space operator whose squared norms on an orthonormal basis have finite sum."
aliases = ["Hilbert–Schmidt class", "Hilbert Schmidt operator", "Schatten 2-class operator"]
domains = ["functional-analysis", "operator-algebras"]
section_mode = "progressive"
+++

Let \(H\) and \(K\) be [[linear-algebra/hilbert-space|Hilbert spaces]]. A
[[functional-analysis/bounded-linear-operator|bounded operator]]
\(T:H\to K\) is **Hilbert–Schmidt** if, for one—and hence every—
[[linear-algebra/orthonormal-basis|orthonormal basis]] \((e_i)\) of \(H\),
\[
\sum_i\lVert Te_i\rVert_K^2<\infty.
\]
The basis-independent quantity
\[
\lVert T\rVert_{\mathrm{HS}}
=\left(\sum_i\lVert Te_i\rVert_K^2\right)^{1/2}
\]
is the **Hilbert–Schmidt norm**. The Hilbert–Schmidt operators form
\(\mathcal S^2(H,K)\), the \(p=2\) [[functional-analysis/schatten-class-operator|Schatten
class]]. Every Hilbert–Schmidt operator is
[[linear-algebra/compact-operator|compact]], but a compact operator need not
be Hilbert–Schmidt. The condition measures square-summability across
orthogonal input directions and is independent of all choices of basis.

## Equivalent characterizations

For \(T:H\to K\), the following conditions are equivalent:

- \(T\) is Hilbert–Schmidt;
- its [[functional-analysis/singular-values|singular values]] satisfy
  \(\sum_n s_n(T)^2<\infty\);
- the positive operator \(T^*T\) has finite trace.

With the trace understood as the basis-independent sum of diagonal
coefficients,
\[
\lVert T\rVert_{\mathrm{HS}}^2
=\operatorname{Tr}(T^*T)
=\operatorname{Tr}(TT^*).
\]
These formulas also show that \(T\) is Hilbert–Schmidt exactly when \(T^*\)
is.

## Hilbert-space and ideal structure

For \(S,T\in\mathcal S^2(H,K)\), the formula
\[
\langle S,T\rangle_{\mathrm{HS}}=\operatorname{Tr}(T^*S)
\]
makes \(\mathcal S^2(H,K)\) a Hilbert space. If \(A\) and \(B\) are bounded
operators of compatible sizes, then
\[
\lVert ATB\rVert_{\mathrm{HS}}
\leq \lVert A\rVert\,\lVert T\rVert_{\mathrm{HS}}\,\lVert B\rVert.
\]
Consequently, \(\mathcal S^2(H)\) is a two-sided operator ideal. The product
of two Hilbert–Schmidt operators is trace class, a fact behind many
operator-valued integral formulas.

## Examples and near misses

On \(\ell^2\), the diagonal operator
\(T(x_n)=(a_nx_n)\) is Hilbert–Schmidt exactly when
\((a_n)\in\ell^2\), and then
\(\lVert T\rVert_{\mathrm{HS}}=\lVert(a_n)\rVert_{\ell^2}\). Every
[[functional-analysis/finite-rank-operator|finite-rank operator]] is Hilbert–Schmidt.

The diagonal operator with \(a_n=n^{-1/2}\) is compact but not
Hilbert–Schmidt. Thus convergence of singular values to zero is insufficient;
their squares must be summable.

## Canonical scope and legacy entry

This general \(H\to K\) definition is the canonical corpus entry for
Hilbert–Schmidt operators. The older
[[shale-paper/hilbert-schmidt-operator|Shale-paper Hilbert–Schmidt entry]]
records the same notion only in the specialized \(H\to H\) setting and is
retained for compatibility with links in that project. New general-purpose
content should link to the present functional-analysis entry.

## References

1. Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., American Mathematical Society, 2005. [DOI record](https://doi.org/10.1090/surv/120). Relevant: Chapters 1–2 on Hilbert–Schmidt operators, trace ideals, and ideal inequalities.
2. Rajendra Bhatia, *Matrix Analysis*, Springer, 1997. [DOI record](https://doi.org/10.1007/978-1-4612-0653-8). Relevant: Chapter IV on unitarily invariant norms and Schatten classes.
