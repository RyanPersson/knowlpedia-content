+++
id = "linear-algebra/quadratic-form"
title = "Quadratic form"
kind = "definition"
summary = "A homogeneous degree-two scalar-valued function whose polarization is bilinear."
aliases = ["quadratic space"]
domains = ["linear-algebra"]
section_mode = "progressive"
+++

Let \(V\) be a [[linear-algebra/vector-space|vector space]] over a [[algebra-rings/field|field]] \(k\). A **quadratic form** on \(V\) is a function \(q:V\to k\) such that
\[
q(av)=a^2q(v)
\]
for all \(a\in k\), \(v\in V\), and the polarization
\[
B_q(v,w)=q(v+w)-q(v)-q(w)
\]
is a [[linear-algebra/bilinear-form|bilinear form]]. The pair \((V,q)\) is called a quadratic space.

## Characteristic not two

If \(2\) is invertible in \(k\), then \(B_q\) is symmetric and
\[
q(v)=\frac12B_q(v,v).
\]
Thus quadratic forms and symmetric bilinear forms determine one another in this setting. In characteristic \(2\), the quadratic form contains information not recoverable from its polarization.

## Nondegeneracy

The radical of \(q\) is the radical of \(B_q\):
\[
\operatorname{rad}(q)=\{v\in V:B_q(v,w)=0\text{ for every }w\in V\}.
\]
The form is nondegenerate when this radical is zero.

## References

1. T. Y. Lam, *Introduction to Quadratic Forms over Fields*, American Mathematical Society, 2005. [DOI record](https://doi.org/10.1090/gsm/067). Relevant: Chapter I.
