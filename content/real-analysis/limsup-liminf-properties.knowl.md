+++
id = "real-analysis/limsup-liminf-properties"
title = "Basic Properties of limsup and liminf"
kind = "knowl"
summary = "Standard inequalities and identities involving limit superior and limit inferior."
aliases = ["limsup-liminf-properties", "Basic Properties of limsup and liminf"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/limsup-liminf-properties.md"
+++

Let $(a_n)$ and $(b_n)$ be real sequences. Their [[real-analysis/limit-superior|limit superior]] and [[real-analysis/limit-inferior|limit inferior]], regarded as extended real numbers, satisfy:

1. $\liminf_{n\to\infty}a_n\le \limsup_{n\to\infty}a_n$.
2. If $a_n\le b_n$ eventually, then
   $$
   \limsup a_n\le\limsup b_n
   \quad\text{and}\quad
   \liminf a_n\le\liminf b_n.
   $$
3. $\liminf a_n=-\limsup(-a_n)$.
4. If $a_n\to L\in\mathbb R$, then $\limsup a_n=\liminf a_n=L$.
5. If $\limsup a_n<\alpha$, then $a_n<\alpha$ eventually. If $\liminf a_n>\beta$, then $a_n>\beta$ eventually.

## Remarks

The strict inequalities in item 5 are essential: equality with $\alpha$ or $\beta$ need not imply an eventual strict bound.
