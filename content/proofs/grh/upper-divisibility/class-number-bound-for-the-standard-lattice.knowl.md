+++
id = "proofs/grh/upper-divisibility/class-number-bound-for-the-standard-lattice"
title = "Explicit bound for the number of classes in the genus of the standard lattice"
kind = "theorem"
summary = "The number of classes of the definite unitary group at the standard level is at most (1 + 2c^3)^(4 f r^2) with c = 6N(fr)^2."
aliases = ["class count bound"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Space.card_stdClasses_le", "New.Space.stdClasses_eq_of_gram_eq", "New.Space.isIntegral_conjTranspose_mul_apply", "New.Space.norm_gram_apply_le_cube", "New.Space.norm_map_mul_apply_le"]
lean_files = ["src/New/UpperBound/Size/ClassCount.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] with \(f\) infinite places and a fixed CM type, let \(N\ne0\) be a natural number lying in the [[?c:Different ideal|different]] of \(E/\mathbb{Q}\), let \(n\) be a finite index set with \(r\) elements, let \(G_f\) be the finite adelic points of the unitary group of the hermitian form \(\sum_{i\in n}x_i\bar x_i\) over \(E\), \(\Gamma\) its group of rational points and \(K_0=G_f\cap\mathrm{GL}_n(\widehat{\mathcal O}_E)\) the [[?lean:New.stdLevel|standard level]] (the stabiliser of the standard lattice \(\widehat{\mathcal O}_E^{\,n}\)). Then the set of [[?c:Class of a hermitian lattice in a genus|classes]] \(\Gamma\backslash G_f/K_0\) is finite with
\[
\bigl\lvert\Gamma\backslash G_f/K_0\bigr\rvert\;\le\;\bigl(1+2c^{3}\bigr)^{4fr^{2}},\qquad c=6N(fr)^{2}.
\]

## Proof

For each class fix a representative \(g\in G_f\).

*Short basis.* By [[?lean:New.Space.exists_short_basis_stdSpace|`exists_short_basis_stdSpace`]] (quoted; this uses that \(N\) lies in the different) there is \(Y_g\in\mathrm{GL}_n(E)\) with \(A_g:=g^{-1}Y_g\) integral (entries in \(\widehat{\mathcal O}_E\)) and with every entry of every complex conjugate of \(Y_g\) of absolute value at most \(c\).

*Rational approximation.* By [[?lean:New.exists_principal_near_of_mem_differentIdeal|`exists_principal_near_of_mem_differentIdeal`]] (quoted) every finite adele \(y\) has an \(\alpha\in E\) with \(y-\alpha\in\widehat{\mathcal O}_E\) and \(\lvert\alpha\rvert_w\le(2f)^2N\) at every infinite place \(w\). Applying this to the entries of \(A_g^{-1}\) gives a matrix \(X_g\) over \(E\) with \(A_g^{-1}-X_g\) integral and entries of size at most \((2f)^2N\).

*The invariant.* Put \(G_g=Y_g^{*}Y_g\) (the Gram matrix of the basis) and attach to the class the pair of matrices \((G_g,\,G_gX_g)\), that is \(2r^2\) elements of \(E\).

(a) *They are algebraic integers.* If \(gY\) and \(gZ\) are integral for a unitary \(g\) then \(Y^{*}Z=(gY)^{*}(gZ)\) is integral at every finite place, hence has entries in \(\mathcal O_E\). Apply this to \(g^{-1}\) with \(Y=Z=Y_g\), and with \(Z=Y_gX_g\): indeed \(g^{-1}Y_gX_g=A_gX_g=1-A_g(A_g^{-1}-X_g)\) is integral.

(b) *They are small.* At every infinite place the entries of \(G_g\) are at most \(r\,c^2\le c^3\), and those of \(G_gX_g\) at most \(r\cdot rc^2\cdot(2f)^2N=4N(fr)^2c^2\le c^3\).

(c) *They determine the class.* Suppose \((G_{g'},G_{g'}X_{g'})=(G_g,G_gX_g)\). Then \(X_{g'}=X_g\) since \(G_g\) is invertible. The matrix
\[
A_{g'}A_g^{-1}=A_{g'}\bigl(A_g^{-1}-X_g\bigr)+A_{g'}X_{g'}
\]
is integral, as both terms are. Since \(Y_{g'}^{*}Y_{g'}=Y_g^{*}Y_g\), the matrix \(\gamma=Y_gY_{g'}^{-1}\) is a rational isometry of the standard form, so \(\gamma\in\Gamma\), and \(k:=(\gamma g')^{-1}g=A_{g'}A_g^{-1}\) is an integral element of \(G_f\), hence \(k\in K_0\) (its inverse is \(k^{*}\)). Thus \(g=\gamma g'k\) and the classes agree.

*Counting.* The map from classes to vectors of \(2r^2\) algebraic integers of \(E\), all of whose conjugates have absolute value at most \(c^3\), is injective. The number of such vectors is at most \((1+2c^{3})^{2r^2\cdot 2f}\) by [[?lean:New.Filling.encard_le_of_isIntegral_norm_le|`Filling.encard_le_of_isIntegral_norm_le`]] (quoted: an integer of a field of degree \(2f\) whose conjugates are bounded by \(R\) is one of at most \((1+2R)^{2f}\) elements). \(\blacksquare\)

*Status.* The existence of short bases, the rational approximation and the count of bounded algebraic integers are quoted from other files.

## References

1. Lean: `New.Space.card_stdClasses_le`, `New.Space.stdClasses_eq_of_gram_eq` in `src/New/UpperBound/Size/ClassCount.lean`.
