+++
id = "nonassociative-algebra/simple-euclidean-jordan-algebra"
title = "Simple Euclidean Jordan algebra"
kind = "definition"
summary = "A Euclidean Jordan algebra with no nonzero proper Jordan ideals."
aliases = ["simple Euclidean Jordan algebra", "simple formally real Jordan algebra"]
domains = ["nonassociative-algebra"]
section_mode = "progressive"
+++

A **simple Euclidean Jordan algebra** is a nonzero
[[nonassociative-algebra/euclidean-jordan-algebra|Euclidean Jordan algebra]]
\(J\) whose only [[nonassociative-algebra/ideal-in-a-jordan-algebra|Jordan ideals]] are \(0\) and \(J\). A Jordan ideal is a
[[convex-analysis/linear-subspace|linear subspace]] \(I\subseteq J\) satisfying \(J\circ I\subseteq I\).

## Classification

Up to isomorphism, the simple Euclidean Jordan algebras are:

1. the rank-one algebra \(\mathbb R\);
2. \(\mathfrak h_n(\mathbb R)\), \(n\geq3\);
3. \(\mathfrak h_n(\mathbb C)\), \(n\geq3\), regarded as a real algebra;
4. \(\mathfrak h_n(\mathbb H)\), \(n\geq3\);
5. the [[nonassociative-algebra/spin-factor-jordan-algebra|spin factors]]
   \(\mathbb R\oplus V\) with \(\dim V\geq2\);
6. the [[nonassociative-algebra/exceptional-jordan-algebra|exceptional
   Jordan algebra]] \(\mathfrak h_3(\mathbb O)\).

The restriction \(n\geq3\) prevents duplication: the degree-two matrix
algebras \(\mathfrak h_2(\mathbb R)\), \(\mathfrak h_2(\mathbb C)\), and
\(\mathfrak h_2(\mathbb H)\) are spin factors. So is
\(\mathfrak h_2(\mathbb O)\), although octonionic Hermitian matrices do not
produce a matrix family in arbitrary degree.

## Decomposition theorem

Every Euclidean Jordan algebra decomposes uniquely up to permutation as an
orthogonal direct sum of simple ideals. The one-dimensional factor is
\(\mathfrak h_1(\mathbb R)\) and is sometimes left implicit as the degenerate
rank-one case. Conventions for the lowest-dimensional spin factors should
therefore always be checked.

All factors except \(\mathfrak h_3(\mathbb O)\) are
[[nonassociative-algebra/special-and-exceptional-jordan-algebras|special]].
The Albert algebra is the unique exceptional factor in the Euclidean
classification.

## References

1. Pascual Jordan, John von Neumann, and Eugene Wigner, “On an Algebraic Generalization of the Quantum Mechanical Formalism,” *Annals of Mathematics* 35 (1934), 29–64. [JSTOR record](https://www.jstor.org/stable/1968117).
2. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994. [Publisher record](https://global.oup.com/academic/product/analysis-on-symmetric-cones-9780198534778).
