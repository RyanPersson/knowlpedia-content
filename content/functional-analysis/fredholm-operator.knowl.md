+++
id = "functional-analysis/fredholm-operator"
title = "Fredholm operator"
kind = "definition"
summary = "A bounded operator with closed range and finite-dimensional kernel and cokernel."
aliases = ["Fredholm index", "Atkinson operator"]
domains = ["functional-analysis", "operator-algebras"]
prerequisites = ["linear-algebra/hilbert-space", "functional-analysis/bounded-linear-operator"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(H_0,H_1\) be [[linear-algebra/hilbert-space|Hilbert spaces]]. A
[[functional-analysis/bounded-linear-operator|bounded operator]]
\(T:H_0\to H_1\) is **Fredholm** if its range is closed and both \(\ker T\)
and the cokernel \(H_1/\operatorname{ran}T\) are finite-dimensional.
Equivalently, \(\ker T\) and \(\ker T^*\) are finite-dimensional and
\(\operatorname{ran}T\) is closed. Its **Fredholm index** is
\[
\operatorname{ind}(T)=\dim\ker T-\dim\ker T^*.
\]
The closed-range hypothesis is essential: finite-dimensional kernel and dense, nonclosed range do not make an operator Fredholm.

## Atkinson characterization

Atkinson's theorem says that \(T\) is Fredholm exactly when it is invertible modulo [[linear-algebra/compact-operator|compact operators]]. Concretely, this means there is a bounded \(S:H_1\to H_0\) such that
\[
ST-I_{H_0}
\quad\text{and}\quad
TS-I_{H_1}
\]
are compact. Such an \(S\) is called a parametrix modulo compact operators. When \(H_0=H_1=H\), the image of \(T\) is therefore invertible in the Calkin algebra \(B(H)/K(H)\).

## Stability and index

Fredholmness is open in the [[linear-algebra/operator-norm|operator norm]], and the index is locally constant on the set of Fredholm operators. If \(K:H_0\to H_1\) is compact, then
\[
T+K\ \text{is Fredholm}
\qquad\text{and}\qquad
\operatorname{ind}(T+K)=\operatorname{ind}(T).
\]
If \(T:H_0\to H_1\) and \(S:H_1\to H_2\) are Fredholm, then
\[
\operatorname{ind}(ST)=\operatorname{ind}(S)+\operatorname{ind}(T).
\]
These facts make the index insensitive to many analytic perturbations while retaining global information.

## Example

The unilateral shift \(U:\ell^2(\mathbb N)\to\ell^2(\mathbb N)\),
\[
U(x_0,x_1,\ldots)=(0,x_0,x_1,\ldots),
\]
has zero-dimensional kernel and a one-dimensional cokernel. Hence \(U\) is Fredholm and \(\operatorname{ind}(U)=-1\).

## Unbounded convention

A closed [[functional-analysis/densely-defined-operator|densely defined operator]] is also sometimes called Fredholm when it has closed range and finite-dimensional kernel and cokernel. That is a distinct unbounded notion: boundedness, domains, and adjoints must be handled explicitly. Under suitable regularity, an unbounded Fredholm operator can be represented by a bounded transform, but the two definitions should not be silently identified.

## References

- [F. V. Atkinson, “The normal solubility of linear equations in normed spaces,” *Matematicheskii Sbornik* 28(70) (1951), 3–14](https://www.mathnet.ru/eng/sm5589)
- [Nigel Higson and John Roe, *Analytic K-Homology*, Chapter 1 (Oxford University Press, 2000)](https://doi.org/10.1093/oso/9780198511762.001.0001)
