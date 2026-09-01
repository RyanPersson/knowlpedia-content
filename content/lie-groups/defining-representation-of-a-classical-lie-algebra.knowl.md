+++
id = "lie-groups/defining-representation-of-a-classical-lie-algebra"
title = "Defining representation of a classical Lie algebra"
kind = "definition"
summary = "The natural representation obtained from the matrix realization of a classical Lie algebra."
aliases = ["natural representation of a classical Lie algebra", "standard representation of a classical Lie algebra", "vector representation"]
domains = ["lie-groups", "representation-theory"]
prerequisites = ["lie-groups/lie-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

The **defining representation** of a classical matrix [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\subseteq\mathfrak{gl}(V)\) is the natural action on \(V\):
\[
\rho:\mathfrak g\hookrightarrow\mathfrak{gl}(V),
\qquad
\rho(X)v=Xv.
\]
For the complex simple classical families, this gives
\[
\begin{array}{c|c|c}
\text{type}&\mathfrak g&V\\ \hline
A_{n-1}&\mathfrak{sl}_n(\mathbb C)&\mathbb C^n\\
B_n&\mathfrak{so}_{2n+1}(\mathbb C)&\mathbb C^{2n+1}\\
C_n&\mathfrak{sp}_{2n}(\mathbb C)&\mathbb C^{2n}\\
D_n&\mathfrak{so}_{2n}(\mathbb C)&\mathbb C^{2n}.
\end{array}
\]
The same phrase is used for \(\mathfrak{gl}_n\) and for real forms acting on their natural real or complex vector spaces.

## Preserved tensors

The matrix realization can be characterized by tensors preserved infinitesimally. The algebra \(\mathfrak{sl}(V)\) consists of endomorphisms preserving a nonzero volume form to first order. The algebra \(\mathfrak{so}(V,q)\) preserves a nondegenerate symmetric [[linear-algebra/bilinear-form|bilinear form]] \(q\), while \(\mathfrak{sp}(V,\omega)\) preserves a nondegenerate alternating form \(\omega\):
\[
q(Xv,w)+q(v,Xw)=0,
\qquad
\omega(Xv,w)+\omega(v,Xw)=0.
\]

## Highest weights and constructions

With the standard numbering of [[lie-groups/simple-root|simple roots]], the defining representation has [[lie-groups/highest-weight|highest weight]] \(\omega_1\) in each classical family. It is therefore a [[lie-groups/fundamental-representation|fundamental representation]]. Tensor, symmetric, and [[lie-groups/exterior-power-representation|exterior powers]] of the defining module produce many other representations.

For \(\mathfrak{sl}_n\), every fundamental representation is an exterior power \(\Lambda^k\mathbb C^n\). For orthogonal algebras, the defining module is also called the **vector representation** to distinguish it from spin representations, which live naturally on the [[lie-groups/spin-group|spin group]].

## Group versus Lie algebra

The defining representations of \(SL_n\), \(SO_n\), and \(Sp_{2n}\) differentiate to the displayed Lie-algebra representations. For the [[lie-groups/simply-connected-lie-group|simply connected]] group \(\operatorname{Spin}(n)\), however, the vector representation is the composite
\[
\operatorname{Spin}(n)\longrightarrow SO(n)\longrightarrow GL(\mathbb R^n)
\]
and has kernel \(\{\pm1\}\). Thus it is faithful as a representation of \(\mathfrak{so}_n\) but not as a representation of \(\operatorname{Spin}(n)\).

“Standard representation” can mean a different preferred module in other contexts, especially for [[algebra-representation-theory/induced-representation|induced representations]] of reductive groups. The adjective “defining” should be tied to an explicit matrix realization \(\mathfrak g\subseteq\mathfrak{gl}(V)\).

## References

1. William Fulton and Joe Harris, *Representation Theory: A First Course*, Springer, 1991, §§15–20. [Publisher record](https://doi.org/10.1007/978-1-4612-0979-9).
2. James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972, §§8 and 13. [Publisher record](https://doi.org/10.1007/978-1-4684-9444-2).
