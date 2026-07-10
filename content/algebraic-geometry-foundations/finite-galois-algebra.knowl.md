+++
id = "algebraic-geometry-foundations/finite-galois-algebra"
title = "Finite Galois algebra"
kind = "definition"
summary = "A finite étale algebra with a group action satisfying the Galois torsor identity."
aliases = ["finite Galois algebra", "G-Galois algebra", "Galois algebra"]
domains = ["algebraic-geometry-foundations"]
+++

A finite Galois field extension is the connected case. If connectedness is dropped, the same symmetry can act transitively across several field factors, so the correct algebraic object is more general than a field.

Let \(F\) be a [[algebra-rings/field|field]] and \(G\) a finite [[algebra-groups/group|group]]. A **finite \(G\)-Galois \(F\)-algebra** is a [[algebraic-geometry-foundations/finite-etale-algebra|finite étale \(F\)-algebra]] \(A\) with an action of \(G\) by \(F\)-algebra automorphisms such that the canonical map

\[
A\otimes_F A\longrightarrow\prod_{g\in G}A,
\qquad a\otimes b\longmapsto\bigl(a\,g(b)\bigr)_{g\in G}
\]

is an isomorphism. Equivalently, \(A^G=F\) and \(\dim_F A=|G|\), together with the corresponding Galois descent condition.

Geometrically, \(\operatorname{Spec}A\to\operatorname{Spec}F\) is a torsor under the [[algebraic-geometry-foundations/constant-finite-group-scheme|constant finite group scheme]] attached to \(G\). If \(\operatorname{Spec}A\) is [[algebraic-geometry-foundations/connected-scheme|connected]], then \(A\) is a field and \(A/F\) is a [[algebra-fields-galois/galois-extension|finite Galois extension]] with group \(G\).

**Warning.** Some authors use “Galois algebra” with slightly different hypotheses or for more general base rings. Stating the acting group and the canonical-map condition removes the ambiguity.
