+++
id = "algebra-hyperstructures/integral-hyperring"
title = "Integral hyperring"
kind = "definition"
summary = "A nontrivial commutative hyperring without multiplicative zero divisors."
aliases = ["hyperdomain", "integral hyperdomain"]
domains = ["algebra-hyperstructures", "algebra-rings"]
section_mode = "progressive"
+++

An **integral hyperring**, also called a **hyperdomain**, is a commutative
[[algebra-hyperstructures/hyperring|hyperring]] \(R\) with \(0\ne1\) and no
multiplicative zero divisors:
\[
ab=0\quad\Longrightarrow\quad a=0\ \text{or}\ b=0.
\]
This condition concerns the single-valued multiplication. Hyperaddition may
still be genuinely multivalued.

## Relation to familiar objects

Every hyperfield is an integral hyperring because every nonzero element is
multiplicatively invertible. An ordinary commutative ring, regarded as a
singleton-addition hyperring, is integral in this sense exactly when it is an
[[algebra-rings/integral-domain|integral domain]].

An integral hyperring need not be a hyperfield: nonzero elements are required
to multiply without producing zero, but they need not all be units.

## Role in partial hyperfields

A partial hyperfield selects a multiplicative subgroup of the units of an
integral hyperring. The no-zero-divisors condition ensures that the selected
nonzero coefficients retain field-like multiplicative behavior even though
only part of the ambient hyperaddition is visible.

## References

1. Matthew Baker and Nathan Bowler, “Matroids over partial hyperstructures,” *Advances in Mathematics* 343 (2019), 821–863. [arXiv:1709.09707](https://arxiv.org/abs/1709.09707). Relevant: §2.6, integral hyperrings in the definition of partial hyperfields.
2. Jaiung Jun, “Algebraic Geometry Over Hyperrings,” *Advances in Mathematics* 323 (2018), 142–192. [arXiv:1512.04837](https://arxiv.org/abs/1512.04837). Relevant: integral hyperrings and their spectra.
