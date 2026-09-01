+++
id = "linear-algebra/quadratic-form"
title = "Quadratic form"
kind = "definition"
summary = "A homogeneous degree-two scalar-valued function whose polarization is bilinear."
aliases = ["quadratic space"]
domains = ["linear-algebra"]
prerequisites = ["linear-algebra/vector-space", "algebra-rings/field", "linear-algebra/bilinear-form"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
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

## Polar radical and nondegeneracy

The **polar radical** of \(q\) is the radical of \(B_q\):
\[
\operatorname{rad}(B_q)
=\{v\in V:B_q(v,w)=0\text{ for every }w\in V\}.
\]
When \(2\) is invertible, \(q\) is called **nondegenerate** exactly when this
radical is zero. In characteristic \(2\), authors use several related
notions—regular, nonsingular, and nondegenerate—and may also require
conditions on the restriction of \(q\) to its polar radical. Statements in
that setting must specify the convention rather than referring to “the
radical of \(q\)” without qualification.

## References

1. T. Y. Lam, *Introduction to Quadratic Forms over Fields*, American Mathematical Society, 2005. [DOI record](https://doi.org/10.1090/gsm/067). Relevant: Chapter I.
