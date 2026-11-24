+++
id = "arithmetic-geometry/galois-localization-kernel"
title = "Localization kernel in Galois cohomology"
kind = "definition"
summary = "Global cohomology classes whose restrictions vanish at every place in a specified set."
aliases = ["locally trivial cohomology classes", "global-to-local kernel"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/galois-cohomology", "algebra-fields-galois/decomposition-group"]
+++

Let \(K\) be a number field, \(M\) a discrete module with continuous action of its absolute Galois group, and \(S\) a set of places of \(K\). Restriction to a [[algebra-fields-galois/decomposition-group|decomposition group]] at each \(v\in S\) defines a map on [[arithmetic-geometry/galois-cohomology|Galois cohomology]]. Its **localization kernel** in degree \(i\) is
\[
\ker\!\left(H^i(K,M)\longrightarrow\prod_{v\in S}H^i(K_v,M)\right),
\]
where \(K_v\) is the completion of \(K\) at \(v\). A class belongs to the kernel exactly when it becomes zero at every place in \(S\).

## Testing a degree-one class

A global \(1\)-cocycle represents a class in this kernel if for every \(v\in S\) its restriction can be written as \(g\mapsto g\,m_v-m_v\) for some \(m_v\in M\). The choice of \(m_v\) may depend on \(v\). The global class itself vanishes precisely when a single \(m\in M\) gives that formula on the entire absolute Galois group.

## References

- J. S. Milne, [Arithmetic Duality Theorems, chapter I, §4, global duality and localization maps](https://www.jmilne.org/math/Books/ADTnot.pdf).
