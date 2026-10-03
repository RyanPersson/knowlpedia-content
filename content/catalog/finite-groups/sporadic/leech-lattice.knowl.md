+++
id = "catalog/finite-groups/sporadic/leech-lattice"
title = "Leech lattice"
kind = "knowl"
summary = "The even unimodular Euclidean lattice in dimension 24 with no vectors of squared length two."
aliases = ["Leech lattice", "Lambda24"]
domains = ["catalog", "linear-algebra", "algebra-groups"]
section_mode = "progressive"
prerequisites = ["linear-algebra/euclidean-lattice", "linear-algebra/inner-product"]
dependency_heuristic = "finite-groups-semantic-author-review-v1"
dependency_review_count = 1
+++

The **Leech lattice** \(\Lambda\subset\mathbb R^{24}\) is, up to an orthogonal transformation, the unique [[linear-algebra/euclidean-lattice|full-rank Euclidean lattice]] satisfying
\[
\operatorname{covol}(\Lambda)=1,\qquad
\langle x,y\rangle\in\mathbb Z,\qquad
\langle x,x\rangle\in2\mathbb Z
\quad(x,y\in\Lambda),
\]
and containing no vector \(x\) with \(\langle x,x\rangle=2\). Here \(\langle-,-\rangle\) is the standard positive-definite [[linear-algebra/inner-product|inner product]], and covolume is the volume of a lattice basis parallelepiped. The integrality, evenness, and covolume-one conditions say that the lattice is **even unimodular**.

## Normalization and symmetry

Its shortest nonzero vectors have squared length \(4\). Thus a “norm-4 vector” in this setting has Euclidean length \(2\); norm denotes squared length.

Write \(O(\Lambda)\) for the group of real linear isometries preserving \(\Lambda\). Its quotient by \(\{I,-I\}\) is [[catalog/finite-groups/sporadic/co1|\(\mathrm{Co}_1\)]]. Stabilizers of vectors with squared lengths \(4\) and \(6\) give [[catalog/finite-groups/sporadic/co2|\(\mathrm{Co}_2\)]] and [[catalog/finite-groups/sporadic/co3|\(\mathrm{Co}_3\)]], respectively.

## References

1. Henry Cohn and Abhinav Kumar, [Optimality and uniqueness of the Leech lattice among lattices](https://arxiv.org/pdf/math/0403263), Appendix B, first paragraph (p. 36 in the arXiv PDF), for the uniqueness characterization; §2 for minimal length \(2\) at covolume one.
2. Robert A. Wilson, [Finite Simple Groups, Chapter 5 notes](https://webspace.maths.qmul.ac.uk/r.a.wilson/FSG/notes5.pdf), §§5.3.1–5.3.4, especially equations (5.16)–(5.17).
