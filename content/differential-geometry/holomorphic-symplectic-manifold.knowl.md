+++
id = "differential-geometry/holomorphic-symplectic-manifold"
title = "Holomorphic symplectic manifold"
kind = "definition"
summary = "A complex manifold equipped with a closed nondegenerate holomorphic two-form."
aliases = ["complex symplectic manifold"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

A **holomorphic symplectic manifold** is a pair \((X,\sigma)\) consisting of a [[differential-geometry/complex-manifold|complex manifold]] \(X\) and a [[differential-geometry/holomorphic-symplectic-form|holomorphic symplectic form]] \(\sigma\) on it. Thus \(\sigma\) is a closed holomorphic \(2\)-form whose contraction map \(T^{1,0}X\to T^{*1,0}X\) is an isomorphism at every point. Isomorphisms of such pairs are [[differential-geometry/biholomorphism|biholomorphisms]] \(f:X\to Y\) satisfying \(f^*\sigma_Y=\sigma_X\). Saying merely that \(X\) “is holomorphic symplectic” usually asserts the existence of some such form without selecting one.
The complex structure and form are both part of the equipped object; neither is determined solely by the underlying [[fiber-bundles/smooth-manifold|smooth manifold]].

## Structural consequences

The complex dimension of \(X\) is even, say \(2m\), and \(\sigma^m\) is a nowhere-vanishing holomorphic top form. Therefore the canonical bundle of \(X\) is trivial. The real and imaginary parts of \(\sigma\) make the underlying smooth manifold symplectic in two different ways.

If \(X\) is compact and Kähler, these facts place it inside Ricci-flat Kähler geometry. They do not by themselves imply simple connectedness, irreducibility, or one-dimensionality of the space of holomorphic \(2\)-forms.

## Standard examples

The total space of the [[differential-geometry/holomorphic-cotangent-bundle|holomorphic cotangent bundle]] of any complex manifold carries its canonical holomorphic symplectic form. Complex tori of even dimension also admit translation-invariant examples whenever their tangent [[linear-algebra/vector-space|vector space]] is equipped with a nondegenerate alternating complex form.

A K3 surface carries a nowhere-vanishing holomorphic \(2\)-form and is the basic compact simply connected example. Products of K3 surfaces are holomorphic symplectic but fail the irreducibility condition described below.

## Relation to hyperkähler terminology

An **[[differential-geometry/irreducible-holomorphic-symplectic-manifold|irreducible holomorphic symplectic manifold]]** is usually required to be compact, Kähler, and simply connected, with \(H^0(X,\Omega_X^2)\) spanned by its symplectic form. Under these hypotheses it corresponds to the compact irreducible hyperkähler setting [Huybrechts, §1].

**Warning.** Some authors use “holomorphic symplectic” or “hyperkähler” only for this compact irreducible class. The definition in this knowl is broader and includes noncompact [[fiber-bundles/cotangent-bundle|cotangent bundles]], complex tori, and products.

## References

1. Daniel Huybrechts, “Compact Hyperkähler Manifolds: Basic Results,” *Inventiones Mathematicae* 135 (1999), 63–113. [DOI record](https://doi.org/10.1007/s002220050280). Relevant: §1, irreducible holomorphic symplectic and hyperkähler manifolds.
2. Arnaud Beauville, “Holomorphic Symplectic Geometry: A Problem List,” in *Complex and Differential Geometry*, Springer Proceedings in Mathematics 8, 2011. [Author-hosted paper](https://math.univ-cotedazur.fr/~beauvill/pubs/Pbsymp.pdf). Relevant: §1.1, definitions and standard compact examples.
