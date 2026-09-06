+++
id = "linear-algebra/minkowski-vector-space"
title = "Minkowski vector space"
kind = "definition"
summary = "Four-dimensional real vector space with the Lorentzian quadratic form −t²+x²+y²+z²."
aliases = ["Minkowski quadratic space", "Lorentzian vector space R1,3"]
domains = ["linear-algebra", "mathematical-physics"]
prerequisites = ["linear-algebra/bilinear-form", "linear-algebra/quadratic-form", "linear-algebra/signature-of-symmetric-bilinear-form"]
dependency_review_count = 1
section_mode = "progressive"
+++

In this collection, **Minkowski vector space** is \(\mathbb R^{1,3}=\mathbb R^4\) with coordinates \((t,x,y,z)\), symmetric [[linear-algebra/bilinear-form|bilinear form]]
\[
\eta(u,v)=-u_0v_0+u_1v_1+u_2v_2+u_3v_3,
\]
and associated [[linear-algebra/quadratic-form|quadratic form]]
\[
q(v)=\eta(v,v)=-t^2+x^2+y^2+z^2.
\]
Thus the matrix of \(\eta\) is \(\operatorname{diag}(-1,1,1,1)\); throughout this collection, the [[linear-algebra/signature-of-symmetric-bilinear-form|signature]] notation \((1,3)\) means one negative and three positive directions.

## Causal types

A nonzero vector \(v\) is **timelike**, **null** (or lightlike), or **spacelike** according as \(q(v)<0\), \(q(v)=0\), or \(q(v)>0\). The timelike cone has two [[topology/connected-component|connected components]]. Choosing one as the future cone is a [[differential-geometry/time-orientation|time orientation]].

Sources that list positive directions first call the displayed form's signature \((3,1)\). Other sources reverse the overall sign and use \(t^2-x^2-y^2-z^2\); in this collection's negative-first ordering, that opposite form has signature \((3,1)\). Formulas in linked knowls use the displayed \((-+++)\) form, so the [[lie-groups/hermitian-matrix-model-of-minkowski-space|Hermitian matrix model]] satisfies \(\det X(v)=-q(v)\), not \(\det X(v)=q(v)\).

## References

1. Barrett O'Neill, *Semi-Riemannian Geometry With Applications to Relativity*, Academic Press, 1983, Chapter 5. [Publisher record](https://doi.org/10.1016/C2009-0-11874-8).
2. Gregory L. Naber, *The Geometry of Minkowski Spacetime*, 2nd ed., Springer, 2012, Chapter 1. [Publisher record](https://doi.org/10.1007/978-1-4419-7838-7).
