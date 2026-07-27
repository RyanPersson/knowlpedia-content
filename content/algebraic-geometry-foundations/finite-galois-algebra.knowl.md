+++
id = "algebraic-geometry-foundations/finite-galois-algebra"
title = "Finite Galois algebra"
kind = "definition"
summary = "A finite étale algebra with a group action satisfying the Galois torsor identity."
aliases = ["finite Galois algebra", "G-Galois algebra", "Galois algebra"]
domains = ["algebraic-geometry-foundations"]
+++

Let \(F\) be a [[algebra-rings/field|field]] and \(G\) a finite [[algebra-groups/group|group]]. A **finite \(G\)-Galois \(F\)-algebra** is a [[algebraic-geometry-foundations/finite-etale-algebra|finite étale \(F\)-algebra]] \(A\) with an action of \(G\) by \(F\)-algebra automorphisms such that the canonical map

\[
A\otimes_F A\longrightarrow\prod_{g\in G}A,
\qquad a\otimes b\longmapsto\bigl(a\,g(b)\bigr)_{g\in G}
\]

is an isomorphism.

## Interpretation

Geometrically, \(\operatorname{Spec}A\to\operatorname{Spec}F\) is a torsor under the [[algebraic-geometry-foundations/constant-finite-group-scheme|constant finite group scheme]] attached to \(G\). If \(\operatorname{Spec}A\) is [[algebraic-geometry-foundations/connected-scheme|connected]], then \(A\) is a field and \(A/F\) is a [[algebra-fields-galois/galois-extension|finite Galois extension]] with group \(G\).

## Remarks

**Warning.** Some authors use “Galois algebra” with slightly different hypotheses or for more general base rings. Stating the acting group and the canonical-map condition removes the ambiguity.
