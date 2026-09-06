+++
id = "lie-groups/weights-of-the-defining-sl3-representation"
title = "Weights of the defining sl₃-representation"
kind = "example"
summary = "The three multiplicity-one weights of the natural three-dimensional representation of sl3."
aliases = ["weights of the standard sl3 representation", "sl3 defining weights", "weight diagram of the 3 of sl3"]
domains = ["lie-groups", "representation-theory"]
prerequisites = ["lie-groups/defining-representation-of-a-classical-lie-algebra", "lie-groups/cartan-subalgebra", "lie-groups/weight-of-a-representation"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(V=\mathbb C^3\) be the [[lie-groups/defining-representation-of-a-classical-lie-algebra|defining representation]] of \(\mathfrak{sl}_3(\mathbb C)\), and take the [[lie-groups/cartan-subalgebra|Cartan subalgebra]]
\[
\mathfrak h=\left\{\operatorname{diag}(h_1,h_2,h_3):
h_1+h_2+h_3=0\right\}.
\]
Define \(\varepsilon_i\in\mathfrak h^*\) by \(\varepsilon_i(\operatorname{diag}(h_1,h_2,h_3))=h_i\). Then the three [[lie-groups/weight-of-a-representation|weights]] of \(V\) are
\[
\varepsilon_1,\qquad\varepsilon_2,\qquad\varepsilon_3,
\qquad
\varepsilon_1+\varepsilon_2+\varepsilon_3=0,
\]
each with multiplicity one. The standard basis vector \(e_i\) spans the \(\varepsilon_i\)-weight space.

## Simple-root coordinates

Choose the [[lie-groups/simple-root|simple roots]]
\[
\alpha_1=\varepsilon_1-\varepsilon_2,
\qquad
\alpha_2=\varepsilon_2-\varepsilon_3.
\]
With the corresponding [[lie-groups/positive-root|positive roots]], the [[lie-groups/highest-weight|highest weight]] is
\[
\omega_1=\varepsilon_1.
\]
The three weights form the string
\[
\omega_1,\qquad
\omega_1-\alpha_1,\qquad
\omega_1-\alpha_1-\alpha_2.
\]
Geometrically they are the vertices of an equilateral triangle centered at the origin in the two-dimensional real span of the roots. The [[lie-groups/weyl-group|Weyl group]] \(S_3\) permutes the three vertices.

## Exterior power and dual

The second exterior power has weights
\[
\varepsilon_1+\varepsilon_2=-\varepsilon_3,
\quad
\varepsilon_1+\varepsilon_3=-\varepsilon_2,
\quad
\varepsilon_2+\varepsilon_3=-\varepsilon_1.
\]
The determinant volume form identifies
\[
\Lambda^2V\cong V^*,
\]
whose highest weight is \(\omega_2=-\varepsilon_3\). This realizes the nontrivial symmetry of the \(A_2\) [[lie-groups/dynkin-diagram|Dynkin diagram]] as the exchange of the defining representation with its [[lie-groups/dual-representation-lie|dual]].

## Group-level form

The same weight calculation describes the defining representation of \(SL_3(\mathbb C)\). It does not descend to \(PSL_3(\mathbb C)\), because the center acts by nontrivial scalar matrices. Infinitesimal weight data alone do not record this obstruction.

## References

1. William Fulton and Joe Harris, *Representation Theory: A First Course*, Springer, 1991, §§12–15. [Publisher record](https://doi.org/10.1007/978-1-4612-0979-9).
2. Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015, Chapters 7 and 10. [Publisher record](https://doi.org/10.1007/978-3-319-13467-3).
