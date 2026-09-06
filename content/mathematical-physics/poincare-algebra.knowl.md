+++
id = "mathematical-physics/poincare-algebra"
title = "Poincaré algebra"
kind = "definition"
summary = "The semidirect-product Lie algebra of Lorentz transformations and spacetime translations."
aliases = ["inhomogeneous Lorentz algebra", "Poincare Lie algebra", "iso(1,3)"]
domains = ["mathematical-physics", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/minkowski-vector-space", "lie-groups/poincare-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((V,\eta)\) be a finite-dimensional real Minkowski vector space, so
\(\eta\) has Lorentzian signature. Its **Poincaré algebra** is the
semidirect-product [[lie-groups/lie-algebra|Lie algebra]]
\[
\mathfrak{iso}(V,\eta)
=\mathfrak{so}(V,\eta)\ltimes V,
\]
where the translation algebra \(V\) is abelian and
\(\mathfrak{so}(V,\eta)\) acts through its defining representation. Its
bracket is
\[
[(A,v),(B,w)]
=\bigl([A,B],Aw-Bv\bigr).
\]

For four-dimensional [[linear-algebra/minkowski-vector-space|Minkowski
space]], this is \(\mathfrak{iso}(1,3)\), with dimension \(6+4=10\). It is
the Lie algebra of the [[lie-groups/poincare-group|Poincaré group]] and of its
identity component. Thus passing to the proper, orthochronous component does
not change the Lie algebra.

For a nondegenerate form of arbitrary signature, the same semidirect-product
formula defines the **inhomogeneous orthogonal algebra**
\(\mathfrak{iso}(p,q)\). The name “Poincaré algebra” is reserved here for
Lorentzian signature.

## Structure and extensions

The Lorentz algebra is a subalgebra and the translations form an abelian
ideal. The quotient by translations is \(\mathfrak{so}(V,\eta)\). This
semidirect structure is extended in the
[[mathematical-physics/super-poincare-algebra|super-Poincaré algebra]] by
odd supercharges whose bracket produces translations.

[[algebra-groups/central-extension|Central extensions]], internal \(R\)-symmetries, and conformal extensions are
additional structures, not part of the unextended Poincaré algebra.

## References

1. S. Weinberg, *The Quantum Theory of Fields, Volume I: Foundations*, Cambridge University Press, 1995. [Publisher record](https://doi.org/10.1017/CBO9781139644167). Relevant: Chapter 2.
2. J. Figueroa-O'Farrill, “Classification of kinematical Lie algebras,” *Journal of Mathematical Physics* 59, 2018, 061701. [Article](https://doi.org/10.1063/1.5016285).
