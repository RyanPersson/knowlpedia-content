+++
id = "algebra-homological/nine-lemma"
title = "Nine lemma (3×3 lemma)"
kind = "knowl"
summary = "In a commutative 3×3 diagram in an abelian category, exact columns and two exact rows force the remaining row to be exact."
aliases = ["nine-lemma", "Nine lemma (3×3 lemma)"]
domains = ["algebra-homological"]
prerequisites = ["algebra-category-theory/abelian-category", "algebra-category-theory/exact-sequence-categorical"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-homological/nine-lemma.md"
+++

Let \(\mathcal A\) be an [[algebra-category-theory/abelian-category|abelian category]]. Consider a commutative \(3\times 3\) diagram
\[
\begin{array}{ccccccccc}
0 &\to& A' &\xrightarrow{}& A &\xrightarrow{}& A'' &\to& 0\\
&& \downarrow && \downarrow && \downarrow && \\
0 &\to& B' &\xrightarrow{}& B &\xrightarrow{}& B'' &\to& 0\\
&& \downarrow && \downarrow && \downarrow && \\
0 &\to& C' &\xrightarrow{}& C &\xrightarrow{}& C'' &\to& 0
\end{array}
\]
If the three columns and the first two rows are [[algebra-category-theory/exact-sequence-categorical|exact]], then the third row
\[
0\to C' \to C \to C'' \to 0
\]
is exact. Dually, exact rows together with two exact columns force the remaining column to be exact.

## Remarks

The lemma can be proved by a diagram chase using the [[algebra-homological/snake-lemma|snake lemma]], or by a kernel–cokernel argument in the abelian category.
