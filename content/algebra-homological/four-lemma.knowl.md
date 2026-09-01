+++
id = "algebra-homological/four-lemma"
title = "Four lemma"
kind = "knowl"
summary = "Diagram-chase criteria ensuring the middle map in a morphism of exact sequences is injective or surjective."
aliases = ["four-lemma", "Four lemma"]
domains = ["algebra-homological"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-homological/four-lemma.md"
+++

Let
\[
\begin{array}{ccccccccc}
A_1 &\to& A_2 &\to& A_3 &\to& A_4 &\to& A_5\\
\downarrow f_1 && \downarrow f_2 && \downarrow f_3 && \downarrow f_4 && \downarrow f_5\\
B_1 &\to& B_2 &\to& B_3 &\to& B_4 &\to& B_5
\end{array}
\]
be a commutative diagram of \(R\)-modules with exact rows.

The **four lemma** has two forms:

1. If \(f_1\) is surjective and \(f_2,f_4\) are injective, then \(f_3\) is injective.
2. If \(f_2,f_4\) are surjective and \(f_5\) is injective, then \(f_3\) is surjective.

## Remarks

For modules, the assertions follow by diagram chasing. Analogous categorical formulations replace injective and surjective maps by suitable [[algebra-category-theory/monomorphism-category|monomorphisms]] and [[algebra-category-theory/epimorphism-category|epimorphisms]]. The result is closely related to the [[algebra-homological/five-lemma|five lemma]].
