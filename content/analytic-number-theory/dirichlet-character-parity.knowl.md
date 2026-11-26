+++
id = "analytic-number-theory/dirichlet-character-parity"
title = "Parity of a Dirichlet character"
kind = "definition"
summary = "The value of the character at minus one determines its parity."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/dirichlet-character","algebra-rings/group-of-units","analytic-number-theory/induced-dirichlet-character"]
+++

The **parity** of a complex [[analytic-number-theory/dirichlet-character|Dirichlet character]] \(\chi\) is the unique \(a\in\{0,1\}\) with \(\chi(-1)=(-1)^a\). The character is even if \(a=0\) and odd if \(a=1\). The value is necessarily a sign since \((-1)^2=1\) in the [[algebra-rings/group-of-units|unit group]].

## Changing the modulus

An [[analytic-number-theory/induced-dirichlet-character|induced character]] has the same parity as its inducing character, since \(-1\) is a unit at both moduli. The inverse character also has the same parity, since a sign equals its inverse.

## References

- [Parity under change of level](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/ZeroSymmetry.lean#L49)
