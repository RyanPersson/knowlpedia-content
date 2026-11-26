+++
id = "harmonic-analysis/hecke-eigensystem"
title = "Hecke eigensystem"
kind = "definition"
summary = "A common character of a commutative Hecke algebra acting on a space of forms."
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/hecke-algebra-locally-compact-group-pair", "linear-algebra/eigenvector"]
+++

Let a commutative [[harmonic-analysis/hecke-algebra-locally-compact-group-pair|Hecke algebra]] \(\mathcal H\) act linearly on \(V\) over a field \(k\). A **Hecke eigensystem** occurring in \(V\) is a \(k\)-algebra homomorphism \(\lambda:\mathcal H\to k\) for which some nonzero common [[linear-algebra/eigenvector|eigenvector]] \(v\) satisfies \(Tv=\lambda(T)v\) for every \(T\in\mathcal H\).

## A congruence between eigensystems

For eigenvalues in a common number ring, two systems can have equal reductions modulo a prime ideal even when their characteristic-zero eigenvalues differ. Separating them by a projection may then introduce denominators.

## References

- [New/Congruences/GaloisRepresentations/RowsFromEigensystems.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/RowsFromEigensystems.lean)
