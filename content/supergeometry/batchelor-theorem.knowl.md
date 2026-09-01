+++
id = "supergeometry/batchelor-theorem"
title = "Batchelor theorem"
kind = "theorem"
summary = "Every finite-dimensional smooth real supermanifold is noncanonically split."
aliases = ["Batchelor-Gawedzki theorem", "smooth splitting theorem for supermanifolds"]
domains = ["supergeometry"]
prerequisites = ["supergeometry/supermanifold", "fiber-bundles/vector-bundle"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(X\) be a finite-dimensional smooth real
[[supergeometry/supermanifold|supermanifold]] whose reduced manifold is
Hausdorff and paracompact. The **Batchelor theorem** states that there is a
[[fiber-bundles/vector-bundle|vector bundle]] \(E\to X_{\mathrm{red}}\) and an isomorphism
\[
X\cong \Pi E
\]
of supermanifolds. Equivalently,
\[
\mathcal O_X\cong
\Lambda_{\mathcal O_{X_{\mathrm{red}}}}
  (\mathcal J_X/\mathcal J_X^2),
\]
after identifying the locally free module
\(\mathcal J_X/\mathcal J_X^2\) with sections of \(E^*\).

## Noncanonical is essential

The theorem is an existence theorem. A splitting requires choices, commonly
constructed using partitions of unity, and is generally neither unique nor
natural with respect to supermanifold morphisms. Thus the smooth category is
not obtained by simply declaring that vector bundles and their exterior
algebras are the morphism-free data of all supermanifolds.

The result is special to the smooth real setting. Complex-analytic and
algebraic supermanifolds can have obstruction classes preventing a global
splitting, so the statement must not be transported to those categories
without additional hypotheses.

## References

1. M. Batchelor, “The structure of supermanifolds,” *Transactions of the American Mathematical Society* 253, 1979, 329–338. [Article](https://doi.org/10.1090/S0002-9947-1979-0536950-X).
2. K. Gawędzki, “Supersymmetries—mathematics of supergeometry,” *Annales de l’Institut Henri Poincaré A* 27(4), 1977, 335–366. [Numdam record](http://www.numdam.org/item/AIHPA_1977__27_4_335_0/).
