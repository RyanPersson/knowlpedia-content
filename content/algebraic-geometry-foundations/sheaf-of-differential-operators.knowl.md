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
sheaf \(\mathcal T_X\), subject to
\[
\xi f-f\xi=\xi(f)
\]
for local functions \(f\) and vector fields \(\xi\).

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
