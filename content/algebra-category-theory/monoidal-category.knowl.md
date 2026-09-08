+++
id = "algebra-category-theory/monoidal-category"
title = "Monoidal category"
kind = "definition"
summary = "A category with an associative tensor product and a tensor unit, coherently up to specified isomorphisms."
aliases = ["tensor category in the weak sense"]
domains = ["algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "algebra-category-theory/natural-isomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **monoidal category** is a [[algebra-category-theory/category|category]] \(\mathcal C\) equipped with a bifunctor
\[
\otimes:\mathcal C\times\mathcal C\longrightarrow\mathcal C,
\]
an object \(\mathbb 1\), and [[algebra-category-theory/natural-isomorphism|natural isomorphisms]]
\[
\begin{aligned}\alpha_{X,Y,Z}&:(X\otimes Y)\otimes Z\overset{\sim}{\longrightarrow}X\otimes(Y\otimes Z),\\
\lambda_X&:\mathbb 1\otimes X\overset{\sim}{\longrightarrow}X,\\
\rho_X&:X\otimes\mathbb 1\overset{\sim}{\longrightarrow}X.\end{aligned}
\]
The associator \(\alpha\) and unitors \(\lambda,\rho\) must satisfy the following equations for all objects, with composition read from right to left:
\[
\alpha_{W,X,Y\otimes Z}\circ\alpha_{W\otimes X,Y,Z}
=(\operatorname{id}_W\otimes\alpha_{X,Y,Z})\circ
\alpha_{W,X\otimes Y,Z}\circ(\alpha_{W,X,Y}\otimes\operatorname{id}_Z),
\]
\[
(\operatorname{id}_X\otimes\lambda_Y)\circ\alpha_{X,\mathbb1,Y}
=\rho_X\otimes\operatorname{id}_Y.
\]
These are the pentagon and triangle coherence axioms, respectively.

## Why coherence matters

The tensor product need not be literally associative or unital. The coherence axioms ensure that every canonical composite built from associators and unitors between two parenthesizations is the same. Calculations can therefore suppress these isomorphisms without making arbitrary choices.

## Examples

- Sets with Cartesian product and a one-point set form a monoidal category.
- Modules over a commutative ring form a monoidal category under [[algebra-modules/tensor-product|tensor product]], with the base ring as unit.
- Endofunctors of a category form a generally non-symmetric monoidal category under composition.

## References

1. Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed., Springer, 1998. [DOI record](https://doi.org/10.1007/978-1-4757-4721-8). Relevant: Chapter VII.
