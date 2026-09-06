+++
id = "langlands/isobaric-automorphic-representation"
title = "Isobaric automorphic representation"
kind = "definition"
summary = "An automorphic representation of GL_n formed as the Langlands quotient of cuspidal data on a standard Levi subgroup."
aliases = ["isobaric sum", "Langlands isobaric sum", "boxplus of automorphic representations"]
domains = ["langlands", "harmonic-analysis"]
prerequisites = ["langlands-letter/knowls/global-local-fields-completions", "langlands/cuspidal-automorphic-representation", "langlands-letter/knowls/adeles-restricted-product", "langlands/automorphic-representation", "algebraic-geometry-foundations/levi-subgroup"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F\) be a
[[langlands-letter/knowls/global-local-fields-completions|global field]] and
let \(n=n_1+\cdots+n_r\). Given unitary
[[langlands/cuspidal-automorphic-representation|cuspidal automorphic
representations]] \(\pi_i\) of
\(\operatorname{GL}_{n_i}(\mathbb A_F)\), where \(\mathbb A_F\) is the
[[langlands-letter/knowls/adeles-restricted-product|adele ring]], their
**isobaric sum**

\[
\pi_1\boxplus\cdots\boxplus\pi_r
\]

is the irreducible [[langlands/automorphic-representation|automorphic
representation]] of
\(\operatorname{GL}_n(\mathbb A_F)\) obtained as the Langlands quotient of the
normalized parabolic induction of
\(\pi_1\otimes\cdots\otimes\pi_r\) from the standard
[[algebraic-geometry-foundations/levi-subgroup|Levi subgroup]]
\(\prod_i\operatorname{GL}_{n_i}\).

An automorphic representation obtained this way is **isobaric**.  More general
Langlands data may include real powers of determinant; the unitary isobaric
normalization places those exponents into the cuspidal constituents in the
standard way.

## Local factors

At every place, the local component is the corresponding
[[harmonic-analysis/langlands-classification-p-adic-group|local Langlands
quotient]] at nonarchimedean places. Standard
[[langlands-letter/knowls/euler-product-and-local-factor|\(L\)-functions]]
multiply:

\[
L(s,\pi_1\boxplus\cdots\boxplus\pi_r)
=\prod_i L(s,\pi_i).
\]

The multiset of cuspidal summands is unique.  This follows from
[[langlands/strong-multiplicity-one-theorem|strong multiplicity one]] and the
classification of the
[[langlands/discrete-automorphic-spectrum|discrete spectrum]] of general
linear groups.

## References

1. Hervé Jacquet and Joseph Shalika, “On Euler products and the classification
   of automorphic representations I,” *American Journal of Mathematics* 103
   (1981), 499–558. [JSTOR](https://doi.org/10.2307/2374103).
2. C. Mœglin and J.-L. Waldspurger, *Spectral Decomposition and Eisenstein
   Series*, Cambridge Tracts in Mathematics 113, Cambridge University Press,
   1995.
