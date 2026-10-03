+++
id = "catalog/morphisms/linear-endomorphisms-of-sl2-complex"
title = "Linear endomorphisms of sl(2,C) after forgetting its bracket"
kind = "example"
summary = "The same complex three-dimensional Lie algebra has M3(C) or M6(R) as its linear endomorphism algebra."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["catalog/categories/vector-spaces", "lie-groups/special-linear-lie-algebra"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

Let \(\mathfrak g=\mathfrak{sl}_2(\mathbb C)\), the complex [[linear-algebra/vector-space|vector space]] of traceless \(2\times2\) matrices. As a complex vector space it has dimension \(3\), and as an [[linear-algebra/realification-of-a-complex-vector-space|underlying real vector space]] it has dimension \(6\). Consequently, after choosing bases,
\[
\begin{aligned}
\operatorname{End}_{\mathbb C\text{-}\mathbf{Vect}}(\mathfrak g)&\cong M_3(\mathbb C),&
\operatorname{Aut}_{\mathbb C\text{-}\mathbf{Vect}}(\mathfrak g)&\cong GL_3(\mathbb C),\\
\operatorname{End}_{\mathbb R\text{-}\mathbf{Vect}}(\mathfrak g)&\cong M_6(\mathbb R),&
\operatorname{Aut}_{\mathbb R\text{-}\mathbf{Vect}}(\mathfrak g)&\cong GL_6(\mathbb R).
\end{aligned}
\]
These are vector-space morphisms, without the requirement of preserving the [[fiber-bundles/lie-bracket|Lie bracket]].

## Bases and scalar restriction

A complex basis is
\[
E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
F=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
A real basis is \((E,F,H,iE,iF,iH)\). Complex-linear maps form the real-linear maps commuting with the complex structure \(X\mapsto iX\). Entrywise conjugation is real-linear and invertible but does not commute with this complex structure.

## Retaining the bracket

The [[catalog/categories/lie-algebras|Lie-algebra categories]] additionally impose \(T([X,Y])=[T(X),T(Y)]\). For example \(T=2\operatorname{id}\) is an invertible [[linear-algebra/linear-map|linear map]] but is not a Lie-algebra homomorphism: the two sides are \(2[X,Y]\) and \(4[X,Y]\). This distinguishes linear automorphisms from Lie-algebra automorphisms.

The group \(SL(2,\mathbb C)\) itself is a different carrier and is not a vector space; see [[catalog/morphisms/sl2-complex-real-versus-holomorphic-maps|its real and complex group maps]].
