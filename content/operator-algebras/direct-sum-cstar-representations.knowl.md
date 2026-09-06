+++
id = "operator-algebras/direct-sum-cstar-representations"
title = "Direct sum of C*-representations"
kind = "definition"
summary = "The representation acting coordinatewise on the Hilbert direct sum of a family of representation spaces."
aliases = ["direct sum of *-representations", "Hilbert direct sum representation"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/cstar-representation", "convex-analysis/linear-combination"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] and let
\(\pi_i:A\to B(H_i)\), \(i\in I\), be
[[operator-algebras/cstar-representation|\(C^*\)-representations]]. Their
**direct sum** is the representation
\[
\bigoplus_{i\in I}\pi_i:A\longrightarrow
B\left(\bigoplus_{i\in I}H_i\right)
\]
defined by
\[
\left(\bigoplus_i\pi_i\right)(a)(\xi_i)_i
   =(\pi_i(a)\xi_i)_i.
\]
It is well defined because \(\|\pi_i(a)\|\leq\|a\|\) uniformly in \(i\).
The representation space is the Hilbert direct sum, so its vectors satisfy
\(\sum_i\|\xi_i\|^2<\infty\), even when \(I\) is uncountable.
Products, adjoints, and [[convex-analysis/linear-combination|linear combinations]] are preserved coordinatewise,
so this bounded operator-valued map is again a \(C^*\)-representation.

## Kernels and faithfulness

The kernel satisfies
\[
\ker\left(\bigoplus_i\pi_i\right)=\bigcap_i\ker(\pi_i).
\]
Consequently, the direct sum is faithful exactly when the family
\((\pi_i)\) [[real-analysis/separates-points|separates points]] of \(A\). This observation constructs faithful
representations from sufficiently large families and underlies the
[[operator-algebras/universal-representation|universal representation]].

## Nondegeneracy and reducing summands

Each \(H_i\) is a reducing subspace for the direct-sum representation. If
every \(\pi_i\) is nondegenerate, then \(\bigoplus_i\pi_i\) is
nondegenerate; conversely, a zero or degenerate summand remains visible as a
degenerate reducing part. Unitary intertwiners on the summands assemble into
a unitary intertwiner of their direct sums.

## Examples and distinction

For characters \(\chi_1,\ldots,\chi_n\) of a commutative \(C^*\)-algebra,
\(\bigoplus_j\chi_j\) is the corresponding diagonal matrix
representation. The construction is not a direct integral: a direct sum
uses counting measure and square-summable coordinate families, whereas a
[[harmonic-analysis/direct-integral-unitary-representations|direct integral of representations]] requires measurable fields and ignores changes on
[[measure-theory/null-set|null sets]].

## References

1. Gerard J. Murphy, *\(C^*\)-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §3.4 on direct sums, cyclic representations, and the universal representation.
