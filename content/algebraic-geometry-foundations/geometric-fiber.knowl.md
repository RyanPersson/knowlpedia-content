+++
id = "algebraic-geometry-foundations/geometric-fiber"
title = "Geometric fiber"
kind = "definition"
summary = "The fiber of a scheme morphism after base change to an algebraic closure of a residue field."
aliases = ["geometric fiber", "geometric fibre"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/morphism-of-schemes", "algebraic-geometry-foundations/fiber-product-of-schemes", "algebra-commutative/residue-field", "algebra-fields-galois/algebraic-closure"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
+++

Let \(f:X\to S\) be a [[algebraic-geometry-foundations/morphism-of-schemes|morphism of schemes]], let \(s\in S\), and let \(\kappa(s)\) be its [[algebra-commutative/residue-field|residue field]]. Choose an [[algebra-fields-galois/algebraic-closure|algebraic closure]] \(\overline{\kappa(s)}\). The **geometric fiber** over the geometric point \(\overline{s}=\operatorname{Spec}(\overline{\kappa(s)})\to S\) is the [[algebraic-geometry-foundations/fiber-product-of-schemes|fiber product]]

\[
X_{\overline{s}}:=X\times_S\operatorname{Spec}(\overline{\kappa(s)}).
\]

The ordinary fiber is \(X_s=X\times_S\operatorname{Spec}(\kappa(s))\); the geometric fiber extends its scalars to an algebraic closure.

## Reference

[Stacks Project, Geometrically regular schemes, Tag 038S](https://stacks.math.columbia.edu/tag/038S).
