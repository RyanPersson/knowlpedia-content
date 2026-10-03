+++
id = "catalog/finite-groups/relationships/endomorphisms-of-finite-simple-groups"
title = "Endomorphisms of a finite simple group"
kind = "theorem"
summary = "Every endomorphism of a finite simple group is either the trivial homomorphism or an automorphism."
aliases = []
domains = ["catalog", "algebra-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/finite-group", "algebra-groups/simple-group", "algebra-groups/kernel-is-normal", "algebra-groups/automorphism-group"]
dependency_heuristic = "finite-groups-semantic-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[algebra-groups/finite-group|finite]] [[algebra-groups/simple-group|simple group]]. Every group endomorphism \(f:G\to G\) is either the trivial homomorphism \(0_G:g\mapsto e\), or an [[algebra-groups/automorphism-group|automorphism]]. Consequently,
\[
\operatorname{End}_{\mathbf{Grp}}(G)=\{0_G\}\sqcup\operatorname{Aut}_{\mathbf{Grp}}(G),
\qquad
|\operatorname{End}_{\mathbf{Grp}}(G)|=1+|\operatorname{Aut}_{\mathbf{Grp}}(G)|.
\]
This is a decomposition of a monoid into its zero element and its group of units.

## Proof

The [[algebra-groups/kernel-is-normal|kernel is normal]], so simplicity gives \(\ker f=G\) or \(\ker f=\{e\}\). The first case is the trivial map. In the second case \(f\) is injective, hence bijective because its domain and codomain are the same [[shared-foundations/finite-set|finite set]]. Its inverse preserves multiplication, so \(f\) is an automorphism. Nontriviality of \(G\) makes the two cases disjoint.

## The role of the category

The same formula holds in the [[algebra-category-theory/full-subcategory|full subcategories]] of finite groups and finite simple groups. It does not describe arbitrary functions on the underlying set, of which there are \(|G|^{|G|}\).

For two different finite simple groups, a nontrivial homomorphism is injective but need not be surjective. The endomorphism conclusion uses the fact that the source and target coincide.
