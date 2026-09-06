+++
id = "operator-algebras/normal-star-homomorphism"
title = "Normal *-homomorphism"
kind = "definition"
summary = "A star homomorphism between von Neumann algebras that is continuous for their ultraweak topologies."
aliases = ["ultraweakly continuous star homomorphism"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/star-homomorphism", "operator-algebras/normal-linear-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) and \(N\) be
[[operator-algebras/von-neumann-algebra|von Neumann algebras]]. A
[[operator-algebras/star-homomorphism|\(*\)-homomorphism]]
\(\pi:M\to N\) is **normal** if it is
[[operator-algebras/normal-linear-map|normal as a linear map]], equivalently
continuous from the ultraweak topology of \(M\) to that of \(N\). Thus there
is a bounded preadjoint \(\pi_*:N_*\to M_*\) satisfying
\[
\pi_*(\omega)=\omega\circ\pi\qquad(\omega\in N_*).
\]
Normality does not by itself require \(\pi\) to be unital or injective.
If the chosen category uses unital morphisms, preservation of the identity is
an additional axiom.

## Equivalent order criterion

Because every \(*\)-homomorphism is positive, \(\pi\) is normal exactly when
it preserves suprema of bounded increasing nets of positive elements:
\[
\pi\!\left(\sup_i x_i\right)=\sup_i\pi(x_i).
\]
It is enough to test the corresponding monotone-continuity condition on
increasing nets of projections. This criterion is order-theoretic but is
equivalent to ultraweak continuity only because the map is positive.

## Examples and a non-example

The identity map, inclusions of von Neumann subalgebras, and spatial
amplifications \(x\mapsto x\otimes I_K\) are normal. In contrast, let
\(\mathcal U\) be a free ultrafilter on \(\mathbb N\). The ultrafilter
character
\[
\ell^\infty(\mathbb N)\longrightarrow\mathbb C,\qquad
(x_n)\longmapsto\lim_{\mathcal U}x_n
\]
is a unital \(*\)-homomorphism but is not normal: the projections onto the
first \(m\) coordinates increase to \(1\), while every one has ultrafilter
limit \(0\).

## Stability and conventions

Composites of normal \(*\)-homomorphisms are normal, and restricting the
codomain to a von Neumann subalgebra containing the range does not change
normality. The terms “normal,” “ultraweakly continuous,” and “weak-star
continuous” agree here when each algebra carries its canonical predual.

**Warning.** Norm continuity is insufficient: every \(*\)-homomorphism of
\(C^*\)-algebras is norm-continuous, including the non-normal ultrafilter
character above.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: the chapters on von Neumann algebra topologies, preduals, and normal maps.
2. Shôichirô Sakai, *C*-Algebras and *W*-Algebras, Springer, 1971; Classics in Mathematics reprint, 1998. [DOI record](https://doi.org/10.1007/978-3-642-61993-9). Relevant: the abstract predual formulation and normal homomorphisms.
