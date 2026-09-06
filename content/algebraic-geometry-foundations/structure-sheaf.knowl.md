+++
id = "algebraic-geometry-foundations/structure-sheaf"
title = "Structure sheaf"
kind = "knowl"
summary = "The sheaf of rings that supplies the local algebraic functions on a scheme."
aliases = ["structure-sheaf", "Structure sheaf"]
domains = ["algebraic-geometry-foundations"]
legacy_source_path = "algebraic-geometry-foundations/structure-sheaf.md"
prerequisites = ["algebraic-geometry-foundations/sheaf", "algebra-commutative/prime-spectrum", "algebra-commutative/localization-ring", "algebraic-geometry-foundations/stalk", "algebra-commutative/local-ring"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **structure sheaf** on a space \(X\) is a [[algebraic-geometry-foundations/sheaf|sheaf]] of rings \(\mathcal O_X\) whose sections are regarded as functions on open subsets of \(X\). A [[algebraic-geometry-foundations/scheme|scheme]] is not merely its topological space: its structure sheaf carries the local algebra that distinguishes it from other schemes with the same points.

For the [[algebra-commutative/prime-spectrum|prime spectrum]] \(X=\operatorname{Spec}A\), the structure sheaf is characterized on a basic Zariski open set
\[
D(f)=\{\mathfrak p\in\operatorname{Spec}A:f\notin\mathfrak p\}
\]
by
\[
\mathcal O_X(D(f))=A_f,
\]
the [[algebra-commutative/localization-ring|localization]] obtained by inverting \(f\). At a point \(\mathfrak p\), its [[algebraic-geometry-foundations/stalk|stalk]] is \(\mathcal O_{X,\mathfrak p}\cong A_{\mathfrak p}\), a [[algebra-commutative/local-ring|local ring]].

## Examples

On \(\operatorname{Spec}k[x]\), the section \(1/x\) is regular on \(D(x)\), although it is not a global polynomial.
