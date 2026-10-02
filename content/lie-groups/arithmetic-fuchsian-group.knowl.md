+++
id = "lie-groups/arithmetic-fuchsian-group"
title = "Arithmetic Fuchsian group"
kind = "definition"
summary = "A Fuchsian group commensurable with a quaternion norm-one group split at exactly one real place."
aliases = ["arithmetic Fuchsian groups"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/fuchsian-group", "algebra-groups/commensurable-subgroups", "algebra-groups/quaternion-order-norm-one-group", "algebra-rings/quaternion-real-place-ramification", "algebra-fields-galois/number-field", "algebra-rings/quaternion-algebra", "algebra-fields-galois/ring-of-integers"]
dependency_heuristic = "transcript-connections-semantic-v1"
dependency_review_count = 1
+++
A [[lie-groups/fuchsian-group|Fuchsian group]] \(\Gamma\) is **arithmetic** if it is [[algebra-groups/commensurable-subgroups|commensurable up to conjugacy]] in \(\operatorname{PSL}_2(\mathbb R)\) with the projective image of \(\mathcal O^1\), for the following data:

- a totally real [[algebra-fields-galois/number-field|number field]] \(F\);
- a [[algebra-rings/quaternion-algebra|quaternion algebra]] \(B/F\), split at exactly one real embedding and [[algebra-rings/quaternion-real-place-ramification|ramified at the others]];
- an order \(\mathcal O\subset B\) over the [[algebra-fields-galois/ring-of-integers|ring of integers]] of \(F\), with [[algebra-groups/quaternion-order-norm-one-group|norm-one group]] \(\mathcal O^1\).

The image uses a splitting \(B\otimes_{F,\sigma}\mathbb R\cong M_2(\mathbb R)\) at the distinguished real embedding \(\sigma\), followed by quotienting by \(\{\pm I\}\).

## Examples and scope

Taking \(F=\mathbb Q\), \(B=M_2(\mathbb Q)\), and \(\mathcal O=M_2(\mathbb Z)\) gives \(\operatorname{PSL}_2(\mathbb Z)\).

Such groups have finite hyperbolic covolume. An arbitrary infinite-index subgroup of one need not be arithmetic in this sense. A definite rational quaternion algebra has no split real place and does not yield a Fuchsian lattice by this construction.

## References

1. John Voight, *Quaternion Algebras*, [§38.3](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_38), Definition 38.3.4, Proposition 38.3.8, and §38.3.10; see also §38.4 for compactness.
