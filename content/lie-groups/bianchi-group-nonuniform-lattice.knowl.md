+++
id = "lie-groups/bianchi-group-nonuniform-lattice"
title = "Bianchi groups are nonuniform lattices"
kind = "theorem"
summary = "Bianchi groups are discrete and have finite covolume but noncompact quotient."
aliases = []
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/bianchi-group", "lie-groups/lattice-in-lie-group", "lie-groups/uniform-lattice", "lie-groups/psl2c-action-on-hyperbolic-three-space"]
+++

Every [[algebra-groups/bianchi-group|Bianchi group]] \(\Gamma_d=\operatorname{PSL}_2(\mathcal O_{\mathbb Q(\sqrt{-d})})\) is a [[lie-groups/uniform-lattice|nonuniform lattice]] in \(\operatorname{PSL}_2(\mathbb C)\). Thus it is discrete, and its hyperbolic quotient is noncompact with finite volume.

## Discreteness directly

In the chosen complex embedding, \(\mathcal O_K\) is generated over \(\mathbb Z\) by two real-linearly independent complex numbers. It is therefore discrete in \(\mathbb C\). Matrices with these entries form a discrete subset of \(M_2(\mathbb C)\); passing to the finite central quotient preserves discreteness.

## What needs more than discreteness

Finite covolume requires reduction theory; it does not follow merely from integral entries. Noncompactness is witnessed by cusps, including the end associated to the boundary point \(\infty\). The [[differential-geometry/bianchi-orbifold-volume-formula|volume formula]] and [[differential-geometry/bianchi-cusp-ideal-class-correspondence|cusp correspondence]] give more precise statements.

## References

1. T. Church, B. Farb, and A. Putman, *Integrality in the Steinberg module and the top-dimensional cohomology of SL_n O_K*, Example 5.6, p. 31 of the linked version. [Author-hosted paper](https://math.uchicago.edu/~farb/papers/Steinberg2.pdf)
2. F. Paulin, *Regards croisés sur les séries de Poincaré et leurs applications*, Theorem 6, p. 12. [Author’s text](https://www.imo.universite-paris-saclay.fr/~frederic.paulin/preprints/Neuchatel.pdf)
