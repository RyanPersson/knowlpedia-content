+++
id = "operator-algebras/normal-positive-map"
title = "Normal positive map"
kind = "definition"
summary = "A positive linear map between von Neumann algebras that is ultraweakly continuous."
aliases = ["normal order-positive map"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/positive-linear-map", "operator-algebras/normal-linear-map"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) and \(N\) be
[[operator-algebras/von-neumann-algebra|von Neumann algebras]]. A **normal
positive map** is a
[[operator-algebras/positive-linear-map|positive linear map]]
\(\Phi:M\to N\) that is
[[operator-algebras/normal-linear-map|normal]], meaning ultraweakly
continuous. Equivalently, for every bounded increasing net
\((x_i)\) in \(M_+\),
\[
\Phi\!\left(\sup_i x_i\right)=\sup_i\Phi(x_i).
\]
No unitality, faithfulness, or complete positivity is implicit. Since von
Neumann algebras are unital, positivity already makes \(\Phi\) bounded; the
extra adjective “normal” specifies its compatibility with the preduals and
with monotone suprema.

## Preadjoint and order criteria

Normality is equivalent to the existence of a bounded preadjoint
\(\Phi_*:N_*\to M_*\) given by
\[
\Phi_*(\omega)=\omega\circ\Phi.
\]
For positive maps, it is enough to test monotone preservation on increasing
nets of projections. These formulations let one pass between weak-star
continuity, [[operator-algebras/normal-functional|normal functionals]], and
order convergence.

## Examples and a non-example

Every [[operator-algebras/normal-star-homomorphism|normal
\(*\)-homomorphism]] is a normal positive map. If \(\xi\in H\), the vector
functional
\[
\mathcal B(H)\longrightarrow\mathbb C,\qquad
x\longmapsto\langle x\xi,\xi\rangle
\]
is normal and positive. [[operator-algebras/normal-conditional-expectation|Normal conditional expectations]] provide
operator-valued examples. By contrast, a free-ultrafilter state on
\(\ell^\infty(\mathbb N)\) is positive and unital but not normal, because it
sends every finite-coordinate projection to \(0\) although those projections
increase to \(1\).

## Stability and distinctions

Compositions and positive scalar multiples of normal positive maps remain
normal and positive. Matrix amplification introduces a separate condition:
a normal positive map need not be completely positive, while a
[[operator-algebras/normal-completely-positive-map|normal completely positive map]]
is normal at every matrix level.

**Warning.** “Normal” is not a synonym for positive, unital, or
norm-continuous. It is the monotone or weak-star continuity condition, and
dropping it permits positive maps that ignore increasing limits.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: the chapters on preduals, normal maps, positive maps, and monotone convergence.
2. Shôichirô Sakai, *C*-Algebras and *W*-Algebras, Springer, 1971; Classics in Mathematics reprint, 1998. [DOI record](https://doi.org/10.1007/978-3-642-61993-9). Relevant: order and weak-star formulations of normal positive maps.
