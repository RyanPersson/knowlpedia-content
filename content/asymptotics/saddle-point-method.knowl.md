+++
id = "asymptotics/saddle-point-method"
title = "Saddle-point method"
kind = "knowl"
summary = "Asymptotic evaluation of contour integrals and coefficient formulas using stationary points of the phase."
aliases = ["saddle-point-method", "Saddle-point method"]
domains = ["asymptotics"]
legacy_source_path = "asymptotics/saddle-point-method.md"
+++

The **saddle-point method** is a complex-analytic method for estimating integrals with a large parameter,
\[
I(n)=\int_{\Gamma} e^{n\phi(z)}\,\psi(z)\,dz
\]
as \(n\to\infty\). Here \(\phi\) and \(\psi\) are analytic near the relevant part of the contour \(\Gamma\). One deforms \(\Gamma\), without crossing singularities, through stationary points of \(\phi\) along directions on which \(\operatorname{Re}\phi\) decreases.

## Nondegenerate saddle

A point \(z_0\) is a nondegenerate saddle of \(\phi\) if
\[
\phi'(z_0)=0
\quad\text{and}\quad
\phi''(z_0)\neq 0.
\]

Near such a point,
\[
\phi(z)=\phi(z_0)+\tfrac12\phi''(z_0)(z-z_0)^2+\cdots,
\]
so integration along a steepest-descent direction reduces locally to a Gaussian integral. The resulting leading factor has order
\[
e^{n\phi(z_0)}n^{-1/2}.
\]
Its complex phase and square-root branch depend on the orientation of the deformed contour, so there is no contour-independent formula obtained merely by inserting \(\phi''(z_0)\).

## Coefficient asymptotics

For an analytic generating function
\[
F(z)=\sum_{n\ge 0} a_n z^n.
\]
Cauchy's formula gives
\[
a_n=\frac{1}{2\pi i}\oint \frac{F(z)}{z^{n+1}}\,dz,
\]
and a positive saddle radius \(r=r_n\) is commonly chosen to satisfy
\[
\frac{r F'(r)}{F(r)} = n.
\]

Define
\[
a(r)=\frac{rF'(r)}{F(r)},\qquad b(r)=r\,a'(r),
\]
and let \(a(r_n)=n\). Under additional admissibility hypotheses that ensure this saddle dominates the rest of the circle,
\[
a_n \sim \frac{F(r_n)}{r_n^{\,n}\sqrt{2\pi\,b(r_n)}}.
\]
Analyticity and the saddle equation alone do not imply this formula; one also needs uniform local approximation and decay away from the saddle.

## Relation to Laplace's method
The method is the complex analogue of [[asymptotics/laplaces-method|Laplace's method]]. Both rely on:
- identifying the dominant point (maximum/saddle),
- making a local quadratic approximation,
- evaluating a Gaussian integral.

## Practical notes
- Choosing the correct contour (often a steepest descent path) is part of the method; it ensures the contribution away from the saddle is negligible.
- Multiple saddle points can contribute, in which case the leading term may be a sum of their contributions.
- Degenerate saddles, where \(\phi''(z_0)=0\), require higher-order expansions and have different powers of \(n\).
