+++
id = "algebraic-geometry-foundations/sheaf-of-differential-operators"
title = "Sheaf of differential operators"
kind = "definition"
summary = "The filtered sheaf D_X generated locally by functions and vector fields acting as differential operators."
aliases = ["D_X", "differential-operator sheaf"]
domains = ["algebraic-geometry-foundations", "langlands"]
section_mode = "progressive"
+++

Let \(X\) be a smooth algebraic variety over a field of characteristic \(0\).
The **sheaf of differential operators** \(\mathcal D_X\) is the sheaf of
associative algebras generated locally by \(\mathcal O_X\) and the tangent
sheaf [[algebraic-geometry-foundations/tangent-sheaf|\(\mathcal T_X\)]]. Its
relations include multiplication in \(\mathcal O_X\), the
\(\mathcal O_X\)-module structure on \(\mathcal T_X\), and
\[
\xi f-f\xi=\xi(f),
\qquad
\xi\eta-\eta\xi=[\xi,\eta]
\]
for local functions \(f\) and vector fields \(\xi,\eta\). Equivalently,
\(\mathcal D_X\) is the universal enveloping algebra of the Lie algebroid
\(\mathcal T_X\).

It has the order filtration
\(\mathcal D_X^{\leq0}\subseteq\mathcal D_X^{\leq1}\subseteq\cdots\), and the
associated graded algebra is canonically
\(\operatorname{Sym}_{\mathcal O_X}\mathcal T_X\).

## Left and right conventions

Left and right \(\mathcal D_X\)-modules are equivalent after twisting by the
canonical line bundle, but formulas for pullback and pushforward depend on the
choice. A geometric-Langlands statement must fix one convention.

## References

1. Joseph Bernstein, “Algebraic theory of D-modules,” unpublished lecture
   notes, 1983; English translation hosted by
   [MPIM](https://www.mpim-bonn.mpg.de/node/6072).
