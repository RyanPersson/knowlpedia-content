+++
id = "linear-algebra/multilinear-map"
title = "Multilinear map"
kind = "definition"
summary = "A map of vector spaces that is linear in each argument separately."
aliases = ["multilinear map"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/vector-space", "linear-algebra/linear-map", "shared-foundations/cartesian-product"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 1
+++

Let \(V_1,\ldots,V_k,W\) be [[linear-algebra/vector-space|vector spaces]] over the same field \(K\), with \(k\ge1\). A map \(f:V_1\times\cdots\times V_k\to W\) is **multilinear** if, for every argument position \(i\), fixed values of the other arguments, \(u,v\in V_i\), and \(a,b\in K\),
\[
f(v_1,\ldots,au+bv,\ldots,v_k)
=a f(v_1,\ldots,u,\ldots,v_k)+b f(v_1,\ldots,v,\ldots,v_k).
\]

## Terminology and examples

Such a map is also called \(k\)-linear. For \(k=1\) this is a [[linear-algebra/linear-map|linear map]]; for \(k=2\) it is a bilinear map.

The product \((x,y,z)\mapsto xyz\) from \(K^3\) to \(K\) is trilinear. A multilinear map need not be linear as a map from the product vector space: \((x,y)\mapsto xy\) is bilinear but does not preserve addition of pairs.


## References

1. Bernhard Leeb, [Some multilinear algebra](https://www.math.lmu.de/~leeb/lehre/texte/ana3/ana3_multilinalg.pdf), 2020, §§1.1, 1.4 and 2.3.
