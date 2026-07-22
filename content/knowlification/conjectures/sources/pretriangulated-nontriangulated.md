Let \(\mathcal C\) be a preadditive category with a zero object and an additive shift autoequivalence \([1]:\mathcal C\to\mathcal C\). A triangle is a diagram
\[
X\xrightarrow{f}Y\xrightarrow{g}Z\xrightarrow{h}X[1].
\]
A chosen class of distinguished triangles makes \(\mathcal C\) pretriangulated, in the convention used by mathlib, when it is stable under isomorphism and rotation, every morphism extends to a distinguished triangle, and morphisms between the first two terms of distinguished triangles can be completed to morphisms of triangles.

A triangulated category is a pretriangulated category that also satisfies the octahedral axiom. For composable morphisms \(X\to Y\to Z\), that axiom relates distinguished triangles for the two maps and their composite by an additional distinguished triangle and a commuting octahedral diagram.

## Open problem

Does there exist a pretriangulated category that is not triangulated? Equivalently, do the pretriangulated axioms force the octahedral axiom, or can one choose distinguished triangles satisfying the former axioms while violating the latter?

This is a logical independence question about axiom systems, not merely a request for a pathological category. A positive answer requires an explicit category, shift, and distinguished-triangle class satisfying all pretriangulated obligations, together with a demonstrated failure of octahedrality.

## Formal source

This page follows `FormalConjectures/Mathoverflow/31809.lean`. In its mathlib formulation, the assumptions provide `Pretriangulated C`, while the desired conclusion is `IsTriangulated C`; the latter is precisely the extra octahedron condition in `Mathlib.CategoryTheory.Triangulated.Triangulated`.
