+++
id = "linear-algebra/exterior-power"
title = "Exterior power of a vector space"
kind = "definition"
summary = "The vector space representing alternating multilinear maps of a fixed degree."
aliases = ["exterior power of a vector space"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/alternating-multilinear-map", "linear-algebra/linear-map"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 1
+++

For a vector space \(V\) over \(K\) and \(k\ge1\), its **\(k\)-th exterior power** is a vector space \(\Lambda^k V\) equipped with an [[linear-algebra/alternating-multilinear-map|alternating multilinear map]]
\[
\iota:V^k\to\Lambda^kV,\qquad (v_1,\ldots,v_k)\mapsto v_1\wedge\cdots\wedge v_k,
\]
satisfying the universal property: for every vector space \(W\) and alternating multilinear map \(f:V^k\to W\), there exists a unique [[linear-algebra/linear-map|linear map]] \(\widetilde f:\Lambda^kV\to W\) with \(f=\widetilde f\circ\iota\). Set \(\Lambda^0V=K\).

## Basis and low degrees

If \(e_1,\ldots,e_n\) is a basis of \(V\), the wedges \(e_{i_1}\wedge\cdots\wedge e_{i_k}\) with \(i_1<\cdots<i_k\) form a basis of \(\Lambda^kV\). Thus \(\dim\Lambda^kV=\binom nk\), and \(\Lambda^kV=0\) for \(k>n\). There is a canonical identification \(\Lambda^1V=V\).

## Relation to the exterior algebra

These spaces are the graded pieces of the [[algebra-modules/exterior-algebra|exterior algebra]] of \(V\). The universal property determines each exterior power up to the unique isomorphism preserving its distinguished alternating map.


## References

1. Bernhard Leeb, [Some multilinear algebra](https://www.math.lmu.de/~leeb/lehre/texte/ana3/ana3_multilinalg.pdf), 2020, §§1.1, 1.4 and 2.3.
