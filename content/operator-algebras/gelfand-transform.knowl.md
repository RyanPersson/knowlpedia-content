+++
id = "operator-algebras/gelfand-transform"
title = "Gelfand transform"
kind = "definition"
summary = "The map representing each element of a commutative C-star algebra as a function on its character space."
aliases = ["Gelfand representation"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/commutative-cstar-algebra", "operator-algebras/character-space", "operator-algebras/star-homomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/commutative-cstar-algebra|commutative \(C^*\)-algebra]] with
[[operator-algebras/character-space|character space]] \(\Delta(A)\). The
**Gelfand transform** of \(a\in A\) is the function
\[
\widehat a:\Delta(A)\to\mathbb C,\qquad \widehat a(\chi)=\chi(a).
\]
The assignment \(\Gamma_A(a)=\widehat a\) is a
[[operator-algebras/star-homomorphism|\(*\)-homomorphism]]
\(A\to C_0(\Delta(A))\), also called the Gelfand
representation. For \(C^*\)-algebras, the commutative Gelfand--Naimark theorem
states that \(\Gamma_A\) is an isometric \(*\)-isomorphism. Thus the transform
recovers both the algebra and its norm from scalar-valued characters. Each
transformed element is continuous and vanishes at infinity.

## Algebraic and spectral properties

For \(a,b\in A\) and \(\lambda\in\mathbb C\),
\[
\widehat{ab}=\widehat a\,\widehat b,\qquad
\widehat{a^*}=\overline{\widehat a},\qquad
\widehat{\lambda a+b}=\lambda\widehat a+\widehat b.
\]
Moreover,
\(\|a\|=\|\widehat a\|_\infty\), and the range of \(\widehat a\), with zero
added when required in the nonunital case, determines \(\sigma_A(a)\).
Surjectivity onto \(C_0(\Delta(A))\) is the substantive \(C^*\)-algebra
theorem.

## Canonical model

For \(A=C_0(X)\), every character is evaluation at a unique \(x\in X\).
After identifying \(X\) with \(\Delta(A)\), the transform sends a function
\(f\) to the same function:
\(\widehat f(\chi_x)=f(x)\). This model explains why multiplication,
involution, and norm become pointwise multiplication, complex conjugation,
and the [[real-analysis/supremum-norm|supremum norm]].

## Scope

The Gelfand transform is defined more generally for commutative Banach
algebras, but it need not then be isometric or surjective. For a
noncommutative \(C^*\)-algebra, scalar characters see only commutative
quotients and can fail to separate points. The representation theorem in the
core therefore requires commutativity.

## References

1. Gerard J. Murphy, *\(C^*\)-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: the chapter proving the Gelfand representation theorem for commutative \(C^*\)-algebras.
2. Gert K. Pedersen, *\(C^*\)-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: the introductory chapter on spectra and commutative \(C^*\)-algebras.
