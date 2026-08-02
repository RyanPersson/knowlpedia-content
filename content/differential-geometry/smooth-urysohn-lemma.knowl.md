+++
id = "differential-geometry/smooth-urysohn-lemma"
title = "Smooth Urysohn lemma"
kind = "lemma"
summary = "Disjoint closed subsets of a smooth manifold can be separated by a smooth function valued between zero and one."
aliases = ["smooth separation lemma", "smooth cutoff lemma"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]] and let \(A,B\subseteq M\) be disjoint [[topology/closed-set|closed sets]]. There exists a [[fiber-bundles/smooth-map|smooth map]] \(f:M\to[0,1]\) such that \(f|_A=0\) and \(f|_B=1\). Equivalently, if \(A\subseteq U\) with \(A\) closed and \(U\) open, there is a smooth \(f:M\to[0,1]\) satisfying \(f=1\) on \(A\) and \(\operatorname{supp}f\subseteq U\). No compactness of \(A\) is required, and the support in the equivalent formulation need not be compact. The equalities hold on the entire prescribed closed sets, not merely at selected points.

## Construction

Choose a locally finite [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|smooth partition of unity]] adapted to the two-set cover \(M\setminus A\) and \(M\setminus B\). The sum of the partition functions assigned to \(M\setminus A\) has value \(0\) on \(A\) and \(1\) on \(B\). Local finiteness makes the sum smooth. For the cutoff formulation, first choose a [[topology/neighborhood|neighborhood]] \(V\) of \(A\) whose closure lies in \(U\), then separate \(A\) from \(M\setminus V\).

## Relationship to bump functions

When \(A\) is compact and \(U\) is a prescribed neighborhood, the cutoff can be chosen with compact support in \(U\), hence as a [[differential-geometry/bump-function|bump function]]. For noncompact \(A\), a function equal to \(1\) on all of \(A\) cannot have compact support; the smooth Urysohn lemma still provides a cutoff whose support is closed and contained in \(U\).

## Conventions and scope

**Warning.** The topological Urysohn lemma yields a continuous separator on normal spaces. Smooth separation additionally uses the partitions of unity available on the standard Hausdorff, second-countable smooth manifolds. On a smooth space without paracompactness, the smooth conclusion can fail.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Graduate Texts in Mathematics 218, Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: the chapter on smooth functions, bump functions, and partitions of unity.
2. Loring W. Tu, *An Introduction to Manifolds*, 2nd ed., Universitext, Springer, 2011. [DOI record](https://doi.org/10.1007/978-1-4419-7400-6). Relevant: Chapter 13, partitions of unity and smooth separation.
