+++
id = "arithmetic-geometry/tate-twist"
title = "Tate twist of a Galois module"
kind = "definition"
summary = "Tensoring a Galois module by a power of the cyclotomic character."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/galois-group", "algebra-fields-galois/primitive-root-of-unity"]
+++

Let \(\ell\) be a prime invertible in a field \(K\), and \(G_K\) its absolute [[algebra-fields-galois/galois-group|Galois group]]. The rank-one module \(\mathbb Z_\ell(1)=\varprojlim_n\mu_{\ell^n}\) has transition maps \(z\mapsto z^\ell\) on the groups of [[algebra-fields-galois/primitive-root-of-unity|roots of unity]]. For a \(\mathbb Z_\ell\)-module \(M\) with \(G_K\)-action, the **Tate twist** \(M(j)\) is \(M\otimes_{\mathbb Z_\ell}\mathbb Z_\ell(1)^{\otimes j}\), with diagonal action and dual powers for \(j<0\).

## The character on a twist

Writing \(\chi_\ell\) for the character describing the action on the compatible roots of unity, the matrix of \(g\) on \(M(j)\) is \(\chi_\ell(g)^j\) times its matrix on \(M\).

## References

- [New/Congruences/FirstOrder/TateTwistCocycles.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/TateTwistCocycles.lean)
