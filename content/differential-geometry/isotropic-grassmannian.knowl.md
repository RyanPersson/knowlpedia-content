+++
id = "differential-geometry/isotropic-grassmannian"
title = "Isotropic Grassmannian"
kind = "definition"
summary = "The parameter space of fixed-dimensional isotropic subspaces of a symplectic vector space."
aliases = ["symplectic Grassmannian of isotropic planes"]
domains = ["differential-geometry", "linear-algebra"]
prerequisites = ["differential-geometry/symplectic-vector-space", "differential-geometry/grassmannian", "differential-geometry/isotropic-subspace"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((V,\omega)\) be a \(2n\)-dimensional real or complex [[differential-geometry/symplectic-vector-space|symplectic vector space]], and let \(0\leq k\leq n\). The **isotropic Grassmannian** is
\[
\operatorname{IGr}_k(V,\omega)
=\{L\in\operatorname{Gr}_k(V):\omega|_{L\times L}=0\}.
\]
It is the subspace of the [[differential-geometry/grassmannian|Grassmannian]] consisting of \(k\)-planes that are [[differential-geometry/isotropic-subspace|isotropic]]. The bound \(k\leq n\) is forced by nondegeneracy of \(\omega\). Over \(\mathbb R\) it is a smooth compact manifold; over \(\mathbb C\) it is also a smooth projective variety.
Its points therefore parametrize isotropic subspaces while retaining their position inside the fixed ambient symplectic space.

## Homogeneous-space structure

The [[lie-groups/symplectic-group|symplectic group]] of \((V,\omega)\) acts transitively on \(\operatorname{IGr}_k(V,\omega)\). Over \(\mathbb C\), the stabilizer of an isotropic \(k\)-plane is a parabolic subgroup, so the isotropic Grassmannian is a homogeneous projective variety. Its dimension over the base field is
\[
k(2n-k)-\binom{k}{2}.
\]
This results from imposing the \(\binom{k}{2}\) independent equations expressing the vanishing of \(\omega\) on the tautological \(k\)-plane.

## Extremal cases and examples

For \(k=1\), every line is isotropic, so \(\operatorname{IGr}_1(V,\omega)=\operatorname{Gr}_1(V)\). For \(k=n\), isotropic subspaces are maximal and therefore Lagrangian; the resulting space is the [[differential-geometry/lagrangian-grassmannian|Lagrangian Grassmannian]]. A \(k\)-plane on which \(\omega\) has nonzero restriction is a decisive non-example.

## Conventions and scope

“Isotropic Grassmannian” is also used for quadratic spaces, where isotropy is defined by a symmetric quadratic form and the resulting orthogonal Grassmannian has different geometry. The notation \(\operatorname{IGr}\) here always refers to a nondegenerate alternating form. The real [[fiber-bundles/smooth-manifold|smooth manifold]] and complex projective variety are two scalar-field realizations of the same incidence condition.

## References

1. William Fulton and Joe Harris, *Representation Theory: A First Course*, Springer, 1991. [Springer DOI record](https://doi.org/10.1007/978-1-4612-0979-9). Relevant: §17.3, symplectic groups, isotropic flags, and their homogeneous spaces.
2. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Springer, 2001. [Springer DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: Chapter 1, symplectic linear algebra and isotropic and Lagrangian subspaces.
