+++
id = "lie-groups/arithmetic-kleinian-group"
title = "Arithmetic Kleinian group"
kind = "definition"
summary = "A Kleinian group commensurable with a projective norm-one group from a quaternion order with one complex place."
aliases = []
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/kleinian-group", "algebra-groups/commensurable-subgroups", "algebra-groups/quaternion-order-norm-one-group", "algebra-rings/quaternion-real-place-ramification", "algebra-rings/split-quaternion-algebra", "algebra-fields-galois/field-embedding"]
+++

A [[lie-groups/kleinian-group|Kleinian group]] \(\Gamma\) is **arithmetic** if it is [[algebra-groups/commensurable-subgroups|commensurable up to conjugacy]] in \(\operatorname{PSL}_2(\mathbb C)\) with the projective image of \(\rho(\mathcal O^1)\), for data satisfying all of the following:

- \(K\) is a number field with exactly one conjugate pair of nonreal complex embeddings;
- \(B\) is a quaternion algebra over \(K\), [[algebra-rings/quaternion-real-place-ramification|ramified at every real embedding]];
- \(\mathcal O\subset B\) is an order and \(\mathcal O^1\) is its [[algebra-groups/quaternion-order-norm-one-group|norm-one group]];
- \(\rho:B\hookrightarrow M_2(\mathbb C)\) comes from a splitting \(B\otimes_{K,\sigma}\mathbb C\cong M_2(\mathbb C)\) at one of the nonreal embeddings \(\sigma\).

“One complex place” means one conjugate pair, not one individual embedding. The finite-index commensurability requirement is essential; an arbitrary infinite-index subgroup of such a group need not be arithmetic in this sense.

## Geometric consequence

These groups have finite hyperbolic covolume. The real-place ramification condition makes the other archimedean norm-one factors compact. Bianchi groups arise from the split algebra over an imaginary quadratic field.

## References

1. F. W. Gehring, C. Maclachlan, G. J. Martin, and A. W. Reid, *Arithmeticity, discreteness and volume*, Transactions of the AMS 349 (1997). [Author-hosted paper](https://math.rice.edu/~ar99/ADV.pdf), §4, definition on p. 3618.
