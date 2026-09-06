+++
id = "differential-geometry/symplectic-basis"
title = "Symplectic basis"
kind = "definition"
summary = "An ordered basis in which a symplectic form has its standard block matrix."
aliases = ["Darboux basis"]
domains = ["differential-geometry", "linear-algebra"]
prerequisites = ["differential-geometry/symplectic-vector-space"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((V,\omega)\) be a \(2n\)-dimensional [[differential-geometry/symplectic-vector-space|symplectic vector space]]. A **symplectic basis** is an ordered basis
\[
(e_1,\ldots,e_n,f_1,\ldots,f_n)
\]
such that, for \(1\leq i,j\leq n\),
\[
\omega(e_i,e_j)=0,\qquad
\omega(f_i,f_j)=0,\qquad
\omega(e_i,f_j)=\delta_{ij}.
\]
Alternation then gives \(\omega(f_i,e_j)=-\delta_{ij}\). Thus the definition fixes both the pairings and the ordering of the basis vectors; an arbitrary basis made from individually isotropic vectors need not be symplectic.
Such a basis places \(\omega\) in its standard normal form.

## Matrix form

In a symplectic basis, the matrix of \(\omega\) is
\[
J=\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix}.
\]
Conversely, an ordered basis is symplectic exactly when the matrix of \(\omega\) in that basis is \(J\). This converts form-preservation questions into the matrix identity \(A^{\mathsf T}JA=J\).

## Adapted decompositions

The spans \(E=\operatorname{span}(e_1,\ldots,e_n)\) and \(F=\operatorname{span}(f_1,\ldots,f_n)\) are complementary [[differential-geometry/isotropic-subspace|isotropic subspaces]]. The form pairs \(E\) and \(F\) perfectly, so \(F\) identifies with the dual of \(E\). Each plane \(\operatorname{span}(e_i,f_i)\) is symplectic, and \(V\) is their symplectically orthogonal direct sum.

## Existence and conventions

The [[differential-geometry/symplectic-basis-theorem|symplectic basis theorem]] guarantees that such a basis exists. Some authors order the vectors as \(e_1,f_1,\ldots,e_n,f_n\), producing a block-diagonal matrix with \(2\times2\) symplectic blocks instead of the displayed \(J\). Others reverse the sign of \(J\); these are ordering conventions, not different symplectic structures.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: §1.1, symplectic bases and standard form.
2. Victor Guillemin and Shlomo Sternberg, *Symplectic Techniques in Physics*, Cambridge University Press, 1984. [Publisher record](https://doi.org/10.1017/CBO9780511624112). Relevant: Chapter 1, linear symplectic geometry.
