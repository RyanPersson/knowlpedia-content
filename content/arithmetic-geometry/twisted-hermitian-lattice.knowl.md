+++
id = "arithmetic-geometry/twisted-hermitian-lattice"
title = "Hermitian lattice data for a family of twists"
kind = "definition"
summary = "A family of linear lifts and local integral submodules, with a rational metric at the distinguished twist."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/padic-comparison-place", "linear-algebra/inner-product-space", "linear-algebra/gram-matrix"]
+++

Fix a complex [[linear-algebra/vector-space|vector space]] \(V\) and an index set \(T\) with distinguished element \(1\). **Twisted Hermitian lattice data** consist of a [[linear-algebra/linear-map|linear map]] \(\Theta_t:V\to H_t\) to a complex [[linear-algebra/inner-product-space|inner product space]] for each \(t\), a set of allowed \(t\)'s at each prime, and an \(\mathcal O_\iota\)-[[algebra-modules/submodule|submodule]] \(L_{t,\iota}\subseteq H_t\) for every [[arithmetic-geometry/padic-comparison-place|comparison]] \(\iota\). Two compatibility conditions complete the data.

- For allowed \(t\), \(\langle L_{t,\bar\iota},L_{t,\iota}\rangle\subseteq\mathcal O_\iota\).
- A linear coordinate map \(H_1\to\mathbb C^I\) for finite \(I\) realizes its inner product as \(\bar u^{\,T}Gv\) for a rational positive definite [[linear-algebra/gram-matrix|Gram matrix]] \(G\).

## Integral vectors

The integral vectors in \(V\) at \(\iota\) form the intersection of the inverse images \(\Theta_t^{-1}(L_{t,\iota})\) over the twists allowed at that prime. This gives one simultaneous integrality condition for all those twists.

## References

- [New/Reduction/Lattices/TwistedLattice.lean, TwistedLattice](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L109)
