+++
id = "mathematical-physics/supertranslation-algebra"
title = "Supertranslation algebra"
kind = "definition"
summary = "A two-step nilpotent Lie superalgebra whose odd spinors bracket into even spacetime translations."
aliases = ["supersymmetry translation algebra", "supertranslation Lie superalgebra"]
domains = ["mathematical-physics", "supergeometry"]
prerequisites = ["differential-geometry/spinor-module", "algebra-modules/bilinear-map", "supergeometry/lie-superalgebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((V,\eta)\) be a real pseudo-Euclidean vector space, let \(S\) be a real
[[differential-geometry/spinor-module|spinor module]], and choose a
\(\operatorname{Spin}(V,\eta)\)-equivariant symmetric [[algebra-modules/bilinear-map|bilinear map]]
\[
\Gamma:\operatorname{Sym}^2 S\longrightarrow V.
\]
The corresponding **supertranslation algebra** is the [[supergeometry/lie-superalgebra|Lie superalgebra]]
\[
\mathfrak t=V_{\bar0}\oplus S_{\bar1}
\]
with
\[
[s_1,s_2]=\Gamma(s_1,s_2),\qquad
[V,V]=[V,S]=0.
\]
It is two-step nilpotent when \(\Gamma\ne0\).

Because \(S\) is odd, graded skew-symmetry makes its odd–odd bracket
**symmetric**, not alternating. Since \(V\) is central, the
odd–odd–odd Jacobi identity is automatic. Spin-equivariance is the condition
needed to let Lorentz transformations act by automorphisms.

## Choices and variants

The spinor representation and the admissible bilinear maps depend on
dimension, signature, reality condition, and chirality. Extended
\(\mathcal N\)-supersymmetry replaces \(S\) by spinors tensored with a
multiplicity space. Central or higher-degree “brane charges” are extensions
of the basic supertranslation algebra rather than part of this definition.

The ordinary translation algebra \(V\) is the even reduction. Adjoining the
Lorentz algebra produces the
[[mathematical-physics/super-poincare-algebra|super-Poincaré algebra]], while
integrating \(\mathfrak t\) produces
[[supergeometry/super-minkowski-space|super-Minkowski space]] with its
supertranslation group structure and
[[supergeometry/supertranslation-distribution|supertranslation
distribution]].

## References

1. P. Deligne and J. W. Morgan, “Notes on supersymmetry (following Joseph Bernstein),” in *Quantum Fields and Strings: A Course for Mathematicians*, Volume 1, American Mathematical Society, 1999, 41–97. Relevant: spinors and supertranslation algebras.
2. J. Figueroa-O'Farrill, “Majorana spinors,” lecture notes, 2001. [Author manuscript](https://www.maths.ed.ac.uk/~jmf/Teaching/Lectures/Majorana.pdf). Relevant: admissible spinor bilinears and supersymmetry algebras.
