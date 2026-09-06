+++
id = "fiber-bundles/intrinsic-torsion-of-a-g-structure"
title = "Intrinsic torsion of a G-structure"
kind = "definition"
summary = "The connection-independent torsion class that obstructs a G-structure from admitting a torsion-free compatible connection."
aliases = ["intrinsic torsion", "torsion class of a G-structure"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["lie-groups/lie-algebra", "fiber-bundles/g-structure", "fiber-bundles/connection-compatible-with-a-reduction", "fiber-bundles/associated-bundle"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(V=\mathbb R^n\), let \(G\subseteq\operatorname{GL}(V)\) have [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\), and let \(Q\) be a [[fiber-bundles/g-structure|\(G\)-structure]] on an \(n\)-manifold. A [[fiber-bundles/connection-compatible-with-a-reduction|compatible connection]] has torsion in \(\Lambda^2V^*\otimes V\). Changing the connection by \(A\in V^*\otimes\mathfrak g\) changes its torsion by
\[
\delta A(u,v)=A(u)v-A(v)u.
\]
The **intrinsic torsion** of \(Q\) is the resulting section of the [[fiber-bundles/associated-bundle|associated bundle]] with fiber
\[
\frac{\Lambda^2V^*\otimes V}{\delta(V^*\otimes\mathfrak g)}.
\]
Its class is independent of the chosen compatible connection.
These fiberwise classes transform \(G\)-equivariantly, which is why they assemble into a globally defined tensorial section on \(M\).

## Obstruction interpretation

The intrinsic torsion vanishes exactly when the \(G\)-structure admits at least one torsion-free compatible connection. Indeed, vanishing says that the torsion of a chosen compatible connection lies in the image of \(\delta\); subtracting the corresponding \(\mathfrak g\)-valued connection change removes it. Conversely, every torsion-free compatible connection represents the zero class.

This is an existence obstruction, not generally a uniqueness statement. The kernel of
\[
\delta:V^*\otimes\mathfrak g\longrightarrow\Lambda^2V^*\otimes V
\]
measures how two torsion-free compatible connections may differ.

## Decomposition into torsion classes

When \(G\) is compact, invariant [[linear-algebra/inner-product|inner products]] allow the quotient to be represented by a \(G\)-invariant complement to \(\delta(V^*\otimes\mathfrak g)\). Decomposing that complement into irreducible \(G\)-modules yields the named torsion classes used for almost Hermitian, \(G_2\), and \(\operatorname{Spin}(7)\) structures. The quotient definition remains canonical even when no preferred complement is chosen.

For an \(\operatorname O(n)\)-structure, the Levi–Civita connection is torsion-free and compatible, so intrinsic torsion vanishes. For an almost Hermitian \(U(n)\)-structure, nonzero components measure failures of the associated almost complex and fundamental-form data to satisfy stronger integrability conditions.

## Conventions and scope

Some authors call a chosen representative in a preferred complement “the intrinsic torsion,” while others reserve the term for the quotient class. These are equivalent only after the complement has been fixed. Intrinsic torsion must also be distinguished from the [[fiber-bundles/torsion-2-form|torsion]] of a particular compatible connection, which depends on that connection.

## References

1. Simon Salamon, *Riemannian Geometry and Holonomy Groups*, Pitman Research Notes in Mathematics 201, Longman Scientific & Technical, 1989. [Bibliographic record](https://openlibrary.org/books/OL2032692M/Riemannian_geometry_and_holonomy_groups). Relevant: Chapter 4, \(G\)-structures, torsion, and holonomy reductions.
2. Andreas Čap and Jan Slovák, *Parabolic Geometries I: Background and General Theory*, Mathematical Surveys and Monographs 154, American Mathematical Society, 2009. [AMS record](https://bookstore.ams.org/surv-154). Relevant: §3.1, underlying structures and intrinsic torsion.
