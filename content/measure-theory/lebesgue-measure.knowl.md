+++
id = "measure-theory/lebesgue-measure"
title = "Lebesgue measure"
kind = "knowl"
summary = "The standard complete translation-invariant measure on Euclidean space built from covering by rectangles."
aliases = ["lebesgue-measure", "Lebesgue measure"]
domains = ["measure-theory"]
prerequisites = ["measure-theory/outer-measure","measure-theory/caratheodory-measurable-set"]
dependency_review_count = 1
legacy_source_path = "measure-theory/lebesgue-measure.md"
+++

A **Lebesgue measure** on \(\mathbb R^n\) is the complete [[measure-theory/measure|measure]] \(\lambda^n\) obtained from the [[measure-theory/outer-measure|outer measure]]
\[
\lambda^{n,*}(E)
=\inf\left\{\sum_{k=1}^\infty \operatorname{vol}(R_k)\,:\, E\subseteq \bigcup_{k=1}^\infty R_k,\ \text{each } R_k \text{ is a measurable rectangle}\right\},
\]
where the \(R_k\) are half-open boxes and
\[
\operatorname{vol}(R)=\prod_{i=1}^n (b_i-a_i).
\]

A set \(E\subseteq\mathbb R^n\) is **Lebesgue measurable** if it is [[measure-theory/caratheodory-measurable-set|Carathéodory measurable]] for \(\lambda^{n,*}\), and then \(\lambda^n(E)=\lambda^{n,*}(E)\).

This construction yields the unique complete, translation-invariant measure on the Lebesgue measurable sets normalized by \(\lambda^n([0,1]^n)=1\).

## Examples

- On \(\mathbb R\), \(\lambda^1((a,b))=b-a\).
- Every countable subset of \(\mathbb R^n\) has Lebesgue measure \(0\).
