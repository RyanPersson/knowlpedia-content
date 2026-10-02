+++
id = "fiber-bundles/structure-group"
title = "Structure group"
kind = "definition"
summary = "The chosen group acting on the model fiber through which a bundle's transition functions are specified."
aliases = ["structure group", "structural group"]
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/g-bundle"]
+++

The **structure group** of a [[fiber-bundles/g-bundle|G-bundle]] with model fiber \(F\) is the specified group \(G\), acting on \(F\), in which its transition maps \(g_{ij}:U_i\cap U_j\to G\) take values. The change of fiber coordinates is
\[
(b,f)\longmapsto(b,g_{ij}(b)\cdot f).
\]
Thus the structure group records which transformations of the model fiber are permitted by the chosen bundle structure.

## Examples and reductions

A real rank-\(n\) [[fiber-bundles/vector-bundle|vector bundle]] has structure group \(\mathrm{GL}(n,\mathbb R)\). A [[fiber-bundles/bundle-metric|bundle metric]] permits orthonormal local frames, whose transitions lie in \(\mathrm O(n)\). This gives a [[fiber-bundles/reduction-of-structure-group|reduction of structure group]] of the associated frame bundle.

For a [[fiber-bundles/principal-g-bundle|principal G-bundle]], the model fiber is \(G\) itself; the transition functions act by left multiplication and commute with the principal right action.

## What the choice specifies

The underlying fiber bundle need not determine a unique structure group or a unique reduction. Nor is the structure group generally the [[fiber-bundles/gauge-group|gauge group]], whose elements are automorphisms of the whole principal bundle over its base.
