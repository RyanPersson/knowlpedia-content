+++
id = "algebra-category-theory/simple-object"
title = "Simple object"
kind = "definition"
summary = "A nonzero object of an abelian category with no nonzero proper subobjects."
aliases = []
domains = ["algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/abelian-category", "algebra-category-theory/monomorphism-category"]
+++

A **simple object** of an [[algebra-category-theory/abelian-category|abelian category]] \(\mathcal A\) is an object \(S\not\cong0\) such that every [[algebra-category-theory/monomorphism-category|monomorphism]] \(U\hookrightarrow S\) has either \(U\cong0\) or is an isomorphism. Equivalently, its only subobjects are \(0\) and \(S\), where subobjects are monomorphisms into \(S\) identified up to isomorphism over \(S\).

## Examples and a distinction

In vector spaces, the simple objects are the one-dimensional spaces. In a module category they are precisely [[algebra-modules/simple-module|simple modules]]. All one-dimensional \(k\)-vector spaces are isomorphic, so there is one isomorphism class of simples, although there are many objects.

A simple object cannot split as a direct sum of two nonzero objects. The converse fails: the abelian group \(\mathbb Z/4\mathbb Z\) has the proper nonzero subgroup \(2\mathbb Z/4\mathbb Z\), but cannot be written as a direct sum of two nonzero subgroups.

## Endomorphisms

A nonzero map between simple objects is an isomorphism: its kernel must vanish and its image must be the target. Thus \(\operatorname{End}(S)\) is a division ring. If the category is \(k\)-linear, Hom spaces are finite-dimensional, and \(k\) is algebraically closed, then \(\operatorname{End}(S)=k\operatorname{id}_S\). Indeed, every endomorphism has an eigenvalue in the sense that its minimal polynomial over \(k\) has a root; in a division algebra this forces that endomorphism to be scalar.

## References

P. Etingof, S. Gelaki, D. Nikshych, and V. Ostrik, *Tensor Categories* (2015), §1.5 and Proposition 1.8.4; [author-hosted text](https://math.mit.edu/~etingof/egnobookfinal.pdf).
