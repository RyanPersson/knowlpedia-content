+++
id = "catalog/lie-algebras/sp-2n-c"
title = "sp(2n,C) — complex symplectic Lie algebra"
kind = "definition"
summary = "sp(2n,C) — complex symplectic Lie algebra."
aliases = ["sp(2n,C) — complex symplectic Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/symplectic-lie-algebra", "lie-groups/lie-algebra"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

For an integer \(n\geq1\), the **complex symplectic [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{sp}(2n,\mathbb C)\) consists of matrices preserving the standard alternating form infinitesimally:

\[
\mathfrak{sp}(2n,\mathbb C)=\{X\in M_{2n}(\mathbb C):X^T J+JX=0\},\qquad J=\begin{pmatrix}0&I_{n}\\-I_{n}&0\end{pmatrix}.
\]


The bracket is \([X,Y]=XY-YX\). Transpose is used without conjugation.

## Block description and size convention

Writing matrices in four equal blocks, the defining equation gives

\[
X=\begin{pmatrix}A&B\\C&-A^T\end{pmatrix},\qquad B=B^T,\quad C=C^T.
\]

Thus there are \(n^2+2\frac{n(n+1)}2=n(2n+1)\) independent complex parameters. This is a complex [[lie-groups/lie-algebra|Lie algebra]]; its underlying real dimension doubles.

The number \(2n\) is the full matrix size; the compact quaternionic algebra \(\mathfrak{sp}(n)\) is a different real form.
