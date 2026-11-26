+++
id = "arithmetic-geometry/integral-vectors-for-a-family-of-twists"
title = "Vectors integral for a family of twists"
kind = "definition"
summary = "The common inverse image of the integral modules for the twists allowed at one prime."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/twisted-hermitian-lattice","arithmetic-geometry/padic-comparison-place","algebra-modules/submodule","algebra-fields-galois/valuation-ring"]
+++

In [[arithmetic-geometry/twisted-hermitian-lattice|twisted Hermitian lattice data]], fix a [[arithmetic-geometry/padic-comparison-place|comparison]] \(\iota\) over \(p\). A vector \(v\in V\) is **integral at \(\iota\) for the family of twists** if \(\Theta_t v\in L_{t,\iota}\) for every \(t\) allowed at \(p\). These vectors form the [[algebra-modules/submodule|submodule]] \(\bigcap_{t\ {\rm allowed\ at}\ p}\Theta_t^{-1}(L_{t,\iota})\) over the [[algebra-fields-galois/valuation-ring|valuation ring]] \(\mathcal O_\iota\).

## References

- [Integral vectors at a comparison](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L146)
