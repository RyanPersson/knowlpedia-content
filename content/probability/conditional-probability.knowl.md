+++
id = "probability/conditional-probability"
title = "Conditional probability"
kind = "knowl"
summary = "Probability of an event given another event or a sigma-algebra representing available information"
aliases = ["conditional-probability", "Conditional probability"]
domains = ["probability"]
legacy_source_path = "probability/conditional-probability.md"
+++

A **conditional probability** is the probability of an event after restricting to information in another event or in a sub-[[measure-theory/sigma-algebra|sigma-algebra]].  On a [[probability/probability-space|probability space]] \((\Omega,\mathcal F,\mathbb P)\), for events \(A,B\in\mathcal F\) with \(\mathbb P(B)>0\), the conditional probability of \(A\) given \(B\) is
\[
\mathbb P(A\mid B)\;=\;\frac{\mathbb P(A\cap B)}{\mathbb P(B)}.
\]

More generally, for a sub-\(\sigma\)-algebra \(\mathcal G\subseteq\mathcal F\), the conditional probability of \(A\) given \(\mathcal G\) is the \(\mathcal G\)-measurable [[probability/random-variable|random variable]] defined by
\[
\mathbb P(A\mid \mathcal G)\;=\;\mathbb E[\mathbf 1_A\mid \mathcal G],
\]

where \(\mathbb E[\cdot\mid \mathcal G]\) denotes [[probability/conditional-expectation|conditional expectation]].

## Remarks

Conditioning on \(\sigma(B)=\{\varnothing,B,B^c,\Omega\}\) records both sides of the partition: when \(0<\mathbb P(B)<1\),
\[
\mathbb P(A\mid\sigma(B))
=\mathbb P(A\mid B)\mathbf 1_B+\mathbb P(A\mid B^c)\mathbf 1_{B^c}
\quad\text{almost surely}.
\]
Thus the event-conditioned number \(\mathbb P(A\mid B)\) is the value of this random variable on \(B\), not the entire conditional random variable.

## Examples

- If a fair die is rolled, \(A=\{\text{even}\}\) and \(B=\{\text{roll}>3\}\), then \(\mathbb P(A\mid B)=\frac{2/6}{3/6}=\frac{2}{3}\).
- If \(A\) and \(B\) are [[probability/independence-events|independent events]] with \(\mathbb P(B)>0\), then \(\mathbb P(A\mid B)=\mathbb P(A)\).
- For a sub-\(\sigma\)-algebra \(\mathcal G\), if \(A\in\mathcal G\) then \(\mathbb P(A\mid \mathcal G)=\mathbf 1_A\) almost surely, while if \(\mathcal G=\{\varnothing,\Omega\}\) then \(\mathbb P(A\mid \mathcal G)=\mathbb P(A)\).
