+++
id = "topology/separated-centers-under-torus-covers"
title = "Separated centers under finitely many torus covers"
kind = "theorem"
summary = "Finitely many centers can be chosen to avoid a fixed finite collection of iterated covering coincidences."
aliases = []
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/integer-matrix-torus-cover", "topology/flat-torus", "topology/nowhere-dense-set", "real-analysis/density-of-q", "linear-algebra/operator-norm", "shared-foundations/finite-set", "topology/intersection-of-dense-open-is-dense"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(J\) be a nonsingular integer matrix and \(D\ge0\) an integer. Assume \(J^j-I\) is nonsingular for \(1\le j\le D\). For every finite number \(N\) of labels, there are rational torus points \(c_1,\ldots,c_N\) and \(r>0\) such that
\[
J^j\overline B(c_\nu,r)\cap\overline B(c_\mu,r)=\varnothing
\]
for all \(0\le j\le D\), except \(j=0,\mu=\nu\). Images and balls are taken on the [[topology/flat-torus|unit flat torus]].

## Proof

Choose the centers to avoid \(J^jc_\nu=c_\mu\). For distinct labels this equation is a closed set with empty interior in the product of tori. For the same label and \(j>0\), the forbidden points form the finite kernel of the covering induced by \(J^j-I\). The complement of the finitely many forbidden sets is open and dense; rational tuples are dense, so a rational tuple lies in the complement.

The finitely many nonzero distances \(d(J^jc_\nu,c_\mu)\) have positive minimum \(\eta\). Choose \(r\) with \((1+\max_{0\le j\le D}\|J^j\|)r<\eta\). The triangle inequality gives the result. It follows that corresponding preimages at levels whose difference is at most \(D\) are disjoint, for every nonexcluded label pair.
