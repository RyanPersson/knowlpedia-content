+++
id = "linear-algebra/semilinear-map"
title = "Semilinear map"
kind = "definition"
summary = "An additive map between vector spaces that twists scalar multiplication by a field homomorphism."
aliases = ["semilinear transformation", "sigma-semilinear map", "semilinear isomorphism"]
domains = ["linear-algebra", "algebra-fields-galois"]
prerequisites = ["linear-algebra/vector-space", "algebra-fields-galois/field-automorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(V\) be a [[linear-algebra/vector-space|vector space]] over a field \(k\), let \(W\) be a vector space over a field \(\ell\), and let \(\sigma:k\to\ell\) be a field homomorphism. A map \(T:V\to W\) is **\(\sigma\)-semilinear** if
\[
T(v+w)=T(v)+T(w),\qquad T(av)=\sigma(a)T(v)
\]
for all \(v,w\in V\) and \(a\in k\). When \(k=\ell\) and \(\sigma\) is a [[algebra-fields-galois/field-automorphism|field automorphism]], one simply calls \(T\) semilinear.

## Relation to linear maps

For \(\sigma=\operatorname{id}_k\), semilinearity is ordinary [[linear-algebra/linear-map|linearity]]. More generally, if \({}_{\sigma}W\) denotes \(W\) with scalar action \(a\cdot_\sigma w=\sigma(a)w\), then a \(\sigma\)-semilinear map \(V\to W\) is the same additive function as a \(k\)-linear map \(V\to{}_{\sigma}W\).

A bijective semilinear self-map has an associated automorphism \(\sigma\), and its inverse is \(\sigma^{-1}\)-semilinear. Composing a \(\sigma\)-semilinear map with a \(\tau\)-semilinear map gives a \(\tau\circ\sigma\)-semilinear map.

## Projective significance

A semilinear isomorphism sends linear subspaces to linear subspaces and therefore induces a collineation of [[algebraic-geometry-foundations/projective-space|projective spaces]]. The [[algebraic-geometry-foundations/fundamental-theorem-of-projective-geometry|fundamental theorem of projective geometry]] says that, in projective dimension at least two, every collineation arises this way.

## Examples

Coordinatewise complex conjugation on \(\mathbb C^n\) is semilinear for the automorphism \(z\mapsto\overline z\), but it is not \(\mathbb C\)-linear. Over a field with no nontrivial automorphisms, every semilinear self-map is linear.

## References

1. Emil Artin, *Geometric Algebra*, Interscience, 1957. Relevant: Chapter II, §§3–4, semilinear transformations and projective geometry.
2. Peter J. Cameron, *Projective and Polar Spaces*, Queen Mary and Westfield College, 1992. [Author-maintained text](https://www.maths.qmul.ac.uk/~pjc/pps/). Relevant: Chapter 1, semilinear maps and collineations.
