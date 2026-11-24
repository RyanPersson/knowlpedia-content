+++
id = "arithmetic-geometry/galois-cohomology"
title = "Galois cohomology with abelian coefficients"
kind = "definition"
summary = "Continuous cohomology of a Galois group acting on an abelian coefficient module."
aliases = ["Galois cohomology groups", "continuous Galois cohomology"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/galois-group", "algebra-homological/cochain-complex"]
+++

Let \(G\) be a [[algebra-fields-galois/galois-group|Galois group]], with its profinite topology for an infinite Galois extension, and let \(M\) be a discrete abelian group with continuous \(G\)-action. The **Galois cohomology groups** \(H^i(G,M)\) are obtained from the [[algebra-homological/cochain-complex|complex of continuous cochains]] \(G^i\to M\) with the group-cohomology differential. Degree zero is the subgroup of fixed elements.

## What a class in degree one records

A 1-cocycle is a continuous function \(c\) satisfying \(c(gh)=c(g)+g\,c(h)\). Two cocycles give the same \(H^1\) class if their difference is \(g\mapsto g\,m-m\) for some \(m\in M\). Restricting a class to a local Galois group tests it at a place. The [[arithmetic-geometry/galois-localization-kernel|kernel of a family of such restrictions]] can contain global information invisible to those local tests.

## References

- J. S. Milne, [Arithmetic Duality Theorems, chapter I, §§0 and 4, cohomology and global-to-local maps](https://www.jmilne.org/math/Books/ADTnot.pdf).
