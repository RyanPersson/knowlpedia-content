+++
id = "functional-analysis/measurable-field-hilbert-spaces"
title = "Measurable field of Hilbert spaces"
kind = "definition"
summary = "A family of Hilbert spaces equipped with a countably generated measurable structure on its sections."
aliases = ["measurable Hilbert bundle", "Borel field of Hilbert spaces", "measurable family of Hilbert spaces"]
domains = ["functional-analysis", "measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/measurable-space", "linear-algebra/hilbert-space", "convex-analysis/linear-subspace"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((X,\Sigma)\) be a [[measure-theory/measurable-space|measurable space]]. A **measurable field of Hilbert spaces** consists of [[linear-algebra/hilbert-space|Hilbert spaces]] \(H_x\) and a [[convex-analysis/linear-subspace|linear subspace]] \(\mathcal M\subseteq\prod_{x\in X}H_x\) of sections such that:

1. \(x\mapsto\lVert\xi(x)\rVert\) is measurable for every \(\xi\in\mathcal M\);
2. a section \(\eta\) lies in \(\mathcal M\) whenever \(x\mapsto\langle\eta(x),\xi(x)\rangle\) is measurable for every \(\xi\in\mathcal M\); and
3. some sequence \((\xi_n)\) in \(\mathcal M\) has \(\{\xi_n(x):n\geq1\}\) dense in every \(H_x\).

The elements of \(\mathcal M\) are the **measurable sections**.

## Fundamental sequences and coordinates

A sequence as in the third axiom is called a fundamental sequence. Measurable fiberwise Gram–Schmidt operations turn one into sections that form an [[linear-algebra/orthonormal-basis|orthonormal basis]] after zero vectors are omitted. Relative to such sections, measurability can be checked through scalar coordinate functions. The countability requirement forces every fiber to be separable and is what makes direct-integral constructions manageable.

## Direct integrals

Given a [[measure-theory/measure-space|measure space]] \((X,\Sigma,\mu)\), one takes measurable sections satisfying
\[
\int_X\lVert\xi(x)\rVert^2\,d\mu(x)<\infty
\]
and identifies sections equal [[measure-theory/almost-everywhere|almost everywhere]]. The resulting Hilbert space, denoted \(\int_X^\oplus H_x\,d\mu(x)\), has [[linear-algebra/inner-product|inner product]] obtained by integrating the fiber inner products. Measurable fields therefore supply the varying-fiber data behind continuous decompositions of operators and representations.

## Examples and conventions

A fixed separable Hilbert space \(H\) gives the constant field \(H_x=H\), with measurability tested against a countable orthonormal basis. More generally, measurable subsets can carry fibers of different finite or countably infinite dimensions. Unlike a topological [[fiber-bundles/vector-bundle|vector bundle]], a measurable field need not have a topology on the disjoint union of its fibers.

**Warning.** Some sources use “Borel field” only when the base is a standard Borel space, and some package the structure by choosing a fundamental sequence rather than the maximal space \(\mathcal M\). These presentations are equivalent in the usual countably generated setting but should not be conflated with continuous Hilbert bundles.

## References

1. M. Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [Springer DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter IV, §8, and the chapter “Tensor Products of Operator Algebras and Direct Integrals.”
