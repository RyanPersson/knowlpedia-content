+++
id = "catalog/morphisms/restriction-of-scalars-endomorphisms"
title = "Comparing K-linear and F-linear endomorphisms of a K-algebra"
kind = "theorem"
summary = "Restriction of scalars and forgetting multiplication give inclusions of endomorphism collections, with distinct algebraic constraints."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-commutative/restriction-of-scalars", "catalog/categories/vector-spaces", "catalog/categories/unital-associative-algebras"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

Let \(K/F\) be a specified [[algebra-fields-galois/field-extension|field extension]] and \(A\) a unital associative \(K\)-algebra. Use \(k\text{-}\mathbf{Alg}_1\) for the [[catalog/categories/unital-associative-algebras|category of unital algebras and unit-preserving maps]] and \(k\text{-}\mathbf{Vect}\) for the [[catalog/categories/vector-spaces|category of vector spaces and linear maps]]. After [[algebra-commutative/restriction-of-scalars|restricting scalars]] along \(F\hookrightarrow K\), the same underlying functions give inclusions
\[
\begin{array}{ccc}
\operatorname{End}_{K\text{-}\mathbf{Alg}_1}(A)&\subseteq&\operatorname{End}_{F\text{-}\mathbf{Alg}_1}(A)\\
\cap&&\cap\\
\operatorname{End}_{K\text{-}\mathbf{Vect}}(A)&\subseteq&\operatorname{End}_{F\text{-}\mathbf{Vect}}(A).
\end{array}
\]
The vertical inclusions require multiplication and unit preservation. The horizontal inclusions forget part of the scalar-linearity requirement. The analogous inclusions hold for automorphism groups.

## Dimensions in the finite case

If \([K:F]=d<\infty\) and \(\dim_K A=m<\infty\), then \(\dim_F A=dm\), and choices of bases give
\[
\operatorname{End}_K(A)\cong M_m(K),\qquad
\operatorname{End}_F(A)\cong M_{dm}(F)
\]
for the vector-space endomorphism algebras. Their automorphism groups are \(GL_m(K)\) and \(GL_{dm}(F)\). These formulas do not classify the algebra endomorphisms.

## Recovering the extra constraints

An \(F\)-linear map is \(K\)-linear exactly when it commutes with every scalar multiplication \(L_a:x\mapsto ax\), \(a\in K\). To be a unital algebra map it must also satisfy
\[
f(xy)=f(x)f(y),\qquad f(1)=1.
\]
These are different requirements. They should not be conflated with semilinearity, which allows a [[algebra-fields-galois/field-automorphism|field automorphism]] to twist the scalar action.

## Example

Take \(K=\mathbb C\), \(F=\mathbb R\), \(A=\mathbb C\). Conjugation is an \(F\)-algebra automorphism but is not \(K\)-linear. The real-linear map \(z\mapsto2z\) is invertible but preserves neither multiplication nor the unit. The [[catalog/morphisms/complex-numbers-linear-versus-algebra-maps|full calculation for this example]] makes all four collections explicit.
