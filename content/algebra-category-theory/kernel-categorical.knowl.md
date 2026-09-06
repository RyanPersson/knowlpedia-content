+++
id = "algebra-category-theory/kernel-categorical"
title = "Kernel (categorical)"
kind = "knowl"
summary = "In a pointed category, the kernel of f:A→B is the equalizer of f and the zero morphism A→B."
aliases = ["kernel-categorical", "Kernel (categorical)"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/kernel-categorical.md"
prerequisites = ["algebra-category-theory/category", "algebra-category-theory/morphism", "algebra-category-theory/composition-category", "algebra-category-theory/zero-object", "algebra-category-theory/additive-category"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Throughout, assume \(\mathcal C\) is a [[algebra-category-theory/category|category]] with a zero object (e.g. any [[algebra-category-theory/additive-category|additive category]]), so that for any objects \(A,B\) there is a distinguished **zero morphism** \(0_{A,B}:A\to B\).

Given a morphism \(f:A\to B\) in \(\mathcal C\), a **kernel** of \(f\) is a morphism
\[
k:K\to A
\]
such that:
1. \(f\circ k = 0_{K,B}\), and
2. (Universal property) for every morphism \(t:T\to A\) with \(f\circ t=0_{T,B}\), there exists a unique morphism \(u:T\to K\) with
   \[
   k\circ u = t.
   \]

It is the categorical version of the solution set of \(f(x)=0\), expressed by a universal property rather than by elements.

## Equivalent characterizations

Equivalently, \(k:K\to A\) is an [[algebra-category-theory/equalizer|equalizer]] of the parallel pair \(f,0_{A,B}:A\rightrightarrows B\).

## Remarks

A kernel, if it exists, is unique up to unique [[algebra-category-theory/isomorphism-category|isomorphism]]. In any category, kernels are [[algebra-category-theory/monomorphism-category|monomorphisms]] (because equalizers are monic).

## Examples
1. **\(\mathbf{Ab}\).** For a homomorphism \(f:A\to B\) of abelian groups, \(\ker(f)\subseteq A\) with inclusion \(\ker(f)\hookrightarrow A\) is the categorical kernel.

2. **\(R\)\(-\)\(\mathbf{Mod}\).** For an \(R\)-linear map \(f:M\to N\), the usual submodule \(\{m\in M : f(m)=0\}\) with inclusion is the kernel.

3. **\(\mathbf{Grp}\).** For a group homomorphism \(f:G\to H\), the usual kernel \(\{g\in G : f(g)=e\}\) with inclusion is the categorical kernel (here the zero morphism \(G\to H\) is the constant map to the identity element).
