+++
id = "analytic-number-theory/quadratic-dirichlet-twist"
title = "Quadratic twist of a Dirichlet character"
kind = "definition"
summary = "The pointwise product of a Dirichlet character with a quadratic character."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/dirichlet-character", "analytic-number-theory/legendre-symbol"]
+++

Given a [[analytic-number-theory/dirichlet-character|Dirichlet character]] \(\chi\) and a quadratic Dirichlet character \(\eta\), the **quadratic twist** \(\chi\eta\) is the product \(n\mapsto\chi(n)\eta(n)\) on a common multiple of their moduli, with both characters extended to that level. For an odd prime \(d\) coprime to the modulus of \(\chi\), one may take \(\eta(n)=\bigl(\frac nd\bigr)\), the [[analytic-number-theory/legendre-symbol|Legendre symbol]].

## Effect on a prime

At a prime away from both moduli the twist multiplies the Euler coefficient by \(1\) or \(-1\). At a prime dividing the chosen common modulus the extended character is zero.

## References

- [Lib/General/NumberTheory/ImaginaryQuadraticField.lean, quadTwist](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/ImaginaryQuadraticField.lean#L64)
