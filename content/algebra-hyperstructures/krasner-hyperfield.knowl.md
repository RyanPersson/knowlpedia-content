+++
id = "algebra-hyperstructures/krasner-hyperfield"
title = "Krasner hyperfield"
kind = "example"
summary = "The two-element hyperfield with 1⊞1={0,1}."
aliases = ["Krasner field", "field of one element as a hyperfield"]
domains = ["algebra-hyperstructures", "algebra-rings"]
prerequisites = []
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

The **Krasner hyperfield** is the two-element set
\(\mathbb K=\{0,1\}\) with ordinary multiplication, \(0\) as additive
identity, and
\[
1\boxplus1=\{0,1\}.
\]
Together with \(0\boxplus x=\{x\}\), this determines all of its
hyperaddition and makes \(\mathbb K\) a hyperfield.

## Quotient realization

If \(F\) is a field with at least three elements, then
\[
F/F^\times\cong\mathbb K.
\]
There are two multiplicative orbits, \(0\) and the nonzero elements. A sum of
two nonzero representatives can be zero, and suitable representatives also
give a nonzero sum, producing both elements of \(1\boxplus1\).

For \(F=\mathbb F_2\), however, the quotient sum of the sole nonzero orbit
with itself is only \(\{0\}\); the “at least three elements” hypothesis is
therefore essential for this realization.

## Boolean comparison

The [[algebra-rings/boolean-semifield|Boolean semifield]] also has carrier \(\{0,1\}\) and ordinary
multiplication, but \(1+1=1\) there. The Krasner hyperfield has a genuinely
multivalued sum containing both \(0\) and \(1\), so the two structures are
not isomorphic and should not be conflated.

## References

1. Alain Connes and Caterina Consani, “The hyperring of adèle classes,” *Journal of Number Theory* 131 (2011), 159–194. [arXiv:1001.4260](https://arxiv.org/abs/1001.4260). Relevant: the Krasner hyperfield \(\mathbb K\) and quotient hyperrings.
2. Matthew Baker and Nathan Bowler, “Matroids over hyperfields,” 2017. [arXiv:1601.01204](https://arxiv.org/abs/1601.01204). Relevant: Example 2.4.
