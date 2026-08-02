+++
id = "complex-analysis/cauchy-riemann-equations"
title = "Cauchy–Riemann equations"
kind = "definition"
summary = "The coordinate equations characterizing complex-linear real derivatives."
aliases = ["Cauchy-Riemann equations", "CR equations"]
domains = ["complex-analysis", "partial-differential-equations"]
section_mode = "progressive"
+++

Write \(f(x+iy)=u(x,y)+iv(x,y)\). At a point where the real [[real-analysis/partial-derivative|partial derivatives]] exist, the **Cauchy–Riemann equations** are
\[
u_x=v_y,\qquad u_y=-v_x.
\]
Equivalently, the real derivative matrix has the form
\[
Df=\begin{pmatrix}a&-b\\ b&a\end{pmatrix},
\]
so it represents multiplication by \(a+ib\).

## Wirtinger notation

With
\[
\frac{\partial}{\partial z}=\frac12\left(\frac{\partial}{\partial x}-i\frac{\partial}{\partial y}\right),
\qquad
\frac{\partial}{\partial\bar z}=\frac12\left(\frac{\partial}{\partial x}+i\frac{\partial}{\partial y}\right),
\]
the equations become \(\partial f/\partial\bar z=0\). This compact notation does not remove the regularity hypotheses needed in the [[complex-analysis/cauchy-riemann-criterion|Cauchy–Riemann criterion]].

## References

1. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapter II, §2.
