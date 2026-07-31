+++
id = "algebra-hyperstructures/hyperfield"
title = "Hyperfield"
kind = "definition"
summary = "A nontrivial hyperring whose nonzero elements form a multiplicative group."
domains = ["algebra-hyperstructures", "algebra-rings"]
section_mode = "progressive"
+++

A **hyperfield** is a [[algebra-hyperstructures/hyperring|hyperring]] \(F\)
with \(0\ne1\) such that \(F\setminus\{0\}\) is an abelian group under its
single-valued multiplication. Hyperaddition remains a canonical
hypergroup operation and may be genuinely multivalued.

## Fields as a special case

Every ordinary field is a hyperfield by making each sum singleton-valued.
Conversely, a hyperfield with only singleton sums is an ordinary field.
The [[algebra-hyperstructures/krasner-hyperfield|Krasner]],
[[algebra-hyperstructures/sign-hyperfield|sign]], and
[[algebra-hyperstructures/tropical-hyperfield|tropical]] hyperfields are
genuinely multivalued examples.

## What “division” means

Multiplicative division by a nonzero element is ordinary and unique.
Additive subtraction is different: the solutions of
\(c\in a\boxplus x\) form a set controlled by reversibility. A hyperfield is
therefore not a field with a nondeterministically chosen sum; the whole set
\(a\boxplus b\) is structural data.

## Associated tract

The [[algebra-hyperstructures/hyperfield-as-a-tract|tract associated with
\(F\)]] retains precisely the finite hypersums that contain zero. This
forgets the other values of a hyper-sum and does not identify arbitrary
tracts with hyperfields.

## References

1. Matthew Baker and Nathan Bowler, “Matroids over hyperfields,” 2017. [arXiv:1601.01204](https://arxiv.org/abs/1601.01204). Relevant: §2 and the standard examples.
2. Oleg Viro, “Hyperfields for Tropical Geometry I: Hyperfields and dequantization,” 2010. [arXiv:1006.3034](https://arxiv.org/abs/1006.3034).
