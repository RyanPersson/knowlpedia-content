+++
id = "arithmetic-geometry/anticyclotomic-character"
title = "Anticyclotomic Hecke character"
kind = "definition"
summary = "A Hecke character of a CM field on which complex conjugation acts by inversion."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/cm-field", "algebra-fields-galois/ideles-artin-reciprocity-hecke-character"]
+++

Let \(E\) be a [[arithmetic-geometry/cm-field|CM field]] with complex conjugation \(c\). An **anticyclotomic character** is a [[algebra-fields-galois/ideles-artin-reciprocity-hecke-character|Hecke character]] \(\xi\) of \(E\) such that \(\xi(ca)=\xi(a)^{-1}\) for each idele class \(a\).

## Characters from the norm-one torus

The idele class \(a/c(a)\) has relative norm one. Pulling back a character of the norm-one torus along \(a\mapsto a/c(a)\) gives an anticyclotomic character. Its powers obey the same conjugation identity.

## References

- [New/Reduction/Data/LevelAndTwists.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/LevelAndTwists.lean)
