+++
id = "algebra-modules/direct-sum-universal-property"
title = "Direct sum universal property"
kind = "knowl"
summary = "The direct sum is characterized by a universal mapping property from the summands."
aliases = ["direct-sum-universal-property", "Direct sum universal property"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/direct-sum-universal-property.md"
prerequisites = ["algebra-modules/direct-sum-modules", "algebra-modules/module-homomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(R\) be a [[algebra-rings/ring|ring]], let \(\{M_i\}_{i\in I}\) be a family of \(R\)-[[algebra-modules/module|modules]], and let \(\iota_i:M_i\to \bigoplus_{i\in I}M_i\) be the canonical maps. The **direct sum universal property** states that for every \(R\)-[[algebra-modules/module|module]] \(N\) and family of [[algebra-modules/module-homomorphism|homomorphisms]] \(f_i:M_i\to N\), there is a unique homomorphism
\[
f:\bigoplus_{i\in I}M_i\longrightarrow N
\]
such that \(f\circ\iota_i=f_i\) for every \(i\in I\).

This is the defining [[algebra-category-theory/coproduct|coproduct]] property of the [[algebra-modules/direct-sum-modules|direct sum]] in the [[algebra-category-theory/category|category]] of \(R\)-modules, stated in terms of [[algebra-modules/module-homomorphism|module homomorphisms]].
