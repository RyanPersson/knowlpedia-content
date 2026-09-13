+++
id = "topology/integer-matrix-torus-cover"
title = "Integer-matrix torus covering"
kind = "definition"
summary = "A nonsingular integer matrix induces a finite covering of the unit torus."
aliases = ["integer torus covering", "covering matrix"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/flat-torus", "topology/covering-space", "linear-algebra/integer-lattice-index", "linear-algebra/matrix-inverse"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A nonsingular integer matrix \(A\) induces the **torus covering**
\[
p_A:\mathbb T^n\longrightarrow\mathbb T^n,\qquad [x]\longmapsto[Ax].
\]
Integer entries make the map well-defined. It is a [[topology/covering-space|covering map]] with \(|\det A|\) sheets.

## Fibers and local inverses

The map is onto since \(A^{-1}y\) is a preimage of \(y\). Its kernel is \(A^{-1}\mathbb Z^n/\mathbb Z^n\), identified by multiplication by \(A\) with \(\mathbb Z^n/A\mathbb Z^n\). Every fiber is a translate of this finite kernel. Small neighborhoods of the finitely many preimages give disjoint inverse branches of the linear map, proving the covering property. If \(|\det A|=1\), the map is a torus automorphism. If \(|\det A|>1\), it is not injective; local lifts must retain their sheet labels.

## References

- [Hatcher, Algebraic Topology, §1.3 (covering spaces and deck transformations)](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf).
