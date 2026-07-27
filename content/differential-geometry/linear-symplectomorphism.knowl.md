+++
id = "differential-geometry/linear-symplectomorphism"
title = "Linear symplectomorphism"
kind = "definition"
summary = "An invertible linear map that preserves the symplectic forms on its source and target."
aliases = ["symplectic linear isomorphism", "linear canonical transformation"]
domains = ["differential-geometry", "linear-algebra"]
section_mode = "progressive"
+++

Let \((V,\omega_V)\) and \((W,\omega_W)\) be finite-dimensional [[differential-geometry/symplectic-vector-space|symplectic vector spaces]]. A **linear symplectomorphism** is a bijective [[differential-geometry/symplectic-linear-map|symplectic linear map]] \(T:V\to W\); explicitly,
\[
\omega_W(Tv,Tv')=\omega_V(v,v')
\quad\text{for all }v,v'\in V.
\]
Its inverse is automatically symplectic. When \(V=W\) and \(\omega_V=\omega_W=\omega\), linear symplectomorphisms are the automorphisms of the pair \((V,\omega)\).
Equivalently, \(T\) is an isomorphism of [[linear-algebra/vector-space|vector spaces]] carrying the target form exactly to the source form, with no choice of basis involved.

## Automorphism group

The automorphisms of \((V,\omega)\) form the [[lie-groups/symplectic-group|symplectic group]] \(\operatorname{Sp}(V,\omega)\) under composition. After choosing a [[differential-geometry/symplectic-basis|symplectic basis]], this group is represented by matrices satisfying
\[
A^{\mathsf T}JA=J.
\]
Taking determinants gives \((\det A)^2=1\); in fact every real symplectic matrix has determinant \(1\).

## Relation to general symplectic maps

A symplectic linear map between finite-dimensional spaces of equal dimension is automatically a linear symplectomorphism because it is injective. In unequal dimensions a symplectic linear map can exist only from the smaller space to the larger one and need not be onto. Thus “symplectic” and “[[differential-geometry/symplectomorphism|symplectomorphism]]” should not be conflated when source and target dimensions may differ.

## Examples and conventions

Every change from one symplectic basis of \(V\) to another is a linear symplectomorphism. On \((\mathbb R^2,dx\wedge dy)\), rotations and the shear \((x,y)\mapsto(x+y,y)\) are examples, whereas \((x,y)\mapsto(2x,2y)\) is not. In Hamiltonian mechanics, “linear canonical transformation” is a common synonym when the chosen form is the standard phase-space form.

## References

1. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: Chapter 2, linear symplectic geometry.
2. Victor Guillemin and Shlomo Sternberg, *Symplectic Techniques in Physics*, Cambridge University Press, 1984. [Publisher record](https://doi.org/10.1017/CBO9780511624112). Relevant: Chapter 1, the linear symplectic group.
