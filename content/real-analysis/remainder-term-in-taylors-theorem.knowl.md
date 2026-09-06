+++
id = "real-analysis/remainder-term-in-taylors-theorem"
title = "Remainder term in Taylor's theorem"
kind = "knowl"
summary = "The difference f(x)−T_k f(x;a), measuring Taylor approximation error."
aliases = ["remainder-term-in-taylors-theorem", "Remainder term in Taylor's theorem"]
domains = ["real-analysis"]
prerequisites = []
dependency_review_count = 1
legacy_source_path = "real-analysis/remainder-term-in-taylors-theorem.md"
+++

Suppose \(f\) has derivatives through order \(k\) at \(a\). Its Taylor polynomial of degree at most \(k\) about \(a\) is
\[
T_kf(x;a)=\sum_{j=0}^k\frac{f^{(j)}(a)}{j!}(x-a)^j.
\]
The **remainder term of order \(k\)** is
\[
R_k(x;a)=f(x)-T_kf(x;a)
\]
at every \(x\) where \(f(x)\) is defined.

Taylor's theorem supplies additional hypotheses under which \(R_k(x;a)\) has a Lagrange or integral representation, and hence can be estimated.

## Examples

- If \(f\) is a polynomial of degree \(\le k\), then \(R_k(x;a)\equiv 0\) for all \(x\).
- For \(f(x)=e^x\) about \(a=0\), \(R_1(x;0)=e^x-(1+x)\).
- For \(f(x)=\sin x\) about \(a=0\), \(R_3(x;0)=\sin x-\left(x-\frac{x^3}{6}\right)\).
