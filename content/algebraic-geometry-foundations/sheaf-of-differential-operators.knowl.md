+++
id = "algebraic-geometry-foundations/sheaf-of-differential-operators"
title = "Sheaf of differential operators"
kind = "definition"
summary = "The filtered sheaf D_X generated locally by functions and vector fields acting as differential operators."
aliases = ["D_X", "differential-operator sheaf"]
domains = ["algebraic-geometry-foundations", "langlands"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/tangent-sheaf", "fiber-bundles/vector-field", "lie-groups/universal-enveloping-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
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
for local functions \(f\) and [[fiber-bundles/vector-field|vector fields]] \(\xi,\eta\). Equivalently,
\(\mathcal D_X\) is the universal [[lie-groups/universal-enveloping-algebra|enveloping algebra]] of the Lie algebroid
\(\mathcal T_X\).

It has the order filtration
\(\mathcal D_X^{\leq0}\subseteq\mathcal D_X^{\leq1}\subseteq\cdots\), and the
associated graded algebra is canonically
\(\operatorname{Sym}_{\mathcal O_X}\mathcal T_X\).

## Left and right conventions

Left and right \(\mathcal D_X\)-modules are equivalent after twisting by the
canonical [[fiber-bundles/line-bundle|line bundle]], but formulas for pullback and pushforward depend on the
choice. A geometric-Langlands statement must fix one convention.

## References

1. Victor Ginzburg, [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), §2.1, Definition 2.1.5 and Corollaries 2.1.7–2.1.8 (generators and order filtration); §2.5.2, Proposition 2.5.3 (left and right modules).
