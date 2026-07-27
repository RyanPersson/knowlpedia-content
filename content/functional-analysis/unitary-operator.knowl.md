+++
id = "functional-analysis/unitary-operator"
title = "Unitary operator"
kind = "definition"
summary = "A surjective linear isometry between complex Hilbert spaces."
aliases = ["unitary transformation", "unitary isomorphism"]
domains = ["functional-analysis", "linear-algebra"]
section_mode = "progressive"
+++

Let \(H\) and \(K\) be complex [[linear-algebra/hilbert-space|Hilbert
spaces]]. A **unitary operator** is a surjective [[linear-algebra/linear-map|linear map]] \(U:H\to K\)
that preserves [[linear-algebra/inner-product|inner products]]:
\[
\langle Ux,Uy\rangle_K=\langle x,y\rangle_H
\qquad(x,y\in H).
\]
Equivalently, \(U\) is bounded and its
[[functional-analysis/adjoint-bounded-operator|Hilbert-space adjoint]]
satisfies
\[
U^*U=I_H,\qquad UU^*=I_K.
\]
In that case \(U^{-1}=U^*\) and \(\lVert Ux\rVert=\lVert x\rVert\). When
\(H=K\), the unitary operators form a group under composition, called the
unitary group of \(H\). Surjectivity is essential: an isometric embedding
need not be unitary.

## Equivalent characterizations

For a bounded linear map \(U:H\to K\), the following are equivalent: \(U\) is
unitary; \(U\) is a surjective isometry; \(U^*U=I_H\) and \(UU^*=I_K\); and
\(U\) sends some [[linear-algebra/orthonormal-basis|orthonormal basis]] of
\(H\) onto an orthonormal basis of \(K\). The single identity \(U^*U=I_H\)
asserts only that \(U\) is an isometry, while \(UU^*=I_K\) supplies surjectivity
[Conway, Chapter II](https://doi.org/10.1007/978-1-4757-3828-5).

## Spectral and geometric properties

A unitary operator on \(H\) is normal, has [[linear-algebra/operator-norm|operator norm]] \(1\) when
\(H\neq0\), and has spectrum contained in the unit circle. Unitary
conjugation \(T\mapsto U T U^*\) preserves adjoints, products, spectra,
operator norms, and singular values. Thus unitary equivalence expresses a
change of Hilbert-space coordinates without changing intrinsic operator
data.

## Examples and non-examples

Multiplication by a [[measure-theory/measurable-function|measurable function]] \(u\) with \(|u|=1\) almost
everywhere is unitary on \(L^2\). The bilateral shift on
\(\ell^2(\mathbb Z)\) is unitary. The unilateral shift on
\(\ell^2(\mathbb N)\) preserves norms but is not surjective, so it is an
isometry rather than a unitary operator.

## Conventions and scope

For real [[linear-algebra/hilbert-space|Hilbert spaces]], the analogous maps are normally called orthogonal
operators. In physics, “unitary” may also describe an antiunitary symmetry
informally, but an antiunitary map is conjugate-linear and is not unitary
under the definition above.

## References

1. John B. Conway, *A Course in Functional Analysis*, 2nd ed., Springer, 1990. [DOI record](https://doi.org/10.1007/978-1-4757-3828-5). Relevant: Chapter II on Hilbert-space operators, adjoints, isometries, and unitaries.
