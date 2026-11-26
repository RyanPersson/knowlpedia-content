+++
id = "proofs/grh/spanning-core/hilbert-schmidt-norm-of-a-linear-map"
title = "Hilbert–Schmidt norm of a linear map (finite dimension)"
kind = "definition"
summary = "The norm of a linear map between finite-dimensional inner product spaces given by the sum of squared lengths of the images of an orthonormal basis."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.hilbertSchmidtVector", "New.hilbertSchmidtNorm", "New.inner_hilbertSchmidtVector", "New.hilbertSchmidtNorm_sq_eq_trace", "New.hilbertSchmidtNorm_sq_eq_sum", "New.hilbertSchmidtNorm_sq_eq_sum_entries", "New.hilbertSchmidtNorm_adjoint", "New.hilbertSchmidtNorm_le_of_norm_le", "New.orthoProj", "New.hilbertSchmidtNorm_orthoProj_sq", "New.hilbertSchmidtNorm_comp_orthoProj_le", "New.hilbertSchmidtNorm_orthoProj_comp_sq"]
lean_files = ["src/New/Spanning/SecondMoment/FewTranslates.lean"]
+++

Let \(S\) and \(T\) be finite-dimensional complex [[linear-algebra/inner-product-space|inner product spaces]] and \(A\colon S\to T\) a [[linear-algebra/linear-map|linear map]]. Fix an [[linear-algebra/orthonormal-basis|orthonormal basis]] \(b_1,\dots,b_d\) of \(S\). The **Hilbert–Schmidt norm** of \(A\) is
\[
\lVert A\rVert_{\mathrm{HS}}=\Bigl(\sum_{i=1}^d\lVert A b_i\rVert^2\Bigr)^{1/2},
\]
and the **Hilbert–Schmidt inner product** of two linear maps \(A,B\colon S\to T\) is \(\langle A,B\rangle_{\mathrm{HS}}=\sum_{i=1}^d\langle Ab_i,Bb_i\rangle\). Both are independent of the basis (Property 1). This is the norm of a [[functional-analysis/hilbert-schmidt-operator|Hilbert–Schmidt operator]] in finite dimension. For a subspace \(U\) we write \(\mathrm{pr}_U\) for the [[linear-algebra/orthogonal-projection|orthogonal projection]] onto \(U\).

## Properties

Write \(A^*\) for the [[?c:adjoint of a linear map|adjoint]] and \(\operatorname{tr}\) for the [[linear-algebra/trace|trace]].

1. \(\langle A,B\rangle_{\mathrm{HS}}=\operatorname{tr}(A^*B)\); in particular \(\lVert A\rVert_{\mathrm{HS}}^2=\operatorname{tr}(A^*A)=\sum_i\lVert Ac_i\rVert^2\) for every orthonormal basis \((c_i)\) of \(S\), and \(\lVert A\rVert^2_{\mathrm{HS}}=\sum_{i,j}\lvert\langle Ac_i,d_j\rangle\rvert^2\) for orthonormal bases \((c_i)\) of \(S\), \((d_j)\) of \(T\).
2. \(\lVert A^*\rVert_{\mathrm{HS}}=\lVert A\rVert_{\mathrm{HS}}\).
3. If \(A\colon S\to T\), \(B\colon S\to T'\) satisfy \(\lVert Ax\rVert\le\lVert Bx\rVert\) for all \(x\), then \(\lVert A\rVert_{\mathrm{HS}}\le\lVert B\rVert_{\mathrm{HS}}\).
4. \(\lVert\mathrm{pr}_U\rVert_{\mathrm{HS}}^2=\dim U\) for a subspace \(U\subseteq S\).
5. \(\lVert A\,\mathrm{pr}_U\rVert_{\mathrm{HS}}\le\lVert A\rVert_{\mathrm{HS}}\) for a subspace \(U\subseteq S\).
6. \(\lVert\mathrm{pr}_WA\rVert_{\mathrm{HS}}^2=\operatorname{Re}\langle\mathrm{pr}_W,AA^*\rangle_{\mathrm{HS}}\) for a subspace \(W\subseteq T\) (the inner product of endomorphisms of \(T\)).

## Proof

(1) \(\operatorname{tr}(A^*B)=\sum_i\langle b_i,A^*Bb_i\rangle=\sum_i\langle Ab_i,Bb_i\rangle\), and the trace does not depend on the basis. The entry formula is Parseval's identity \(\lVert Ac_i\rVert^2=\sum_j\lvert\langle Ac_i,d_j\rangle\rvert^2\).
(2) \(\operatorname{tr}(AA^*)=\operatorname{tr}(A^*A)\).
(3) Compare the sums over a basis term by term.
(4) \(\mathrm{pr}_U^*\mathrm{pr}_U=\mathrm{pr}_U\) has trace \(\dim U\).
(5) By (2), \(\lVert A\,\mathrm{pr}_U\rVert_{\mathrm{HS}}=\lVert\mathrm{pr}_UA^*\rVert_{\mathrm{HS}}\), and \(\lVert\mathrm{pr}_UA^*x\rVert\le\lVert A^*x\rVert\); apply (3) and (2).
(6) \((\mathrm{pr}_WA)^*(\mathrm{pr}_WA)=A^*\mathrm{pr}_WA\), whose trace equals \(\operatorname{tr}(\mathrm{pr}_WAA^*)=\langle\mathrm{pr}_W,AA^*\rangle_{\mathrm{HS}}\).

## Remarks

In the Lean source the vector \((Ab_i)_i\in T^d\) is `hilbertSchmidtVector A`, for a fixed standard orthonormal basis, and the norm is its norm in the \(\ell^2\)-direct sum.

## References

1. Lean: `New.hilbertSchmidtNorm` and the lemmas after it in `src/New/Spanning/SecondMoment/FewTranslates.lean`.

## References

1. Lean: `New.hilbertSchmidtVector`, `New.hilbertSchmidtNorm`, `New.inner_hilbertSchmidtVector`, `New.hilbertSchmidtNorm_sq_eq_trace`, `New.hilbertSchmidtNorm_sq_eq_sum`, `New.hilbertSchmidtNorm_sq_eq_sum_entries`, `New.hilbertSchmidtNorm_adjoint`, `New.hilbertSchmidtNorm_le_of_norm_le`, `New.orthoProj`, `New.hilbertSchmidtNorm_orthoProj_sq`, `New.hilbertSchmidtNorm_comp_orthoProj_le`, `New.hilbertSchmidtNorm_orthoProj_comp_sq` in `src/New/UpperBound/ElementaryDivisors/.lean`.
