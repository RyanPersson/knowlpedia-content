+++
id = "linear-algebra/alternating-multilinear-map"
title = "Alternating multilinear map"
kind = "definition"
summary = "A multilinear map that vanishes whenever two arguments agree."
aliases = ["alternating multilinear map"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/multilinear-map"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 1
+++

Let \(V,W\) be vector spaces over a field \(K\), and let \(k\ge1\). A [[linear-algebra/multilinear-map|multilinear map]] \(f:V^k\to W\) is **alternating** if
\[
f(v_1,\ldots,v_k)=0
\quad\text{whenever }v_i=v_j\text{ for some }i\ne j.
\]

## Signs and characteristic

Swapping two arguments negates the value. The converse holds in characteristic different from \(2\), but not in characteristic \(2\): there, the bilinear map \((x,y)\mapsto xy\) on \(K\) is skew-symmetric because \(-1=1\), yet its value at \((1,1)\) is nonzero.

For \(k=1\), the alternation condition is vacuous. Scalar-valued alternating multilinear maps are called alternating forms.

## Example

The map \(((x_1,x_2),(y_1,y_2))\mapsto x_1y_2-x_2y_1\) is an alternating bilinear form on \(K^2\).


## References

1. Bernhard Leeb, [Some multilinear algebra](https://www.math.lmu.de/~leeb/lehre/texte/ana3/ana3_multilinalg.pdf), 2020, §§1.1, 1.4 and 2.3.
