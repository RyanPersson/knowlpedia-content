+++
id = "algebra-category-theory/group-object"
title = "Group object"
kind = "definition"
summary = "An object carrying multiplication, identity, and inverse morphisms that satisfy the group axioms internally."
aliases = ["internal group"]
domains = ["algebra-category-theory"]
prerequisites = ["algebra-category-theory/category", "algebra-category-theory/categorical-product", "algebra-category-theory/terminal-object"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(\mathcal C\) be a [[algebra-category-theory/category|category]] with finite [[algebra-category-theory/categorical-product|products]] and [[algebra-category-theory/terminal-object|terminal object]] \(1\). A **group object** in \(\mathcal C\) is an object \(G\) with morphisms
\[
\begin{aligned}
m&:G\times G\to G,\\
e&:1\to G,\\
i&:G\to G.
\end{aligned}
\]
For every object \(T\), write \(!_T:T\to1\) for the unique morphism and define
operations on generalized elements \(f,g:T\to G\) using their product pairing
\(\langle f,g\rangle:T\to G\times G\):
\[
\begin{aligned}
f*g&=m\circ\langle f,g\rangle,\\
e_T&=e\circ !_T,\\
f^{-1}&=i\circ f.
\end{aligned}
\]
The group-object axioms require, for all \(f,g,h:T\to G\),
\[
\begin{aligned}
(f*g)*h&=f*(g*h),\\
e_T*f&=f=f*e_T,\\
f^{-1}*f&=e_T=f*f^{-1}.
\end{aligned}
\]
These are the associativity, identity, and inverse laws, tested on generalized
elements from every object \(T\).

## Generalized elements

For every object \(T\), composition with \(m,e,i\) makes
\[
\operatorname{Hom}_{\mathcal C}(T,G)
\]
a group under the operations above.
The construction is contravariantly natural in \(T\): precomposition with a
morphism \(S\to T\) is a group homomorphism. This is a reliable way to read
the internal axioms, although ordinary elements alone may not detect all
morphisms in every category.

## Examples

- Group objects in sets are ordinary [[algebra-groups/group|groups]].
- Group objects in topological spaces are [[topology/topological-group|topological groups]].
- Group objects in smooth manifolds are [[fiber-bundles/lie-group|Lie groups]].
- Group objects in schemes are [[algebraic-geometry-foundations/group-scheme|group schemes]].

## References

1. Francis Borceux, *Handbook of Categorical Algebra 2: Categories and Structures*, Cambridge University Press, 1994. [DOI record](https://doi.org/10.1017/CBO9780511525865). Relevant: internal algebraic structures.
