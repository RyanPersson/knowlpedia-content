+++
id = "nonassociative-algebra/hermitian-matrix-jordan-algebra"
title = "Hermitian matrix Jordan algebra"
kind = "definition"
summary = "Self-adjoint matrices over a real normed division algebra, with the symmetrized matrix product in the degrees where the Jordan identity holds."
aliases = ["Hermitian matrix Jordan algebra", "h_n(K)", "self-adjoint matrix Jordan algebra"]
domains = ["nonassociative-algebra"]
prerequisites = ["linear-algebra/vector-space", "nonassociative-algebra/euclidean-jordan-algebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

For \(\mathbb K=\mathbb R,\mathbb C\), or \(\mathbb H\), the **Hermitian
matrix Jordan algebra** \(\mathfrak h_n(\mathbb K)\) is the real [[linear-algebra/vector-space|vector space]]
of matrices \(X\in M_n(\mathbb K)\) satisfying \(X^*=X\), with product
\[
X\circ Y=\frac12(XY+YX).
\]
It is a [[nonassociative-algebra/euclidean-jordan-algebra|Euclidean Jordan
algebra]] for every \(n\geq1\).

## Exactly when the construction is Jordan

For \(\mathbb K=\mathbb R,\mathbb C,\mathbb H\), associativity of matrix
multiplication proves the Jordan identity in every size. Quaternionic matrices
are associative because the quaternion algebra is associative, even though it
is noncommutative.

For \(\mathbb K=\mathbb O\), the same displayed formula gives a Jordan algebra
only for \(n=1,2,3\):

- \(\mathfrak h_1(\mathbb O)\cong\mathbb R\);
- \(\mathfrak h_2(\mathbb O)\) is a [[nonassociative-algebra/spin-factor-jordan-algebra|spin factor]];
- \(\mathfrak h_3(\mathbb O)\) is the exceptional [[nonassociative-algebra/exceptional-jordan-algebra|Albert algebra]].

For \(n\geq4\), octonionic matrix multiplication does not satisfy the Jordan
identity on all Hermitian matrices, so \(\mathfrak h_n(\mathbb O)\) is not a
Jordan algebra under this formula. The notation must not be presented as a
uniform Jordan construction for arbitrary normed division algebras and sizes.

## Dimensions and Euclidean form

If \(d=\dim_{\mathbb R}\mathbb K\), then
\[
\dim_{\mathbb R}\mathfrak h_n(\mathbb K)
=n+\frac{d\,n(n-1)}{2}.
\]
The diagonal entries are real, while each off-diagonal pair contributes one
copy of \(\mathbb K\). The standard Euclidean form is
\(\langle X,Y\rangle=\operatorname{Re}\operatorname{Tr}(XY)\), equivalently
the Jordan trace of \(X\circ Y\).

The algebras \(\mathfrak h_2(\mathbb C)\) and
\(\mathfrak h_3(\mathbb C)\) are respectively the observables of a complex
qubit and qutrit. Positive elements of trace one are their density matrices.

## References

1. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994. [Publisher record](https://global.oup.com/academic/product/analysis-on-symmetric-cones-9780198534778).
2. Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer, 2000. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-12622-6).
