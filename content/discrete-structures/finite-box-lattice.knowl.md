+++
id = "discrete-structures/finite-box-lattice"
title = "Finite box in the lattice"
kind = "knowl"
summary = "A finite cube-shaped subset of the integer lattice used as a finite region."
aliases = ["finite-box-lattice", "Finite box in the lattice"]
domains = ["discrete-structures"]
legacy_source_path = "discrete-structures/finite-box-lattice.md"
prerequisites = ["discrete-structures/lattice-zd", "shared-foundations/natural-numbers"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **finite box** (or **finite cube**) in the [[discrete-structures/lattice-zd|integer lattice]] is a region of the form
\[
\Lambda_L := \{x=(x_1,\dots,x_d)\in\mathbb{Z}^d : |x_i|\le L \text{ for all } i\},
\]
where \(L\) is a nonnegative [[shared-foundations/natural-numbers|integer]].

This is the cube centered at the origin with side length \(2L+1\) (in lattice units). Its cardinality is
\[
|\Lambda_L|=(2L+1)^d.
\]

## Remarks

**Translations and other conventions.**
- Any translate \(\Lambda_L+a:=\{x+a:x\in\Lambda_L\}\) is also a finite box.
- Some authors use \(\{0,1,\dots,L-1\}^d\) as the “box of side length \(L\)”; this differs from \(\Lambda_L\) by translation and a minor change of parameter.

Finite boxes are common finite-volume regions for lattice models. The [[discrete-structures/boundary-finite-region|boundary of a finite region]] describes the sites or edges adjacent to the complement.
