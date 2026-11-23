+++
id = "arithmetic-geometry/degree-of-a-divisor"
title = "Degree of a divisor on a curve"
kind = "definition"
summary = "The sum of the multiplicities of the closed points of a divisor, weighted by their residue-field degrees."
aliases = ["divisor degree"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/closed-point", "algebra-fields-galois/degree-of-extension"]
+++

On a smooth projective integral curve \(C/k\), a **divisor** \(D=\sum_P n_P[P]\) is a finite formal sum of [[algebraic-geometry-foundations/closed-point|closed points]] with integer coefficients. Its **degree** is
\[
\deg D=\sum_P n_P[\kappa(P):k],
\]
where \(\kappa(P)\) is the residue field of \(P\). A \(k\)-rational point has [[algebra-fields-galois/degree-of-extension|residue degree]] one.

## Zeros and poles

For a nonzero rational function, the divisor of its zeros minus its poles has degree zero. On the projective line \(t^3\) has a triple zero at \(0\) and a pole of order three at infinity. In [[arithmetic-geometry/stepanov-method|Stepanov’s comparison]], a bound on the poles therefore also bounds the total multiplicity of the zeros.

## References

- The Stacks Project, [§33.44, degrees on curves](https://stacks.math.columbia.edu/tag/0AYQ) and [§42.18, principal divisors on proper curves](https://stacks.math.columbia.edu/tag/02RS).
