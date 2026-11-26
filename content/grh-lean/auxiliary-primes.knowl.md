+++
id = "grh-lean/auxiliary-primes"
title = "Auxiliary primes put the local conditions in triangular order"
kind = "theorem"
summary = "Prescribing Frobenius elements lets each new test control a remaining cohomology class."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/tate-twist", "algebra-fields-galois/frobenius-unramified", "algebra-fields-galois/chebotarev-density-theorem"]
+++

For the even classes of the relevant [[arithmetic-geometry/tate-twist|Tate twists]] and a prescribed torsion level \(\ell^\nu\), suitable auxiliary primes impose a triangular family of local conditions while meeting the prescribed Frobenius constraints.

## Proof

Choose the places in order. Construct a Kummer map detecting the new test element while the earlier maps kill it. The [[algebra-fields-galois/chebotarev-density-theorem|Chebotarev density theorem]] gives a prime whose [[algebra-fields-galois/frobenius-unramified|Frobenius]] has the required images. Local reciprocity at this place and at the later ones then bounds the new class after the preceding tests have been imposed. Iterate over the finite ordered list. The resulting local controls enter the denominator estimates.

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#source=New.Congruences.FirstOrder.TrianglePrimes:643).

## References

- [New/Congruences/FirstOrder/TrianglePrimes.lean, exists_isPrimeTriangle](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/TrianglePrimes.lean#L643)
