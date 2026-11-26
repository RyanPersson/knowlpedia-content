+++
id = "grh-lean/attached-representations"
title = "Passing from Hecke eigenvalues to Galois summands"
kind = "theorem"
summary = "The descent pairs supply representations with the weights and local conditions needed for twisting."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/ell-adic-galois-representation", "harmonic-analysis/hecke-eigensystem"]
+++

For each relevant [[harmonic-analysis/hecke-eigensystem|Hecke eigensystem]] of a good form and the specified descent pairs, there are main summands of [[arithmetic-geometry/ell-adic-galois-representation|Galois representations]] satisfying the local and weight conditions used to form the Selmer data.

## Proof

Start from the representations attached to the labeled systems and their [[algebra-fields-galois/frobenius-unramified|Frobenius traces]]. The weight formulas for the source and target compute the [[langlands/hodge-tate-representation|Hodge–Tate jumps]] at conjugate embeddings. These jumps satisfy the inequalities in the main-summand condition. Remove the prescribed character factors and shifts from the traces. The remaining summands have both the required traces and the local conditions for the twisting theorem.

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#source=New.Congruences.GaloisRepresentations.RowsFromEigensystems:480).

## References

- [New/Congruences/GaloisRepresentations/RowsFromEigensystems.lean, exists_isMainSummand_descentPair](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/RowsFromEigensystems.lean#L480)
- [New/Congruences/GaloisRepresentations/AttachedRepresentations.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/AttachedRepresentations.lean)
