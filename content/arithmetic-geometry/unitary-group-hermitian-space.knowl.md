+++
id = "arithmetic-geometry/unitary-group-hermitian-space"
title = "Unitary group of a Hermitian space"
kind = "definition"
summary = "The linear automorphisms preserving the given Hermitian form."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["linear-algebra/hermitian-space", "linear-algebra/linear-map"]
+++

For a [[linear-algebra/hermitian-space|Hermitian space]] \((V,h)\) over a field with involution, its **unitary group** is
\[
 U(V,h)=\{g\in\mathrm{GL}(V):h(gu,gv)=h(u,v)\text{ for all }u,v\in V\}.
\]
The group operation is composition of [[linear-algebra/linear-map|linear maps]].

## References

- [Lib/Adelic/Unitary/Defs.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/Defs.lean)
