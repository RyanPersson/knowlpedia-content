+++
id = "differential-geometry/symplectic-basis-theorem"
title = "Symplectic basis theorem"
kind = "theorem"
summary = "Every finite-dimensional symplectic vector space has even dimension and a basis in standard symplectic form."
aliases = ["linear Darboux theorem", "symplectic Gram–Schmidt theorem"]
domains = ["differential-geometry", "linear-algebra"]
section_mode = "progressive"
+++

Let \((V,\omega)\) be a finite-dimensional real [[differential-geometry/symplectic-vector-space|symplectic vector space]]. The **symplectic basis theorem** states that \(\dim V=2n\) for some \(n\) and that \(V\) has a [[differential-geometry/symplectic-basis|symplectic basis]]
\[
(e_1,\ldots,e_n,f_1,\ldots,f_n)
\]
with
\[
\omega(e_i,e_j)=\omega(f_i,f_j)=0,
\qquad \omega(e_i,f_j)=\delta_{ij}.
\]
Consequently every nondegenerate alternating form of dimension \(2n\) has the same matrix after a change of basis.
In particular, no odd-dimensional real [[linear-algebra/vector-space|vector space]] admits a symplectic form.

## Proof idea

Choose a nonzero vector \(e_1\). Nondegeneracy supplies \(f_1\) with \(\omega(e_1,f_1)=1\). The plane \(H_1=\operatorname{span}(e_1,f_1)\) is symplectic, and
\[
V=H_1\oplus H_1^\omega.
\]
The restriction of \(\omega\) to \(H_1^\omega\) is again nondegenerate. Induction repeats the construction until the complement is zero. This is the alternating-form analogue of Gram–Schmidt orthogonalization [Cannas da Silva, §1.1].

## Consequences

The decomposition into symplectic planes proves that the dimension is even. It also shows that two symplectic vector spaces over the same field are [[differential-geometry/linear-symplectomorphism|linearly symplectomorphic]] exactly when they have the same dimension. In particular, finite-dimensional symplectic linear algebra has no signature invariant analogous to that of a real symmetric [[linear-algebra/bilinear-form|bilinear form]].

## Hypotheses and terminology

The same statement holds over any [[algebra-rings/field|field]] for a nondegenerate alternating form. Characteristic different from \(2\) is needed only when one replaces “alternating” by “skew-symmetric”; in characteristic \(2\), those conditions are not equivalent. The finite-dimensional hypothesis is essential: an infinite-dimensional topological symplectic space need not possess a basis adapted to its form. “Linear Darboux theorem” refers to this algebraic result, not to the local-coordinate theorem for [[differential-geometry/symplectic-manifold|symplectic manifolds]].

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: §1.1, the symplectic basis construction.
2. Victor Guillemin and Shlomo Sternberg, *Symplectic Techniques in Physics*, Cambridge University Press, 1984. [Publisher record](https://doi.org/10.1017/CBO9780511624112). Relevant: Chapter 1, canonical form of a nondegenerate alternating form.
