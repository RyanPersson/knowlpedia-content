+++
id = "algebraic-geometry-foundations/projective-semilinear-group"
title = "Projective semilinear group"
kind = "definition"
summary = "The collineation group obtained from invertible semilinear maps modulo scalar maps."
aliases = ["PGammaL", "PΓL", "projective semilinear transformations"]
domains = ["algebraic-geometry-foundations", "algebra-groups"]
prerequisites = ["linear-algebra/vector-space", "linear-algebra/semilinear-map"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(V\ne0\) be a finite-dimensional [[linear-algebra/vector-space|vector space]] over a field \(k\). The group \(\Gamma L(V)\) consists of all bijective [[linear-algebra/semilinear-map|semilinear self-maps]] of \(V\), allowing every automorphism of \(k\). Its **projective semilinear group** is
\[
\operatorname{P\Gamma L}(V):=\Gamma L(V)/(k^\times I).
\]
The scalar subgroup is normal because a \(\sigma\)-semilinear map conjugates \(\lambda I\) to \(\sigma(\lambda)I\).

## Action and exact sequence

Every semilinear bijection sends lines to lines, so \(\operatorname{P\Gamma L}(V)\) acts faithfully on the incidence geometry of \(\mathbb P(V)\) when \(\dim_kV\ge2\). The automorphism associated to a nonzero semilinear map is unique, and gives an exact sequence
\[
1\longrightarrow\operatorname{PGL}(V)
\longrightarrow\operatorname{P\Gamma L}(V)
\longrightarrow\operatorname{Aut}(k)
\longrightarrow1.
\]
For \(V=k^n\), choosing a basis lifts \(\sigma\in\operatorname{Aut}(k)\) by applying \(\sigma\) coordinatewise, so this sequence splits, though the splitting depends on coordinates.

## Collineations

In projective dimension at least two, the [[algebraic-geometry-foundations/fundamental-theorem-of-projective-geometry|fundamental theorem of projective geometry]] identifies \(\operatorname{P\Gamma L}(V)\) with the full group of collineations of the Desarguesian [[algebraic-geometry-foundations/projective-space|projective space]] \(\mathbb P(V)\). If \(\operatorname{Aut}(k)\) is trivial, then \(\operatorname{P\Gamma L}(V)=\operatorname{PGL}(V)\).

## References

1. Emil Artin, *Geometric Algebra*, Interscience, 1957. Relevant: Chapter II, §§3–4.
2. Peter J. Cameron, *Projective and Polar Spaces*, Queen Mary and Westfield College, 1992. [Author-maintained text](https://www.maths.qmul.ac.uk/~pjc/pps/). Relevant: Chapter 1.
