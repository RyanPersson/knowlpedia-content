+++
id = "catalog/lie-algebras/sp-6-c"
title = "sp(6,C) — complex symplectic Lie algebra"
kind = "definition"
summary = "sp(6,C) — complex symplectic Lie algebra."
aliases = ["sp(6,C) — complex symplectic Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/symplectic-lie-algebra", "lie-groups/lie-algebra"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **complex symplectic [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{sp}(6,\mathbb C)\) consists of matrices preserving the standard alternating form infinitesimally:

\[
\mathfrak{sp}(6,\mathbb C)=\{X\in M_{6}(\mathbb C):X^T J+JX=0\},\qquad J=\begin{pmatrix}0&I_{3}\\-I_{3}&0\end{pmatrix}.
\]


The bracket is \([X,Y]=XY-YX\). Transpose is used without conjugation.

## Block description and size convention

Writing matrices in four equal blocks, the defining equation gives

\[
X=\begin{pmatrix}A&B\\C&-A^T\end{pmatrix},\qquad B=B^T,\quad C=C^T.
\]

Thus there are \(9+2\cdot6=21\) independent complex parameters. This is a complex [[lie-groups/lie-algebra|Lie algebra]]; its underlying real dimension doubles.

The number \(6\) is the full matrix size; the compact quaternionic algebra \(\mathfrak{sp}(3)\) is a different real form.
