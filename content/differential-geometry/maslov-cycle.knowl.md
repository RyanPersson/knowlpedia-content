+++
id = "differential-geometry/maslov-cycle"
title = "Maslov cycle"
kind = "definition"
summary = "The singular incidence hypersurface of Lagrangian planes that fail to be transverse to a fixed Lagrangian plane."
aliases = ["train of a Lagrangian", "Maslov hypersurface"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/symplectic-vector-space", "differential-geometry/lagrangian-grassmannian"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((V,\omega)\) be a real \(2n\)-dimensional [[differential-geometry/symplectic-vector-space|symplectic vector space]], let \(\Lambda(V)\) be its [[differential-geometry/lagrangian-grassmannian|Lagrangian Grassmannian]], and fix \(L_0\in\Lambda(V)\). The **Maslov cycle**, or **train of \(L_0\)**, is
\[
\Sigma(L_0)=\{L\in\Lambda(V):L\cap L_0\neq\{0\}\}.
\]
It is the complement of the open set of Lagrangian planes transverse to \(L_0\). More precisely, \(\Sigma(L_0)\) is a stratified hypersurface with strata
\[
\Sigma_k(L_0)=\{L:\dim(L\cap L_0)=k\},\qquad k\geq1.
\]
The stratum \(\Sigma_1(L_0)\) is a smooth dense hypersurface; strata with \(k\geq2\) form its singular locus. A standard coorientation of the top stratum turns signed intersections with \(\Sigma(L_0)\) into [[differential-geometry/maslov-index|Maslov indices]].

## Stratification

The stratum \(\Sigma_k(L_0)\) has codimension \(k(k+1)/2\) in \(\Lambda(V)\). This follows from a local chart in which nearby Lagrangians are graphs of symmetric forms: the intersection with \(L_0\) becomes the kernel, and the rank-defect-\(k\) locus has that codimension. In particular, the first singular stratum has codimension three, so a generic one-parameter path meets only the smooth stratum.

## Coorientation and crossings

At \(L\in\Sigma_1(L_0)\), a tangent vector to \(\Lambda(V)\) is represented by a quadratic form on \(L\). Restricting it to the line \(L\cap L_0\) gives a scalar; its sign distinguishes the two normal directions and defines the coorientation. For a smooth path \(L(t)\), the corresponding restriction is the crossing form. A nondegenerate crossing is isolated, and its signature gives the local intersection contribution.

## Example in dimension two

When \(V=\mathbb R^2\), every line is Lagrangian and \(\Lambda(V)\cong\mathbb RP^1\cong S^1\). For a fixed line \(L_0\), the Maslov cycle consists of the single point \(L_0\). A rotating line crosses this point once during a half-turn, with sign determined by the direction of rotation. There are no singular strata because two one-dimensional Lagrangians cannot intersect in dimension at least two.

## Conventions and scope

Some authors use \(\Sigma_k\) for the closed locus \(\dim(L\cap L_0)\geq k\), while others use it for the exact-\(k\) stratum. Here \(\Sigma_k(L_0)\) means exact intersection dimension, and \(\Sigma(L_0)\) is their union. The cycle is not a smooth hypersurface globally; treating it as one discards the higher-incidence strata that matter for nongeneric endpoints.

## References

1. V. I. Arnol'd, “On a characteristic class entering into conditions of quantization,” *Functional Analysis and Its Applications* 1 (1967), 1–14. [DOI record](https://doi.org/10.1007/BF01079201). Relevant: the Maslov cycle and its associated characteristic class.
2. Joel Robbin and Dietmar Salamon, “The Maslov index for paths,” *Topology* 32 (1993), 827–844. [DOI record](https://doi.org/10.1016/0040-9383%2893%2990052-W). Relevant: §§1–2, strata, crossing forms, and path indices.
