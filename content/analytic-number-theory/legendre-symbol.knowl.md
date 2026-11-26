+++
id = "analytic-number-theory/legendre-symbol"
title = "Legendre symbol"
kind = "definition"
summary = "The quadratic character of the residue field of an odd prime, extended by zero."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/prime-number", "algebra-fields-galois/finite-field"]
+++

For an odd [[analytic-number-theory/prime-number|prime]] \(d\) and an integer \(n\), the **Legendre symbol** \(\bigl(\frac nd\bigr)\) is \(0\) if \(d\mid n\), \(1\) if \(n\) represents a nonzero square in the [[algebra-fields-galois/finite-field|field]] \(\mathbb F_d\), and \(-1\) otherwise.

## Residues modulo seven

The nonzero squares modulo \(7\) are \(1,2,4\), giving \((2/7)=1\) and \((3/7)=-1\). The symbol is a multiplicative [[analytic-number-theory/dirichlet-character|Dirichlet character]] modulo \(d\).
