+++
id = "lie-groups/d4-root-lattice"
title = "D₄ root lattice"
kind = "definition"
summary = "The even-coordinate-sum sublattice of Z⁴, with twenty-four roots of squared length two."
aliases = ["D4 lattice", "D_4 root lattice"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/root-lattice", "linear-algebra/euclidean-lattice"]
dependency_heuristic = "transcript-connections-semantic-v1"
dependency_review_count = 1
+++
The **\(D_4\) root lattice**, with its standard Euclidean normalization, is
\[
D_4=\{x\in\mathbb Z^4:x_1+x_2+x_3+x_4\in2\mathbb Z\}.
\]
It is the [[lie-groups/root-lattice|integer span of the roots]] \(\pm e_i\pm e_j\) for \(1\le i<j\le4\), using the standard basis of \(\mathbb R^4\). These are its twenty-four shortest nonzero vectors, all of squared length \(2\).

## Hurwitz coordinates and scale

The Euclidean dual is
\[
D_4^*=\{y:\langle y,D_4\rangle\subseteq\mathbb Z\}
=\mathbb Z^4\cup\left(\mathbb Z+\tfrac12\right)^4.
\]
Under the coordinates \(a+bi+cj+dk\leftrightarrow(a,b,c,d)\), this is the additive lattice of Hurwitz quaternions with quadratic norm \(a^2+b^2+c^2+d^2\).

The map
\[
(x_1,x_2,x_3,x_4)\longmapsto
\tfrac12(x_1+x_2,x_1-x_2,x_3+x_4,x_3-x_4)
\]
sends \(D_4\) onto \(D_4^*\) and divides squared lengths by \(2\). Thus the Hurwitz lattice is similar to \(D_4\) with length scale \(1/\sqrt2\), not length scale \(1/2\). Its twenty-four shortest vectors are the [[algebra-groups/binary-tetrahedral-group|Hurwitz units]].

## Direct verification

Pairing with \(e_i-e_j\) shows that dual coordinates have the same fractional part; pairing with \(e_i+e_j\) shows that it is \(0\) or \(1/2\). In the displayed map, the even-sum condition makes all four output coordinates integral or all half-integral, and the inverse sends either case to an even-sum integer vector. This proves both the dual description and the scale statement.
