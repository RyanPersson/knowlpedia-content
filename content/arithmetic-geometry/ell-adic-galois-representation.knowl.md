+++
id = "arithmetic-geometry/ell-adic-galois-representation"
title = "ℓ-adic Galois representation"
kind = "definition"
summary = "A continuous linear action of an absolute Galois group on an ℓ-adic vector space."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/galois-group", "algebra-fields-galois/p-adic-field", "algebra-representation-theory/group-representation"]
+++

Let \(G_K=\operatorname{Gal}(K^{\rm sep}/K)\) be the absolute [[algebra-fields-galois/galois-group|Galois group]] with its profinite topology, and let \(V\) be a finite-dimensional [[linear-algebra/vector-space|vector space]] over a finite extension of the [[algebra-fields-galois/p-adic-field|field \(\mathbb Q_\ell\)]]. An **\(\ell\)-adic Galois representation** is a continuous [[algebra-representation-theory/group-representation|representation]] \(G_K\to\mathrm{GL}(V)\), with the \(\ell\)-adic topology on the target.

## References

- [New/Congruences/GaloisRepresentations/AttachedRepresentations.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/AttachedRepresentations.lean)
